#!/usr/bin/env python3

# Portions of this file contributed by NIST are governed by the
# following statement:
#
# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to Title 17 Section 105 of the
# United States Code, this software is not subject to copyright
# protection within the United States. NIST assumes no responsibility
# whatsoever for its use by other parties, and makes no guarantees,
# expressed or implied, about its quality, reliability, or any other
# characteristic.
#
# We would appreciate acknowledgement if the software is used.

__version__ = "0.1.0"

import argparse
from collections import defaultdict
from typing import DefaultDict, List, Set, Tuple

import case_utils.ontology
from case_utils.namespace import NS_RDF, NS_UCO_CORE
from rdflib import Graph, Literal, URIRef
from rdflib.query import ResultRow


def node_set_to_tuple(n_things: Set[URIRef]) -> Tuple[URIRef, ...]:
    return tuple(sorted(n_things))


def node_tuple_to_ul(n_things: Tuple[URIRef, ...], graph: Graph) -> str:
    parts: List[str] = ["<ul>"]
    for n_thing in n_things:
        parts.append("<li>`")
        parts.append(str(graph.namespace_manager.qname(n_thing)))
        parts.append("`</li>")
    parts.append("</ul>")
    return "".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("in_graph", nargs="+")
    args = parser.parse_args()

    graph = Graph()
    for in_graph in args.in_graph:
        graph.parse(in_graph)

    # Load subclass hierarchy.
    case_utils.ontology.load_subclass_hierarchy(graph)

    # Key elements:
    # 1. kindOfRelationship
    # 2. isDirectional
    # 3. Set of (pre-inference) types of relationship object
    # 4. Set of (pre-inference) types of source
    # 5. Set of (pre-inference) types of target
    # 6. Set of Facet classes attached to Relationship
    # All Sets sorted and cast as tuples.
    counter: DefaultDict[
        Tuple[
            str,
            bool,
            Tuple[URIRef, ...],
            Tuple[URIRef, ...],
            Tuple[URIRef, ...],
            Tuple[URIRef, ...],
        ],
        int,
    ] = defaultdict(int)

    query = """\
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX uco-core: <https://ontology.unifiedcyberontology.org/uco/core/>
SELECT ?nRelationship ?lIsDirectional ?lKindOfRelationship ?nSource ?nTarget
WHERE {
  ?nRelationship
    a/rdfs:subClassOf* uco-core:Relationship ;
    uco-core:isDirectional ?lIsDirectional ;
    uco-core:kindOfRelationship ?lKindOfRelationship ;
    uco-core:source ?nSource ;
    uco-core:target ?nTarget ;
    .
}
"""
    for result in graph.query(query):
        assert isinstance(result, ResultRow)
        assert isinstance(result[0], URIRef)
        assert isinstance(result[1], Literal)
        assert isinstance(result[2], Literal)
        assert isinstance(result[3], URIRef)
        assert isinstance(result[4], URIRef)
        n_relationship = result[0]
        l_is_directional = result[1]
        l_kind_of_relationship = result[2]
        n_source = result[3]
        n_target = result[4]
        n_relationship_types: Set[URIRef] = set()
        n_source_types: Set[URIRef] = set()
        n_target_types: Set[URIRef] = set()
        n_facet_types: Set[URIRef] = set()

        for n_type in graph.objects(n_relationship, NS_RDF.type):
            assert isinstance(n_type, URIRef)
            n_relationship_types.add(n_type)

        for n_type in graph.objects(n_source, NS_RDF.type):
            assert isinstance(n_type, URIRef)
            n_source_types.add(n_type)

        for n_type in graph.objects(n_target, NS_RDF.type):
            assert isinstance(n_type, URIRef)
            n_target_types.add(n_type)

        for n_facet in graph.objects(n_relationship, NS_UCO_CORE.hasFacet):
            assert isinstance(n_facet, URIRef)
            for n_type in graph.objects(n_facet, NS_RDF.type):
                assert isinstance(n_type, URIRef)
                n_facet_types.add(n_type)

        key = (
            str(l_kind_of_relationship),
            bool(l_is_directional),
            node_set_to_tuple(n_relationship_types),
            node_set_to_tuple(n_source_types),
            node_set_to_tuple(n_target_types),
            node_set_to_tuple(n_facet_types),
        )
        counter[key] += 1

    print(
        """\
<!--
GENERATED FILE

To revise file contents, edit:
../relationship_type_statistics_md.py
-->

# Relationship type statistics

This table reports summary statistics of instances of `uco-core:Relationship` and all subclasses, among the CASE example sources (the [CASE website gallery](https://caseontology.org/examples/), [CASE-Examples](https://github.com/casework/CASE-Examples/), and [CASE-Corpora](https://github.com/casework/CASE-Corpora/)).  Each row is a count of `Relationship` instances grouped by the constellation of literal-values and types.  E.g. this `Relationship` instance ...

```turtle
kb:Relationship-a8513237-8a1e-4009-beb1-f85bdae30862
\ta uco-observable:ObservableRelationship ;
\tuco-core:isDirectional true ;
\tuco-core:kindOfRelationship "Resolves_To" ;
\tuco-core:source kb:Domain-1a138692-8508-4055-9113-e868ea3f3c6e ;
\tuco-core:target kb:IPAddress-fe8f8e4e-8851-4b8a-8a1b-1ba3421b967a ;
\t.
kb:Domain-1a138692-8508-4055-9113-e868ea3f3c6e
\ta uco-observable:DomainName ;
\t.
kb:IPAddress-fe8f8e4e-8851-4b8a-8a1b-1ba3421b967a
\ta uco-observable:IPv6Address ;
\t.
```

... would supply this row to the table, incrementing that row's count:

`uco-core:kindOfRelationship` | `rdf:type`s of Relationship object | `uco-core:isDirectional` | `rdf:type`s of `uco-core:source` | `rdf:type`s of `uco-core:target` | `uco-core:Facet`s
--- | --- | --- | --- | --- | ---
`Resolves_To` | `uco-observable:ObservableRelationship` | `True` | <ul><li>`uco-observable:DomainName`</li></ul> | <ul><li>`uco-observable:IPv6Address`</li></ul> | <ul></ul>

Each of the type columns is a sorted list of all of the pre-inference types associated with the relationship's source, target, or any `Facet` attached directly to the relationship.
"""
    )
    print(
        "Count | `uco-core:kindOfRelationship` | `rdf:type`s of Relationship object | `uco-core:isDirectional` | `rdf:type`s of `uco-core:source` | `rdf:type`s of `uco-core:target` | `uco-core:Facet`s"
    )
    print("--- | --- | --- | --- | --- | --- | ---")
    for key in sorted(counter.keys()):
        parts: List[str] = []
        parts.append(str(counter[key]))
        parts.append("`" + key[0] + "`")
        parts.append(node_tuple_to_ul(key[2], graph))
        parts.append("`" + str(key[1]) + "`")
        parts.append(node_tuple_to_ul(key[3], graph))
        parts.append(node_tuple_to_ul(key[4], graph))
        parts.append(node_tuple_to_ul(key[5], graph))
        print(" | ".join(parts))


if __name__ == "__main__":
    main()

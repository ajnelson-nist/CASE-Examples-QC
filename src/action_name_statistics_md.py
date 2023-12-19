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
from typing import DefaultDict, List, Optional, Set, Tuple

import case_utils.ontology
from case_utils.namespace import NS_RDF, NS_UCO_ACTION, NS_UCO_CORE
from rdflib import PROV, TIME, Graph, Literal, URIRef
from rdflib.query import ResultRow

NS_PROV = PROV
NS_TIME = TIME


def node_set_to_tuple(n_things: Set[URIRef]) -> Tuple[URIRef, ...]:
    # Strip OWL-Time and PROV-O concepts, which are typically added
    # mechanically in some of the examples' workflows
    # (e.g. by case-prov).
    _n_things: Set[URIRef] = n_things - {
        NS_PROV.Agent,
        NS_PROV.Activity,
        NS_PROV.Collection,
        NS_PROV.Entity,
        NS_PROV.SoftwareAgent,
        NS_TIME.ProperInterval,
    }
    return tuple(sorted(_n_things))


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
    # 1. Action's name (optional)
    # 2. Set of (pre-inference) types of action
    # 3. Set of (pre-inference) types of action objects (inputs)
    # 4. Set of (pre-inference) types of action results (outputs)
    # 5. Set of (pre-inference) types of action's environment
    # 6. Set of (pre-inference) types of action's instrument
    # 7. Set of (pre-inference) types of action's performer
    # 8. Set of (pre-inference) types of action's location
    # 9. Set of Facet classes attached to Relationship
    # All Sets sorted and cast as tuples.
    counter: DefaultDict[
        Tuple[
            str,
            Tuple[URIRef, ...],
            Tuple[URIRef, ...],
            Tuple[URIRef, ...],
            Tuple[URIRef, ...],
            Tuple[URIRef, ...],
            Tuple[URIRef, ...],
            Tuple[URIRef, ...],
            Tuple[URIRef, ...],
        ],
        int,
    ] = defaultdict(int)

    query = """\
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX uco-action: <https://ontology.unifiedcyberontology.org/uco/action/>
SELECT ?nAction
WHERE {
  ?nAction
    a/rdfs:subClassOf* uco-action:Action ;
    .
}
"""
    for result in graph.query(query):
        assert isinstance(result, ResultRow)
        assert isinstance(result[0], URIRef)
        n_action = result[0]
        n_action_types: Set[URIRef] = set()

        l_action_name: Optional[Literal] = None
        for l_object in graph.objects(n_action, NS_UCO_CORE.name):
            assert isinstance(l_object, Literal)
            l_action_name = l_object

        for n_type in graph.objects(n_action, NS_RDF.type):
            assert isinstance(n_type, URIRef)
            n_action_types.add(n_type)

        def _get_types_of_predicate_objects(n_property: URIRef) -> Set[URIRef]:
            n_types: Set[URIRef] = set()
            for n_object in graph.objects(n_action, n_property):
                assert isinstance(n_object, URIRef)
                for n_type in graph.objects(n_object, NS_RDF.type):
                    assert isinstance(n_type, URIRef)
                    n_types.add(n_type)
            return n_types

        n_environment_types = _get_types_of_predicate_objects(NS_UCO_ACTION.environment)
        n_instrument_types = _get_types_of_predicate_objects(NS_UCO_ACTION.instrument)
        n_location_types = _get_types_of_predicate_objects(NS_UCO_ACTION.location)
        n_object_types = _get_types_of_predicate_objects(NS_UCO_ACTION.object)
        n_performer_types = _get_types_of_predicate_objects(NS_UCO_ACTION.performer)
        n_result_types = _get_types_of_predicate_objects(NS_UCO_ACTION.result)
        n_facet_types = _get_types_of_predicate_objects(NS_UCO_CORE.hasFacet)

        key = (
            "" if l_action_name is None else str(l_action_name),
            node_set_to_tuple(n_action_types),
            node_set_to_tuple(n_object_types),
            node_set_to_tuple(n_result_types),
            node_set_to_tuple(n_environment_types),
            node_set_to_tuple(n_instrument_types),
            node_set_to_tuple(n_performer_types),
            node_set_to_tuple(n_location_types),
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

# Action name statistics

This table reports summary statistics of instances of `uco-action:Action` and all subclasses, among the CASE example sources (the [CASE website gallery](https://caseontology.org/examples/), [CASE-Examples](https://github.com/casework/CASE-Examples/), and [CASE-Corpora](https://github.com/casework/CASE-Corpora/)).  Each row is a count of `Action` instances grouped by the constellation of literal-values and types.  E.g. this `Action` instance ...

```turtle
kb:Action-20ccff7b-3461-4bac-a531-5691f58383f5
\ta
\t\tcase-investigation:InvestigativeAction ,
\t\tuco-observable:ObservableAction
\t\t;
\tuco-core:name "Download" ;
\tuco-action:performer kb:Person-eb9f6e62-7108-42b6-beb3-8af699b67c19 ;
\tuco-action:object
\t\tkb:ProvenanceRecord-6003d616-234f-46b6-be6e-b8b042f51c1e ,
\t\tkb:URL-b1743bf6-0d8e-4a39-bc94-c31b07bb527f
\t\t;
\tuco-action:result
\t\tkb:File-c270f1f6-d4ee-4452-a678-ca5e7c17aa7b ,
\t\tkb:ProvenanceRecord-fbe219e0-5903-44bd-b7fd-ea1bd7bc4732
\t\t;
\t.
kb:File-c270f1f6-d4ee-4452-a678-ca5e7c17aa7b
\ta uco-observable:ArchiveFile ;
\t.
kb:Person-eb9f6e62-7108-42b6-beb3-8af699b67c19
\ta uco-identity:Person ;
\t.
kb:ProvenanceRecord-6003d616-234f-46b6-be6e-b8b042f51c1e
\ta case-investigation:ProvenanceRecord ;
\t.
kb:ProvenanceRecord-fbe219e0-5903-44bd-b7fd-ea1bd7bc4732
\ta case-investigation:ProvenanceRecord ;
\t.
kb:URL-b1743bf6-0d8e-4a39-bc94-c31b07bb527f
\ta uco-observable:URL ;
\t.
```

... would supply this row to the table, incrementing that row's count:

`uco-core:name` | `rdf:type`s of Action object | `rdf:type`s of `uco-action:object`s | `rdf:type`s of `uco-action:result`s | `rdf:type`s of `uco-action:environment` | `rdf:type`s of `uco-action:instrument` | `rdf:type`s of `uco-action:performer` | `rdf:type`s of `uco-action:location` | `uco-core:Facet`s
--- | --- | --- | --- | --- | --- | --- | --- | ---
`Download` | <ul><li>`case-investigation:InvestigativeAction`</li><li>`uco-observable:ObservableAction`</li></ul> | <ul><li>`case-investigation:ProvenanceRecord`</li><li>`uco-observable:URL`</li></ul> | <ul><li>`case-investigation:ProvenanceRecord`</li><li>`uco-observable:File`</li></ul> | <ul></ul> | <ul></ul> | <ul><li>`uco-identity:Person`</li></ul> | <ul></ul> | <ul></ul>

Each of the type columns is a sorted list of all of the pre-inference types associated with the action and its related objects and attached `Facet`s.  (Note that some types were included in the input data that may have been inferred from [`case-prov`](https://github.com/casework/CASE-Implementation-PROV-O) review, particularly pretaining to `prov:` and `time:` prefixed concepts.  Because those types are mechanically added as part of ongoing data maintenance, they have been stripped from this table.)
"""
    )
    print(
        "Count | `uco-core:name` | `rdf:type`s of Action object | `rdf:type`s of `uco-action:object`| `rdf:type`s of `uco-action:result`| `rdf:type`s of `uco-action:environment`   | `rdf:type`s of `uco-action:instrument` | `rdf:type`s of `uco-action:performer` | `rdf:type`s of `uco-action:location` | `uco-core:Facet`s"
    )
    print("--- | --- | --- | --- | --- | --- | --- | --- | --- | ---")
    for key in sorted(counter.keys()):
        parts: List[str] = []
        parts.append(str(counter[key]))
        parts.append("" if key[0] == "" else ("`" + key[0] + "`"))
        parts.append(node_tuple_to_ul(key[1], graph))
        parts.append(node_tuple_to_ul(key[2], graph))
        parts.append(node_tuple_to_ul(key[3], graph))
        parts.append(node_tuple_to_ul(key[4], graph))
        parts.append(node_tuple_to_ul(key[5], graph))
        parts.append(node_tuple_to_ul(key[6], graph))
        parts.append(node_tuple_to_ul(key[7], graph))
        parts.append(node_tuple_to_ul(key[8], graph))
        print(" | ".join(parts))


if __name__ == "__main__":
    main()

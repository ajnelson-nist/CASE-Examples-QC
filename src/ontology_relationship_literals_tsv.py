#!/usr/bin/env python3

# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to title 17 Section 105 of the
# United States Code this software is not subject to copyright
# protection and is in the public domain. NIST assumes no
# responsibility whatsoever for its use by other parties, and makes
# no guarantees, expressed or implied, about its quality,
# reliability, or any other characteristic.
#
# We would appreciate acknowledgement if the software is used.

"""
This script is for reporting the kindOfRelationship vocabulary literals provided by UCO's vocabulary ontology.
"""

__version__ = "0.2.0"

import argparse
import importlib
import logging
import os

import case_utils.ontology
import rdflib.plugins.sparql
from case_utils.namespace import NS_UCO_VOCABULARY

_logger = logging.getLogger(os.path.basename(__file__))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.parse_args()
    logging.basicConfig(level=logging.INFO)

    # _logger.info("sys.getrecursionlimit() = %d." % sys.getrecursionlimit())

    # Pairs: datatype, value
    vocabset = set()

    graph = rdflib.Graph()
    ttl_filename = (
        case_utils.ontology.version_info.built_version_choices_list[-1] + ".ttl"
    )
    ttl_data = importlib.resources.read_text(case_utils.ontology, ttl_filename)
    graph.parse(data=ttl_data, format="turtle")

    nsdict = {k: v for (k, v) in graph.namespace_manager.namespaces()}

    # owl:oneOf query syntax via: https://stackoverflow.com/a/37059201
    query = rdflib.plugins.sparql.processor.prepareQuery(
        """\
SELECT ?lKindOfRelationship
WHERE {
  ?nDataType
    a rdfs:Datatype ;
    owl:oneOf/rdf:rest*/rdf:first ?lKindOfRelationship .
}""",
        initNs=nsdict,
    )  # type: ignore
    for n_datatype in [
        NS_UCO_VOCABULARY.ActionRelationshipTypeVocab,
        NS_UCO_VOCABULARY.ObservableObjectRelationshipVocab,
    ]:
        datatype = n_datatype.toPython()
        for (result_no, result) in enumerate(
            graph.query(query, initBindings={"nDataType": n_datatype})
        ):
            (l_value,) = result
            value = l_value.toPython()
            vocabset.add((datatype, value))
    del graph
    assert len(vocabset) > 0, "Failed to load expected vocabularies."

    for record in sorted(vocabset):
        print("\t".join(record))


if __name__ == "__main__":
    main()

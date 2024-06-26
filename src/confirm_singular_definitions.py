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

"""
This script reviews all .ttl files in a directory for redundant rdfs:comment or rdfs:label statements, which are a sign of merge errors inducing redundant class definitions.
"""

__version__ = "0.1.2"

import argparse
import logging
import os
from typing import Set

import rdflib.plugins.sparql
from rdflib import URIRef
from rdflib.query import ResultRow

_logger = logging.getLogger(os.path.basename(__file__))

CONCEPT_IRIS_WITH_KNOWN_ISSUES: Set[str] = set()


def class_iris_with_redundant_definitions(filepath: str) -> Set[str]:
    graph = rdflib.Graph()
    graph.parse(filepath, format="turtle")
    nsdict = {k: v for (k, v) in graph.namespace_manager.namespaces()}

    query_comments_text = """
SELECT ?nClass
WHERE {
  ?nClass
    rdfs:comment ?lComment1 ;
    rdfs:comment ?lComment2 ;
    .

  FILTER (?lComment1 != ?lComment2)
}
"""
    query_comments_object = rdflib.plugins.sparql.prepareQuery(
        query_comments_text, initNs=nsdict
    )

    query_labels_text = """
SELECT ?nClass
WHERE {
  ?nClass
    rdfs:label ?lLabel1 ;
    rdfs:label ?lLabel2 ;
    .

  FILTER (?lLabel1 != ?lLabel2)
}
"""
    query_labels_object = rdflib.plugins.sparql.prepareQuery(
        query_labels_text, initNs=nsdict
    )

    class_iris: Set[str] = set()
    for query_object in [query_comments_object, query_labels_object]:
        for result in graph.query(query_object):
            assert isinstance(result, ResultRow)
            assert isinstance(result[0], URIRef)
            n_class = result[0]
            class_iri = n_class.toPython()
            class_iris.add(class_iri)

    class_iris -= CONCEPT_IRIS_WITH_KNOWN_ISSUES

    if len(class_iris) > 0:
        _logger.error("File %s.", filepath)
        for class_iri in sorted(class_iris):
            _logger.error("Class found - %s.", class_iri)
    return class_iris


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.parse_args()
    logging.basicConfig(level=logging.INFO)

    class_iris = set()
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        for filename in sorted(filenames):
            if not filename.endswith(".ttl"):
                continue
            filepath = os.path.join(dirpath, filename)
            for class_iri in class_iris_with_redundant_definitions(filepath):
                class_iris.add(class_iri)
    assert len(class_iris) == 0, "Redundant definitions found"


if __name__ == "__main__":
    main()

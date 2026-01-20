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
This script emits all ontology IRIs and version IRIs in the supplied ontology files.
"""

__version__ = "0.1.1"

import argparse
import importlib
import logging
import os
import sys
import typing

import case_utils.ontology.version_info
import rdflib.plugins.sparql
from rdflib import URIRef
from rdflib.query import ResultRow

_logger = logging.getLogger(os.path.basename(__file__))


def graph_file_to_vocabset(
    filename: typing.Optional[str] = None,
) -> typing.Set[rdflib.URIRef]:
    vocabset: typing.Set[rdflib.URIRef] = set()
    if filename is None:
        iri_data = importlib.resources.read_text(
            case_utils.ontology, "ontology_and_version_iris.txt"
        )
        for line in iri_data.split("\n"):
            cleaned_line = line.strip()
            if cleaned_line == "":
                continue
            vocabset.add(rdflib.URIRef(cleaned_line))
    else:
        graph = rdflib.Graph()
        graph.parse(
            filename, format="json-ld" if filename.endswith("json") else "turtle"
        )

        query = rdflib.plugins.sparql.processor.prepareQuery("""\
PREFIX owl: <http://www.w3.org/2002/07/owl#>
SELECT ?s
WHERE {
  { ?s a owl:Ontology }
  UNION
  { ?x owl:ontologyIRI ?s }
  UNION
  { ?y owl:versionIRI ?s }
}""")
        for result_no, result in enumerate(graph.query(query)):
            assert isinstance(result, ResultRow)
            assert isinstance(result[0], URIRef)
            vocabset.add(result[0])
        del graph

    return vocabset


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", nargs="*")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)

    # This is necessary to parse UCO 0.3.0's observable.ttl.
    sys.setrecursionlimit(sys.getrecursionlimit() * 2)
    _logger.info("sys.getrecursionlimit() = %d." % sys.getrecursionlimit())

    vocabset: typing.Set[rdflib.URIRef] = set()

    max_arg_no: int = -1
    for arg_no, arg in enumerate(args.in_file):
        max_arg_no = arg_no
        _logger.info("arg=%r" % arg)
        tmp_vocabset = graph_file_to_vocabset(args.in_file)
        vocabset |= tmp_vocabset
    if max_arg_no == -1:
        tmp_vocabset = graph_file_to_vocabset()
        vocabset |= tmp_vocabset

    for term in sorted(vocabset):
        print(term)


if __name__ == "__main__":
    main()

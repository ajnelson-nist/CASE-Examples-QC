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
This script emits all classes and properties in the supplied ontology files.
"""

__version__ = "0.2.0"

import argparse
import importlib
import logging
import os
import sys
import typing

import case_utils.ontology.version_info
import rdflib.plugins.sparql

_logger = logging.getLogger(os.path.basename(__file__))


def graph_file_to_vocabset(
    filename: typing.Optional[str] = None,
) -> typing.Set[rdflib.URIRef]:
    vocabset: typing.Set[rdflib.URIRef] = set()
    graph = rdflib.Graph()
    if filename is None:
        ttl_filename = (
            case_utils.ontology.version_info.built_version_choices_list[-1] + ".ttl"
        )
        ttl_data = importlib.resources.read_text(case_utils.ontology, ttl_filename)
        graph.parse(data=ttl_data, format="turtle")
    else:
        graph.parse(
            filename, format="json-ld" if filename.endswith("json") else "turtle"
        )

    query = rdflib.plugins.sparql.processor.prepareQuery(
        """\
SELECT ?s
WHERE {
  { ?s a <http://www.w3.org/2002/07/owl#Class> . }
  UNION
  { ?s a <http://www.w3.org/2002/07/owl#DatatypeProperty> . }
  UNION
  { ?s a <http://www.w3.org/2002/07/owl#ObjectProperty> . }
}"""
    )  # type: ignore
    for (result_no, result) in enumerate(graph.query(query)):
        # Skip anonymous classes (such as might be used in OWL complement definitions).
        if isinstance(result[0], rdflib.URIRef):
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
    for (arg_no, arg) in enumerate(args.in_file):
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

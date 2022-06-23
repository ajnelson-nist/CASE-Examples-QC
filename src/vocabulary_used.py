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
This script is for reporting the vocabulary used in knowledge base files.

Literals are skipped.
"""

__version__ = "0.1.0"

import logging
import os

import rdflib.plugins.sparql

_logger = logging.getLogger(os.path.basename(__file__))


def main():
    # _logger.info("sys.getrecursionlimit() = %d." % sys.getrecursionlimit())

    vocabset = set()

    for arg in args.in_file:
        _logger.info("arg=%r" % arg)
        graph = rdflib.Graph()
        graph.parse(arg, format="json-ld" if arg.endswith("json") else "turtle")
        _logger.info("len(graph)=%d" % len(graph))

        query = rdflib.plugins.sparql.prepareQuery("SELECT ?s ?p ?o WHERE {?s ?p ?o}")
        for (result_no, result) in enumerate(graph.query(query)):
            # if result_no == 0:
            #    _logger.info(dir(result[0]))
            vocabset.add(result[0])
            vocabset.add(result[1])
            # _logger.info("type(result[2])=%r" % type(result[2]))
            if not isinstance(result[2], rdflib.term.Literal):
                vocabset.add(result[2])
        del graph

    for term in sorted(vocabset):
        print(term)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", nargs="+")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    main()

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

__version__ = "0.1.0"

import os
import sys
import logging

import rdflib.plugins.sparql

_logger = logging.getLogger(os.path.basename(__file__))

def main():
    # This is necessary to parse UCO 0.3.0's observable.ttl.
    sys.setrecursionlimit(sys.getrecursionlimit() * 2)
    _logger.info("sys.getrecursionlimit() = %d." % sys.getrecursionlimit())

    vocabset = set()

    for arg in args.in_file:
        _logger.info("arg=%r" % arg)
        graph = rdflib.Graph()
        graph.parse(arg, format="json-ld" if arg.endswith("json") else "ttl")
        _logger.info("len(graph)=%d" % len(graph))

        query = rdflib.plugins.sparql.prepareQuery("""\
SELECT ?s
WHERE {
	{ ?s a <http://www.w3.org/2002/07/owl#Class> . }
	UNION
	{ ?s a <http://www.w3.org/2002/07/owl#DatatypeProperty> . }
	UNION
	{ ?s a <http://www.w3.org/2002/07/owl#ObjectProperty> . }
}""")
        for (result_no, result) in enumerate(graph.query(query)):
            vocabset.add(result[0])
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

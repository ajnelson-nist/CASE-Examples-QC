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
This script is for reporting the kindOfRelationship vocabulary literals used in instance-data files.
"""

__version__ = "0.1.0"

import argparse
import logging
import os

import rdflib.plugins.sparql

_logger = logging.getLogger(os.path.basename(__file__))

NS_XSD_STRING_IRI = rdflib.XSD.string.toPython()


def main():
    # _logger.info("sys.getrecursionlimit() = %d." % sys.getrecursionlimit())

    # Pairs: datatype, value
    vocabset = set()

    for arg in args.in_file:
        _logger.info("arg=%r" % arg)
        graph = rdflib.Graph()
        graph.parse(arg, format="json-ld" if arg.endswith("json") else "turtle")
        _logger.info("len(graph)=%d" % len(graph))

        nsdict = {k: v for (k, v) in graph.namespace_manager.namespaces()}

        query = rdflib.plugins.sparql.prepareQuery(
            """\
SELECT ?lKindOfRelationship
WHERE {
  ?nRelationship uco-core:kindOfRelationship ?lKindOfRelationship .
}""",
            initNs=nsdict,
        )
        for result_no, result in enumerate(graph.query(query)):
            (l_value,) = result
            if l_value.datatype is None:
                datatype = NS_XSD_STRING_IRI
            else:
                datatype = l_value.datatype.toPython()
            value = l_value.toPython()
            vocabset.add((datatype, value))
        del graph

    for record in sorted(vocabset):
        print("\t".join(record))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", nargs="+")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    main()

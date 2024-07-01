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
This script is for reporting the kindOfRelationship vocabulary literals used in instance-data files.
"""

__version__ = "0.1.2"

import argparse
import logging
import os

import rdflib.plugins.sparql
from rdflib import Literal
from rdflib.query import ResultRow

_logger = logging.getLogger(os.path.basename(__file__))

NS_XSD_STRING_IRI = rdflib.XSD.string.toPython()


def main() -> None:
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
PREFIX uco-core: <https://ontology.unifiedcyberontology.org/uco/core/>
SELECT ?lKindOfRelationship
WHERE {
  ?nRelationship uco-core:kindOfRelationship ?lKindOfRelationship .
}""",
            initNs=nsdict,
        )
        for result_no, result in enumerate(graph.query(query)):
            assert isinstance(result, ResultRow)
            assert isinstance(result[0], Literal)
            l_value = result[0]
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

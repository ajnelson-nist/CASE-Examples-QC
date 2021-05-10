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

import os
import sys
import logging

import rdflib.plugins.sparql

_logger = logging.getLogger(os.path.basename(__file__))

NS_UCO_VOCABULARY = rdflib.Namespace("https://unifiedcyberontology.org/ontology/uco/vocabulary#")

def main():
    #_logger.info("sys.getrecursionlimit() = %d." % sys.getrecursionlimit())

    # Pairs: datatype, value
    vocabset = set()

    for arg in args.in_file:
        _logger.info("arg=%r" % arg)
        graph = rdflib.Graph()
        graph.parse(arg, format="turtle")
        _logger.info("len(graph)=%d" % len(graph))

        nsdict = {k:v for (k,v) in graph.namespace_manager.namespaces()}

        # owl:oneOf query syntax via: https://stackoverflow.com/a/37059201
        query = rdflib.plugins.sparql.prepareQuery("""\
SELECT ?lKindOfRelationship
WHERE {
  ?nDataType
    a rdfs:Datatype ;
    owl:oneOf/rdf:rest*/rdf:first ?lKindOfRelationship .
}""", initNs=nsdict)
        for n_datatype in [
          NS_UCO_VOCABULARY.ActionRelationshipTypeVocab,
          NS_UCO_VOCABULARY.ObservableObjectRelationshipVocab
        ]:
            datatype = n_datatype.toPython()
            for (result_no, result) in enumerate(graph.query(query, initBindings={"nDataType": n_datatype})):
                (l_value,) = result
                value = l_value.toPython()
                vocabset.add((datatype, value))
        del graph
    assert len(vocabset) > 0, "Failed to load expected vocabularies."

    for record in sorted(vocabset):
        try:
            print("\t".join(record))
        except:
            _logger.error(record)
            raise

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("in_file", nargs="+")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    main()

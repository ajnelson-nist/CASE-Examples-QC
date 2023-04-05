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
This script performs a review of a graph's UCO Hash nodes.  Hash nodes
identified with a UUIDv5 are checked to see if they are generated from a
URN scheme, based on this draft IETF memo:

https://datatracker.ietf.org/doc/html/draft-thiemann-hash-urn-01

Note that at the time of this writing, that memo was expired (expiration
date 2004-03-04) and did not have a linked superseding document.
"""

__version__ = "0.2.0"

import argparse
import binascii
import logging
import re
import uuid
import warnings
from typing import Dict, Optional, Set, Tuple

from case_utils.namespace import NS_UCO_TYPES, NS_UCO_VOCABULARY
from rdflib import Graph, IdentifiedNode, Literal, URIRef
from rdflib.query import ResultRow

L_MD5 = Literal("MD5", datatype=NS_UCO_VOCABULARY.HashNameVocab)
L_SHA1 = Literal("SHA1", datatype=NS_UCO_VOCABULARY.HashNameVocab)
L_SHA256 = Literal("SHA256", datatype=NS_UCO_VOCABULARY.HashNameVocab)
L_SHA3_256 = Literal("SHA3-256", datatype=NS_UCO_VOCABULARY.HashNameVocab)
L_SHA3_512 = Literal("SHA3-512", datatype=NS_UCO_VOCABULARY.HashNameVocab)
L_SHA384 = Literal("SHA384", datatype=NS_UCO_VOCABULARY.HashNameVocab)
L_SHA512 = Literal("SHA512", datatype=NS_UCO_VOCABULARY.HashNameVocab)

CASTED_METHODS: Dict[Literal, str] = {
    L_MD5: "md5",
    L_SHA1: "sha1",
    L_SHA256: "sha256",
    L_SHA384: "sha384",
    L_SHA512: "sha512",
    L_SHA3_256: "sha3-256",
    L_SHA3_512: "sha3-512",
}

RX_UUID = re.compile(
    "[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}$", re.IGNORECASE
)


def hash_node_to_iri_summary(
    graph: Graph, n_hash: IdentifiedNode
) -> Optional[Tuple[str, str, str]]:
    l_hash_method: Optional[Literal] = None
    for triple in graph.triples((n_hash, NS_UCO_TYPES.hashMethod, None)):
        assert isinstance(triple[2], Literal)
        l_hash_method = triple[2]
    assert l_hash_method is not None

    l_hash_value: Optional[Literal] = None
    for triple in graph.triples((n_hash, NS_UCO_TYPES.hashValue, None)):
        assert isinstance(triple[2], Literal)
        l_hash_value = triple[2]
    assert l_hash_value is not None

    if l_hash_method not in CASTED_METHODS:
        warnings.warn("Unimplemented hash method: %s." % str(l_hash_method))
        return None

    hash_method_str = CASTED_METHODS[l_hash_method]
    hash_value_str: str = binascii.hexlify(l_hash_value.toPython()).decode().lower()

    urn_template = "urn:hash::%s:%s"
    urn_populated = urn_template % (hash_method_str, hash_value_str)

    return (
        hash_method_str,
        hash_value_str,
        str(uuid.uuid5(uuid.NAMESPACE_URL, urn_populated)),
    )


def unexpected(graph: Graph) -> Set[Tuple[str, str, str, Optional[str]]]:
    retval: Set[Tuple[str, str, str, Optional[str]]] = set()
    nsdict: Dict[str, URIRef] = {"uco-types": URIRef(str(NS_UCO_TYPES))}
    for result in graph.query(
        """\
SELECT ?nHash
WHERE {
  ?nHash a/rdfs:subClassOf* uco-types:Hash .
}
""",
        initNs=nsdict,
    ):
        assert isinstance(result, ResultRow)
        assert isinstance(result[0], IdentifiedNode)
        n_hash: IdentifiedNode = result[0]

        recorded_hash_uuid: Optional[str] = None
        if isinstance(n_hash, URIRef):
            n_hash_str = str(n_hash)
            if len(n_hash_str) < 36:
                logging.debug("Skip 1")
                # Custom non-IRI scheme in use.
                continue
            if RX_UUID.search(n_hash_str) is None:
                logging.debug("Skip 2")
                logging.debug(n_hash_str)
                # Custom non-IRI scheme in use.
                continue
            recorded_hash_uuid = n_hash_str[-36:]

        iri_summary = hash_node_to_iri_summary(graph, n_hash)
        if iri_summary is None:
            continue
        (
            hash_method_str,
            hash_value_str,
            expected_hash_uuid,
        ) = iri_summary
        if recorded_hash_uuid != expected_hash_uuid:
            retval.add(
                (
                    hash_method_str,
                    hash_value_str,
                    expected_hash_uuid,
                    recorded_hash_uuid,
                )
            )
    return retval


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("in_graph")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    graph = Graph()
    graph.parse(args.in_graph)

    logging.debug("len(graph) = %d.", len(graph))

    unexpected_nodes = unexpected(graph)
    for unexpected_node in sorted(unexpected_nodes):
        logging.error(unexpected_node)
    assert 0 == len(unexpected_nodes)


if __name__ == "__main__":
    main()

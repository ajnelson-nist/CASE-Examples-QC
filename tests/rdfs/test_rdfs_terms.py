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
These tests RDFS-namespace concepts used in CASE and UCO for typos.
It was written on discovery of typos in concept names in UCO 0.6.0.
"""

import importlib.resources
import logging
import os
from typing import Generator, Set

import case_utils.ontology
import pytest
import rdflib

_logger = logging.getLogger(os.path.basename(__file__))


@pytest.fixture
def rdfs_iris() -> Generator[Set[str], None, None]:
    NS_RDFS = rdflib.RDFS
    # _logger.debug(dir(rdflib.RDFS))
    iris = set()
    # This list is copied from the source code of rdflib 5.0.0,
    # namespace.py.  In this version of rdflib, the term list does not
    # seem to be programmatically accessible.
    concept_names = [
        "Resource",
        "Class",
        "subClassOf",
        "subPropertyOf",
        "comment",
        "label",
        "domain",
        "range",
        "seeAlso",
        "isDefinedBy",
        "Literal",
        "Container",
        "ContainerMembershipProperty",
        "member",
        "Datatype",
    ]
    for term in concept_names:
        iris.add(NS_RDFS[term].toPython())
    yield iris


def test_rdfs_term_names(rdfs_iris: Set[str]) -> None:
    assert len(rdfs_iris) > 0, "Failed to load closed set of RDFS IRIs."


def test_rdfs_typos(rdfs_iris: Set[str]) -> None:
    ttl_data = importlib.resources.read_text(case_utils.ontology, "case-0.5.0.ttl")
    ontology_graph = rdflib.Graph()
    ontology_graph.parse(data=ttl_data, format="turtle")
    _logger.debug("len(ontology_graph) = %d.", len(ontology_graph))

    # RDFS concept IRI, as a string.
    rdfs_iris_found = set()

    for triple_no, triple in enumerate(ontology_graph.triples((None, None, None))):
        if 0 == triple_no:
            _logger.debug("triple0 = %r.", (triple,))
        for term in triple:
            if not isinstance(term, rdflib.URIRef):
                continue
            term_string = term.toPython()
            if term_string.startswith("http://www.w3.org/2000/01/rdf-schema#"):
                rdfs_iris_found.add(term_string)
    assert len(rdfs_iris_found) > 0, "No RDFS IRIs found."

    rdfs_iris_not_recognized = rdfs_iris_found - rdfs_iris
    try:
        assert rdfs_iris_not_recognized == set(), "Suspected non-RDFS IRI found."
    except AssertionError:
        for iri in sorted(rdfs_iris_not_recognized):
            _logger.error("iri %r found in ontology files:", iri)
        raise

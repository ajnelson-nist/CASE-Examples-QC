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
These tests RDFS-namespace concepts used in CASE and UCO for typos.
It was written on discovery of typos in concept names in UCO 0.6.0.
"""

import collections
import glob
import logging
import os
import sys

import pytest
import rdflib

_logger = logging.getLogger(os.path.basename(__file__))

@pytest.fixture
def rdfs_iris():
    NS_RDFS = rdflib.RDFS
    #_logger.debug(dir(rdflib.RDFS))
    iris = set()
    # This list is copied from the source code of rdflib 5.0.0,
    # namespace.py.  In this version of rdflib, the term list does not
    # seem to be programmatically accessible.
    concept_names = [
        "Resource", "Class", "subClassOf", "subPropertyOf", "comment", "label",
        "domain", "range", "seeAlso", "isDefinedBy", "Literal", "Container",
        "ContainerMembershipProperty", "member", "Datatype"]
    for term in concept_names:
        iris.add(NS_RDFS[term].toPython())
    yield iris

@pytest.fixture
def top_srcdir():
    """NB: This hard-codes path assumptions."""
    top_srcdir = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
    yield top_srcdir

@pytest.fixture
def ontology_paths_case(top_srcdir):
    """NB: This hard-codes path assumptions."""
    case_srcdir = os.path.join(top_srcdir, "dependencies", "CASE-Examples", "dependencies", "CASE")
    _logger.debug("case_srcdir = %r.", case_srcdir)
    assert "CASE" == os.path.basename(case_srcdir)
    filepaths = set()
    for filepath in glob.glob(os.path.join(case_srcdir, "ontology", "*", "*.ttl")):
        # Skip any syntax-normalization files.
        if "/." in filepath:
            continue
        filepaths.add(filepath)
    yield filepaths

@pytest.fixture
def ontology_paths_uco(top_srcdir):
    """NB: This hard-codes path assumptions."""
    uco_srcdir = os.path.join(top_srcdir, "dependencies", "CASE-Examples", "dependencies", "UCO")
    _logger.debug("uco_srcdir = %r.", uco_srcdir)
    assert "UCO" == os.path.basename(uco_srcdir)
    filepaths = set()
    for filepath in glob.glob(os.path.join(uco_srcdir, "uco-*", "*.ttl")):
        # Skip any syntax-normalization files.
        if "/." in filepath:
            continue
        filepaths.add(filepath)
    yield filepaths

def test_ontology_paths_case(ontology_paths_case):
    assert len(ontology_paths_case) > 0, "Failed to glob CASE .ttl paths."

def test_ontology_paths_uco(ontology_paths_uco):
    assert len(ontology_paths_uco) > 0, "Failed to glob UCO .ttl paths."

def test_rdfs_term_names(rdfs_iris):
    assert len(rdfs_iris) > 0, "Failed to load closed set of RDFS IRIs."

#TODO - Uncomment this xfail line on adoption of UCO 0.6.0.
#TODO - Delete this xfail line on adoption of earliest UCO version that fixes the typos.
#@pytest.mark.xfail
def test_rdfs_typos(ontology_paths_case, ontology_paths_uco, rdfs_iris):
    turtle_filepaths = ontology_paths_case | ontology_paths_uco

    # Key: RDFS concept IRI, as a string.
    # Value: Basename of turtle file path, to identify potential typo sources.
    rdfs_iri_in_files = collections.defaultdict(set)

    for turtle_filepath in sorted(turtle_filepaths):
        graph = rdflib.Graph()
        _logger.debug("Parsing %r.", turtle_filepath)
        turtle_basename = os.path.basename(turtle_filepath)
        graph.parse(turtle_filepath, format="turtle")
        _logger.debug("len(graph) = %d.", len(graph))
        for (triple_no, triple) in enumerate(graph.triples((None, None, None))):
            if 0 == triple_no:
                _logger.debug("triple0 = %r.", (triple,))
            for term in triple:
                if not isinstance(term, rdflib.URIRef):
                    continue
                term_string = term.toPython()
                if term_string.startswith("http://www.w3.org/2000/01/rdf-schema#"):
                    rdfs_iri_in_files[term_string].add(turtle_basename)
    rdfs_iris_found = set([key for key in rdfs_iri_in_files.keys()])
    assert len(rdfs_iris_found) > 0, "No RDFS IRIs found."

    rdfs_iris_not_recognized = rdfs_iris_found - rdfs_iris
    try:
        assert rdfs_iris_not_recognized == set(), "Suspected non-RDFS IRI found."
    except:
        for iri in sorted(rdfs_iris_not_recognized):
            _logger.error("iri %r found in ontology files:", iri)
            for basename in sorted(rdfs_iri_in_files[iri]):
                _logger.error("* %s", basename)
        raise

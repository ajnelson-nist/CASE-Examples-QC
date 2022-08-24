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
This program takes as input a graph file (any format accepted by
RDFLib), and prints to stdout a sed script suitable for translating all
occurrences of those strings into the form accepted as part of the
resolution of UCO Issue 430.

The sed script can then be applied to whichever files need all instances
of an IRI converted.  The workflow which this script originally
supported involved running this program on a single JSON-LD file,
reviewing and adjusting the sed script to change stand-in patterns for
patterns meant to be encouraged among the CASE community, and then
applying the adjusted script with this command:

    sed -i -f issue_430_conformance.sed *.json *.md *.py *.sparql *.ttl

Note to avoid conflicts with some IRIs being prefixes of other IRIs, the
sed script is intentionally generated to apply in reverse sort order.

References:
* https://github.com/ucoProject/UCO/issues/430
"""

__version__ = "0.1.0"

import argparse
import typing
import uuid

import rdflib


def compact_iri(
    iri: rdflib.URIRef, prefix_local_part: rdflib.Namespace, prefix_label: str
) -> str:
    """
    :returns: Returns prefixed form.

    >>> import rdflib
    >>> ns1 = rdflib.Namespace("http://example.org/kb/")
    >>> iri1 = ns1["thing-1"]
    >>> compact_iri(iri1, ns1, "kb")
    'kb:thing-1'
    >>> ns2 = rdflib.Namespace("urn:example:")
    >>> compact_iri(iri1, ns2, "ex")
    'http://example.org/kb/thing-1'
    """
    return str(iri).replace(str(prefix_local_part), prefix_label + ":")


def main() -> None:
    parser = argparse.ArgumentParser()
    # Flag names drawn from Turtle specification:
    # https://www.w3.org/TR/turtle/#prefixed-name
    parser.add_argument("--prefix-label", default="kb")
    parser.add_argument("--prefix-local-part", default="http://example.org/kb/")
    parser.add_argument("in_graph")
    args = parser.parse_args()

    graph = rdflib.Graph()
    graph.parse(args.in_graph)
    ns_base = rdflib.Namespace(args.prefix_local_part)

    kb_subjects: typing.Set[rdflib.URIRef] = set()
    for triple in graph.triples((None, None, None)):
        for triple_member in [triple[0], triple[2]]:
            if isinstance(triple_member, rdflib.URIRef):
                if str(triple_member).startswith(str(ns_base)):
                    kb_subjects.add(triple_member)

    new_uuids_set: typing.Set[str] = set()
    for kb_subject in kb_subjects:
        new_uuids_set.add(str(uuid.uuid4()))
    new_uuids = sorted(new_uuids_set)

    substitution: typing.Dict[rdflib.URIRef, rdflib.URIRef] = dict()
    for (kb_subject_no, kb_subject) in enumerate(sorted(kb_subjects)):
        substitution[kb_subject] = rdflib.URIRef(
            str(kb_subject) + "-" + new_uuids[kb_subject_no]
        )

    for kb_subject in reversed(sorted(kb_subjects)):
        print(
            "s@%s@%s@g"
            % (
                compact_iri(kb_subject, ns_base, "kb"),
                compact_iri(substitution[kb_subject], ns_base, "kb"),
            )
        )


if __name__ == "__main__":
    main()

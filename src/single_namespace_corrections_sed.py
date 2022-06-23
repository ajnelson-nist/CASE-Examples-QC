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
This script emits a long series of sed commands to revise @type declarations and dictionary key names.

Only terms that appear in a single namespace are emitted.
"""

__version__ = "0.2.0"

import collections
import logging
import os

_logger = logging.getLogger(os.path.basename(__file__))


def main():
    nsdict = {
        "case-investigation": "https://caseontology.org/ontology/case/investigation#",
        "case-vocabulary": "https://caseontology.org/ontology/case/vocabulary#",
        "uco-action": "https://unifiedcyberontology.org/ontology/uco/action#",
        "uco-core": "https://unifiedcyberontology.org/ontology/uco/core#",
        "uco-identity": "https://unifiedcyberontology.org/ontology/uco/identity#",
        "uco-investigation": "https://unifiedcyberontology.org/ontology/uco/investigation#",
        "uco-location": "https://unifiedcyberontology.org/ontology/uco/location#",
        "uco-marking": "https://unifiedcyberontology.org/ontology/uco/marking#",
        "uco-observable": "https://unifiedcyberontology.org/ontology/uco/observable#",
        "uco-pattern": "https://unifiedcyberontology.org/ontology/uco/pattern#",
        "uco-role": "https://unifiedcyberontology.org/ontology/uco/role#",
        "uco-time": "https://unifiedcyberontology.org/ontology/uco/time#",
        "uco-tool": "https://unifiedcyberontology.org/ontology/uco/tool#",
        "uco-types": "https://unifiedcyberontology.org/ontology/uco/types#",
        "uco-victim": "https://unifiedcyberontology.org/ontology/uco/victim#",
    }

    nsdict_inverse = {nsdict[k]: k for k in nsdict.keys()}

    # Key: concept
    # Value: set of prefixes (the KEYS of nsdict above)
    concept_to_prefixes = collections.defaultdict(set)

    with open(args.in_file, "r") as in_fh:
        for line in in_fh:
            cleaned_line = line.strip()
            if cleaned_line == "":
                continue
            line_parts = cleaned_line.split("#")
            concept = line_parts[1]
            namespace = line_parts[0] + "#"
            prefix = nsdict_inverse[namespace]
            concept_to_prefixes[concept].add(prefix)

    for concept in sorted(concept_to_prefixes.keys()):
        prefixes = concept_to_prefixes[concept]
        if len(prefixes) > 1:
            # Concept appears in multiple namespaces.  Skip, as sed would make erroneous assignments.
            continue
        prefix = [x for x in prefixes][0]
        print(
            """\
s/"@type": "%s"/"@type": "%s:%s"/\
"""
            % (concept, prefix, concept)
        )
        print(
            """\
s/"%s": /"%s:%s": /\
"""
            % (concept, prefix, concept)
        )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("in_file")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    main()

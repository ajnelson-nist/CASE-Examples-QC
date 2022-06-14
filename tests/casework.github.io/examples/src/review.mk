#!/usr/bin/make -f

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

SHELL := /bin/bash

# GNU versions of utilities, prefixed with "g", are used here where possible because of unimportant whitespace and sorting differences appearing when using default utility names in macOS (which calls up the BSD versions) and Linux (which calls up the GNU versions).

COMM ?= $(shell which gcomm 2>/dev/null || which comm)
ifeq ($(COMM),)
$(error comm not found)
endif

SORT ?= $(shell which gsort 2>/dev/null || which sort)
ifeq ($(SORT),)
$(error sort not found)
endif

WC ?= $(shell which gwc 2>/dev/null || which wc)
ifeq ($(WC),)
$(error wc not found)
endif

top_srcdir := $(shell cd ../../../.. ; pwd)

rdf_toolkit_jar := $(top_srcdir)/dependencies/CASE-Examples/dependencies/CASE-unstable/dependencies/UCO/lib/rdf-toolkit.jar

subjectdir_basename := $(shell basename $$PWD)

all: \
  README.md

%.diff: \
  %
	test 1 -eq $$(git ls-tree HEAD $< | $(WC) -l)  # Confirm Markdown file is git-tracked.
	git diff $< > _$@
	@# Confirm patch file exists, but is empty.
	test -e _$@ && test ! -s _$@ \
	  || (echo "ERROR:review.mk:The file '$<' needs to be regenerated by running with 'make' and committing the update." >&2 ; exit 1)
	mv _$@ $@

$(rdf_toolkit_jar):
	@echo "ERROR:Makefile:rdf-toolkit.jar not downloaded; please run 'make download' from the top-level directory ($(top_srcdir))." >&2
	@exit 2

# BSD sed file replacements c/o:
#   https://stackoverflow.com/a/34070185
# This answer works if using GNU sed:
#   https://stackoverflow.com/a/6790967
README.md: \
  README.md.in \
  wc_l_undefined_kindOfRelationships.txt \
  wc_l_undefined_concepts.txt
	rm -f _$@ __$@
	cp README.md.in __$@
	sed \
	  -e '/@WC_L_UNDEFINED_KINDOFRELATIONSHIPS_TXT@/r wc_l_undefined_kindOfRelationships.txt' \
	  -e '/@WC_L_UNDEFINED_KINDOFRELATIONSHIPS_TXT@/d' \
	  __$@ \
	  > _$@
	cp _$@ __$@
	sed \
	  -e '/@WC_L_UNDEFINED_CONCEPTS_TXT@/r wc_l_undefined_concepts.txt' \
	  -e '/@WC_L_UNDEFINED_CONCEPTS_TXT@/d' \
	  __$@ \
	  > _$@
	rm __$@
	mv _$@ $@

$(subjectdir_basename).ttl: \
  $(top_srcdir)/dependencies/casework.github.io/examples/$(subjectdir_basename)/$(subjectdir_basename).json \
  $(rdf_toolkit_jar)
	java -jar $(rdf_toolkit_jar) \
	  --infer-base-iri \
	  --inline-blank-nodes \
	  --source $< \
	  --source-format json-ld \
	  --target $@_ \
	  --target-format turtle
	mv $@_ $@

# Tests:
# * The render of the README.md file and the local-ontology list that are tracked in Git are up-to-date.
# The .diff files should not be retained.  If any are found after calling 'make check', they illustrate a problem.
check: \
  README.md.diff \
  undefined_kindOfRelationships.tsv.diff \
  undefined_concepts.txt.diff
	@rm -f $^

clean:
	@rm -f \
	  *.tsv \
	  *.ttl \
	  *.txt \
	  *_

undefined_concepts.txt: \
  $(top_srcdir)/tests/ontology_vocabulary.txt \
  used_concepts.txt
	LC_ALL=C \
	  $(COMM) \
	    -13 \
	    $(top_srcdir)/tests/ontology_vocabulary.txt \
	    used_concepts.txt \
	    > $@_
	mv $@_ $@

undefined_kindOfRelationships.tsv: \
  used_kindOfRelationships.tsv \
  $(top_srcdir)/tests/ontology_relationship_literals.tsv
	LC_ALL=C \
	  $(COMM) \
	    -13 \
	    $(top_srcdir)/tests/ontology_relationship_literals.tsv \
	    <(LC_ALL=C $(SORT) $<) \
	    > $@_
	mv $@_ $@

# The grep patterns confirm that:
# * There is a namespace present (the colon - blank nodes were slipping by otherwise)
# * Expected namespaces like w3.org are ignored (egrep -v for acme, purl, w3)
# * Example knowledge base items are ignored (grep -v '/kb/')
used_concepts.txt: \
  $(subjectdir_basename).ttl \
  $(top_srcdir)/src/vocabulary_used.py
	source $(top_srcdir)/venv/bin/activate \
	  && python $(top_srcdir)/src/vocabulary_used.py \
	    $< \
	    > $@___
	grep ':' $@___ \
	  | egrep -v '(acme.org|atlassian.net|purl.org|w3.org)' \
	    | grep -v '/kb#' \
	      | grep -v '/kb/' \
	        > $@__
	rm $@___
	LC_ALL=C \
	  $(SORT) \
	    $@__ \
	    > $@_
	rm $@__
	mv $@_ $@

used_kindOfRelationships.tsv: \
  $(subjectdir_basename).ttl \
  $(top_srcdir)/src/data_relationship_literals_tsv.py
	source $(top_srcdir)/venv/bin/activate \
	  && python3 $(top_srcdir)/src/data_relationship_literals_tsv.py \
	    $< \
	    > $@_
	mv $@_ $@

wc_l_undefined_kindOfRelationships.txt: \
  undefined_kindOfRelationships.tsv
	$(WC) -l \
	  $< \
	  | grep -v ' total' \
	    > _$@
	mv _$@ $@

wc_l_undefined_concepts.txt: \
  undefined_concepts.txt
	$(WC) -l \
	  undefined_concepts.txt \
	  | grep -v ' total' \
	    > _$@
	mv _$@ $@

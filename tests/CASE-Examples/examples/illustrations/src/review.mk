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

SHELL = /bin/bash

# GNU versions of utilities, prefixed with "g", are used here where possible because of unimportant whitespace and sorting differences appearing when using default utility names in macOS (which calls up the BSD versions) and Linux (which calls up the GNU versions).

COMM ?= $(shell which gcomm 2>/dev/null || which comm)
ifeq ($(COMM),)
$(error comm not found)
endif

SORT ?= $(shell which gsort 2>/dev/null || which sort)
ifeq ($(SORT),)
$(error sort not found)
endif

top_srcdir := $(shell cd ../../../../.. ; pwd)

rdf_toolkit_jar := $(top_srcdir)/dependencies/CASE-Examples/dependencies/CASE-Utilities-Python/dependencies/CASE/lib/rdf-toolkit.jar

subjectdir_basename := $(shell basename $$PWD)

all: \
  $(subjectdir_basename).json \
  undefined_concepts.txt \
  undefined_kindOfRelationships.tsv

.PHONY: \
  normalize

$(rdf_toolkit_jar):
	@echo "ERROR:Makefile:rdf-toolkit.jar not downloaded; please run 'make download' from the top-level directory ($(top_srcdir))." >&2
	@exit 2

$(subjectdir_basename).json: \
  $(top_srcdir)/dependencies/CASE-Examples/examples/illustrations/$(subjectdir_basename)/$(subjectdir_basename).json
	source $(top_srcdir)/venv/bin/activate \
	  && python -m json.tool \
	    $< \
	    $@_
	mv $@_ $@

$(subjectdir_basename).ttl: \
  $(top_srcdir)/dependencies/CASE-Examples/examples/illustrations/$(subjectdir_basename)/$(subjectdir_basename).json \
  $(rdf_toolkit_jar)
	java -jar $(rdf_toolkit_jar) \
	  --infer-base-iri \
	  --inline-blank-nodes \
	  --source $< \
	  --source-format json-ld \
	  --target $@_ \
	  --target-format turtle
	mv $@_ $@

# 'Check' enforces that normalization works and further is how the files are tracked.
# (Reminder: diff exits non-0 on finding any differences.)
check: \
  $(subjectdir_basename).json \
  $(subjectdir_basename).ttl
	diff \
	  $(top_srcdir)/dependencies/CASE-Examples/examples/illustrations/$(subjectdir_basename)/$< \
	  $<

clean:
	@rm -f \
	  *.json \
	  *.tsv \
	  *.ttl \
	  *.txt \
	  *_

normalize: \
  $(subjectdir_basename).json \
  $(subjectdir_basename).ttl

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

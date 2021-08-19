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

SORT ?= $(shell which gsort 2>/dev/null || which sort)
ifeq ($(SORT),)
$(error sort not found)
endif

top_srcdir := ..

all: \
  all-CASE-Examples \
  all-casework.github.io

all-CASE-Examples: \
  ontology_relationship_literals.tsv \
  ontology_vocabulary.txt
	$(MAKE) \
	  --directory CASE-Examples

all-casework.github.io: \
  ontology_relationship_literals.tsv \
  ontology_vocabulary.txt
	$(MAKE) \
	  --directory casework.github.io

.PHONY: \
  all-CASE-Examples \
  all-casework.github.io \
  check-CASE-Examples \
  check-casework.github.io \
  check-rdfs \
  normalize

check: \
  check-CASE-Examples \
  check-casework.github.io \
  check-rdfs

check-CASE-Examples: \
  ontology_relationship_literals.tsv \
  ontology_vocabulary.txt
	$(MAKE) \
	  --directory CASE-Examples \
	  check

check-casework.github.io: \
  ontology_relationship_literals.tsv \
  ontology_vocabulary.txt
	$(MAKE) \
	  --directory casework.github.io \
	  check

check-rdfs:
	$(MAKE) \
	  --directory rdfs \
	  check

clean:
	@rm -f \
	  ontology_relationship_literals.tsv \
	  ontology_vocabulary.txt
	@$(MAKE) \
	  --directory casework.github.io \
	  clean
	@$(MAKE) \
	  --directory CASE-Examples \
	  clean

normalize: \
  $(top_srcdir)/.lib.done.log
	$(MAKE) \
	  --directory CASE-Examples \
	  normalize

ontology_relationship_literals.tsv: \
  $(top_srcdir)/src/ontology_relationship_literals_tsv.py
	source $(top_srcdir)/venv/bin/activate \
	  && python3 $(top_srcdir)/src/ontology_relationship_literals_tsv.py \
	    $(top_srcdir)/dependencies/CASE-Examples/dependencies/CASE-0.4.0/*-vocabulary.ttl \
	    > $@__
	LC_ALL=C \
	  $(SORT) \
	    $@__ \
	    > $@_
	rm $@__
	mv $@_ $@

#This file is needed to test examples in CASE-Examples and the website.
ontology_vocabulary.txt: \
  $(top_srcdir)/src/ontology_classes_properties.py
	source $(top_srcdir)/venv/bin/activate \
	  && python3 $(top_srcdir)/src/ontology_classes_properties.py \
	    $(top_srcdir)/dependencies/CASE-Examples/dependencies/CASE-0.4.0/*.ttl \
	    > $@__
	LC_ALL=C \
	  $(SORT) \
	    $@__ \
	    > $@_
	rm $@__
	mv $@_ $@

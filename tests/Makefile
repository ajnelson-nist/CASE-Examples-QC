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
  ontology_vocabulary.txt
	$(MAKE) \
	  --directory CASE-Examples

all-casework.github.io: \
  ontology_vocabulary.txt
	$(MAKE) \
	  --directory casework.github.io

.PHONY: \
  all-CASE-Examples \
  all-casework.github.io \
  check-CASE-Examples \
  check-casework.github.io \
  normalize

check: \
  check-CASE-Examples \
  check-casework.github.io

check-CASE-Examples: \
  ontology_vocabulary.txt
	$(MAKE) \
	  --directory CASE-Examples \
	  check

check-casework.github.io: \
  ontology_vocabulary.txt
	$(MAKE) \
	  --directory casework.github.io \
	  check

clean:
	@rm -f \
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

#This file is needed to test examples in CASE-Examples and the website.
ontology_vocabulary.txt: \
  $(top_srcdir)/src/ontology_classes_properties.py
	source $(top_srcdir)/venv/bin/activate \
	  && python $(top_srcdir)/src/ontology_classes_properties.py \
	    $(top_srcdir)/dependencies/CASE-Examples/dependencies/CASE/ontology/*/*ttl \
	    $(top_srcdir)/dependencies/CASE-Examples/dependencies/UCO/*/*ttl \
	    > $@__
	LC_ALL=C \
	  $(SORT) \
	    $@__ \
	    > $@_
	rm $@__
	mv $@_ $@

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

top_srcdir := $(shell cd .. ; pwd)

SORT ?= $(shell which gsort 2>/dev/null || which sort)
ifeq ($(SORT),)
$(error sort not found)
endif

WC ?= $(shell which gwc 2>/dev/null || which wc)
ifeq ($(WC),)
$(error wc not found)
endif

exdirs := \
  CASE-Examples/examples/illustrations \
  casework.github.io/examples

undefined_concepts_dependencies            := $(foreach exdir,$(exdirs),$(exdir)/undefined_concepts.txt)
undefined_kindOfRelationships_dependencies := $(foreach exdir,$(exdirs),$(exdir)/undefined_kindOfRelationships.tsv)
used_concepts_dependencies                 := $(foreach exdir,$(exdirs),$(exdir)/used_concepts.txt)
used_kindOfRelationships_dependencies      := $(foreach exdir,$(exdirs),$(exdir)/used_kindOfRelationships.tsv)

all: \
  undefined_concepts.txt \
  undefined_kindOfRelationships.tsv \
  used_concepts.txt \
  used_kindOfRelationships.tsv

check: \
  undefined_concepts.txt \
  undefined_kindOfRelationships.tsv \
  used_concepts.txt \
  used_kindOfRelationships.tsv
	#TODO - Test git-tracked state

clean:
	@rm -f \
	  *_ \
	  _* \
	  undefined_concepts.txt \
	  undefined_kindOfRelationships.tsv \
	  used_concepts.txt \
	  used_kindOfRelationships.tsv

undefined_concepts.txt: \
  $(undefined_concepts_dependencies)
	cat $^ \
	  | LC_ALL=C $(SORT) \
	    | uniq \
	      > $@_
	mv $@_ $@

undefined_kindOfRelationships.tsv: \
  $(undefined_kindOfRelationships_dependencies)
	cat $^ \
	  | LC_ALL=C $(SORT) \
	    | uniq \
	      > $@_
	mv $@_ $@

used_concepts.txt: \
  $(used_concepts_dependencies)
	cat $^ \
	  | LC_ALL=C $(SORT) \
	    | uniq \
	      > $@_
	mv $@_ $@

used_kindOfRelationships.tsv: \
  $(used_kindOfRelationships_dependencies)
	cat $^ \
	  | LC_ALL=C $(SORT) \
	    | uniq \
	      > $@_
	mv $@_ $@

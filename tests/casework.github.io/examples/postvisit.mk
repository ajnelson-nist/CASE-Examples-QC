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

top_srcdir := $(shell cd ../../.. ; pwd)

SORT ?= $(shell which gsort 2>/dev/null || which sort)
ifeq ($(SORT),)
$(error sort not found)
endif

WC ?= $(shell which gwc 2>/dev/null || which wc)
ifeq ($(WC),)
$(error wc not found)
endif

exdirs := $(shell find * -maxdepth 0 -type d | sort | egrep -v '^src$$')

undefined_concepts_dependencies            := $(foreach exdir,$(exdirs),$(exdir)/undefined_concepts.txt)
undefined_kindOfRelationships_dependencies := $(foreach exdir,$(exdirs),$(exdir)/undefined_kindOfRelationships.tsv)
used_concepts_dependencies                 := $(foreach exdir,$(exdirs),$(exdir)/used_concepts.txt)
used_kindOfRelationships_dependencies      := $(foreach exdir,$(exdirs),$(exdir)/used_kindOfRelationships.tsv)

all: \
  README.md \
  used_concepts.txt \
  used_kindOfRelationships.tsv

.PRECIOUS: \
  undefined_concepts.txt \
  undefined_kindOfRelationships.tsv \
  wc_l_undefined_concepts.txt \
  wc_l_undefined_kindOfRelationships.txt

# BSD sed file replacements c/o:
#   https://stackoverflow.com/a/34070185
# This answer works if using GNU sed:
#   https://stackoverflow.com/a/6790967
README.md: \
  README.md.in \
  wc_l_undefined_concepts.txt \
  wc_l_undefined_kindOfRelationships.txt
	rm -f _$@ __$@
	cp README.md.in __$@
	sed \
	  -e '/@WC_L_UNDEFINED_CONCEPTS_TXT@/r wc_l_undefined_concepts.txt' \
	  -e '/@WC_L_UNDEFINED_CONCEPTS_TXT@/d' \
	  __$@ \
	  > _$@
	cp _$@ __$@
	sed \
	  -e '/@WC_L_UNDEFINED_KINDOFRELATIONSHIPS_TXT@/r wc_l_undefined_kindOfRelationships.txt' \
	  -e '/@WC_L_UNDEFINED_KINDOFRELATIONSHIPS_TXT@/d' \
	  __$@ \
	  > _$@
	rm __$@
	mv _$@ $@

check: \
  README.md
	#TODO - Test git-tracked state

clean:
	@rm -f \
	  *_ \
	  _* \
	  README.md \
	  undefined_concepts.txt \
	  undefined_kindOfRelationships.tsv \
	  used_concepts.txt \
	  used_kindOfRelationships.tsv \
	  wc_l_undefined_concepts.txt \
	  wc_l_undefined_kindOfRelationships.txt

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

wc_l_undefined_concepts.txt: \
  undefined_concepts.txt
	$(WC) -l \
	  $(undefined_concepts_dependencies) \
	  undefined_concepts.txt \
	  | grep -v ' total' \
	    > _$@
	mv _$@ $@

wc_l_undefined_kindOfRelationships.txt: \
  undefined_kindOfRelationships.tsv
	$(WC) -l \
	  $(undefined_kindOfRelationships_dependencies) \
	  undefined_kindOfRelationships.tsv \
	  | grep -v ' total' \
	    > _$@
	mv _$@ $@

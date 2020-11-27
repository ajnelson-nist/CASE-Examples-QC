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

REALPATH ?= $(shell which grealpath 2>/dev/null || which realpath)
ifeq ($(REALPATH),)
$(error realpath not found)
endif

SORT ?= $(shell which gsort 2>/dev/null || which sort)
ifeq ($(SORT),)
$(error sort not found)
endif

WC ?= $(shell which gwc 2>/dev/null || which wc)
ifeq ($(WC),)
$(error wc not found)
endif

top_srcdir := $(shell $(REALPATH) ../../..)

FILES := \
  Oresteia \
  accounts \
  bulk_extractor_forensic_path \
  call_log \
  device \
  exif_data \
  file \
  forensic_lifecycle \
  location \
  message \
  mobile_device_and_sim_card \
  multipart_file \
  network_connection \
  raw_data \
  reconstructed_file \
  sms_and_contacts

NORMALIZED_JSON := $(foreach filename,$(FILES),$(filename).json)
NORMALIZED_TTL := $(foreach filename,$(FILES),$(filename).ttl)

CHECK_TARGETS := $(foreach filename,$(FILES),check-$(filename))

LOCAL_ONTOLOGY_VOCABULARY_TARGETS := $(foreach filename,$(FILES),local_ontology_vocabulary-$(filename).txt)

all: \
  README.md \
  single_namespace_corrections.sed

.PHONY: \
  normalize

$(top_srcdir)/.lib.done.log:
	@echo "ERROR:Makefile:rdf-toolkit.jar not downloaded; please run 'make download' from the top-level directory ($(top_srcdir))." >&2
	@exit 2

%.json: \
  $(top_srcdir)/dependencies/CASE-Examples/examples/%.json
	source $(top_srcdir)/venv/bin/activate \
	  && python -m json.tool \
	    $< \
	    $@_
	mv $@_ $@

%.ttl: \
  $(top_srcdir)/dependencies/CASE-Examples/examples/%.json \
  $(top_srcdir)/.lib.done.log
	java -jar $(top_srcdir)/lib/rdf-toolkit.jar \
	  --infer-base-iri \
	  --inline-blank-nodes \
	  --source $< \
	  --source-format json-ld \
	  --target $@_ \
	  --target-format turtle
	mv $@_ $@

# BSD sed file replacements c/o:
#   https://stackoverflow.com/a/34070185
# This answer works if using GNU sed:
#   https://stackoverflow.com/a/6790967
README.md: \
  .README.md.in \
  wc_l_local_ontology_vocabulary.txt
	rm -f _$@ __$@
	cp .README.md.in __$@
	sed \
	  -e '/@WC_L_LOCAL_ONTOLOGY_VOCABULARY_TXT@/r wc_l_local_ontology_vocabulary.txt' \
	  -e '/@WC_L_LOCAL_ONTOLOGY_VOCABULARY_TXT@/d' \
	  __$@ \
	  > _$@
	rm __$@
	mv _$@ $@

# 'Check' enforces that normalization works and further is how the files are tracked.
check: \
  $(CHECK_TARGETS)

# (Reminder: diff exits non-0 on finding any differences.)
# Dependency order: This recipe needs to have %.json be listed first among dependencies, so the instructions can use the first-dependency variable.
check-%: \
  %.json \
  %.ttl
	diff \
	  $(top_srcdir)/dependencies/CASE-Examples/examples/$< \
	  $<

clean:
	@rm -f \
	  *.json \
	  *.sed \
	  *.ttl \
	  *.txt \
	  *_
	@touch .README.md.in

# The grep patterns confirm that:
# * There is a namespace present (the colon - blank nodes were slipping by otherwise)
# * Expected namespaces like w3.org are ignored (egrep -v for acme, purl, w3)
# * Example knowledge base items are ignored (grep -v ':kb:')
local_ontology_vocabulary-%.txt: \
  %.ttl \
  $(top_srcdir)/src/vocabulary_used.py \
  $(top_srcdir)/tests/ontology_vocabulary.txt
	source $(top_srcdir)/venv/bin/activate \
	  && python $(top_srcdir)/src/vocabulary_used.py \
	    $< \
	    > $@___
	grep ':' $@___ \
	  | egrep -v '(acme.org|purl.org|w3.org)' \
	    | grep -v '/kb#' \
	      > $@__
	rm $@___
	LC_ALL=C \
	  $(COMM) \
	    -13 \
	    $(top_srcdir)/tests/ontology_vocabulary.txt \
	    <(LC_ALL=C $(SORT) $@__) \
	    > $@_
	rm $@__
	mv $@_ $@

normalize: \
  $(NORMALIZED_JSON) \
  $(NORMALIZED_TTL)

# This sed script is to help with unambiguous mappings that are straightforward mechanical work.
# To use it, run (e.g. for Oresteia):
#   sed -f single_namespace_corrections.sed Oresteia.json > mapped-Oresteia.json
single_namespace_corrections.sed: \
  $(top_srcdir)/src/single_namespace_corrections_sed.py \
  $(top_srcdir)/tests/ontology_vocabulary.txt
	source $(top_srcdir)/venv/bin/activate \
	  && python $(top_srcdir)/src/single_namespace_corrections_sed.py \
	    $(top_srcdir)/tests/ontology_vocabulary.txt \
	    > $@__
	LC_ALL=C $(SORT) $@__ > $@_
	rm $@__
	mv $@_ $@

undefined_vocabulary.txt: \
  $(LOCAL_ONTOLOGY_VOCABULARY_TARGETS)
	cat $^ \
	  | LC_ALL=C $(SORT) \
	    | uniq \
	      > $@_
	mv $@_ $@

wc_l_local_ontology_vocabulary.txt: \
  undefined_vocabulary.txt
	$(WC) -l \
	  $(LOCAL_ONTOLOGY_VOCABULARY_TARGETS) \
	  undefined_vocabulary.txt \
	  | grep -v ' total' \
	    > _$@
	mv _$@ $@

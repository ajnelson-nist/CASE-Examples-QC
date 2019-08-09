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
  single_namespace_corrections.sed \
  undefined_vocabulary.txt

.PHONY: \
  normalize

$(top_srcdir)/lib/rdf-toolkit.jar:
	@echo "ERROR:Makefile:rdf-toolkit.jar not downloaded; please run 'make download' from the top-level directory ($(top_srcdir))." >&2
	@exit 2

%.json: \
  $(top_srcdir)/deps/CASE/examples/%.json
	source $(top_srcdir)/venv/bin/activate \
	  && python -m json.tool \
	    $< \
	    $@_
	mv $@_ $@

%.ttl: \
  $(top_srcdir)/deps/CASE/examples/%.json \
  $(top_srcdir)/lib/rdf-toolkit.jar
	java -jar $(top_srcdir)/lib/rdf-toolkit.jar \
	  --infer-base-iri \
	  --inline-blank-nodes \
	  --source $< \
	  --source-format json-ld \
	  --target $@_ \
	  --target-format turtle
	mv $@_ $@

# 'Check' enforces that normalization works and further is how the files are tracked.
check: \
  $(CHECK_TARGETS)

# (Reminder: diff exits non-0 on finding any differences.)
# Dependency order: This recipe needs to have %.json be listed first among dependencies, so the instructions can use the first-dependency variable.
check-%: \
  %.json \
  %.ttl
	diff \
	  $(top_srcdir)/deps/CASE/examples/$< \
	  $<

clean:
	@rm -f \
	  *.json \
	  *.sed \
	  *.ttl \
	  *.txt \
	  *_

# The grep patterns confirm that:
# * There is a namespace present (the colon - blank nodes were slipping by otherwise)
# * Expected namespaces like w3.org are ignored (egrep -v for acme, purl, w3)
# * Example knowledge base items are ignored (grep -v ':kb:')
local_ontology_vocabulary-%.txt: \
  %.ttl \
  $(top_srcdir)/src/vocabulary_used.py \
  ontology_vocabulary.txt
	source $(top_srcdir)/venv/bin/activate \
	  && python $(top_srcdir)/src/vocabulary_used.py \
	    $< \
	    > $@___
	grep ':' $@___ \
	  | egrep -v '(acme.org|purl.org|w3.org)' \
	    | grep -v ':kb:' \
	      > $@__
	rm $@___
	$(COMM) \
	  -13 \
	  ontology_vocabulary.txt \
	  $@__ \
	  > $@_
	rm $@__
	mv $@_ $@

normalize: \
  $(NORMALIZED_JSON) \
  $(NORMALIZED_TTL)

ontology_vocabulary.txt: \
  $(top_srcdir)/src/ontology_classes_properties.py
	source $(top_srcdir)/venv/bin/activate \
	  && python $(top_srcdir)/src/ontology_classes_properties.py \
	    $(top_srcdir)/deps/{CASE,UCO}/*/*ttl \
	    > $@_
	mv $@_ $@

# This sed script is to help with unambiguous mappings that are straightforward mechanical work.
# To use it, run (e.g. for Oresteia):
#   sed -f single_namespace_corrections.sed Oresteia.json > mapped-Oresteia.json
single_namespace_corrections.sed: \
  $(top_srcdir)/src/single_namespace_corrections_sed.py \
  ontology_vocabulary.txt
	source $(top_srcdir)/venv/bin/activate \
	  && python $(top_srcdir)/src/single_namespace_corrections_sed.py \
	    ontology_vocabulary.txt \
	    > $@__
	$(SORT) $@__ > $@_
	rm $@__
	mv $@_ $@

undefined_vocabulary.txt: \
  $(LOCAL_ONTOLOGY_VOCABULARY_TARGETS)
	cat $^ \
	  | $(SORT) \
	    | uniq \
	      > $@_
	mv $@_ $@

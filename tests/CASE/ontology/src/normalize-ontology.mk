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

# This Makefile is assumed to execute in a directory three directories
# deep into the repository, as indicated by the variable top_srcdir.

SHELL = /bin/bash

GREALPATH ?= $(shell which grealpath 2>/dev/null || which realpath)
ifeq ($(GREALPATH),)
$(error GNU realpath not found)
endif

# E.g. master/master.ttl
TARGET_TTL_RELPATH ?=
ifeq ($(TARGET_TTL_RELPATH),)
$(error Required parameter TARGET_TTL_RELPATH, as relative path from /ontology under the CASE repository root, not found)
endif

TARGET_TTL_BASENAME := $(shell basename $(TARGET_TTL_RELPATH))

top_srcdir := $(shell $(GREALPATH) ../../../..)

all: \
  $(TARGET_TTL_BASENAME)

.PHONY: \
  normalize

$(TARGET_TTL_BASENAME): \
  $(top_srcdir)/dependencies/CASE-Examples/dependencies/CASE/ontology/$(TARGET_TTL_RELPATH) \
  $(top_srcdir)/lib/rdf-toolkit.jar
	java -jar $(top_srcdir)/lib/rdf-toolkit.jar \
	  --infer-base-iri \
	  --inline-blank-nodes \
	  --source $< \
	  --source-format turtle \
	  --target $@_ \
	  --target-format turtle
	mv $@_ $@

$(top_srcdir)/lib/rdf-toolkit.jar:
	@echo "ERROR:Makefile:rdf-toolkit.jar not downloaded; please run 'make download' from the top-level directory ($(top_srcdir))." >&2
	@exit 2

# (Reminder: diff exits non-0 on finding any differences.)
check: \
  $(TARGET_TTL_BASENAME)
	diff \
	  $(top_srcdir)/dependencies/CASE-Examples/dependencies/CASE/ontology/$(TARGET_TTL_RELPATH) \
	  $(TARGET_TTL_BASENAME)

normalize: \
  $(TARGET_TTL_BASENAME)

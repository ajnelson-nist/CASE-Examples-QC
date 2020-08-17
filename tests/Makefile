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

top_srcdir := ..

all:
	$(MAKE) \
	  --directory CASE-Examples

.PHONY: \
  check-CASE \
  check-CASE-Examples \
  clean-CASE \
  clean-CASE-Examples \
  normalize \
  normalize-CASE \
  normalize-CASE-Examples

check: \
  check-CASE \
  check-CASE-Examples

check-CASE:
	$(MAKE) \
	  --directory CASE \
	  check

check-CASE-Examples:
	$(MAKE) \
	  --directory CASE-Examples \
	  check

clean: \
  clean-CASE \
  clean-CASE-Examples

clean-CASE:
	@$(MAKE) \
	  --directory CASE \
	  clean

clean-CASE-Examples:
	@$(MAKE) \
	  --directory CASE-Examples \
	  clean

normalize: \
  normalize-CASE \
  normalize-CASE-Examples

normalize-CASE: \
  $(top_srcdir)/lib/rdf-toolkit.jar
	$(MAKE) \
	  --directory CASE \
	  normalize

normalize-CASE-Examples: \
  $(top_srcdir)/lib/rdf-toolkit.jar
	$(MAKE) \
	  --directory CASE-Examples \
	  normalize

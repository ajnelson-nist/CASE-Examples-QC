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

# TODO: This Makefile can include additional rules to add UCO to the
# unit test suite.  Unfortunately, at the time of this writing, UCO's
# primary branch has normalization errors, so the tests are temporarily
# omitted.

SHELL := /bin/bash

top_srcdir := ../../..

all: \
  all-CASE \
  all-UCO

all-CASE:
	$(MAKE) \
	  --directory CASE

all-UCO:
	$(MAKE) \
	  --directory UCO

.PHONY: \
  all-CASE \
  all-UCO \
  check-CASE \
  check-UCO \
  clean-CASE \
  clean-UCO \
  normalize \
  normalize-CASE \
  normalize-UCO

# TODO: When UCO incorporates rdf-toolkit in its merge review process,
# add check-UCO to this dependency list.
check: \
  check-CASE

check-CASE:
	$(MAKE) \
	  --directory CASE \
	  check

check-UCO:
	$(MAKE) \
	  --directory UCO \
	  check

clean: \
  clean-CASE \
  clean-UCO

clean-CASE:
	@$(MAKE) \
	  --directory CASE \
	  clean

clean-UCO:
	@$(MAKE) \
	  --directory UCO \
	  clean

normalize: \
  normalize-CASE \
  normalize-UCO

normalize-CASE: \
  $(top_srcdir)/.lib.done.log
	$(MAKE) \
	  --directory CASE \
	  normalize

normalize-UCO: \
  $(top_srcdir)/.lib.done.log
	$(MAKE) \
	  --directory UCO \
	  normalize

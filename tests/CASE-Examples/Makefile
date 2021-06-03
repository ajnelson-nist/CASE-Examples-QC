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

top_srcdir := ../..

all:
	$(MAKE) \
	  --directory examples/illustrations

.PHONY: \
  check-dependencies \
  check-examples \
  clean-dependencies \
  clean-examples \
  normalize \
  normalize-dependencies \
  normalize-examples

check: \
  check-dependencies \
  check-examples

check-dependencies:
	$(MAKE) \
	  --directory dependencies/CASE-0.4.0 \
	  check

check-examples:
	$(MAKE) \
	  --directory examples/illustrations \
	  check

clean: \
  clean-dependencies \
  clean-examples

clean-dependencies:
	@$(MAKE) \
	  --directory dependencies/CASE-0.4.0 \
	  clean

clean-examples:
	@$(MAKE) \
	  --directory examples/illustrations \
	  clean

normalize: \
  normalize-dependencies \
  normalize-examples

normalize-dependencies: \
  $(top_srcdir)/.lib.done.log
	$(MAKE) \
	  --directory dependencies/CASE-0.4.0 \
	  normalize

normalize-examples: \
  $(top_srcdir)/.lib.done.log
	$(MAKE) \
	  --directory examples/illustrations \
	  normalize

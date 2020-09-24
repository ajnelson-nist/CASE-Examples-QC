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

all: \
  all-CASE-Examples \
  all-casework.github.io

all-CASE-Examples:
	$(MAKE) \
	  --directory CASE-Examples

all-casework.github.io:
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

check-CASE-Examples:
	$(MAKE) \
	  --directory CASE-Examples \
	  check

check-casework.github.io:
	$(MAKE) \
	  --directory casework.github.io \
	  check

clean:
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

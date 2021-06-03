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

top_srcdir := ../../../..

all: \
  all-UCO

all-UCO:
	$(MAKE) \
	  --directory UCO

.PHONY: \
  all-UCO \
  check-UCO \
  clean-UCO \
  normalize \
  normalize-UCO

check: \
  check-UCO

check-UCO:
	$(MAKE) \
	  --directory UCO \
	  check

clean: \
  clean-UCO

clean-UCO:
	@$(MAKE) \
	  --directory UCO \
	  clean

normalize: \
  normalize-UCO

normalize-UCO: \
  $(top_srcdir)/.lib.done.log
	$(MAKE) \
	  --directory UCO \
	  normalize

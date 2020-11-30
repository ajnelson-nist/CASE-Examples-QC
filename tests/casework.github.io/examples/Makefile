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

top_srcdir := ../../..

all: \
  all-asgard \
  all-owl_trafficking \
  all-urgent_evidence

all-asgard:
	$(MAKE) \
	  --directory asgard

all-owl_trafficking:
	$(MAKE) \
	  --directory owl_trafficking

all-urgent_evidence:
	$(MAKE) \
	  --directory urgent_evidence

.PHONY: \
  all-asgard \
  all-owl_trafficking \
  all-urgent-evidence \
  check-asgard \
  check-owl_trafficking \
  check-urgent-evidence

check: \
  check-asgard \
  check-owl_trafficking \
  check-urgent-evidence

check-asgard:
	$(MAKE) \
	  --directory asgard \
	  check

check-owl_trafficking:
	$(MAKE) \
	  --directory owl_trafficking \
	  check

check-urgent_evidence:
	$(MAKE) \
	  --directory urgent_evidence \
	  check

clean:
	@$(MAKE) \
	  --directory asgard \
	  clean
	@$(MAKE) \
	  --directory owl_trafficking \
	  clean
	@$(MAKE) \
	  --directory urgent_evidence \
	  clean

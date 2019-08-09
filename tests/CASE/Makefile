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

all: \
  all-examples

.PHONY: \
  all-examples \
  check-case-core \
  check-case-master \
  check-examples \
  normalize \
  normalize-case-core \
  normalize-case-master \
  normalize-examples

all-examples:
	$(MAKE) \
	  --directory examples

check: \
  check-case-core \
  check-case-master \
  check-examples

check-case-core: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory case-core \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=case-core/core.ttl \
	  check

check-case-master: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory case-master \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=case-master/case.ttl \
	  check

check-examples:
	$(MAKE) \
	  --directory examples \
	  check

clean:
	@$(MAKE) \
	  --directory examples \
	  clean

normalize: \
  normalize-case-core \
  normalize-case-master \
  normalize-examples

normalize-case-core: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory case-core \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=case-core/core.ttl \
	  normalize

normalize-case-master: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory case-master \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=case-master/case.ttl \
	  normalize

normalize-examples:
	$(MAKE) \
	  --directory examples \
	  normalize

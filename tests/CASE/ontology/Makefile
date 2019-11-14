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

# This recipe intentionally left blank.
all:

.PHONY: \
  check-core \
  check-master \
  normalize \
  normalize-core \
  normalize-master

check: \
  check-core \
  check-master

check-core: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory core \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=core/core.ttl \
	  check

check-master: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory master \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=master/case.ttl \
	  check

# This recipe intentionally left blank.
clean:

normalize: \
  normalize-core \
  normalize-master

normalize-core: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory core \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=core/core.ttl \
	  normalize

normalize-master: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory master \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=master/case.ttl \
	  normalize

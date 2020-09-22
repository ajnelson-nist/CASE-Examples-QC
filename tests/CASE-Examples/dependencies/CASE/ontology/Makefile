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
  check-investigation \
  check-master \
  check-vocabulary \
  clean-investigation \
  clean-master \
  clean-vocabulary \
  normalize \
  normalize-investigation \
  normalize-master \
  normalize-vocabulary

check: \
  check-investigation \
  check-master \
  check-vocabulary

check-investigation: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory investigation \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=investigation/investigation.ttl \
	  check

check-master: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory master \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=master/case.ttl \
	  check

check-vocabulary: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory vocabulary \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=vocabulary/vocabulary.ttl \
	  check

clean: \
  clean-investigation \
  clean-master \
  clean-vocabulary

clean-investigation:
	@$(MAKE) \
	  --directory investigation \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=investigation/investigation.ttl \
	  clean

clean-master:
	@$(MAKE) \
	  --directory master \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=master/case.ttl \
	  clean

clean-vocabulary:
	@$(MAKE) \
	  --directory vocabulary \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=vocabulary/vocabulary.ttl \
	  clean

normalize: \
  normalize-investigation \
  normalize-master \
  normalize-vocabulary

normalize-investigation: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory investigation \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=investigation/investigation.ttl \
	  normalize

normalize-master: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory master \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=master/case.ttl \
	  normalize

normalize-vocabulary: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory vocabulary \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=vocabulary/vocabulary.ttl \
	  normalize

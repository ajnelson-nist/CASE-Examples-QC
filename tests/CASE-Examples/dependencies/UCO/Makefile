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

# This recipe intentionally left blank.
all:

.PHONY: \
  check-action \
  check-core \
  check-identity \
  check-location \
  check-marking \
  check-master \
  check-observable \
  check-pattern \
  check-role \
  check-time \
  check-tool \
  check-types \
  check-victim \
  check-vocabulary \
  normalize \
  normalize-action \
  normalize-core \
  normalize-identity \
  normalize-location \
  normalize-marking \
  normalize-master \
  normalize-observable \
  normalize-pattern \
  normalize-role \
  normalize-time \
  normalize-tool \
  normalize-types \
  normalize-victim \
  normalize-vocabulary

check: \
  check-action \
  check-core \
  check-identity \
  check-location \
  check-marking \
  check-master \
  check-observable \
  check-pattern \
  check-role \
  check-time \
  check-tool \
  check-types \
  check-victim \
  check-vocabulary

check-action: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-action \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-action/action.ttl \
	  check
	$(MAKE) \
	  --directory uco-action \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-action/action-da.ttl \
	  check

check-core: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-core \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-core/core.ttl \
	  check
	$(MAKE) \
	  --directory uco-core \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-core/core-da.ttl \
	  check

check-identity: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-identity \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-identity/identity.ttl \
	  check
	$(MAKE) \
	  --directory uco-identity \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-identity/identity-da.ttl \
	  check

check-location: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-location \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-location/location.ttl \
	  check
	$(MAKE) \
	  --directory uco-location \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-location/location-da.ttl \
	  check

check-marking: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-marking \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-marking/marking.ttl \
	  check
	$(MAKE) \
	  --directory uco-marking \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-marking/marking-da.ttl \
	  check

# NOTE - Does not fit remainder of file path pattern.
check-master: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-master \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-master/uco.ttl \
	  check

check-observable: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-observable \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-observable/observable.ttl \
	  check
	$(MAKE) \
	  --directory uco-observable \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-observable/observable-da.ttl \
	  check

check-pattern: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-pattern \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-pattern/pattern.ttl \
	  check
	$(MAKE) \
	  --directory uco-pattern \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-pattern/pattern-da.ttl \
	  check

check-role: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-role \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-role/role.ttl \
	  check

check-time: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-time \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-time/time.ttl \
	  check

check-tool: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-tool \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-tool/tool.ttl \
	  check
	$(MAKE) \
	  --directory uco-tool \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-tool/tool-da.ttl \
	  check

check-types: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-types \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-types/types.ttl \
	  check
	$(MAKE) \
	  --directory uco-types \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-types/types-da.ttl \
	  check

check-victim: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-victim \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-victim/victim.ttl \
	  check

check-vocabulary: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-vocabulary \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-vocabulary/vocabulary.ttl \
	  check

clean: \
  clean-action \
  clean-core \
  clean-identity \
  clean-location \
  clean-marking \
  clean-master \
  clean-observable \
  clean-pattern \
  clean-role \
  clean-time \
  clean-tool \
  clean-types \
  clean-victim \
  clean-vocabulary

clean-action: \
  src/normalize-ontology.mk
	@$(MAKE) \
	  --directory uco-action \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-action/action.ttl \
	  clean

clean-core: \
  src/normalize-ontology.mk
	@$(MAKE) \
	  --directory uco-core \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-core/core.ttl \
	  clean

clean-identity: \
  src/normalize-ontology.mk
	@$(MAKE) \
	  --directory uco-identity \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-identity/identity.ttl \
	  clean

clean-location: \
  src/normalize-ontology.mk
	@$(MAKE) \
	  --directory uco-location \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-location/location.ttl \
	  clean

clean-marking: \
  src/normalize-ontology.mk
	@$(MAKE) \
	  --directory uco-marking \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-marking/marking.ttl \
	  clean

# NOTE - Does not fit remainder of file path pattern.
clean-master: \
  src/normalize-ontology.mk
	@$(MAKE) \
	  --directory uco-master \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-master/uco.ttl \
	  clean

clean-observable: \
  src/normalize-ontology.mk
	@$(MAKE) \
	  --directory uco-observable \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-observable/observable.ttl \
	  clean

clean-pattern: \
  src/normalize-ontology.mk
	@$(MAKE) \
	  --directory uco-pattern \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-pattern/pattern.ttl \
	  clean

clean-role: \
  src/normalize-ontology.mk
	@$(MAKE) \
	  --directory uco-role \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-role/role.ttl \
	  clean

clean-time: \
  src/normalize-ontology.mk
	@$(MAKE) \
	  --directory uco-time \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-time/time.ttl \
	  clean

clean-tool: \
  src/normalize-ontology.mk
	@$(MAKE) \
	  --directory uco-tool \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-tool/tool.ttl \
	  clean

clean-types: \
  src/normalize-ontology.mk
	@$(MAKE) \
	  --directory uco-types \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-types/types.ttl \
	  clean

clean-victim: \
  src/normalize-ontology.mk
	@$(MAKE) \
	  --directory uco-victim \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-victim/victim.ttl \
	  clean

clean-vocabulary: \
  src/normalize-ontology.mk
	@$(MAKE) \
	  --directory uco-vocabulary \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-vocabulary/vocabulary.ttl \
	  clean


normalize: \
  normalize-action \
  normalize-core \
  normalize-identity \
  normalize-location \
  normalize-marking \
  normalize-master \
  normalize-observable \
  normalize-pattern \
  normalize-role \
  normalize-time \
  normalize-tool \
  normalize-types \
  normalize-victim \
  normalize-vocabulary

normalize-action: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-action \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-action/action.ttl \
	  normalize

normalize-core: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-core \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-core/core.ttl \
	  normalize

normalize-identity: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-identity \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-identity/identity.ttl \
	  normalize

normalize-location: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-location \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-location/location.ttl \
	  normalize

normalize-marking: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-marking \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-marking/marking.ttl \
	  normalize

# NOTE - Does not fit remainder of file path pattern.
normalize-master: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-master \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-master/uco.ttl \
	  normalize

normalize-observable: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-observable \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-observable/observable.ttl \
	  normalize

normalize-pattern: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-pattern \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-pattern/pattern.ttl \
	  normalize

normalize-role: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-role \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-role/role.ttl \
	  normalize

normalize-time: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-time \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-time/time.ttl \
	  normalize

normalize-tool: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-tool \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-tool/tool.ttl \
	  normalize

normalize-types: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-types \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-types/types.ttl \
	  normalize

normalize-victim: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-victim \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-victim/victim.ttl \
	  normalize

normalize-vocabulary: \
  src/normalize-ontology.mk
	$(MAKE) \
	  --directory uco-vocabulary \
	  --file $$PWD/src/normalize-ontology.mk \
	  TARGET_TTL_RELPATH=uco-vocabulary/vocabulary.ttl \
	  normalize

#!/usr/bin/make -f

# Portions of this file contributed by NIST are governed by the
# following statement:
#
# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to Title 17 Section 105 of the
# United States Code, this software is not subject to copyright
# protection within the United States. NIST assumes no responsibility
# whatsoever for its use by other parties, and makes no guarantees,
# expressed or implied, about its quality, reliability, or any other
# characteristic.
#
# We would appreciate acknowledgement if the software is used.

SHELL := /bin/bash

exdirs := $(shell find * -maxdepth 0 -type d | sort | egrep -v '^src$$')

all_targets   := $(foreach exdir,$(exdirs),all-$(exdir))
check_targets := $(foreach exdir,$(exdirs),check-$(exdir))
clean_targets := $(foreach exdir,$(exdirs),clean-$(exdir))

all: \
  $(all_targets)
	LC_ALL=C \
	  $(MAKE) \
	    --file postvisit.mk

all-%:
	$(MAKE) \
	  --directory $$(echo $@ | sed -e 's/^all-//') \
	  --file $$PWD/src/review.mk

check: \
  $(check_targets)
	LC_ALL=C \
	  $(MAKE) \
	    --file postvisit.mk \
	    check

check-%:
	$(MAKE) \
	  --directory $$(echo $@ | sed -e 's/^check-//') \
	  --file $$PWD/src/review.mk \
	  check

clean: \
  $(clean_targets)
	@$(MAKE) \
	  --file postvisit.mk \
	  clean

clean-%:
	@$(MAKE) \
	  --directory $$(echo $@ | sed -e 's/^clean-//') \
	  --file $$PWD/src/review.mk \
	  clean

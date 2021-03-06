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

illdirs := $(shell find * -maxdepth 0 -type d | sort | egrep -v '^src$$')

all_targets       := $(foreach illdir,$(illdirs),all-$(illdir))
check_targets     := $(foreach illdir,$(illdirs),check-$(illdir))
clean_targets     := $(foreach illdir,$(illdirs),clean-$(illdir))
normalize_targets := $(foreach illdir,$(illdirs),normalize-$(illdir))

all: \
  $(all_targets)
	$(MAKE) \
	  --file postvisit.mk

all-%:
	$(MAKE) \
	  --directory $$(echo $@ | sed -e 's/^all-//') \
	  --file $$PWD/src/review.mk

check: \
  $(check_targets)
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

normalize: \
  $(normalize_targets)

normalize-%:
	$(MAKE) \
	  --directory $$(echo $@ | sed -e 's/^normalize-//') \
	  --file $$PWD/src/review.mk \
	  normalize

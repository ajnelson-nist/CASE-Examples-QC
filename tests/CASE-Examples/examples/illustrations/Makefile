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

top_srcdir := $(shell cd ../../../.. ; pwd)

illustrations_dir := $(top_srcdir)/dependencies/CASE-Examples/examples/illustrations

illdirs := $(shell cd $(illustrations_dir) ; find * -maxdepth 0 -type d | sort | egrep -v '^src$$')

all_targets       := $(foreach illdir,$(illdirs),all-$(illdir))
check_targets     := $(foreach illdir,$(illdirs),check-$(illdir))
clean_targets     := $(foreach illdir,$(illdirs),clean-$(illdir))

all: \
  $(all_targets)
	LC_ALL=C \
	  $(MAKE) \
	    --file postvisit.mk

all-%:
	$(MAKE) \
	  --directory $$(echo $@ | sed -e 's/^all-//')

check: \
  $(check_targets)
	LC_ALL=C \
	  $(MAKE) \
	    --file postvisit.mk \
	    check

check-%:
	$(MAKE) \
	  --directory $$(echo $@ | sed -e 's/^check-//') \
	  check

clean: \
  $(clean_targets)
	@$(MAKE) \
	  --file postvisit.mk \
	  clean

clean-%:
	@$(MAKE) \
	  --directory $$(echo $@ | sed -e 's/^clean-//') \
	  clean

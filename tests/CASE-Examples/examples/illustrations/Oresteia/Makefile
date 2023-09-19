#!/usr/bin/make -f

# Portions of this file contributed by NIST are governed by the following
# statement:
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

include ../src/review.mk

# Augment 'all' with extra figures for Oresteia.
all: \
  $(subjectdir_basename)-prov-focus-sms-message-4e9bfb9e-c4b4-4ebd-a7b0-a49eba0811a6.svg \
  $(subjectdir_basename)-prov-focus-sms-message-853716fe-c35e-45af-81d3-368dfb6b7eba.svg

$(subjectdir_basename)-prov-focus-sms-message-4e9bfb9e-c4b4-4ebd-a7b0-a49eba0811a6.dot: \
  $(subjectdir_basename)-prov.ttl
	source $(top_srcdir)/venv/bin/activate \
	  && case_prov_dot \
	    --debug \
	    --entity-ancestry http://example.org/kb/sms-message-4e9bfb9e-c4b4-4ebd-a7b0-a49eba0811a6 \
	    _$@ \
	    $<
	mv _$@ $@

$(subjectdir_basename)-prov-focus-sms-message-853716fe-c35e-45af-81d3-368dfb6b7eba.dot: \
  $(subjectdir_basename)-prov.ttl
	source $(top_srcdir)/venv/bin/activate \
	  && case_prov_dot \
	    --debug \
	    --entity-ancestry http://example.org/kb/sms-message-853716fe-c35e-45af-81d3-368dfb6b7eba \
	    _$@ \
	    $<
	mv _$@ $@

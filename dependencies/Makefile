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

top_srcdir := $(shell cd .. ; pwd)

all: \
  CASE-Corpora/dependencies/CASE-develop.ttl \
  CASE-Corpora/dependencies/CASE-develop-2.0.0.ttl \
  CASE-Corpora/dependencies/CASE-unstable.ttl \
  CASE-Corpora/dependencies/CASE-unstable-2.0.0.ttl \
  imports-transitive.ttl

CASE-Corpora/dependencies/CASE-develop.ttl: \
  CASE-Corpora/dependencies/dependencies.ttl
	@#Guarantee timestamp order.
	touch -c $@
	test -r $@

CASE-Corpora/dependencies/CASE-develop-2.0.0.ttl: \
  CASE-Corpora/dependencies/dependencies.ttl
	@#Guarantee timestamp order.
	touch -c $@
	test -r $@

CASE-Corpora/dependencies/CASE-unstable.ttl: \
  CASE-Corpora/dependencies/dependencies.ttl
	@#Guarantee timestamp order.
	touch -c $@
	test -r $@

CASE-Corpora/dependencies/CASE-unstable-2.0.0.ttl: \
  CASE-Corpora/dependencies/dependencies.ttl
	@#Guarantee timestamp order.
	touch -c $@
	test -r $@

CASE-Corpora/dependencies/CDO-Shapes-Time/shapes/sh-time.ttl: \
  CASE-Corpora/dependencies/dependencies.ttl
	test -r $@

CASE-Corpora/dependencies/dependencies.ttl: \
  CASE-Corpora/.gitmodules
	$(MAKE) \
	  --directory CASE-Corpora \
	  all-dependencies
	test -r $@

CASE-Corpora/shapes/shapes.ttl: \
  CASE-Corpora/dependencies/dependencies.ttl
	$(MAKE) \
	  --directory CASE-Corpora \
	  all-shapes
	test -r $@

check: \
  all

clean:
	@rm -f \
	  *.ttl

imports-transitive.ttl: \
  CASE-Corpora/catalog/shared.ttl \
  CASE-Corpora/dependencies/dependencies.ttl \
  CASE-Corpora/ontology/case-corpora.ttl \
  CASE-Corpora/shapes/shapes.ttl \
  CASE-Corpora/taxonomy/devices/drafting.ttl \
  CASE-Examples/examples/illustrations/file/drafting.ttl \
  CASE-Examples/examples/illustrations/partitions/drafting.ttl \
  CASE-Examples/examples/illustrations/spear_phishing/drafting.ttl \
  UCO-Profile-BFO/dependencies/CDO-Shapes-BFO/dependencies/BFO.ttl \
  UCO-Profile-BFO/dependencies/CDO-Shapes-BFO/shapes/sh-bfo.ttl \
  UCO-Profile-BFO/ontology/uco-bfo.ttl \
  UCO-Profile-FOAF/dependencies/CDO-Shapes-FOAF/dependencies/foaf.ttl \
  UCO-Profile-FOAF/dependencies/CDO-Shapes-FOAF/shapes/sh-foaf.ttl \
  UCO-Profile-FOAF/ontology/uco-foaf.ttl \
  UCO-Profile-GeoSPARQL/dependencies/CDO-Shapes-GeoSPARQL/dependencies/geo.ttl \
  UCO-Profile-GeoSPARQL/dependencies/CDO-Shapes-GeoSPARQL/shapes/sh-geo.ttl \
  UCO-Profile-GeoSPARQL/ontology/uco-geo.ttl \
  UCO-Profile-GeoSPARQL/shapes/sh-uco-geo.ttl \
  UCO-Profile-Time/dependencies/CDO-Shapes-Time/dependencies/time.ttl \
  UCO-Profile-Time/dependencies/CDO-Shapes-Time/shapes/sh-time.ttl \
  UCO-Profile-Time/ontology/uco-time.ttl \
  UCO-Profile-Time/shapes/sh-uco-time.ttl \
  UCO-Profile-gufo/dependencies/CDO-Shapes-gufo/dependencies/gufo.ttl \
  UCO-Profile-gufo/dependencies/CDO-Shapes-gufo/shapes/sh-gufo.ttl \
  UCO-Profile-gufo/ontology/uco-gufo.ttl
	source $(top_srcdir)/venv/bin/activate \
	  && rdfpipe \
	    --output-format turtle \
	    $^ \
	    > _$@
	mv _$@ $@

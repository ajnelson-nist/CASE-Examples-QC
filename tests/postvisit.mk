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

top_srcdir := $(shell cd .. ; pwd)

SORT ?= $(shell which gsort 2>/dev/null || which sort)
ifeq ($(SORT),)
$(error sort not found)
endif

WC ?= $(shell which gwc 2>/dev/null || which wc)
ifeq ($(WC),)
$(error wc not found)
endif

rdf_toolkit_jar := $(top_srcdir)/dependencies/CASE-Examples/dependencies/CASE-develop/dependencies/UCO/lib/rdf-toolkit.jar

exdirs := \
  CASE-Corpora/catalog \
  CASE-Examples/examples/illustrations \
  casework.github.io/examples

undefined_concepts_dependencies            := $(foreach exdir,$(exdirs),$(exdir)/undefined_concepts.txt)
undefined_kindOfRelationships_dependencies := $(foreach exdir,$(exdirs),$(exdir)/undefined_kindOfRelationships.tsv)
used_concepts_dependencies                 := $(foreach exdir,$(exdirs),$(exdir)/used_concepts.txt)
used_kindOfRelationships_dependencies      := $(foreach exdir,$(exdirs),$(exdir)/used_kindOfRelationships.tsv)

all: \
  prov-constraints.log \
  action_name_statistics.md \
  relationship_type_statistics.md \
  undefined_concepts.txt \
  undefined_kindOfRelationships.tsv \
  used_concepts.txt \
  used_kindOfRelationships.tsv

.PHONY: \
  check-prov-constraints

action_name_statistics.md: \
  kb.ttl \
  $(top_srcdir)/src/action_name_statistics_md.py
	source $(top_srcdir)/venv/bin/activate \
	  && python3 $(top_srcdir)/src/action_name_statistics_md.py \
	    kb.ttl \
	    > _$@
	mv _$@ $@

check: \
  check-prov-constraints \
  kb-case_prov_check.ttl \
  kb_validation-develop.ttl \
  kb_validation-develop-2.0.0.ttl \
  kb_validation-unstable.ttl \
  kb_validation-unstable-2.0.0.ttl \
  undefined_concepts.txt \
  undefined_kindOfRelationships.tsv \
  used_concepts.txt \
  used_kindOfRelationships.tsv
	#TODO - Test git-tracked state

check-prov-constraints: \
  prov-constraints.log
	@test 1 -eq $$(tail -n1 $< | grep 'True' | wc -l) \
	  || (echo "ERROR:illustration.mk:prov-constraints reported a constraint error." >&2 ; exit 1)

clean:
	@rm -rf \
	  __pycache__
	@rm -f \
	  *_ \
	  _* \
	  undefined_concepts.txt \
	  undefined_kindOfRelationships.tsv \
	  used_concepts.txt \
	  used_kindOfRelationships.tsv

# TODO - Update all examples to the point where the --allow-warnings flag can be removed.
kb-case_prov_check.ttl: \
  kb-prov-time.ttl
	rm -f __$@ _$@
	source $(top_srcdir)/venv/bin/activate \
	  && case_prov_check \
	    --allow-warnings \
	    --format turtle \
	    kb-prov-time.ttl \
	    kb.ttl \
	    > __$@
	java -jar $(rdf_toolkit_jar) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

kb-prov-time.ttl: \
  kb.ttl
	rm -f __$@ _$@
	export CASE_DEMO_NONRANDOM_UUID_BASE="$(top_srcdir)" \
	  && source $(top_srcdir)/venv/bin/activate \
	    && case_prov_rdf \
	      --use-deterministic-uuids \
	      __$@ \
	      $<
	java -jar $(rdf_toolkit_jar) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

kb_validation-develop.ttl: \
  $(top_srcdir)/dependencies/CASE-Corpora/dependencies/CASE-develop.ttl \
  deactivate_uuid_suggestion.ttl \
  kb.ttl
	rm -f __$@
	source $(top_srcdir)/venv/bin/activate \
	  && case_validate \
	    --allow-infos \
	    --built-version none \
	    --ontology-graph $(top_srcdir)/dependencies/CASE-Corpora/dependencies/CASE-develop.ttl \
	    --ontology-graph deactivate_uuid_suggestion.ttl \
	    --format turtle \
	    --output __$@ \
	    $(top_srcdir)/dependencies/imports-transitive.ttl \
	    kb.ttl \
	    kb-entailment.ttl
	java -jar $(rdf_toolkit_jar) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

kb_validation-develop-2.0.0.ttl: \
  $(top_srcdir)/dependencies/CASE-Corpora/dependencies/CASE-develop-2.0.0.ttl \
  deactivate_uuid_suggestion.ttl \
  kb.ttl
	rm -f __$@
	source $(top_srcdir)/venv/bin/activate \
	  && case_validate \
	    --allow-infos \
	    --built-version none \
	    --ontology-graph $(top_srcdir)/dependencies/CASE-Corpora/dependencies/CASE-develop-2.0.0.ttl \
	    --ontology-graph deactivate_uuid_suggestion.ttl \
	    --format turtle \
	    --output __$@ \
	    $(top_srcdir)/dependencies/imports-transitive.ttl \
	    kb.ttl \
	    kb-entailment.ttl
	java -jar $(rdf_toolkit_jar) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

kb_validation-unstable.ttl: \
  $(top_srcdir)/dependencies/CASE-Corpora/dependencies/CASE-unstable.ttl \
  deactivate_uuid_suggestion.ttl \
  kb.ttl
	rm -f __$@
	source $(top_srcdir)/venv/bin/activate \
	  && case_validate \
	    --allow-warnings \
	    --built-version none \
	    --ontology-graph $(top_srcdir)/dependencies/CASE-Corpora/dependencies/CASE-unstable.ttl \
	    --ontology-graph deactivate_uuid_suggestion.ttl \
	    --format turtle \
	    --output __$@ \
	    $(top_srcdir)/dependencies/imports-transitive.ttl \
	    kb.ttl \
	    kb-entailment.ttl
	java -jar $(rdf_toolkit_jar) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

kb_validation-unstable-2.0.0.ttl: \
  $(top_srcdir)/dependencies/CASE-Corpora/dependencies/CASE-unstable-2.0.0.ttl \
  deactivate_uuid_suggestion.ttl \
  kb.ttl
	rm -f __$@
	source $(top_srcdir)/venv/bin/activate \
	  && case_validate \
	    --allow-warnings \
	    --built-version none \
	    --ontology-graph $(top_srcdir)/dependencies/CASE-Corpora/dependencies/CASE-unstable-2.0.0.ttl \
	    --ontology-graph deactivate_uuid_suggestion.ttl \
	    --format turtle \
	    --output __$@ \
	    $(top_srcdir)/dependencies/imports-transitive.ttl \
	    kb.ttl \
	    kb-entailment.ttl \
	    || true
	test -s __$@
	java -jar $(rdf_toolkit_jar) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

kb.ttl: \
  $(top_srcdir)/dependencies/CASE-Corpora/catalog/kb-all.ttl \
  $(top_srcdir)/dependencies/imports-transitive.ttl \
  $(top_srcdir)/src/entail.py \
  CASE-Examples/examples/illustrations/kb.ttl \
  casework.github.io/examples/kb.ttl
	source $(top_srcdir)/venv/bin/activate \
	  && rdfpipe \
	    --output-format turtle \
	    $(top_srcdir)/dependencies/CASE-Corpora/catalog/kb-all.ttl \
	    CASE-Examples/examples/illustrations/kb.ttl \
	    casework.github.io/examples/kb.ttl \
	    > __$@
	source $(top_srcdir)/venv/bin/activate \
	  && python3 $(top_srcdir)/src/entail.py \
	    kb-entailment.ttl \
	    $(top_srcdir)/dependencies/imports-transitive.ttl \
	    __$@
	source $(top_srcdir)/venv/bin/activate \
	  && case_validate \
	    --allow-infos \
	    __$@ \
	    $(top_srcdir)/dependencies/imports-transitive.ttl \
	    kb-entailment.ttl
	java -jar $(rdf_toolkit_jar) \
	  --inline-blank-nodes \
	  --source __$@ \
	  --source-format turtle \
	  --target _$@ \
	  --target-format turtle
	rm __$@
	mv _$@ $@

prov-constraints.log: \
  $(top_srcdir)/dependencies/prov-check/provcheck/provconstraints.py \
  kb-prov-time.ttl
	source $(top_srcdir)/venv/bin/activate \
	  && python3 $(top_srcdir)/dependencies/prov-check/provcheck/provconstraints.py \
	    --debug \
	    kb-prov-time.ttl \
	    > _$@ \
	    2>&1
	mv _$@ $@

relationship_type_statistics.md: \
  kb.ttl \
  $(top_srcdir)/src/relationship_type_statistics_md.py
	source $(top_srcdir)/venv/bin/activate \
	  && python3 $(top_srcdir)/src/relationship_type_statistics_md.py \
	    kb.ttl \
	    > _$@
	mv _$@ $@

undefined_concepts.txt: \
  $(undefined_concepts_dependencies)
	cat $^ \
	  | LC_ALL=C $(SORT) \
	    | uniq \
	      > $@_
	mv $@_ $@

undefined_kindOfRelationships.tsv: \
  $(undefined_kindOfRelationships_dependencies)
	cat $^ \
	  | LC_ALL=C $(SORT) \
	    | uniq \
	      > $@_
	mv $@_ $@

used_concepts.txt: \
  $(used_concepts_dependencies)
	cat $^ \
	  | LC_ALL=C $(SORT) \
	    | uniq \
	      > $@_
	mv $@_ $@

used_kindOfRelationships.tsv: \
  $(used_kindOfRelationships_dependencies)
	cat $^ \
	  | LC_ALL=C $(SORT) \
	    | uniq \
	      > $@_
	mv $@_ $@

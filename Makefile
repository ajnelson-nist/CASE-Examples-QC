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

# Conventions of Makefiles in this project:
#
# * Recipes write to temporary files that are named after the target
#   with trailing underscores, so a failed partial run is not mistaken
#   for an up-to-date result.
#
# * Recipes are listed in alphabetical order of the target.
#
# * Dependencies are listed in alphabetical order, unless the $<
#   wildcard (first dependency) is used in a patterned target
#   (a target with a '%').
#
# * Where options are available between BSD and GNU variants of some
#   tools, GNU tools are used to follow cross-platform conventions.  For
#   instance, sort order of non alphanumeric characters may change
#   between Linux, macOS and FreeBSD systems, causing enigmatic
#   behaviors between tools like 'sort' and 'comm'.
#
# * Commands' lines are broken up vertically with escaped line breaks,
#   and flags used in alphabetical order on the long-name form (e.g.
#   'make --directory d' instead of 'make -C d'), as much as possible.
#   Shell control flow characters are put at the beginning of lines when
#   multiple commands are joined, or output is redirected. These
#   conventions are from what is ultimately personal devloper opinion,
#   but are believed to make flag presence and argument order more clear
#   in a smaller two-dimensional screen region than in screen-wrapping
#   lines.  Lines in Make files tend to get long from the Make behavior
#   of each shell line in a recipe executing in an independent shell.
#
#  * The Make variable $(top_srcdir), where defined, will refer to the
#    root directory of the Git repository.


SHELL = /bin/bash

PYTHON3 ?= $(shell which python3.8 2>/dev/null || which python3.7 2>/dev/null || which python3.6 2>/dev/null || which python3)

VIRTUALENV ?= $(shell which virtualenv-3.8 2>/dev/null || which virtualenv-3.7 2>/dev/null || which virtualenv-3.6 2>/dev/null || which virtualenv)
ifeq ($(VIRTUALENV),)
$(error virtualenv not found)
endif

all: \
  .git_submodule_init-CASE.done.log \
  .git_submodule_init-UCO.done.log \
  .venv.done.log \
  lib/rdf-toolkit.jar
	$(MAKE) \
	  --directory tests/CASE

.PHONY: \
  download \
  normalize

.git_submodule_init-CASE.done.log: \
  .gitmodules
	test -r deps/CASE/README.md \
	  || (git submodule init deps/CASE && git submodule update deps/CASE)
	@test -r deps/CASE/README.md \
	  || (echo "ERROR:Makefile:CASE submodule README.md file not found, even though CASE submodule initialized." >&2 ; exit 2)
	touch $@

# CASE submodule tracked as a dependency to prevent .git lock contention issues.
.git_submodule_init-UCO.done.log: \
  .git_submodule_init-CASE.done.log \
  .gitmodules
	test -r deps/UCO/README.md \
	  || (git submodule init deps/UCO && git submodule update deps/UCO)
	@test -r deps/UCO/README.md \
	  || (echo "ERROR:Makefile:UCO submodule README.md file not found, even though UCO submodule initialized." >&2 ; exit 2)
	touch $@

.venv.done.log: \
  deps/requirements.txt
	rm -rf venv
	$(VIRTUALENV) \
	  --python=$(PYTHON3) \
	  --system-site-packages \
	  venv
	source venv/bin/activate \
	  ; pip install -r deps/requirements.txt
	touch $@

check: \
  .git_submodule_init-CASE.done.log \
  .venv.done.log \
  lib/rdf-toolkit.jar
	$(MAKE) \
	  --directory tests/CASE \
	  check

clean:
	@$(MAKE) \
	  --directory tests/CASE \
	  clean

download: \
  .git_submodule_init-CASE.done.log \
  .git_submodule_init-UCO.done.log \
  .venv.done.log \
  lib/rdf-toolkit.jar

lib/rdf-toolkit.jar:
	$(MAKE) \
	  -C lib \
	  rdf-toolkit.jar
	test -r $@

normalize: \
  .venv.done.log \
  lib/rdf-toolkit.jar
	$(MAKE) \
	  -C tests/CASE \
	  normalize

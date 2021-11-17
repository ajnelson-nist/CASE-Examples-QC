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

all: \
  .venv.done.log
	$(MAKE) \
	  --directory tests

.PHONY: \
  download \
  normalize

.git_submodule_init.done.log: \
  .gitmodules
	# CASE-Examples
	test -r dependencies/CASE-Examples/README.md \
	  || (git submodule init dependencies/CASE-Examples && git submodule update dependencies/CASE-Examples)
	@test -r dependencies/CASE-Examples/README.md \
	  || (echo "ERROR:Makefile:CASE-Examples submodule README.md file not found, even though CASE-Examples submodule initialized." >&2 ; exit 2)
	$(MAKE) \
	  --directory dependencies/CASE-Examples \
	  .git_submodule_init.done.log
	# casework.github.io
	test -r dependencies/casework.github.io/README.md \
	  || (git submodule init dependencies/casework.github.io && git submodule update dependencies/casework.github.io)
	@test -r dependencies/casework.github.io/README.md \
	  || (echo "ERROR:Makefile:casework.github.io submodule README.md file not found, even though casework.gitub.io submodule initialized." >&2 ; exit 2)
	touch $@

.venv.done.log: \
  .git_submodule_init.done.log \
  deps/requirements.txt
	rm -rf venv
	$(PYTHON3) -m venv \
	  venv
	source venv/bin/activate \
	  && pip install \
	    --upgrade \
	    pip \
	    setuptools \
	    wheel
	source venv/bin/activate \
	  && pip install \
	    dependencies/CASE-Examples/dependencies/CASE-Utilities-Python
	source venv/bin/activate \
	  && pip install \
	    --requirement deps/requirements.txt
	touch $@

check: \
  .venv.done.log
	$(MAKE) \
	  --directory tests \
	  check

clean:
	@$(MAKE) \
	  --directory tests \
	  clean

download: \
  .venv.done.log

normalize: \
  .venv.done.log
	$(MAKE) \
	  --directory tests \
	  normalize

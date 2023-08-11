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
  .venv-pre-commit/var/.pre-commit-built.log \
  all-tests

.PHONY: \
  all-dependencies \
  all-tests \
  check-mypy \
  check-supply-chain \
  check-supply-chain-pre-commit \
  check-supply-chain-submodules \
  check-tests \
  download \
  normalize

.git_submodule_init.done.log: \
  .gitmodules
	# CASE-Corpora
	test -r dependencies/CASE-Corpora/README.md \
	  || git submodule update --init dependencies/CASE-Corpora
	@test -r dependencies/CASE-Corpora/README.md \
	  || (echo "ERROR:Makefile:CASE-Corpora submodule README.md file not found, even though CASE-Corpora submodule initialized." >&2 ; exit 2)
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
  dependencies/CASE-Corpora/requirements.txt \
  dependencies/CASE-Examples/requirements.txt
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
	    --requirement dependencies/CASE-Corpora/requirements.txt
	source venv/bin/activate \
	  && pip install \
	    --requirement dependencies/CASE-Examples/requirements.txt
	touch $@

# This virtual environment is meant to be built once and then persist, even through 'make clean'.
# If a recipe is written to remove this flag file, it should first run `pre-commit uninstall`.
.venv-pre-commit/var/.pre-commit-built.log:
	rm -rf .venv-pre-commit
	test -r .pre-commit-config.yaml \
	  || (echo "ERROR:Makefile:pre-commit is expected to install for this repository, but .pre-commit-config.yaml does not seem to exist." >&2 ; exit 1)
	$(PYTHON3) -m venv \
	  .venv-pre-commit
	source .venv-pre-commit/bin/activate \
	  && pip install \
	    --upgrade \
	    pip \
	    setuptools \
	    wheel
	source .venv-pre-commit/bin/activate \
	  && pip install \
	    pre-commit
	source .venv-pre-commit/bin/activate \
	  && pre-commit install
	mkdir -p \
	  .venv-pre-commit/var
	touch $@

all-dependencies: \
  .venv.done.log
	$(MAKE) \
	  --directory dependencies

all-tests: \
  all-dependencies
	$(MAKE) \
	  --directory tests

check: \
  check-mypy \
  .venv-pre-commit/var/.pre-commit-built.log
	$(MAKE) \
	  --directory tests \
	  check

check-mypy: \
  .venv.done.log
	source venv/bin/activate \
	  && mypy --strict \
	    src \
	    tests

# This target's dependencies potentially modify the working directory's Git state, so it is intentionally not a dependency of check.
check-supply-chain: \
  check-mypy \
  check-supply-chain-pre-commit \
  check-supply-chain-submodules

check-supply-chain-pre-commit: \
  .venv-pre-commit/var/.pre-commit-built.log
	source .venv-pre-commit/bin/activate \
	  && pre-commit autoupdate
	git diff \
	  --exit-code \
	  .pre-commit-config.yaml

check-supply-chain-submodules: \
  .git_submodule_init.done.log
	git submodule update \
	  --remote
	git diff \
	  --exit-code \
	  --ignore-submodules=dirty \
	  dependencies

check-tests: \
  all-tests
	$(MAKE) \
	  --directory tests \
	  check

clean:
	@$(MAKE) \
	  --directory tests \
	  clean

# This recipe guarantees a timestamp update order, and is otherwise a nop.
dependencies/CASE-Corpora/requirements.txt: \
  .git_submodule_init.done.log
	test -r $@
	touch $@

# This recipe guarantees a timestamp update order, and is otherwise a nop.
dependencies/CASE-Examples/requirements.txt: \
  .git_submodule_init.done.log
	test -r $@
	touch $@

download: \
  .venv.done.log

normalize: \
  .venv.done.log
	$(MAKE) \
	  --directory tests \
	  normalize

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

PYTHON3 ?= python3

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
  download

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
	# UCO-Profile-BFO
	test -r dependencies/UCO-Profile-BFO/README.md \
	  || git submodule update \
	    --init \
	    dependencies/UCO-Profile-BFO
	@test -r dependencies/UCO-Profile-BFO/README.md \
	  || (echo "ERROR:Makefile:UCO-Profile-BFO submodule README.md file not found, even though UCO-Profile-BFO submodule initialized." >&2 ; exit 2)
	$(MAKE) \
	  --directory dependencies/UCO-Profile-BFO \
	  .git_submodule_init.done.log
	# UCO-Profile-FOAF
	test -r dependencies/UCO-Profile-FOAF/README.md \
	  || git submodule update \
	    --init \
	    dependencies/UCO-Profile-FOAF
	@test -r dependencies/UCO-Profile-FOAF/README.md \
	  || (echo "ERROR:Makefile:UCO-Profile-FOAF submodule README.md file not found, even though UCO-Profile-FOAF submodule initialized." >&2 ; exit 2)
	$(MAKE) \
	  --directory dependencies/UCO-Profile-FOAF \
	  .git_submodule_init.done.log
	# UCO-Profile-GeoSPARQL
	test -r dependencies/UCO-Profile-GeoSPARQL/README.md \
	  || git submodule update \
	    --init \
	    dependencies/UCO-Profile-GeoSPARQL
	@test -r dependencies/UCO-Profile-GeoSPARQL/README.md \
	  || (echo "ERROR:Makefile:UCO-Profile-GeoSPARQL submodule README.md file not found, even though UCO-Profile-GeoSPARQL submodule initialized." >&2 ; exit 2)
	$(MAKE) \
	  --directory dependencies/UCO-Profile-GeoSPARQL \
	  .git_submodule_init.done.log
	# UCO-Profile-PROV-O
	test -r dependencies/UCO-Profile-PROV-O/README.md \
	  || git submodule update \
	    --init \
	    dependencies/UCO-Profile-PROV-O
	@test -r dependencies/UCO-Profile-PROV-O/README.md \
	  || (echo "ERROR:Makefile:UCO-Profile-PROV-O submodule README.md file not found, even though UCO-Profile-PROV-O submodule initialized." >&2 ; exit 2)
	$(MAKE) \
	  --directory dependencies/UCO-Profile-PROV-O \
	  .git_submodule_init.done.log
	# UCO-Profile-Time
	test -r dependencies/UCO-Profile-Time/README.md \
	  || git submodule update \
	    --init \
	    dependencies/UCO-Profile-Time
	@test -r dependencies/UCO-Profile-Time/README.md \
	  || (echo "ERROR:Makefile:UCO-Profile-Time submodule README.md file not found, even though UCO-Profile-Time submodule initialized." >&2 ; exit 2)
	$(MAKE) \
	  --directory dependencies/UCO-Profile-Time \
	  .git_submodule_init.done.log
	# UCO-Profile-gufo
	test -r dependencies/UCO-Profile-gufo/README.md \
	  || git submodule update \
	    --init \
	    dependencies/UCO-Profile-gufo
	@test -r dependencies/UCO-Profile-gufo/README.md \
	  || (echo "ERROR:Makefile:UCO-Profile-gufo submodule README.md file not found, even though UCO-Profile-gufo submodule initialized." >&2 ; exit 2)
	$(MAKE) \
	  --directory dependencies/UCO-Profile-gufo \
	  .git_submodule_init.done.log
	# casework.github.io
	test -r dependencies/casework.github.io/README.md \
	  || (git submodule init dependencies/casework.github.io && git submodule update dependencies/casework.github.io)
	@test -r dependencies/casework.github.io/README.md \
	  || (echo "ERROR:Makefile:casework.github.io submodule README.md file not found, even though casework.gitub.io submodule initialized." >&2 ; exit 2)
	# prov-check
	test -r dependencies/prov-check/README.md \
	  || (git submodule update --init dependencies/prov-check)
	@test -r dependencies/prov-check/README.md \
	  || (echo "ERROR:Makefile:prov-check submodule README.md file not found, even though prov-check submodule initialized." >&2 ; exit 2)
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
	  --directory dependencies/CASE-Corpora \
	  all-dependencies
	$(MAKE) \
	  --directory dependencies

all-tests: \
  all-dependencies
	$(MAKE) \
	  --directory tests

check: \
  all-tests \
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

# Update pre-commit configuration and use the updated config file to
# review code.  Only have Make exit if 'pre-commit run' modifies files.
check-supply-chain-pre-commit: \
  .venv-pre-commit/var/.pre-commit-built.log
	source .venv-pre-commit/bin/activate \
	  && pre-commit autoupdate
	git diff \
	  --exit-code \
	  .pre-commit-config.yaml \
	  || ( \
	      source .venv-pre-commit/bin/activate \
	        && pre-commit run \
	          --all-files \
	          --config .pre-commit-config.yaml \
	    ) \
	    || git diff \
	      --stat \
	      --exit-code \
	      || ( \
	          echo \
	            "WARNING:Makefile:pre-commit configuration can be updated.  It appears the updated would change file formatting." \
	            >&2 \
	            ; exit 1 \
                )
	@git diff \
	  --exit-code \
	  .pre-commit-config.yaml \
	  || echo \
	    "INFO:Makefile:pre-commit configuration can be updated.  It appears the update would not change file formatting." \
	    >&2

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
	@rm -f \
	  .venv.done.log
	@rm -rf \
	  venv

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

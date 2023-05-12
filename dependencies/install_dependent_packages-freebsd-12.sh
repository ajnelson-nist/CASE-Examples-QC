#!/bin/sh

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

set -x
set -e

sudo pkg install --yes \
  coreutils \
  gmake \
  openjdk11-jre \
  py39-sqlite3 \
  wget

# Guarantee /bin/bash.
if [ ! -x /bin/bash ]; then
  cd /bin
    test -x /usr/local/bin/bash
    sudo ln -s \
      /usr/local/bin/bash \
      bash
  cd -
fi
test -x /bin/bash

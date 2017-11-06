#!/bin/bash
# Usage: do_harvest <harvester>.py  
# (e.g. ./do_harvest onomads.py)

docker run --rm -v $(pwd)/$1:/srv/harvest.py -v $(pwd)/iso:/srv/iso \
  axiom/thredds_iso_harvester

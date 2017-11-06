#!/bin/bash
# Usage: do_crawl <harvester>.py  
# (e.g. ./do_crawl onomads.py)

docker run --rm -v $(pwd)/$1:/srv/harvest.py -v $(pwd)/iso:/srv/iso \
  axiom/thredds_iso_harvester

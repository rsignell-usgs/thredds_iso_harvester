# thredds_iso_harvester

Python class/script to harvest ISO metadata records from an [__ncISO enabled__](https://www.unidata.ucar.edu/software/thredds/v4.3/tds/tds4.2/reference/ncISO.html) [THREDDS](http://www.unidata.ucar.edu/software/thredds/current/tds/TDS.html) server.

See https://www.unidata.ucar.edu/software/thredds/v4.3/tds/tds4.2/reference/ncISO.html for instructions on enabling ncISO in [THREDDS](http://www.unidata.ucar.edu/software/thredds/current/tds/TDS.html).

## Docker

By default, the Docker image runs the script it finds at `/srv/harvest.py`.

Create a script which harvests from a THREDDS target, for example:

```
#!python
# coding=utf-8

from thredds_iso_harvester.harvest import ThreddsIsoHarvester

# AOOS
ThreddsIsoHarvester(catalog_url="http://thredds.aoos.org/thredds/catalog.xml",
    out_dir="/srv/iso/aoos")
```

Save this file and then run the Docker image, passing the harvesting script
and ISO output directory as volumes.

```
docker run --rm -v $(pwd)/harvest.py:/srv/harvest.py $(pwd)/iso:/srv/iso \
  axiom/thredds_iso_harvester
```

## Install

First install [lxml's dependencies](http://lxml.de/installation.html#requirements):

```
sudo apt-get install libxml2-dev libxslt-dev python-dev
```

Then install using pip:

```
pip install git+git://github.com/axiom-data-science/thredds_iso_harvester
```

## Upgrade

```
pip install --upgrade --no-deps git+git://github.com/axiom-data-science/thredds_iso_harvester
pip install git+git://github.com/axiom-data-science/thredds_iso_harvester
```

Note: depending on your pip installation, you may need to run the above command using sudo.

## Usage

thredds-iso-harvester can be run from the command line or as a Python class.

### Command line

Run

```
thredds_iso_harvester -h
```

to view options.

Example run:

```
thredds_iso_harvester --output-dir=/srv/http/iso-waf --log=/var/log/iso-harvest.log \
  http://yourserver.org/thredds/catalog.html
```

Example for downloading a subset of data sets:
```
thredds_iso_harvester --output-dir=/srv/http/iso-waf --log=/var/log/iso-harvest.log \
  --select=DATASET1 --select=ANOTHER_DATASET_ID \ 
  http://yourserver.org/thredds/catalog.html
```

### Python class

```
from thredds_iso_harvester.harvest import ThreddsIsoHarvester

ThreddsIsoHarvester(catalog_url="http://yourserver.org/thredds/catalog.html", out_dir="/srv/http/iso-waf")
```

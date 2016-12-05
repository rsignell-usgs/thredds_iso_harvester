## docker run -v $(pwd)/aoos.py:/srv/harvest.py -v $(pwd)/iso:/srv/iso axiom/thredds_iso_harvester

from thredds_iso_harvester.harvest import ThreddsIsoHarvester

# AOOS
ThreddsIsoHarvester(catalog_url="http://thredds.aoos.org/thredds/catalog.xml",
    out_dir="/srv/iso/aoos")

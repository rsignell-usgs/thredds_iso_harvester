from thredds_iso_harvester.harvest import ThreddsIsoHarvester
from thredds_crawler.crawl import Crawl

skip = Crawl.SKIPS
select = ['.*\_best']

ThreddsIsoHarvester(catalog_url="https://ecowatch.ncddc.noaa.gov/thredds/oceanNomads/catalog_aggs.xml",
    skip=skip, select=select,
    out_dir="/srv/iso/onomads")

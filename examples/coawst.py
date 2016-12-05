## docker run -v $(pwd)/coawst.py:/srv/harvest.py -v $(pwd)/iso:/srv/iso axiom/thredds_iso_harvester

from thredds_iso_harvester.harvest import ThreddsIsoHarvester
from thredds_crawler.crawl import Crawl
skip = Crawl.SKIPS + ['.*MATLAB.*', '\..*']
select = ['.*\.ncml']

# FWF
ThreddsIsoHarvester(catalog_url="http://gamone.whoi.edu/thredds/catalog/coawst_4/use/fmrc/catalog.xml", 
    skip=skip, select=select, out_dir="/srv/iso/frf")

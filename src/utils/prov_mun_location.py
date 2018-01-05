import pysal
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DA02_TERM_MUNIC_PATH_SHP = os.path.join(BASE_DIR, "../../resources/G17_Division_administrativa/da02_term_munic_4326.shp")
DA02_TERM_MUNIC_PATH_DBF = os.path.join(BASE_DIR, "../../resources/G17_Division_administrativa/da02_term_munic_4326.dbf")

da02_term_munic_shp = pysal.open(DA02_TERM_MUNIC_PATH_SHP)
da02_term_munic_dbf = pysal.open(DA02_TERM_MUNIC_PATH_DBF)

def locate(lat, lon):
  prov = None
  mun = None

  for pol in da02_term_munic_shp:
    if pol.contains_point((lon, lat)):
      row = da02_term_munic_dbf.get(pol.id)
      mun = row[0]
      prov = row[1]
      break

  return prov, mun

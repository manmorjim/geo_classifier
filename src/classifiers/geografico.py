from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

from utils import db_manager, coordinates, prov_mun_location

IMG_METADATA_TAG_GPS = "GPSInfo"
IMG_METADATA_TAG_GPS_LAT = "GPSLatitude"
IMG_METADATA_TAG_GPS_LAT_REF = "GPSLatitudeRef"
IMG_METADATA_TAG_GPS_LON = "GPSLongitude"
IMG_METADATA_TAG_GPS_LON_REF = "GPSLongitudeRef"

'''
TODO
'''
def __get_cat_geo_from_gps(gps):
  cat_geo = None
  if gps:
    lat, lon = coordinates.get_lat_lon_from_gps(gps)
    prov, mun = prov_mun_location.locate(lat, lon)
    cat_geo = db_manager.get_cat_geo(prov, mun)
  return cat_geo

'''
TODO
'''
def __get_gps_video_metadata(file):
  pass

'''
TODO
'''
def __get_gps_image_metadata(file):
  gpsinfo = None
  fi = Image.open(file['path'])
  tags = fi._getexif()
  if tags:
    for tag, values in tags.items():
      if TAGS.get(tag, tag) == IMG_METADATA_TAG_GPS:
        gpsinfo = {}
        for encoded_subtag in values:
          subvalue = values[encoded_subtag]
          subtag = GPSTAGS.get(encoded_subtag, encoded_subtag)
          if subtag == IMG_METADATA_TAG_GPS_LAT:
            gpsinfo[coordinates.GPS_LAT] = subvalue
          if subtag == IMG_METADATA_TAG_GPS_LAT_REF:
            gpsinfo[coordinates.GPS_LAT_REF] = subvalue
          if subtag == IMG_METADATA_TAG_GPS_LON:
            gpsinfo[coordinates.GPS_LON] = subvalue
          if subtag == IMG_METADATA_TAG_GPS_LON_REF:
            gpsinfo[coordinates.GPS_LON_REF] = subvalue
        break

  return gpsinfo

'''
TODO
'''
def __classify_by_metadata(file):
  cat_geo = None

  if file['type'] == db_manager.IMAGE_TYPE:
    gps = __get_gps_image_metadata(file)
    # gps = __get_gps_image_metadata({'path': '/usr/geo_classifier/20180103_135137.jpg'})
  else:
    gps = __get_gps_video_metadata(file)

  cat_geo = __get_cat_geo_from_gps(gps)

  return cat_geo

'''
TODO
'''
def __classify_by_name(file):
  pass

'''
TODO
'''
def __classify_by_content(file):
  pass

'''
TODO
'''
def classify(file):
  cat_geo_id = None

  cat_geo = __classify_by_metadata(file)

  if cat_geo is None:
    cat_geo = __classify_by_name(file)

  if cat_geo is None:
    cat_geo = __classify_by_content(file)

  if cat_geo:
    cat_geo_id = cat_geo[0]
  return cat_geo_id

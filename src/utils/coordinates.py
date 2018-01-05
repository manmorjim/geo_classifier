
GPS_LAT = "LAT"
GPS_LAT_REF = "LAT_REF"
GPS_LON = "LON"
GPS_LON_REF = "LON_REF"

def gps_degrees_to_decimal(degree):
  d0 = degree[0][0]
  d1 = degree[0][1]
  d = float(d0) / float(d1)

  m0 = degree[1][0]
  m1 = degree[1][1]
  m = float(m0) / float(m1)

  s0 = degree[2][0]
  s1 = degree[2][1]
  s = float(s0) / float(s1)

  return d + (m / 60.0) + (s / 3600.0)

def get_lat_lon_from_gps(gps):
  lat = None
  lon = None

  if gps is not None:
    lat = gps_degrees_to_decimal(gps[GPS_LAT])
    if gps[GPS_LAT_REF] != "N":
      lat = 0 - lat

    lon = gps_degrees_to_decimal(gps[GPS_LON])
    if gps[GPS_LON_REF] != "E":
        lon = 0 - lon

  return lat, lon

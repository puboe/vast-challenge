import csv

def main():
  rows = []
  with open('/Users/Hobbit/git/vast-challenge/VAST/MCBuildingProxSensorData/csv/all-sensors.csv') as csvfile:
    data_reader = csv.reader(csvfile)
    for row in data_reader:
      if row[5] == 'null':
        floor = int(row[3])
        zone = row[4]

        x = 0 
        y = 0
        if floor == 1:
          (x, y) = map_floor_one(row, zone)
          row[5] = x
          row[6] = y
        elif floor == 2:
          (x, y) = map_floor_two(row, zone)
          row[5] = x
          row[6] = y
        elif floor == 3:
          (x, y) = map_floor_three(row, zone)
          row[5] = x
          row[6] = y

      rows.append(row)

    with open('/Users/Hobbit/git/vast-challenge/VAST/MCBuildingProxSensorData/csv/all-sensors-location.csv', 'w') as csvfile:
      writer = csv.writer(csvfile, delimiter=',')
      for row in rows:
        writer.writerow(row)

def map_floor_one(row, zone):
  x = 0
  y = 0
  zone = int(zone)
  if zone == 1:
    x = 165
    y = 60
  elif zone == 2:
    x = 24
    y = 92
  elif zone == 3:
    x = 8
    y = 40
  elif zone == 4:
    x = 80
    y = 56
  elif zone == 5:
    x = 96
    y = 100
  elif zone == 6:
    x = 96
    y = 32
  elif zone == 7:
    x = 160
    y = 8
  elif zone == 8:
    x = 176
    y = 8

  return (x, y)

def map_floor_two(row, zone):
  x = 0
  y = 0
  zone = int(zone)
  if zone == 1:
    x = 60
    y = 32
  elif zone == 2:
    x = 20
    y = 60
  elif zone == 3:
    x = 152
    y = 102
  elif zone == 4:
    x = 80
    y = 56
  elif zone == 5:
    x = 32
    y = 32
  elif zone == 6:
    x = 24
    y = 136
  elif zone == 7:
    x = 152
    y = 96

  return (x, y)

def map_floor_three(row, zone):
  x = 0
  y = 0
  if zone == ' Server Room':
    x = 28
    y = 40
  else:
    zone = int(zone)
    if zone == 1:
      x = 60
      y = 32
    elif zone == 2:
      x = 112
      y = 56
    elif zone == 3:
      x = 20
      y = 56
    elif zone == 4:
      x = 80
      y = 56
    elif zone == 5:
      x = 168
      y = 56
    elif zone == 6:
      x = 24
      y = 104

  return (x, y)

if __name__ == "__main__":
  main()
import csv
import json
import requests

distances = []
SOURCE_FILE = '/home/user/Desktop/uniquePostalCodes.csv'
OUTPUT_FILE = '/home/user/Desktop/distFile.csv'

def runMain():

    with open(SOURCE_FILE) as f:
        content = f.readlines()

    print "Cached data read"

    postalCodes = set(content)
    postalCodes = list(postalCodes)
    counter = 0

    alreadyChecked = set()
    for ix in xrange(len(postalCodes)):
        for iy in xrange(len(postalCodes)):
            x = postalCodes[ix]
            y = postalCodes[iy]
            if x != y:
                if (x, y) not in alreadyChecked:
                    counter += 1
                    alreadyChecked.add((x, y))
                    alreadyChecked.add((y, x))
                    getDistance(x, y)
            writeOut()


def getDistance(go, to):
    response = requests.get('http://www.distance24.org/route.json?stops='+go+'|'+to+'')

    json_data = json.loads(response.text)
    go = go.strip()
    to = to.strip()
    distances.append((go, to, json_data['distance']))
    distances.append((to, go, json_data['distance']))


def writeOut():
    with open(OUTPUT_FILE, 'w') as out:
        csv_out = csv.writer(out)
        for row in distances:
            csv_out.writerow(row)

if __name__ == "__main__":
    runMain()

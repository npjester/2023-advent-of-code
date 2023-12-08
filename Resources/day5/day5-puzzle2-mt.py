import os
import re
import datetime
from multiprocessing import Pool, SimpleQueue

input = open("/Users/npjester/Documents/GitHub/2023-advent-of-code/Resources/day5/example.txt")
seedMatch = re.compile(r'seeds:\s+(?P<seeds>.*)$')
seedMapMatch = re.compile(r'(\d+\s+\d+)')
seedToSoilMapMatch = re.compile(r'seed-to-soil map:')
soilToFertilizerMapMatch = re.compile(r'soil-to-fertilizer map:')
fertilizerToWaterMapMatch = re.compile(r'fertilizer-to-water map:')
waterToLightMapMatch = re.compile(r'water-to-light map:')
lightToTemperatureMapMatch = re.compile(r'light-to-temperature map:')
temperatureToHumidityMapMatch = re.compile(r'temperature-to-humidity map:')
humidityToLocationMapMatch = re.compile(r'humidity-to-location map:')
mapDataMatch = re.compile(r'(?P<destination>\d+)\s+(?P<source>\d+)\s+(?P<range>\d+)$')

def init_worker(almanac,sharedQueue):
    global sharedAlmanac
    global queue
    sharedAlmanac = almanac
    queue = sharedQueue

def getAlmanacFromInput():
    global almanac
    inputArray = []
    almanac = {}
    lineNumber = 0
    for line in input.readlines():
        inputArray.append(line)
        lineNumber += 1
    lineNumber = 0    
    while lineNumber < len(inputArray):
        if inputArray[lineNumber] != "\n":
            if seedMatch.match(inputArray[lineNumber]):
                almanac['seedMaps'] = {}
                dirtySeedMap= seedMapMatch.finditer(seedMatch.match(inputArray[lineNumber]).group('seeds'))
                for dirtySeedMap in dirtySeedMap:
                    seedMap = dirtySeedMap[0].split()
                    almanac['seedMaps'][int(seedMap[0])] = { "seedStart" : int(seedMap[0]), "range" : int(seedMap[1])}
            elif seedToSoilMapMatch.match(inputArray[lineNumber]):
                almanac['seedToSoilMap'] = {}
                mapDataRecordNumber = 0
                while inputArray[lineNumber] != "\n":
                    lineNumber += 1
                    mapData = mapDataMatch.match(inputArray[lineNumber])
                    if mapData:
                        mapDataRecordNumber += 1
                        almanac['seedToSoilMap'][mapDataRecordNumber] = { 'destination' : int(mapData.group('destination')),'source' : int(mapData.group('source')), 'range' : int(mapData.group('range')) }
            elif soilToFertilizerMapMatch.match(inputArray[lineNumber]):
                almanac['soilToFertilizerMap'] = {}
                mapDataRecordNumber = 0
                while inputArray[lineNumber] != "\n":
                    lineNumber += 1
                    mapData = mapDataMatch.match(inputArray[lineNumber])
                    if mapData:
                        mapDataRecordNumber += 1
                        almanac['soilToFertilizerMap'][mapDataRecordNumber] = { 'destination' : int(mapData.group('destination')),'source' : int(mapData.group('source')), 'range' : int(mapData.group('range')) }
            elif fertilizerToWaterMapMatch.match(inputArray[lineNumber]):
                almanac['fertilizerToWaterMap'] = {}
                mapDataRecordNumber = 0
                while inputArray[lineNumber] != "\n":
                    lineNumber += 1
                    mapData = mapDataMatch.match(inputArray[lineNumber])
                    if mapData:
                        mapDataRecordNumber += 1
                        almanac['fertilizerToWaterMap'][mapDataRecordNumber] = { 'destination' : int(mapData.group('destination')),'source' : int(mapData.group('source')), 'range' : int(mapData.group('range')) }
            elif waterToLightMapMatch.match(inputArray[lineNumber]):
                almanac['waterToLightMap'] = {}
                mapDataRecordNumber = 0
                while inputArray[lineNumber] != "\n":
                    lineNumber += 1
                    mapData = mapDataMatch.match(inputArray[lineNumber])
                    if mapData:
                        mapDataRecordNumber += 1
                        almanac['waterToLightMap'][mapDataRecordNumber] = { 'destination' : int(mapData.group('destination')),'source' : int(mapData.group('source')), 'range' : int(mapData.group('range')) }
            elif lightToTemperatureMapMatch.match(inputArray[lineNumber]):
                almanac['lightToTemperatureMap'] = {}
                mapDataRecordNumber = 0
                while inputArray[lineNumber] != "\n":
                    lineNumber += 1
                    mapData = mapDataMatch.match(inputArray[lineNumber])
                    if mapData:
                        mapDataRecordNumber += 1
                        almanac['lightToTemperatureMap'][mapDataRecordNumber] = { 'destination' : int(mapData.group('destination')),'source' : int(mapData.group('source')), 'range' : int(mapData.group('range')) }
            elif temperatureToHumidityMapMatch.match(inputArray[lineNumber]):
                almanac['temperatureToHumidityMap'] = {}
                mapDataRecordNumber = 0
                while inputArray[lineNumber] != "\n":
                    lineNumber += 1
                    mapData = mapDataMatch.match(inputArray[lineNumber])
                    if mapData:
                        mapDataRecordNumber += 1
                        almanac['temperatureToHumidityMap'][mapDataRecordNumber] = { 'destination' : int(mapData.group('destination')),'source' : int(mapData.group('source')), 'range' : int(mapData.group('range')) }
            elif humidityToLocationMapMatch.match(inputArray[lineNumber]):
                almanac['humidityToLocationMap'] = {}
                mapDataRecordNumber = 0
                while inputArray[lineNumber] != "\n" and lineNumber < len(inputArray)-1:
                    lineNumber += 1
                    mapData = mapDataMatch.match(inputArray[lineNumber])
                    if mapData:
                        mapDataRecordNumber += 1
                        almanac['humidityToLocationMap'][mapDataRecordNumber] = { 'destination' : int(mapData.group('destination')),'source' : int(mapData.group('source')), 'range' : int(mapData.group('range')) }
        lineNumber += 1

def getSeedToSoil(seed):
    return getDestinationFromSource(seed, "seedToSoilMap")
    
def getSoilToFertilizer(soil):
    return getDestinationFromSource(soil, "soilToFertilizerMap")

def getFertilizerToWater(fertilizer):
    return getDestinationFromSource(fertilizer, "fertilizerToWaterMap")

def getWaterToLight(water):
    return getDestinationFromSource(water, "waterToLightMap")

def getLightToTemperature(light):
    return getDestinationFromSource(light, "lightToTemperatureMap")

def getTemperatureToHumidity(temperature):
    return getDestinationFromSource(temperature, "temperatureToHumidityMap")

def getHumidityToLocation(humidity):
    return getDestinationFromSource(humidity, "humidityToLocationMap")

def getDestinationFromSource(source, type):
    global sharedAlmanac
    destination = source
    for mapRecord in sharedAlmanac[type]:
        if sharedAlmanac[type][mapRecord]['source'] <= source <= (sharedAlmanac[type][mapRecord]['source'] + sharedAlmanac[type][mapRecord]['range'] - 1 ):
            destination = sharedAlmanac[type][mapRecord]['destination'] + (source - sharedAlmanac[type][mapRecord]['source'])
            return destination
    return destination

def getSeedToSoilForListOfSeeds(seed):
    return getDestinationFromSourceForListOfSeeds(seed, "seedToSoilMap")
    
def getSoilToFertilizerForListOfSeeds(soil):
    return getDestinationFromSourceForListOfSeeds(soil, "soilToFertilizerMap")

def getFertilizerToWaterForListOfSeeds(fertilizer):
    return getDestinationFromSourceForListOfSeeds(fertilizer, "fertilizerToWaterMap")

def getWaterToLightForListOfSeeds(water):
    return getDestinationFromSourceForListOfSeeds(water, "waterToLightMap")

def getLightToTemperatureForListOfSeeds(light):
    return getDestinationFromSourceForListOfSeeds(light, "lightToTemperatureMap")

def getTemperatureToHumidityForListOfSeeds(temperature):
    return getDestinationFromSourceForListOfSeeds(temperature, "temperatureToHumidityMap")

def getHumidityToLocationForListOfSeeds(humidity):
    return getDestinationFromSourceForListOfSeeds(humidity, "humidityToLocationMap")

def getDestinationFromSourceForListOfSeeds(sourceList, type):
    global sharedAlmanac
    destinationList = []
    print(f'Checking {type} for {sourceList}')
    for mapRecord in sharedAlmanac[type]:
        nonMatchedSources = []
        mapRecordSourceList = []
        matchedSources = []
        sourceStart = sharedAlmanac[type][mapRecord]['source']
        sourceEnd = sharedAlmanac[type][mapRecord]['source'] + sharedAlmanac[type][mapRecord]['range']
        mapRecordSourceList = [*range(sourceStart,sourceEnd)]
        matchedSources = list(set(sourceList) & set(mapRecordSourceList))
        nonMatchedSources = list(set(sourceList).difference(set(matchedSources)))
        for source in matchedSources:
            destinationList.append(sharedAlmanac[type][mapRecord]['destination'] + (source - sharedAlmanac[type][mapRecord]['source']))   
    destinationList += nonMatchedSources
    return destinationList

def getLocationForSeed(seed):
    global queue
    soilDestination = getSeedToSoil(seed)
    fertilizerDestination = getSoilToFertilizer(soilDestination)
    waterDestination = getFertilizerToWater(fertilizerDestination)
    lightDestination = getWaterToLight(waterDestination)
    temperatureDestination = getLightToTemperature(lightDestination)
    humidityDestination = getTemperatureToHumidity(temperatureDestination)
    locationDestination = getHumidityToLocation(humidityDestination)
    queue.put((seed,locationDestination))
    return locationDestination

def getLocationForSeeds(seedMap):
    global queue
    print(f'Processing seedMap {seedMap}')
    start = datetime.datetime.now()
    startSeed = seedMap['seedStart']
    maxSeed = seedMap['seedStart'] + seedMap['range']
    print(f'Min: {startSeed} Max: {maxSeed}')
    seedList = [*(range(startSeed,maxSeed))]
    print(f'Seed List: {seedList}')
    soilDestination = getSeedToSoilForListOfSeeds(seedList)
    fertilizerDestination = getSoilToFertilizerForListOfSeeds(soilDestination)
    waterDestination = getFertilizerToWaterForListOfSeeds(fertilizerDestination)
    lightDestination = getWaterToLightForListOfSeeds(waterDestination)
    temperatureDestination = getLightToTemperatureForListOfSeeds(lightDestination)
    humidityDestination = getTemperatureToHumidityForListOfSeeds(temperatureDestination)
    locationDestination = getHumidityToLocationForListOfSeeds(humidityDestination)
    queue.put(min(locationDestination))
    took = datetime.datetime.now() - start
    print(f'Took {took} to get Min for {seedMap}')

def getSeedsFromSeedMap():
    global almanac
    global seedLocations
    sharedQueue = SimpleQueue()
    almanac['seedList'] = []
    seedLocations = []
    start = datetime.datetime.now()
    with Pool(2, initializer=init_worker, initargs=(almanac,sharedQueue,)) as p:
        _ = p.map_async(getLocationForSeeds,almanac['seedMaps'])
        for i in range(len(almanac['seedMaps'])):
            location = sharedQueue.get()
            seedLocations.append(location)
            print(f'Got location {location}', flush=True)
    took = datetime.datetime.now() - start
    print(f'Took {took}')

def getLowestLocationNumberFromSeeds():
    global seedLocations
    seedLocations = []
    almanac['seedLocationData'] = {}
    getSeedsFromSeedMap()
    return min(seedLocations)

def main():
    getAlmanacFromInput()
    lowestLocationNumber = getLowestLocationNumberFromSeeds()
    print(lowestLocationNumber)

if __name__ == "__main__":
    main()
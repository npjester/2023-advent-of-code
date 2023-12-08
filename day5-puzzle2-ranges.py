import os
import re

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
                dirtySeeds = seedMatch.match(inputArray[lineNumber]).group('seeds')
                #print(dirtySeeds)
                dirtySeedMap = seedMapMatch.finditer(dirtySeeds)
                #print(dirtySeedMap)
                for dirtySeedRange in dirtySeedMap:
                    seedMap = dirtySeedRange[0].split()
                    almanac['seedMaps'][int(seedMap[0])] = { "seedStart" : int(seedMap[0]), "range" : int(seedMap[1])}
                    #print(almanac['seedMaps'])
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
    destination = source
    for mapRecord in almanac[type]:
        if almanac[type][mapRecord]['source'] <= source <= (almanac[type][mapRecord]['source'] + almanac[type][mapRecord]['range'] - 1 ):
            destination = almanac[type][mapRecord]['destination'] + (source - almanac[type][mapRecord]['source'])
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
    destinationList = []
    print(f'Checking {type}')
    #print(f'SourceList Length: {len(sourceList)}')
    for mapRecord in almanac[type]:
        nonMatchedSources = []
        mapRecordSourceList = []
        matchedSources = []
        sourceStart = almanac[type][mapRecord]['source']
        sourceEnd = almanac[type][mapRecord]['source'] + almanac[type][mapRecord]['range']
        mapRecordSourceList = [*range(sourceStart,sourceEnd)]
        matchedSources = list(set(sourceList) & set(mapRecordSourceList))
        nonMatchedSources = list(set(sourceList).difference(set(matchedSources)))
        for source in matchedSources:
            destinationList.append(almanac[type][mapRecord]['destination'] + (source - almanac[type][mapRecord]['source']))   
    destinationList += nonMatchedSources
    return destinationList

def getLocationForSeed(seed):
    soilDestination = getSeedToSoil(seed)
    fertilizerDestination = getSoilToFertilizer(soilDestination)
    waterDestination = getFertilizerToWater(fertilizerDestination)
    lightDestination = getWaterToLight(waterDestination)
    temperatureDestination = getLightToTemperature(lightDestination)
    humidityDestination = getTemperatureToHumidity(temperatureDestination)
    locationDestination = getHumidityToLocation(humidityDestination)
    return locationDestination

def getLocationForSeeds(seeds):
    soilDestination = getSeedToSoilForListOfSeeds(seeds)
    fertilizerDestination = getSoilToFertilizerForListOfSeeds(soilDestination)
    waterDestination = getFertilizerToWaterForListOfSeeds(fertilizerDestination)
    lightDestination = getWaterToLightForListOfSeeds(waterDestination)
    temperatureDestination = getLightToTemperatureForListOfSeeds(lightDestination)
    humidityDestination = getTemperatureToHumidityForListOfSeeds(temperatureDestination)
    locationDestination = getHumidityToLocationForListOfSeeds(humidityDestination)
    print(min(locationDestination))
    return min(locationDestination)

def getLocationForSeedsFromSeedMap(seedMap):
    startSeed = almanac['seedMaps'][seedMap]['seedStart']
    maxSeed = almanac['seedMaps'][seedMap]['seedStart'] + almanac['seedMaps'][seedMap]['range']
    print(f'Seed Map Range: {[*range(startSeed,maxSeed)]}')
    minFromSeedMap = getLocationForSeeds([*range(startSeed,maxSeed)])
    return minFromSeedMap

def getSeedsFromSeedMap(): ## Don't think we need this
    almanac['seedList'] = []
    for seedMap in almanac['seedMaps']:
        startSeed = almanac['seedMaps'][seedMap]['seedStart']
        maxSeed = almanac['seedMaps'][seedMap]['seedStart'] + almanac['seedMaps'][seedMap]['range'] + 1
        almanac['seedList'].extend(range(startSeed,maxSeed))

def getLowestLocationNumberFromSeeds():
    seedLocations = []
    almanac['seedLocationData'] = {}
    getSeedsFromSeedMap()
    for seed in almanac['seedList']:
        #print(seed)
        almanac['seedLocationData'][seed] = getLocationForSeed(seed)
        seedLocations.append(almanac['seedLocationData'][seed])
    #print(seedLocations)
    return min(seedLocations)

def getLowestLocationNumberFromSeedMap():
    seedLocations = []
    #almanac['seedLocationData'] = {}
    ##---
    for seedMap in almanac['seedMaps']:
        print(f'Processing: {seedMap}')
        seedLocations.append(getLocationForSeedsFromSeedMap(seedMap))
    print(seedLocations)
    return min(seedLocations)

def main():
    getAlmanacFromInput()
    lowestLocationNumber = getLowestLocationNumberFromSeedMap()
    print(lowestLocationNumber)

if __name__ == "__main__":
    main()
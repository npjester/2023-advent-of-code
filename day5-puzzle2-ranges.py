import os
import re
import logging

logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.DEBUG)

input = open("/Users/npjester/Documents/GitHub/2023-advent-of-code/Resources/day5/input.txt")
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

############# Ranges Below Here ################
def getSeedToSoilForRangeOfSeeds(seed):
    return getDestinationFromSourceForRangeOfSeeds(seed, "seedToSoilMap")
    
def getSoilToFertilizerForRangeOfSeeds(soil):
    return getDestinationFromSourceForRangeOfSeeds(soil, "soilToFertilizerMap")

def getFertilizerToWaterForRangeOfSeeds(fertilizer):
    return getDestinationFromSourceForRangeOfSeeds(fertilizer, "fertilizerToWaterMap")

def getWaterToLightForRangeOfSeeds(water):
    return getDestinationFromSourceForRangeOfSeeds(water, "waterToLightMap")

def getLightToTemperatureForRangeOfSeeds(light):
    return getDestinationFromSourceForRangeOfSeeds(light, "lightToTemperatureMap")

def getTemperatureToHumidityForRangeOfSeeds(temperature):
    return getDestinationFromSourceForRangeOfSeeds(temperature, "temperatureToHumidityMap")

def getHumidityToLocationForRangeOfSeeds(humidity):
    return getDestinationFromSourceForRangeOfSeeds(humidity, "humidityToLocationMap")

def getDestinationFromSourceForRangeOfSeeds(sourceRanges, mapType):
    destinationRanges = {}
    logging.debug(f'Source Range {sourceRanges} checking {mapType}')
    for sourceMap in almanac[mapType]:
        #logging.debug(sourceMap)
        sourceMapStart = almanac[mapType][sourceMap]['source']
        sourceMapEnd = almanac[mapType][sourceMap]['source'] + almanac[mapType][sourceMap]['range'] - 1
        destinationMapStart = almanac[mapType][sourceMap]['destination']
        destinationMapEnd = almanac[mapType][sourceMap]['destination'] + almanac[mapType][sourceMap]['range'] - 1
        logging.debug(f'sourceMapStart: {sourceMapStart} sourceMapEnd: {sourceMapEnd} destMapStart: {destinationMapStart} destMapEnd: {destinationMapEnd}')
        completeMatch = []
        for sourceRange in sourceRanges:
            ## Starts and Ends within source range
            logging.debug(f"Checking {sourceRanges[sourceRange]['start']} to {sourceRanges[sourceRange]['end']}")
            if sourceMapStart <= sourceRanges[sourceRange]['start'] <= sourceMapEnd and sourceMapStart <= sourceRanges[sourceRange]['end'] <= sourceMapEnd:
                mappedStart = destinationMapStart + (sourceRanges[sourceRange]['start'] - sourceMapStart)
                mappedEnd = mappedStart + (sourceRanges[sourceRange]['end'] - sourceRanges[sourceRange]['start'])
                destinationRanges[mappedStart] = {'start':mappedStart,'end':mappedEnd}
                logging.debug(f"Within Source Map Range: {sourceMapStart}-{sourceMapEnd}: {sourceRanges[sourceRange]['start']}-{sourceRanges[sourceRange]['end']} maps to {mappedStart}-{mappedEnd} : {destinationRanges[mappedStart]}")
                completeMatch.append(sourceRange)
            ## Ends within source range
            elif sourceMapStart <= sourceRanges[sourceRange]['end'] <= sourceMapEnd:
                offset = sourceRanges[sourceRange]['end'] - sourceMapStart
                mappedStart = destinationMapStart
                mappedEnd = mappedStart + (offset)
                newEnd = sourceMapStart - 1
                oldEnd = sourceRanges[sourceRange]['end']
                sourceRanges[sourceRange]['end'] = newEnd
                destinationRanges[mappedStart] = {'start':mappedStart,'end':mappedEnd}
                logging.debug(f"Ends in Source Map Range: {sourceMapStart}:{sourceMapEnd}: {sourceRanges[sourceRange]['start']}:{oldEnd} - {mappedStart}:{mappedEnd} : {oldEnd}->{newEnd} {destinationRanges[mappedStart]}")
            ## Starts within source range
            elif sourceMapStart <= sourceRanges[sourceRange]['start'] <= sourceMapEnd:
                newStart = sourceMapEnd + 1
                oldStart = sourceRanges[sourceRange]['start']
                offset = sourceRanges[sourceRange]['start'] - sourceMapStart
                mappedStart = destinationMapStart + (offset)
                mappedEnd = destinationMapEnd
                sourceRanges[sourceRange]['start'] = newStart
                destinationRanges[mappedStart] = {'start':mappedStart,'end':mappedEnd}
                logging.debug(f"Starts in Source Map Range: {sourceMapStart}:{sourceMapEnd}: {oldStart}:{sourceRanges[sourceRange]['end']} - {mappedStart}:{mappedEnd} : {oldStart}->{newStart} {destinationRanges[mappedStart]}")
            else:
                logging.debug(f'Not In Range {sourceMapStart} - {sourceMapEnd}')
        logging.debug(f'Complete Matches: {completeMatch}')
        for source in completeMatch:
            sourceRanges.pop(source)
    for sourceRange in sourceRanges:        
        destinationRanges[sourceRanges[sourceRange]['start']] = {'start':sourceRanges[sourceRange]['start'],'end':sourceRanges[sourceRange]['end']}
    logging.debug(f'{mapType} Destination Range: {destinationRanges}')
    return destinationRanges

def getLowestValueFromRanges(ranges):
    return min(list(ranges.keys()))

def getLocationForSeedRanges(seedRanges):
    soilDestinationRanges = getSeedToSoilForRangeOfSeeds(seedRanges)
    fertilizerDestinationRanges = getSoilToFertilizerForRangeOfSeeds(soilDestinationRanges)
    waterDestinationRanges = getFertilizerToWaterForRangeOfSeeds(fertilizerDestinationRanges)
    lightDestinationRanges = getWaterToLightForRangeOfSeeds(waterDestinationRanges)
    temperatureDestinationRanges = getLightToTemperatureForRangeOfSeeds(lightDestinationRanges)
    humidityDestinationRanges = getTemperatureToHumidityForRangeOfSeeds(temperatureDestinationRanges)
    locationDestinationRanges = getHumidityToLocationForRangeOfSeeds(humidityDestinationRanges)
    lowestLocation = getLowestValueFromRanges(locationDestinationRanges)
    return lowestLocation

def getLowestLocationNumberUsingRanges():
    seedMapRanges = {}
    locations = []
    for seedMap in almanac['seedMaps']:
        seedMapStart = almanac['seedMaps'][seedMap]['seedStart']
        seedMapEnd = almanac['seedMaps'][seedMap]['seedStart'] + almanac['seedMaps'][seedMap]['range'] - 1
        seedMapRanges[seedMapStart] = {"start":seedMapStart,"end":seedMapEnd}
    locations.append(getLocationForSeedRanges(seedMapRanges))
    return min(locations)

def main():
    getAlmanacFromInput()
    lowestLocationNumberRanges = getLowestLocationNumberUsingRanges()
    logging.info(lowestLocationNumberRanges)

if __name__ == "__main__":
    main()
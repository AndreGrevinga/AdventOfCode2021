import os
import sys
inputFile = open("day01/input.txt", "r")
rawInput = inputFile.read()
inputList = rawInput.split(",")


def calculateNumberOfIncreases():
    total = 0
    previousValue = 0
    for numberString in inputList:
        number = int(numberString)
        if not previousValue == 0 and previousValue < number:
            total += 1
        previousValue = number
    return total


def calculateNumberOfIncreasesForThreeMeasurementWindow():
    total = 0
    threeNumbersList = []
    for numberString in inputList:
        number = int(numberString)
        if len(threeNumbersList) == 3:
            previousListSum = sum(threeNumbersList)
            currentListSum = previousListSum - threeNumbersList[0] + number
            del threeNumbersList[0]
            if previousListSum < currentListSum:
                total += 1
        threeNumbersList.append(number)
    return total


print(calculateNumberOfIncreases(),
      calculateNumberOfIncreasesForThreeMeasurementWindow())

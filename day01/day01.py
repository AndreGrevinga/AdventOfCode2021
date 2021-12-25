import os
import sys
inputFile = open("day01/input.txt", "r")
rawInput = inputFile.read()
inputList = rawInput.split(",")


def calculateNumberOfIncreases():
    total = 0
    previousValue = any
    for numberString in inputList:
        number = int(numberString)
        if previousValue is not None and previousValue < number:
            total += 1
        previousValue = number
    return total


print(calculateNumberOfIncreases())

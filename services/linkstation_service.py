from typing import Tuple

availableLinkStations = [
    [0, 0, 10],
    [20, 20, 5],
    [10, 0, 12]
]

def getNearestLinkStation(point: Tuple[int, int]):
    nearestLinkStation = None
    for linkStation in availableLinkStations:
        distance = calculateDistanceBetweenTwoPoints(linkStation, point)
        if distance > linkStation[2]:
            continue
        power = (linkStation[2] - distance)**2
        if nearestLinkStation == None or power > nearestLinkStation[1]:
            nearestLinkStation = (linkStation, power)
    
    if nearestLinkStation == None:
        print(f'No link station within reach for point {point[0]},{point[1]}')
    else:
        print(f'Best link station for point {point[0]},{point[1]} is {nearestLinkStation[0][0]},{nearestLinkStation[0][1]} with power {nearestLinkStation[1]}')

def calculateDistanceBetweenTwoPoints(linkStation, point):
      return ((((linkStation[0] - point[0] )**2) + ((linkStation[1]-point[1])**2) )**0.5)
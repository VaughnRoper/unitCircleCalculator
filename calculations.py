import math
# take 2 inputs - one starting angle and one final angle.
# program should output the matrix that encodes for the transformation
start = input('enter starting angle ')
final = input('enter angle that transformation should result in ')
# the two types of transforms involved in this should be : flip across cener of
# unit circle, rotate around unit circle
# step one: convert angle to raydians
# step 2 : convert raydians to vecor
# startRaydian = [cos(angle), sin(angle)]


def degreeToRaydians(x):
    return (x*math.pi)/180


startRaydian = degreeToRaydians(start)
finalRaydian = degreeToRaydians(final)
startVector = [math.cos(startRaydian), math.sin(startRaydian)]
finalVector = [math.cos(finalRaydian), math.sin(finalRaydian)]
print(startVector)

input('press enter to close')

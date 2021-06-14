import math
import numpy as np
from numpy import matrix
# take 2 inputs - one starting angle and one final angle.
# program should output the matrix that encodes for the transformation
start = float(input('enter starting angle '))
final = float(input('enter angle that transformation should result in '))
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
# start vector * matrix x = final vector. solve for matrix
ScalarX = finalVector[0]/startVector[0]
ScalarY = finalVector[1]/startVector[1]
awnserMatrix = matrix([[ScalarX, 0], [0, ScalarY]])
awnser = np.array(awnserMatrix)
print('The matrix that encodes this transform is:', awnser, sep='\n')

input('press enter to close')

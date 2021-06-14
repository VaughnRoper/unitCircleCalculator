import math
import numpy as np
from numpy import matrix
# import needed libraries
# take 2 inputs - one starting angle and one final angle.
# program should output the matrix that encodes for the transformation between
# these two angles
start = float(input('enter starting angle '))
final = float(input('enter angle that transformation should result in '))
# convert angles to raydians


def degreeToRaydians(x):
    return (x*math.pi)/180


startRaydian = degreeToRaydians(start)
finalRaydian = degreeToRaydians(final)
# convert raydians to vectors by taking their sines and cosines
startVector = [math.cos(startRaydian), math.sin(startRaydian)]
finalVector = [math.cos(finalRaydian), math.sin(finalRaydian)]
# start vector * matrix x = final vector. solve for matrix
# find the scalars that when multiplied by the basis vectors, distort them in a
# way that would turn startVector into finalVector
ScalarX = finalVector[0]/startVector[0]
ScalarY = finalVector[1]/startVector[1]
# now assemble the matrix. scalarX goes in the top left slot, and scalarY goes
# in the Bottom right. the other two slots are 0's, as they make up the
# matrix's null space
awnserMatrix = matrix([[ScalarX, 0], [0, ScalarY]])
# format and print the matrix
awnser = np.array(awnserMatrix)
print('The matrix that encodes this transform is:', awnser, sep='\n')

input('press enter to close')

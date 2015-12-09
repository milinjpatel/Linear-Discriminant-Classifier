import numpy.linalg

def findE(x,b): # Function to find the matrix "E"
    x_inv = numpy.linalg.pinv(x) # Find the Moore-Penrose Inverse of x
    W = numpy.dot(x_inv, b) # Multiple x# and b
    E = numpy.subtract(numpy.dot(x,W), b) # Subtract b from x times W
    E_rounded = numpy.around(E.astype(numpy.double), 1) # Round the E matrix to one decimal point
    return E_rounded, W

def checkEEZ(E): # Check if the matrix "E" is equal to zero
    for row in E:
        if (row != 0):
            return False
    return True

def checkELZ(E): # Check if the matrix "E" is less than zero
    for row in E:
        if (row > 0 or row == 0):
            return False
    return True
    
def done(W): #Print out the equation of the line
   print "Equation of the line is x =", ((W[2]*-1)/W[0]) # Print statement for 2D problems
   #print "Equation of the line is x - y + z =", ((W[3]*-1)/W[0]) # Print statement for 3D problem
    
#x = [[0,0,1], [0,1,1], [-1,0,-1], [-1,-1,-1]] # Example one, solution is possible
x = [[0,0,1], [1,1,1], [0,-1,-1], [-1,0,-1]] # Example two, solution is not possible 
#x = [[0,0,1,1], [1,0,0,1], [1,0,1,1], [1,1,1,1], 
#     [0,0,0,-1], [0,-1,0,-1], [0,-1,-1,-1], [-1,-1,0,-1]] # Example three, 3D problem, solution is a plane
b = [1,1,1,1]
while (True): # Keep running until we find a solution or a solution is not possible
    E,W = findE(x,b)
    EEZ = checkEEZ(E)
    ELZ = checkELZ(E)

    if (EEZ):
        done(W)
        break
    elif (ELZ):
        print "No solution is possible"
        break
    b = numpy.add(b, numpy.add(E, numpy.absolute(E))) # Add b to the addition of E and the absolute value of E
    

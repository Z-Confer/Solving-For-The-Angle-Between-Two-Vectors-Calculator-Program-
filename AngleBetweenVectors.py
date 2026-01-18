import math

#takes user input and assigns a place in the dictionary for all vector coordinates (dependant on the dimensions)
def acceptInput():
    dynamicVarsVectors = {}

    try: 
        #vector input MUST NOT include spaces between integers, for exmaple [2,1] != [2, 1]
        Rn = int(input("R^n, n="))
        Vec1 = input("Input vector 1\n[x,y,z]=")
        Vec2 = input("Input vector 2\n[x,y,z]=")

        #strips user input of the brackets containing vector coordinates
        Vec1 = Vec1.strip("[")
        Vec1 = Vec1.strip("]")

        Vec2 = Vec2.strip("[")
        Vec2 = Vec2.strip("]")

        #splits user inputs after stripping, returns a list containing user input values
        splitVec1 = Vec1.split(",")
        splitVec2 = Vec2.split(",")

        #assigns place in dictionary for the first input vector, of the name type {xn : value} where n is the index of the value in the vector
        for dimension in range(Rn):
            dynamicVarsVectors['x' + str(dimension)] = int(splitVec1[dimension])

        #mirrors above loop but for the second input vector
        for dimension in range(Rn):
            dynamicVarsVectors['y' + str(dimension)] = int(splitVec2[dimension])

        return dynamicVarsVectors, Rn
   
   #catches use case in which a user input value cannot be converted into an integer. Ex. R^n, n="No"
    except ValueError as e:
        print("Error in type input: ", e)
        return acceptInput()
    
    #catches the use case in which the user mixes dimensions of the vectors IE. R^n, n=2, Vec1=[2,3,4]
    except IndexError as e:
        print("Error in vector dimensions: ", e)
        return acceptInput()


#Solves for the magnitude of the input vectors
def solveForMagnitude(dynamicVarsVectors, Rn):
    vectorMagnitudes = []

    #takes the key-value pairs out of the dictionary, adds them, and then square roots the sum
    for vector in ["x", "y"]:
        sumOfCoordinates = 0
        for coordinate in range(Rn):
           sumOfCoordinates +=  math.pow(dynamicVarsVectors[str(vector) + str(coordinate)], 2)
        
        vectorMagnitudes.append(math.sqrt(sumOfCoordinates))

    return vectorMagnitudes


#Solves for the dot product of the two input vectors
def solveForDot(dynamicVarsVectors, Rn):
    dot = 0

    #loops through R^n dimensions and sums the product of two corresponding entries into the input dictionary to find the dot product
    for vector in range(Rn):
        dot += dynamicVarsVectors["x" + str(vector)] * dynamicVarsVectors["y" + str(vector)]

    return dot

#Penultimate function, solving for the degrees in between the two input vectors
def solveForAngle(magVec1, magVec2, dot):
    productMagnitudes = magVec1 * magVec2
    print("\nThe product of the magnitudes are: ", productMagnitudes)

    interiorFunction = dot / productMagnitudes
    print("The quotient of the dot product and the magnitudes is: ", interiorFunction)

    return math.acos(interiorFunction)

#note this code COULD be refacted using math.degrees but ONLY for desktop applications, calculators cannot handle that function
def convertRadiansToDegrees(radians):
    return (180/math.pi) * radians

def main():
    vectors, Rn = acceptInput()
    dot = solveForDot(vectors, Rn)
    print("\nThe dot product is: ", dot)

    magnitudes = solveForMagnitude(vectors, Rn)
    print("The magnitudes are: ", magnitudes, end = "\n\n")

    print(convertRadiansToDegrees(solveForAngle(magnitudes[0], magnitudes[1], dot)), " deg")

main()
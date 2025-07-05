# Global variables maxVal and minVal
maxVal = 100
minVal = -100

# val is a function parameter
def inBounds(val):
	# Local variables bigEnough and smallEnough
	bigEnough = minVal <= val
	print("inBounds: val " + str(val) + "; bigEnough " + str(bigEnough))
	smallEnough = val <= maxVal
	print("inBounds: val " + str(val) + "; smallEnough " + str(smallEnough))
	return bigEnough and smallEnough

print(inBounds(55))
print(inBounds(502))
print(minVal, maxVal) # This is okay, global variables are in scope
# print(val)  #This generates an error
# print(bigEnough) # This generates an error
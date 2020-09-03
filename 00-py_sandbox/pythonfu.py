#print statement
print("Hello World!")

#defining variables
a, b = 1, 2
print(str(a) + " + " + str(b) + " = " + str(a + b))
print("{} + {} = {}").format(a, b, a + b)
print("%d + %d = %d" %(a, b, a + b))
print("")

#defining a function
def sampleFunction():
    print("Inside the function")

#invoke sampleFunction
sampleFunction()

#create lists
#1D variety
list1 = [1, "hello", 3.14]

#2D variety
list2 = [["Mets", 2],
         ["Yankees", 27]]

for i in list1:
    print("{}: {}").format(i, type(i))

print("")
print("Team: {}, Number of Championships: {}").format(list2[0][0], list2[0][1])
print(list2[0])

#dictionary
myDict = {
    "J": 31,
    "Y": 30,
    "S": 6,
    "E": 2
}

print("")
print(myDict["J"])

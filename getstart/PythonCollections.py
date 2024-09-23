print("##########################Python Sets - START##########################################")
firstSet = {"setValue11", "setValue22", "setValue33", "setValue11","setValue55",True,2,1,3}
print(firstSet)
firstSet.add(0)
print(firstSet)
firstSet.add("False")
print(firstSet)
firstSet.add(False)
print(firstSet)

print()
print()

secondSet = {1,2,3,4,5,True,False,0}
print(secondSet)
secondSet.remove(False)
print(secondSet)
print()
print()
print("##########################Python Sets - End##########################################")
print("##########################Python Dictionary - START##########################################")
firstDict = {
    "name": "Arun",
    "course": "Python",
    "year": "2024"
}
print(firstDict)
firstDict["month"]="Sep"
print(firstDict)
print()
print("##########################Python Dictionary - END##########################################")

print("##########################Python List - START##########################################")
name = ["Arun","Bobby","kumar","Umar"]
print(name)
print(name[0])
print(name[1])
print(name[-1])
print(name[-2])
name[2] = "Arunkumar"
print(name)
print(name[0:2])
print(name[1:3])
print(name)
print()

name.append("Harun")
print(len(name))
name.insert(2,"Guru")
print(name)
print("Umar" in name)
name.remove("Harun")
print(name)
name.clear()
print(name)

numbers = [1,2,3,4,5]
for item in numbers:
    print(item)
print()
print("##########################Python List - END##########################################")

print("##########################Python Tuples - START##########################################")
numberTuples = (1,2,3,6,5,7,2,9,1,4,7,3,2,7,8,9)
print(numberTuples.count(2))
print(numberTuples.index(7))
print("##########################Python Tuples - END##########################################")

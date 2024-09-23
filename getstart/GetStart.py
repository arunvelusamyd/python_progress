def helloFunction():
    print("This is my first function")
    print("Bye!")
helloFunction()
print()

######################################################

numberTuples = (1,2,3,6,5,7,2,9,1,4,7,3,2,7,8,9)
print(numberTuples.count(2))
print(numberTuples.index(7))

######################################################

numbers = range(5,50,12)
print(numbers)
for number in numbers:
    print(number)
print()
for number in range(5,10):
    print(number)
print()
for number in range(5):
    print(number)
print()

######################################################

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

######################################################

name.append("Harun")
print(len(name))
name.insert(2,"Guru")
print(name)
print("Umar" in name)
name.remove("Harun")
print(name)
name.clear()
print(name)

######################################################

#numbers = [1,2,3,4,5]
#for item in numbers:
#    print(item)
#print()

######################################################

#i=0
#while i<=5_0:
#    print(i * '*')
#    print(i * "A")
#    i+=1
#print()

######################################################

#weight = float(input("Weight: "))
#isKgOrLb = input("(K)g or L(b)s: ")
#if isKgOrLb.upper() == "K":
#    converted = weight / 0.45
#    print("Weight in Pounds: ", converted)
#elif isKgOrLb.upper() == "L":
#    converted = weight * 0.45
#    print("Weight in Kill0 Gram: ", converted)
#else:
#    print("Please enter right input")
print()

######################################################

temp = 16
if temp > 35:
    print("It's s hot day")
    print("Drink more water")
elif temp > 20:
    print("Weather looks good")
else:
    print("It's too cold")
print("done")
print()

######################################################

print (10/3)
print (10//3)
print (10%3)
print (10*3)
print (10**3)
x=10
x+=3
print(x)
print()

######################################################

minAge = 20
age = 30
firstname = "Arunkumar"
isOnline = False
print("minAge = ",minAge)
print("age = ",age)
print("firstname = ",firstname)
print("isOnline = ",isOnline)

#lastname = input("What is last name?")
#print("Hello,",firstname,lastname)
#print("Hello, "+firstname+" "+lastname)
print()

######################################################

#birth_year = input("Enter your birth year : ")
#age = 2024 - int(birth_year);
#print(age)
print()

######################################################

#firstIp = float(input("First input: "))
#secondIp = float(input("second input: "))
#addResult = firstIp+secondIp;
#print("Added both input. Result is", addResult)
print()

######################################################

helloWorld = "Hello World"
print('Hello' in helloWorld)
print('World' in helloWorld)
print('world' in helloWorld)
print()

######################################################

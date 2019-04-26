#=================Write a function that will add two numbers and print the result==================

print("Let's add numbers together!")
print()
num_One  = int(input("Enter a number: "))
num_Two = int(input("Enter another number: "))
#string interpolation: "%s" %(val, val)
def addition(numOne, numTwo):
  print("The sum of %s and %s is equal to %s" %(str(numOne), str(numTwo) , numOne + numTwo))
print("Addition Function")
addition(num_One, num_Two)
print()

#=================================================================================================#
#going to create a sandwich making function that takes three parameters 

Turkey = "Turkey"
Swiss = "Swiss"
Mustard = "Mustard"

def sandwich_maker(meat, cheese, condiment):
  print("You made a %s and %s sandwich with %s! " %(meat, cheese, condiment))

sandwich_maker(Turkey, Swiss, Mustard)

#=================================================================================================#

#pass a list as a parameter

lang_List = ["Python", "Javascript", "C#"]

def spinTheList(list):
  for item in list:
    print(item)
spinTheList(lang_List)

#===================================================================================================#
#put the contents of one array and move it to an empty array
target_Array = []

filledArray = ["milk", "oreos", "crackers", "peanut butter"]

#loop over the filled array and append the contents into the target_array
for item in filledArray:
  target_Array.append(item)

#loop over the empty array and print its new contents
for x in target_Array:
  print(x)







#access string
a = "Hello World"
print(a[0])
print(a[5])


# use of "in" function
for char in a :
    print (char)
print("H" in a)
if "H" in a:
    print("yes, it it sthre")


# slicing
Name = "Fnu Pratichi"
print(Name[1:3])   #start at 1 and stop at 3(3 not included)
print(Name[:5])
print(Name[2:])
print(Name[:])

# Negative Index
print(Name[-6:-2]) # start from c(-2) and go till -6(not included)

# Modify string
Name = "Pratichi"
print(Name.upper())
print(Name.lower())

#replace string
print(Name.replace("a","P")) # replace a with P


Name1="pratichi"
print(Name1.capitalize())

#split - returns list of items where we specify split 
full_name = "FNUPRATICHI"
print(full_name.split("U"))

#REMOVE WHITESPACE 
Pet_name = "   ABBY SINGH!   "
print(Pet_name.strip())


#STRING CONCATENATION (only strings allowed)
F_name = "Fnu"
L_name = "Pratichi"
age = 26
print(F_name+" "+ L_name)
#print("My first name is " + F_name + " " +  "and last name is " + L_name + " and my age is " + age)

#F-strings - formatted strings
print("My first name is " + F_name + " " +  "and last name is " + L_name, f" and my age is {age}")

# .2f to get 2 after decimal vakues
print(f"my age is {age:.2f}")

print("Hello MR.\"VIKAS\" from india")

thislist = ["apple", "banana", "cherry"]
print(thislist)
newlist = ["aws" , "cloud" , "ip"]
print(thislist.append(newlist))









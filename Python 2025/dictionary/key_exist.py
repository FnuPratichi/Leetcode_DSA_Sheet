#check if key exists or not

dict = {"name" : "anku",
        "age" : 21,
        "date_of_birth" : "11th May"}

check_key = input()

if check_key in dict.keys():
    print("Present")
else:
    print("not present")
        

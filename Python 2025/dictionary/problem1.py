#Creating and Accessing Dictionary Items
student_records = {"name": ["anku, aman", "ram"] ,
                   "age": ['26','25','23'] ,
                   "education" : ["Masters", 'bachelors', 'matsers']
                   }
print(student_records)
print("*" * 50)

print("We can also print like below \n")
print(student_records["name"])
print("*"*50)


#access using get()
print(student_records.get('age'))
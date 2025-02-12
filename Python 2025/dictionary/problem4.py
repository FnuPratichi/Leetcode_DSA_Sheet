# loop in dictionary 
query_name = "Aman"
student_records = {"name": ["Aman" , "Ram" , "Radha" , "Rani"],
                   "class": [12,10,11,9],
                   "marks":[90,100,96,90]}

# for key in student_records:
#     print(key)

# for values in student_records.values():
#     print(values)

for key,values in student_records.items():
    print(key,values)
    if key=="marks":
        print(values)


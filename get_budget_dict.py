# Create the function that takes a list of dictionaries and returns the sum of people's
# budgets.
# Examples
# get_budgets([
# { 'name': 'John', 'age': 21, 'budget': 23000 },
# { 'name': 'Steve', 'age': 32, 'budget': 40000 },
# { 'name': 'Martin', 'age': 16, 'budget': 2700 }
# ]) ➞ 65700


def get_budgets(my_list):
    total = 0
    for person in my_list:
        print(person)
        total = total + person['budget']  
    print(total) 

get_budgets([{ 'name': 'John', 'age': 21, 'budget': 23000 },
            { 'name': 'Steve', 'age': 32, 'budget': 40000 },
            { 'name': 'Martin', 'age': 16, 'budget': 2700 }])

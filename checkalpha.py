my_string = 'Anku'

def isaplha_function():
    my_string = 'ANKU'
    for char in my_string:
        if ord(char) in range(ord('A'),ord('Z')+1):
            print('yes , string contains aplhabets')
        else:
            print("no")

isaplha_function()


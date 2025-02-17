# string1 = "hello world"
# string2 = "helo wrd"

string1 = "hell world"
string2 = "helo wrod"

######## ordereddict

from collections import OrderedDict
first_string = OrderedDict.fromkeys(string1)
second_string = OrderedDict.fromkeys(string2)
if first_string == second_string:
    print("True, the order is same")
else:
    print("False")
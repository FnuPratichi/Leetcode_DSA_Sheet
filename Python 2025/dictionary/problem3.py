#deleting 

Contact_details = {"name" : ['a','b','c'], "number" : ['123', '345','456']}
print(Contact_details['name'])

#popitems to delete last key-vlaue items
key,value = Contact_details.popitem()
print(key,value)

print("after deletion of last key,value we are left with" , Contact_details)

#pop() to remove item
print(Contact_details.pop("name"))

Contact_details['new'] = ['abc' , 1, 'adf', 1.0]
print("added new key and value" , Contact_details)

#to clear all key values from dict
Contact_details.clear()
print("Current key vlaues are" , Contact_details)
#Input 1: 
#test_dict = {1 : ‘Gfg is best for geeks’} 
#sub_list = [‘love’, ‘good’] ( Strings to check in values ) 
#Output : {1: ‘Gfg is best for geeks’}

#Input 2: 
#test_dict = {1 : ‘Gfg is love’, 2: ‘Gfg is good’} 
#sub_list = [‘love’, ‘good’] ( Strings to check in values ) 
#Output : {}


test_dict = {"1": "Anku is the best", "2": "Ram is better than anku"}
substring_value = ["better", "best"]

for key in list(test_dict.keys()):  
    for sub in substring_value:  
        if sub in test_dict[key]:
            test_dict.pop(key)
            break  
print(test_dict)



    



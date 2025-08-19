def findGender(s):
    my_dict = {}
    for i in range(0,len(s)):
        if s[i] not in my_dict:
            my_dict[s[i]] = 1
        else:
            my_dict[s[i]] = my_dict[s[i]]+1
    print(my_dict)


    found_duplicate = False
    for keys,values in my_dict.items():
        if values == 2:
            print("ignore him")
            found_duplicate = True
            break
    if found_duplicate == False:
        print("chat with her")


if __name__ == "__main__":
    findGender("wjmzbr")
    #findGender("xiaodao")
    

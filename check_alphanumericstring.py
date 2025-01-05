def fun(s):
    alnum = False

    for char in s:
        if char.isalnum():
            alnum = True
            break


    if alnum == True:
        print("True")
    else:
        print("False")


fun('anku')
fun('123')
fun('@#$^&()')
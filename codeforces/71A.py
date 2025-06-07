
def Toolong(user_string):
    count = 0
    if len(user_string) < 10:
        print(user_string)
    else:
        for i in range(0,len(user_string)):
            first_word = user_string[0]
            last_word = user_string[len(user_string)-1]
            count = count +1
        count = count-2
        result = first_word[0] + str(count) + last_word[-1]
        print(result)
        

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        user_string = input()
    Toolong(user_string)





    
user_input=input()   # taking input as string so that we can iterate thorugh it
for i in user_input: 
    digit=int(i)    # converting i into int 
    rem=digit%10
    #digit=digit//10
    print(rem)

def decimal_tobinary(number):
    binary_list = []
    if number ==0:
        return '0'
    
    while(number>0):
        rem = number % 2
        binary_list.append(str(rem))
        number = number//2
    print(''.join(binary_list))

decimal_tobinary(10)
decimal_tobinary(5)
decimal_tobinary(7)
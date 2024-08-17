# 1. using two pointers

def rever(num, l, r):
    num_str = str(num)
    num_lis = list(num_str)

    if l>=r:
        return int(''.join(num_lis))
    
    num_lis[l],num_lis[r] = num_lis[r],num_lis[l]    # swap the numbers 

    return rever(int(''.join(num_lis)),l + 1,r - 1 )  # 


number = 431
print(rever(number,0,len(str(number))-1))



# 2. ONE parameter need to finish









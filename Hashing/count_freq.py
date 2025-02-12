"""num = {}
n = int(input('enter the size of dict '))
for _ in range(n):
    key = int(input('enter key'))
    value = int(input('enter values'))
    num[key]=value
print(num)


"""
"""# count frequencies 
count=0
number_list = [1, 2, 1, 2, 0, 5]
query = int(input('enter number for whic you want to know the count '))
for i in number_list:
    if query==i:
        count=count+1
print(count)
"""
# using dict 

def count_freq(num_list,n):
    mp={}
    for i in range(n):
        if num_list[i] in mp:
            mp[num_list[i]]+=1
        else:
            mp[num_list[i]]=1
    for ch in mp:
        print(ch,mp[ch])
if __name__ == '__main__':
    num_list = [10,5,10,5,10,5]
    n = len(num_list)
    count_freq(num_list,n)






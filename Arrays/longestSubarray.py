a = [2, 3, 5, 1, 9]
k = 10

def longest_subarray(a,k):
    length = 0
    for i in range(0,len(a)):
        sum1 = 0
        for j in range(i,len(a)):
            sum1 = sum1+a[j]
            if sum1 == k:
                length = max(length,j-i+1)
    print(length)
longest_subarray(a,k)


# def countMin(mid,m,n):
#     count = 0
#     for i in range(1,min(m,mid)+1):
#         count = count + min(n,mid//i)
#     return count

def countMin(mid, m, n):
    res = 0
    for i in range(1, n + 1):
        res += min(m, mid // i)
    return res

def binarysearch(m,n,k):
    low = 1
    high = m*n
    ans = float('inf')
    while(low<=high):
        mid = (low+high)//2
        min_count = countMin(mid,m,n)
        if min_count >= k:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

if __name__ == "__main__":
    m,n,k = list(map(int,input().split(" ")))
    print(binarysearch(m,n,k))

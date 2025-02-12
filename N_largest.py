# num = [11,20,15,90,1,0]
# size = len(num)
# N = int(input())
# sorted_num = sorted(num,reverse=True)
# print(sorted_num[:N])

import math
points = [(2, 3), (4,5)]
# print euclidean dis : (x2-x1)
p1= points[0]
print(p1)
x1=p1[0]
y1=p1[1]
p2= points[1]
x2=p2[0]
y2=p2[1]
distance = math.sqrt(((x2-x1)**2)+ ((y2-y1)**2))
print(distance)




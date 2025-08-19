from heapq import *

num_items, total_parts = map(int, input().split(" "))
lengths = list(map(int, input().split(" ")))

def sum_of_squares(length, parts):
    base_size = length // parts
    bigger_parts = length - base_size * parts  
    smaller_parts = parts - bigger_parts       
    return smaller_parts * base_size * base_size + bigger_parts * (base_size + 1) * (base_size + 1)

max_heap = []
total = 0

for i in range(num_items):
    length = lengths[i]
    total += length * length  
    gain = -sum_of_squares(length, 1) + sum_of_squares(length, 2)
    heappush(max_heap, (gain, length, 2)) 

for _ in range(total_parts - num_items):
    gain, length, current_parts = heappop(max_heap)
    total += gain  
    next_parts = current_parts + 1
    next_gain = -sum_of_squares(length, current_parts) + sum_of_squares(length, next_parts)
    heappush(max_heap, (next_gain, length, next_parts))

print(total)

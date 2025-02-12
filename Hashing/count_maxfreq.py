from typing import List



def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_map = {}
        # Counting frequencies of elements
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        print(freq_map.values())
maxFrequencyElements()
    
        
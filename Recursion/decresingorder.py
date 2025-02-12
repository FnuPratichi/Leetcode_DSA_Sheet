# Print Numbers in decresing order (N to 1)

class Solution:
    def dec_num(self,n):
        if n < 1:
            return
        print(n, end=" ")
        self.dec_num(n-1)

# Note that we can't call methods directly if we are using self. Object needs to be created
def main():
    ob = Solution()      # Create an instance of the Solution class
    ob.dec_num(10)       # Call the method on the instance

if __name__ == "__main__":
    main()
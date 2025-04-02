# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]


def spiral_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    top = 0
    right = m-1
    left = 0
    bottom = n-1
    ans = []

    while(top<=bottom and left<=right):
        for i in range(left,right+1):
            ans.append(matrix[top][i])
        top = top+1

        for i in range(top,bottom+1):
            ans.append(matrix[i][right])
        right=right-1

        if top<=bottom:
            for i in range(right,left-1,-1):
                ans.append(matrix[bottom][i])
            bottom = bottom-1

        if left<=right:
            for i in range(bottom,top-1,-1):
                ans.append(matrix[i][left])
            left = left+1
    print(ans)

spiral_matrix(matrix)
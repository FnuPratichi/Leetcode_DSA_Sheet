def generate(numRows):
    result = [1]
    result.append([1,1])
    #print(result)
    if numRows == 1:
        print([1])
    if numRows == 2:
        print([1],[1,1])
    previous_list = [[1],[1,1]]

    for j in range(3,numRows):
        previous_list = result[-1]
        new_row = [1]
        for i in range(1,len(previous_list)):
            new_row.append(previous_list[i-1] + previous_list[i])
        new_row.append(1)
        result.append(new_row)
        print(result)

generate(5)


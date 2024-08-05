details= ['1234567890M6724','0987654321F2019', '1234567890M6724', '1234567890M6724']
#for detail in details:
#   for i in detail:
 #       if i=='M':
 #          print(detail)


def countSeniors(details):
    count=0
    for detail in details:
        age=int(detail[11:13])
        if age>60:
            count=count+1
    return count


    
print(countSeniors(details))
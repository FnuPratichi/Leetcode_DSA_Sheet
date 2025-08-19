# def Registration(s):
#     my_dict = {}
#     for word in s:
#         if word not in my_dict:
#             my_dict[word] = 1
#         else:
#             my_dict[word] = my_dict[word] + 1
#     print(my_dict)

#     for key,value in my_dict.items():
#         if value==1:
#              print("OK")

class Solution:

    def __init__(self):
        self.counter = {}

    def registration(self, user):
        if user not in self.counter:
            self.counter[user] = 1
            return "OK"
        else:
            value = self.counter[user]
            self.counter[user] = value + 1
            return user + str(value)




n = int(input())
obj = Solution()
for i in range(0,n):
    user = input().split(" ")[0]
    print(obj.registration(user))








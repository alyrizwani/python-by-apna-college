list = [6,7,0,1,2,3,2,1,0,7,6]
# length = len(list) - 1
# # print(length)
# mid = int(length / 2)
# # print(mid)

# list1 = []
# list1 = list[mid + 1:].reverse()
# if list[:mid] == list1:
#     print("The list is a palindrome")
# else:
#     print("The list is not a palindrome")
list1 = list.copy()
list1.reverse()
if list == list1:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")
number = 11
#  if number % 2 == 0: ---> even   else: ----> odd
#  if number == 10: ---> even   elif number == 12: ----> odd   elif number==15:     ----> else:
db = "mysql"  # oracle, mongodb

# if number%2 ==0:
#     print("even")
# else:
#     print('odd')
#
# if db == "oracle":
#     print('connect to oracle db')
# elif db == "mysql":
#     print('connect to mysql')
#     # functionality...
# else:
#     print('no database')

# for loop
list1 = [12,11,14,15,1,2,3,4,5,6,7,8,9,10,11,5]
tuple1 = (1,2,3,4,5,6)

# need all even number in to another list
req_output = [] #2,4
for num in tuple1:  # 1 , 2  , 3.....10
    if num%2==0:
        req_output.append(num)


print(req_output)

# need all numbers between 5 to 11 from list1
# output =[]
# for num in list1:
#     if num>=5 and num<=11:
#         output.append(num)
# print(output)
# output = sorted(output)
# print(output) # ascending  ---->
# print(list(set(output)))

# nested for loops


"""
1) program to find the number is a Polindrome  ---> 12121   --> reverse same
2) Armstrong   ---> 153    ---> 1 cube 3 + 5 cube 3 +....
"""
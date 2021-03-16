# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [11,22,33,44,55,66,77]

# def dummy_print(var1,var2):
#     print('dataaaaaaaaaaaaaaa111111', var1, var2)
#     print('dataaaaaaaaaaaaaa2222222', var1, var2)
#     print('dataaaaaaaaaaaaaa3333333', var1, var2)
# dummy_print('1',123)
# dummy_print('222', 'sfdhfdfd')
# dummy_print('3', list1)
"""
dataaaaaaaaaaaaaaa111111 1 123
dataaaaaaaaaaaaaa2222222 1 123
dataaaaaaaaaaaaaa3333333 1 123
dataaaaaaaaaaaaaaa111111 222 sfdhfdfd
dataaaaaaaaaaaaaa2222222 222 sfdhfdfd
dataaaaaaaaaaaaaa3333333 222 sfdhfdfd

"""
# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [11,22,33,44,55,66,77]

def even_odd(input):
    req_output = []
    for num in input:
        if num%2==0:
            req_output.append(num)
    print(req_output)
#
even_odd(list1)
# even_odd(list2)

"""
list1 = [-1,2,3,4,-5,6,7,8,-9]

output = []
step1: for i in list1:
step2 :     if i >0:
                output.append(i)
            else:
               return output  
"""

list1 = [1,2,3,4,-5,6,7,8,-9]
list2 = [11,22,-33,44,55,66,77]

def even_odd(input111):
    req_output = []
    for num in input111:
        if num%2==0:
            req_output.append(num)
    return req_output
#
output1 = even_odd(list1)
print('output1-----',output1)
output2 = even_odd(list2)
print('output2----', output2)


"""
what is  generator in python --- instead of return we use yield
uses
"""
var1 = "sknkdnfkdnfkdsfndkfkd;"
def mut(var1, var2):
    output = []
    output1= []
    for i in range(1, var2+1):
        # output.append((var1 ,'*' , i , "=", var1*i))
        yield (var1 ,'*' , i , "=", var1 * i)
    # for i in range(1, var2+1):
    #     output1.append((4 ,'*' , i , "=", var1*i))
    # yield output1
    #multiple

a=mut(2,6)
print(a)
print(next(a))
# # some process
# # mysql, oracle,
print(next(a))

def multi(var1, var2):
    output = []
    for i in range(1, var2+1):
        output.append((var1 ,'*' , i , "=", var1*i))
    return output

# print(multi(2,5))

def numerss(var1):
    data = []
    for i in var1:
        data.append(i**i)
    yield data

# a = numerss([1,2,3,4,5])
# print(next(a))
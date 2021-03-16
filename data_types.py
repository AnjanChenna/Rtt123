
# python pip8 standars

PRODUCT_DETAILS = ["chairs", "bags", "mobiles"]
PRODUCT_DETAILS2 = ["chairs12", "bags12", "mobiles12"]

# print(123)
var1 = 123
var2 = "python121"
var3 = 11.231
print("testing")

# print(var1+var3)
#list
var4 = [1,2,3,"name1","name2", 11.21, "22.3",[11,22],[[12111,1212121,1212]]]
var5 = [{'names':[1,2,3], 'locations':[1,24,]}, {'names':[]}]
# flipkart.... nike [product1_Details 100rs , pd 200rs., 150rs, .......]

var5 = [12, var1, var3, "anj"]  # [12, 123, 11.231, "anj"]

# list operation
PRODUCT_DETAILS.append("mouse")
# ["chairs", "bags", "mobiles" , "mouse"]   # length 4 ---> index 0 to 3
# print(PRODUCT_DETAILS)
# slicing
# indexing --> starts from 0  ,,, -1 from last item
# print(PRODUCT_DETAILS[0])
# print(PRODUCT_DETAILS[-1])

# print(PRODUCT_DETAILS[0:3])   # start index : end index-1
# print(PRODUCT_DETAILS[:3])   # start index : end index-1
# print(PRODUCT_DETAILS[-2:])
string1 = "my-name is-python"
# print(string1[0:10])
list1_split = string1.split('-')   # ["my", "name",...]
# print(list1_split)
# print(PRODUCT_DETAILS)

PRODUCT_DETAILS_TEMP = PRODUCT_DETAILS

# del PRODUCT_DETAILS[0]
# print(PRODUCT_DETAILS)
# print(PRODUCT_DETAILS2)

PRODUCT_DETAILS.extend(PRODUCT_DETAILS2)
# print(PRODUCT_DETAILS)
# del PRODUCT_DETAILS[-1]   # another syntax pop
# PRODUCT_DETAILS.pop()
# PRODUCT_DETAILS.pop()

# print(PRODUCT_DETAILS)

# append, extecd, del, pop, insert    --- mobiles name ---> "mobiles333"
# slicing ----> data read only
# print(PRODUCT_DETAILS[3])

# PRODUCT_DETAILS.insert(3,"mobiles333")
# print(PRODUCT_DETAILS[3])
# ['chairs', 'bags', 'mobiles', 'mobiles333', 'mouse', 'chairs12', 'bags12', 'mobiles12']
# # overwrite  PRODUCT_DETAILS[3] = "mobiles333"
# PRODUCT_DETAILS[3] = "mobiles333"
# print('actual output is',)

# python list , operations

# index  ----> 'mouse' ,,----> "mouse1"
# PRODUCT_DETAILS - ['chairs', 'bags', 'mobiles', 'mouse', 'chairs12', 'bags12', 'mobiles12']
# mouse_index = PRODUCT_DETAILS.index('mouse')  # 3
# print(mouse_index)
# PRODUCT_DETAILS.insert(mouse_index+1,  "mouse1")
# print(PRODUCT_DETAILS)

"""
tuple
"""

# same as list
"""
list             |     tuble
items modify     |     cant modify
mutable                immutable
[]                     ()
[1,2,"at"]             (1,2,"at")
"""

"""
Dictionary  ----> it is a data type in python , it holds  keys and values in a flower brakets
"""
dict1 = {'name': 'python', 'id': 123, 'place':'india'}

# print(list(dict1.keys()))

# all keys
# all_keys = dict1.keys()
# print(all_keys)
# print(type(all_keys))
# keys_to_list = list(all_keys)
# print(keys_to_list)
# print(type(keys_to_list))

# print(dict1.values())
# print(type(PRODUCT_DETAILS))

"""
int , str, list, tuple, dict  -----> type
"""
dict1 = {'name': 'python', 'id': 123, 'place':'india'}

# print(dict1['place'])

dict2 = {'names':['name1','name2', 'name3'], 'id': [1,2,3,]}
dict3 = {
    'names':{
        'location':{'place':['a',[1,2,3], "t",1]},
        'ids': [1,2,3,4,5]},
    'id': [1,2,3,]
}
# print(dict3.keys())

# print(dict3['names'])
print(dict3['names']['location']['place'])
"""
dict3['names'] = {  'location': {'place': ['a', [1, 2, 3], 't', 1]}, 
                    'ids': [1, 2, 3, 4, 5]}
print(dict3['names']['ids'])  
              
"""

# print(dict3["ids"])

# list, tuple ,
# dict , set -->
# set ---> we cant modify data
# set1 = {"laptop", "mouse", "keuboard", "laptop","mouse","mouse","tttttt", "mouse"}
# print(set1)
dict1 = {'name': 'python', 'id': 123, 'place':'india'}
print(dict1)
dict1["location"] = "banglr"
dict1["id"] = 34555
print(dict1)






import csv
file = csv.reader(open(''))
1) no of rows in file
2) no of columns
3) all column names in a list
4) in "Series_title_2" column data : {"Forestry and Logging": count,
                    "Fishing, Aquaculture and Agriculture, Forestry and Fishing Support Services":count
                    ......
                    ....}
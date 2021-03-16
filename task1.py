# pass
# break
# continue
import re
var1 = "aaabaaadbbaaccddaa"
 # (a,b,c,d)
output = {}

count = 1
for i in range(1, len(var1)):
    if var1[i-1] == var1[i]:
        count +=1
    else:
        if var1[i-1] not in output:
            output[var1[i-1]] = count
        count=1

print(output)







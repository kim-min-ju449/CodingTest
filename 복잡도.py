array = [3,5,1,2,4]
summary = 0

for x in array:
    summary +=x

print(summary)
print("=============")
array2 = [3,5,1,2,4]
for i in array2:
    for j in array2:
        temp = i*j
        print(temp)
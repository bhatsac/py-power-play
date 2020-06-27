i = 0
while i < 10:
    print("Current value of i is: ",i)
    i = i+1
else:
    print("Loop is completed..")

A = [1, 2, 3, 4, 5, 6, 7]  # This is a list
B = (1, 2, 3, 4, 5, 6, 7)  # This ia a tuple
C = {1, 2, 3, 4, 5, 6, 7}  # This is a set
D = {"name": "Sachin", "age": 32}  # dictionary
E = "Sachin"
# In keyword
print(2 in B)
print(9 in A)

for i in A:
    print(i)
for i in B:
    print(i)
for i in C:
    print(i)
for i in D:
    print(i)
    print(D[i])
for i,j in D.items():
    print(i, j)
for i in E:
    print(i)


# Range Keyword
for x in range(1, 5, 1):
    print(x, end="\t")
else:
    print("For loop completed")


# Range Keyword
for x in range(1, 100, 3*5):
    print(x)
    if x % 2 == 0:
        break
    else:
        continue
else:
    print("For loop completed")

# Break & continue

for i in range(1, 10):
    if i == 7:
        break
    elif i == 3:
        continue
    print(i, end="\t")
# def replace_word(val):
#     strg = []
#     for i in range(len(val)):
#         if i %2==1:
#             strg += [val[i].upper()]
#         else:
#             strg += [val[i]]
#     return "".join(strg)
# a = input("Enter the string : ").split()
# b = input("Enter the word : ")
# if b not in a:
#     print("Word not found")
#     exit()
# for i in range(len(a)):
#     if a[i] == b:
#         a[i] = replace_word(b)
# print(" ".join(a))



val = int(input("Enter the number :"))
limit = 100
count =0
for i in range(10000):
    if i==limit:
        break
    for j in range(10000):
        if i**3+j**3==val:
            count+=1
            limit=j

if count>=2:
    print("Its a ramanujan value")
else:
    print("Its not a ramanujan value")
    


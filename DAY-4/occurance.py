'''given a string which is the company name in lower case, letter,
 your task is to find the top three most common characters in the string. 
print the three most common along with their occurrence count.
if the occourance count is same then sort them alphabetically.
input 
aabbbccdef
output
b 3
a 2
c 2'''



a  = str(input("enter the string: ")).split()
b={}
for i in a:
    for j in i:
        if j in b:
            b[j]+=1
        else:
            b[j]=1
c=sorted(b.items(),key=lambda x:(-x[1],x[0]))
for i in range(3):
    print(c[i][0],c[i][1])




# input = str(input("enter the num: ")).split()
# new = {}
# for i in input:
#     for j in i:
#         if j in new:
#             new[j] = +1
#         else:
#             new[j]=1
# c = sorted(new.items(), key=lambda x:(-x[1],x[0]))
# for i in range(3):
#     print(c[i][0],c[i][1])


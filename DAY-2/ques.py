


# question 2
#example; input
# input[{"name", "harry", "age", "40"},{"name","rohit", "age","35"}]
# output in sorted ascending order
# [{"name", "rohit", "age", "35"},{"name","harry", "age","40"}]

# solve using ages 





# mydict = {}
# for _ in range(3):
#     name = input("Enter name: ")
#     age = int(input("Enter age: "))
#     mydict[name] = age
#     # reverse the dict
# sorteddict = dict(sorted(mydict.items(), key = lambda ))
# print(sorteddict)





# new=input("enter str: ")
# a= input("enter char to remove: ")
# b= input("which value u want to add: ")

# result = new.replace(a,b)
# print(result)


string = "bbbbbbaaaaaa"
# charcount = {}
# for char in string:
#     if char in charcount:
#         charcount[char] += 1
#     else:
#         charcount[char] = 1
# print(charcount)string = "adshbadsaa"

# charcount = {}

# for char in string:
#     charcount[char] = charcount.get(char, 0) + 1

# print("Repeated :")
# for char, count in charcount.items():
#     if count > 1:
#         print(char)
findstr = "a" 

for char in string[:5]:
    if char == findstr:
        print("True")
        break
else:
    print("false")


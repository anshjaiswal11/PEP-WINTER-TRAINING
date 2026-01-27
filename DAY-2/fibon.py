#create a fnction that take input and it should print the fibonocci series 
 
# def fibonocci(n):
#     a, b = 0, 1
#     series = [] 
#     for _ in range(n):
#         series.append(a)
#         a, b = b, a + b
#     return series   



# use recursion to print fibonocci series
def fibonocci_recur(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibonocci_recur(n - 1)
        series.append(series[-1] + series[-2])
        return series


def a(n):
    a, b = 0, 1
    new_list = []
    for _ in range(n):
        new_list.append(a)
        a, b = b, a+b
    return new_list 

if __name__ == "__main__":
    n = int(input("Enter the number:- "))
    print(a(n))






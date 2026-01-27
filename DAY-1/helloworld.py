import function as func

def func():
    return func.add(5, 3), func.subtract(5, 3), func.multiply(5, 3), func.divide(5, 3)

if __name__ == "__main__":  
    result = func()
    print("Addition:", result[0])
    print("Subtraction:", result[1])
    print("Multiplication:", result[2])
    print("Division:", result[3])

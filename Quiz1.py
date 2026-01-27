def pul_11(*num):
    return sum(num)

def pul_12(func):
    def wrapper(*num):
        return func(*num) // len(num)
    return wrapper

result = pul_12(pul_11)(1, 2, 3, 4, 5)
print(result)

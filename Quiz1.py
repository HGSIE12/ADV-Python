def pul_11(*num):
    return sum(num)

def pul_12(*num):
    def wrapper():
        return pul_11(*num) // len(num)
    return wrapper()

result = pul_12(1, 2, 3, 4, 5)
print(result)

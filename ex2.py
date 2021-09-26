def decorator(func):
    def wrapper(*args,**kwargs):
        val = func(*args,**kwargs)
        if val == 0 :
            return 'Нет'
        elif val > 10:
            return 'очень много'
        else:
            return val
    return wrapper

@decorator
def count_even_number(A):
    count = 0
    for x in A:
        if x % 2 == 0:
            count += 1
    return count

A = list(map(int,input().split()))
print(count_even_number(A))





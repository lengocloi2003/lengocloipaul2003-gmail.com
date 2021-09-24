def even_number(func):
    A = list(map(int, input().split()))
    def count_number():
        count = 0
        for x in A:
            if x % 2 == 0:
                count+=1
        if count>10:
            func(True)
        elif count == 0:
            func(False)
    return count_number
@even_number
def print_count(flag):
    if flag == True:
        print("Очень много")
    else:
        print('Нет')
print_count()




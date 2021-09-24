def even_number(func):
    A = list(map(int, input().split()))
    def count_number():
        count = 0
        for x in A:
            if x % 2 == 0:
                count+=1
        return count
    if count_number()>10:
        func()
    elif count_number() == 0 :
        print('Нет')
@even_number
def print_count():
    print("Очень много")





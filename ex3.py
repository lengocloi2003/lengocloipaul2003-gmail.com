def swap(func):
    def doi_so(x,y,show):
            x,y = y ,x
            show = True
            return func(x,y,show)
    return doi_so

@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show=True)



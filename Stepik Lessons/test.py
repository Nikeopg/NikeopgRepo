import timeit
c  = """
def find_it(seq):
    d = {}
    for i in seq:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    for k,v in d.items():
        if v % 2 != 0:
            return k
"""
x_time = timeit.timeit(c)
print(x_time)
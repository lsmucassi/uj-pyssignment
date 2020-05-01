num_lst = []

def sqr_num(n):
    return n ** 2

for i in range(0, 5):
    num = int(input("Enter a number: "))
    num_lst.append(num)

num_tpl = tuple(num_lst)
for i in num_lst:
    sqr_tpl = sqr_num(i)
    print(sqr_tpl)

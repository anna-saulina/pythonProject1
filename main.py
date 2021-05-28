from random import randint
# В последовательности a(n) найти сумму целых элементов, расположенных между минимальным и максимальным элементами.
a = []
for i in range(999):
    a.append(randint(0, 1000))
print(a)
mn = a.index(min(a))
mx = a.index(max(a))
if mn < mx:
    print(sum(a[mn+1: mx]))
else:
    print(sum(a[mx+1: mn]))
























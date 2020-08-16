def func(k, a):
    j = 0
    while j != len(a)-1:

        for i in range(j, len(a)-1):

            if (a[j]+a[i+1]) == k:
                print("The summ equals k")
                print(f'These elems are equal {a[j]} and {a[i+1]}')
                return [a[j], a[i+1]]
                break
        j += 1
    return False

t1 = func(5, [1, 2, 3, 4, 5])
assert t1 == [1, 4]

t2 = func(5, [1, 2, 7, 7, 5])
assert t2 == False

t3 = func(9, [7, 2, 3, 4, 5])
assert t3 == [7, 2]

def person(name, age, *, city, job):  # *后面的参数被视为命名关键字函数
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


f1(1, 2, 3, 'a', 'b', 'c', x=99)

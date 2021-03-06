from model import *
import math

class Schaffer(model):
    def __init__(i):
        dec = [Has('x', -1e2, 1e2)]
        obj = [Has(name='f1', goal = lt, touch=False),
               Has(name='f2', goal = lt, touch=False)]
        model.__init__(i,dec,obj)
        
    def f1(i, c):
        x = c.decs[0]
        return x**2

    def f2(i,c):
        x = c.decs[0]
        return (x-2)**2

    def objectives(i):
        return [i.f1, i.f2]

class Osyczka2(model):
    def __init__(i):
        dec = [Has('x1', 0,10),
               Has('x2', 0,10),
               Has('x3', 1,5),
               Has('x4', 0,6),
               Has('x5', 1,5),
               Has('x6', 0,10)]
        obj = [Has(name='f1', goal = lt, touch=False),
               Has(name='f2', goal = lt, touch=False)]
        model.__init__(i,dec,obj)

    def f1(i,c):
        [x1,x2,x3,x4,x5,x6] = [x for x in c.decs]
        return -(25*(x1-2)**2+(x2-2)**2+(x3-1)**2*(x4-4)**2+(x5-1)**2)

    def f2(i,c):
        return sum(x**2 for x in c.decs)

    def ok(i,c):
        if not model.ok(i,c): return False
        [x1,x2,x3,x4,x5,x6] = [x for x in c.decs]
        g1 = x1+x2-2
        g2 = 6-x1-x2
        g3 = 2-x2+x1
        g4 = 2-x1+3*x2
        g5 = 4-(x3-3)**2-x4
	g6 = (x5-3)**3+x6-4
	return min(g1,g2,g3,g4,g5,g6) >= 0

    def objectives(i):
        return [i.f1,i.f2]
    

class Kursawe(model):
    def __init__(i):
        dec = [Has('x1', -5,5),
               Has('x2', -5,5),
               Has('x3', -5,5)]
        obj = [Has(name='f1', goal = lt, touch=False),
               Has(name='f2', goal = lt, touch=False)]
        model.__init__(i,dec,obj)

    def f1(i,c):
        [x1,x2,x3] = [x for x in c.decs]
        t1 = math.sqrt(x1**2+x2**2)
        t2 = math.sqrt(x2**2+x3**2)
        return -10*(math.exp(-0.2*t1)+math.exp(-0.2*t2))

    def f2(i,c): # let a=b=1
        return sum(abs(x)+5*math.sin(x) for x in c.decs)

    def objectives(i):
        return [i.f1,i.f2]

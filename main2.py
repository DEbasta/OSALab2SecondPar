from random import random, randint

from scipy.optimize import differential_evolution
from scipy.optimize import linprog


class Lab3:
    I11 = randint(2,5)
    I21 = randint(2,5)
    I31 = randint(2,5)
    J1 = [I11,I21,I31]
    I12 = randint(2,5)
    I22 = randint(2,5)
    I32 = randint(2,5)
    J2 = [I12,I22,I32]
    amounts = [randint(200,700), randint(200,700),  randint(200,700)]
    profit = [randint(50,250), randint(50,250)]
    revenue = [randint(200,1400), randint(200,1400)]
    cost = [randint(70, 300), randint(70, 300)]


    fun = [0,0,0]
    XArr = [[],[],[]]
    Left = [[],[],[]]



    def CF1(self):
        obj1 = [-self.profit[0], -self.profit[1]]
        lhs_ineq = [[self.J1[0], self.J2[0]], [self.J1[1], self.J2[1]], [self.J1[2], self.J2[2]]]
        rhs_ineq = [self.amounts[0], self.amounts[1], self.amounts[2]]
        bnd = [(0, None), (0, None)]
        opt1 = linprog(c=obj1, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd)
        self.fun[0] = -opt1.fun
        self.XArr[0] = opt1.x
        self.Left[0] = opt1.ineqlin.residual

        print(self.amounts)
        print(opt1.ineqlin.residual)

    def CF2(self):
        obj1 = [-self.revenue[0], -self.revenue[1]]
        lhs_ineq = [[self.J1[0], self.J2[0]], [self.J1[1], self.J2[1]], [self.J1[2], self.J2[2]]]
        rhs_ineq = [self.amounts[0], self.amounts[1], self.amounts[2]]
        bnd = [(0, None), (0, None)]
        opt1 = linprog(c=obj1, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd)
        self.fun[1] = -opt1.fun
        self.XArr[1] = opt1.x
        self.Left[1] = opt1.ineqlin.residual

        print(self.amounts)
        print(opt1.ineqlin.residual)

    def CF3(self):
        obj1 = [-self.cost[0], -self.cost[1]]
        lhs_ineq = [[self.J1[0], self.J2[0]], [self.J1[1], self.J2[1]], [self.J1[2], self.J2[2]]]
        rhs_ineq = [self.amounts[0], self.amounts[1], self.amounts[2]]
        bnd = [(0, None), (0, None)]
        opt1 = linprog(c=obj1, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd)
        self.fun[2] = -opt1.fun
        self.XArr[2] = opt1.x
        self.Left[2] = opt1.ineqlin.residual

        print(self.amounts)
        print(opt1.ineqlin.residual)






l = Lab3()

l.CF1()
l.CF2()
l.CF3()
print(l.fun)
print(l.XArr)
print(l.Left)


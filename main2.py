from random import random, randint

from scipy.optimize import differential_evolution
from scipy.optimize import linprog


class Lab3_1:
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


    fun = [0,0,0,0,0]
    XArr = [[],[],[],[],[]]
    Left = [[],[],[],[],[]]

    CF4Det = [1,1,-1]
    CF5Det = [0,0,0]

    XY1 = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    XY2 = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

    def __init__(self):
        self.CF(self.profit,[(0, None), (0, None)], 0)
        self.CF(self.revenue,[(0, None), (0, None)], 1)
        self.CF(self.cost, [(None, 0), (None, 0)], 2)
        a = [(self.CF4Det[0] * self.profit[0] + self.CF4Det[1] * self.revenue[0] + self.CF4Det[2] * self.cost[0]),
             (self.CF4Det[0] * self.profit[0] + self.CF4Det[1] * self.revenue[0] + self.CF4Det[2] * self.cost[0])]
        self.CF(a,[(0, None), (0, None)], 3)
        a = [(self.CF5Det[0] * self.profit[0] + self.CF5Det[1] * self.revenue[0] + self.CF5Det[2] * self.cost[0]),
             (self.CF5Det[0] * self.profit[0] + self.CF5Det[1] * self.revenue[0] + self.CF5Det[2] * self.cost[0])]
        self.CF(a,[(0, None), (0, None)], 4)
        self.genCF5()
        print(self.fun)
        print(self.XArr)
        print(self.Left)
        print(self.CF5Det)
        self.dots()
        print(self.XY1)
        print(self.XY2)


    def genCF5(self):
        R1 = randint(1, 9)
        R2 = randint(1, 9)
        R3 = randint(1, 9)

        R1 = R1 / 10
        R2 = R2 / 10
        R3 = R3 / 10

        R1 = round(R1, 1)
        R2 = round(R2, 1)
        R3 = round(R3, 1)

        SUM = R1 + R2 + R3
        SUM = round(SUM, 1)

        while (SUM != 1):
            if (SUM < 1):
                if ((R1 + 0.1) <= 0.9):
                    R1 += 0.1
                    R1 = round(R1, 1)
                    SUM = R1 + R2 + R3
                    SUM = round(SUM, 1)
                if (SUM < 1):
                    if ((R2 + 0.1) <= 0.9):
                        R2 += 0.1
                        R2 = round(R2, 1)
                        SUM = R1 + R2 + R3
                        SUM = round(SUM, 1)
                if (SUM < 1):
                    if ((R3 + 0.1) <= 0.9):
                        R3 += 0.1
                        R3 = round(R3, 1)
                        SUM = R1 + R2 + R3
                        SUM = round(SUM, 1)
            elif (SUM > 1):
                if ((R1 - 0.1) >= 0.1):
                    R1 -= 0.1
                    R1 = round(R1, 1)
                    SUM = R1 + R2 + R3
                    SUM = round(SUM, 1)
                if (SUM > 1):
                    if ((R2 - 0.1) >= 0.1):
                        R2 -= 0.1
                        R2 = round(R2, 1)
                        SUM = R1 + R2 + R3
                        SUM = round(SUM, 1)
                if (SUM > 1):
                    if ((R3 - 0.1) >= 0.1):
                        R3 -= 0.1
                        R3 = round(R3, 1)
                        SUM = R1 + R2 + R3
                        SUM = round(SUM, 1)
            self.CF5Det = [R1, R2, -R3]

    def CF(self, arr, bounds, iter):
        obj1 = [-arr[0], -arr[1]]
        lhs_ineq = [[self.J1[0], self.J2[0]], [self.J1[1], self.J2[1]], [self.J1[2], self.J2[2]]]
        rhs_ineq = [self.amounts[0], self.amounts[1], self.amounts[2]]
        opt1 = linprog(c=obj1, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bounds)
        if (opt1.fun == 0):
            self.fun[iter] = opt1.fun
        else:
            self.fun[iter] = -opt1.fun
        self.XArr[iter] = opt1.x
        self.Left[iter] = opt1.ineqlin.residual

        print(self.amounts)
        print("  ||  ||   ||")
        print("  \/  \/   \/")
        print(opt1.ineqlin.residual)

    def dots(self):
        for i in range(3):
            self.XY1[i] = [0, self.J1[i]]
            self.XY2[i] = [self.J2[i], 0]

        self.XY1[3] = [0, self.fun[0] * 2 / self.profit[0]]
        self.XY2[3] = [self.fun[0] * 2 / self.profit[1], 0]
        self.XY1[4] = [0, self.fun[1] * 2 / self.revenue[0]]
        self.XY2[4] = [self.fun[1] * 2 / self.revenue[1], 0]
        self.XY1[5] = [0, self.fun[0] * 2 / self.cost[0]]
        self.XY2[5] = [self.fun[0] * 2 / self.cost[1], 0]

        if (self.fun[3] > self.fun[4]):
            self.XY1[6] = [0, self.fun[3] * 2 / self.cost[0]]
            self.XY2[6] = [self.fun[3] * 2 / self.cost[1], 0]
        elif (self.fun[4] > self.fun[3]):
            self.XY1[6] = [0, self.fun[4] * 2 / self.cost[0]]
            self.XY2[6] = [self.fun[4] * 2 / self.cost[1], 0]

class Lab3_2:
    XY1 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    XY2 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    amounts = []
    J1 = []
    J2 = []
    profit = []
    revenue = []
    cost = []

    fun = [0, 0, 0]
    XArr = [[], [], []]
    Left = [[], [], []]

    concessions = 5
    def __init__(self, XY1, XY2, amounts, J1, J2, profit, revenue, cost):
        self.XY1 = XY1
        self.XY2 = XY2
        self.amounts = amounts
        self.J1 = J1
        self.J2 = J2
        self.profit = profit
        self.revenue = revenue
        self.cost = cost

        CF = input("Select CF (1 - 3)\n")
        if (CF == "1"):
            self.CF1(self.profit, [(0, None), (0, None)])
            self.CF2(self.revenue + self.profit, [(0, None), (0, None)])
            self.CF3(self.cost + self.profit + self.revenue, [(0, None), (0, None)])
        elif (CF == "2"):
            self.CF1(self.revenue, [(0, None), (0, None)])
            self.CF2(self.profit + self.revenue, [(0, None), (0, None)])
            self.CF3(self.cost + self.revenue + self.profit, [(0, None), (0, None)])
        elif (CF == "3"):
            self.CF1(self.cost, [(None, 0), (None, 0)])
            self.CF2(self.profit + self.cost, [(0, None), (0, None)])
            self.CF3(self.revenue + self.cost + self.profit, [(0, None), (0, None)])

    def CF1(self, arr, bounds):
        obj1 = [-arr[0], -arr[1]]
        lhs_ineq = [[self.J1[0], self.J2[0]], [self.J1[1], self.J2[1]], [self.J1[2], self.J2[2]]]
        rhs_ineq = [self.amounts[0], self.amounts[1], self.amounts[2]]
        opt1 = linprog(c=obj1, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bounds)
        if (opt1.fun == 0):
            self.fun[0] = opt1.fun
        else:
            self.fun[0] = -opt1.fun
        self.XArr[0] = opt1.x
        self.Left[0] = opt1.ineqlin.residual

        print(self.amounts )
        print("  ||  ||   ||")
        print("  \/  \/   \/")
        print(opt1.ineqlin.residual)

    def CF2(self, arr, bounds):
        obj1 = [-arr[0], -arr[1]]
        lhs_ineq = [[self.J1[0], self.J2[0]], [self.J1[1], self.J2[1]], [self.J1[2], self.J2[2]], [arr[2], arr[3]]]
        rhs_ineq = [self.amounts[0], self.amounts[1], self.amounts[2], self.fun[0] - (self.fun[0] / 100 * self.concessions)]
        opt1 = linprog(c=obj1, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bounds)
        if (opt1.fun == 0):
            self.fun[1] = opt1.fun
        else:
            self.fun[1] = -opt1.fun
        self.XArr[1] = opt1.x
        self.Left[1] = opt1.ineqlin.residual

        print(self.amounts ," " ,self.fun[0] - (self.fun[0] / 100 * self.concessions))
        print("  ||  ||   ||   ||")
        print("  \/  \/   \/   \/")
        print(opt1.ineqlin.residual)

    def CF3(self, arr, bounds):
        obj1 = [-arr[0], -arr[1]]
        lhs_ineq = [[self.J1[0], self.J2[0]], [self.J1[1], self.J2[1]], [self.J1[2], self.J2[2]], [arr[2], arr[3]], [arr[4], arr[5]]]
        rhs_ineq = [self.amounts[0], self.amounts[1], self.amounts[2], self.fun[0] - (self.fun[0] / 100 * self.concessions),
                    self.fun[1] - (self.fun[1] / 100 * self.concessions)]
        opt1 = linprog(c=obj1, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bounds)
        if (opt1.fun == 0):
            self.fun[2] = opt1.fun
        else:
            self.fun[2] = -opt1.fun
        self.XArr[2] = opt1.x
        self.Left[2] = opt1.ineqlin.residual

        print(self.amounts ," " ,self.fun[0] - (self.fun[0] / 100 * self.concessions), " ", self.fun[1] - (self.fun[1] / 100 * self.concessions))
        print("  ||  ||   ||   ||")
        print("  \/  \/   \/   \/")
        print(opt1.ineqlin.residual)








l1 = Lab3_1()
XY1 = [Lab3_1.XY1[0], Lab3_1.XY1[1], Lab3_1.XY1[2], [0,0], [0,0], [0,0]]
XY2 = [Lab3_1.XY2[0], Lab3_1.XY2[1], Lab3_1.XY2[2], [0,0], [0,0], [0,0]]
amounts = Lab3_1.amounts
J1 = Lab3_1.J1
J2 = Lab3_1.J2
profit = Lab3_1.profit
revenue = Lab3_1.revenue
cost = Lab3_1.cost




l2 = Lab3_2(XY1, XY2, amounts, J1, J2, profit, revenue, cost)



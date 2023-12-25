from random import random, randint

from scipy.optimize import differential_evolution


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

    X1 = [profit[0], I11, I21,I31, 1, 0]
    X2 = [profit[1], I12, I22, I32, 0, 1]
    rightCF1 = [0, 0, 0, 0, 0, 0]

    def CF1(self, solution):
        c1,c2 = solution
        return self.X1[0] * c1 + self.X2[0] * c2

    def CF11(self, solution):
        c1,c2 = solution
        return self.X1[1] * c1 + self.X2[1] * c2

    def CF12(self, solution):
        c1,c2 = solution
        return self.X1[2] * c1 + self.X2[2] * c2

    def CF13(self, solution):
        c1,c2 = solution
        return self.X1[3] * c1 + self.X2[3] * c2

    flag1 = False
    flag2 = False
    flag3 = False

    def Counting(self):
            max = self.amounts[0]
            min = self.amounts[0]
            for i in self.amounts:
                if i > max:
                    max = i
                if i < min:
                    min = i

            bounds = [[-100, 100], [-100, 100]]
            Res = differential_evolution(self.CF1, bounds)
            self.rightCF1[5] = Res.x[1]
            self.rightCF1[4] = Res.x[0]
            self.rightCF1[3] = self.X1[3] * Res.x[0] + self.X2[3] * Res.x[1]
            self.rightCF1[2] = self.X1[2] * Res.x[0] + self.X2[2] * Res.x[1]
            self.rightCF1[1] = self.X1[1] * Res.x[0] + self.X2[1] * Res.x[1]
            self.rightCF1[0] = Res.fun
            if self.rightCF1[1] <= self.amounts[0]:
                self.flag1 = True
            else: self.flag1 = False
            if self.rightCF1[2] <= self.amounts[1]:
                self.flag2 = True
            else: self.flag2 = False
            if self.rightCF1[3] <= self.amounts[1]:
                self.flag3 = True
            else:
                self.flag3 = False

            print(Res.x)
            print(Res.fun)
            print(self.rightCF1[1] , " <= " , self.amounts[0])
            print(self.rightCF1[2] , " <= " , self.amounts[1])
            print(self.rightCF1[3] , " <= " , self.amounts[2])




l = Lab3()
l.Counting()

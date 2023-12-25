import math
from array import array

from scipy.optimize import differential_evolution

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

class Lab2:
    def convertStringArray(array):
        retArray = []
        for element in array:
            if (element != ''):
                retArray.append(float(element))
        return retArray

    text_file = open("x1.txt", "r")
    x1 = text_file.read().split(' ')
    y = convertStringArray(x1)
    x1NP = np.array(y, dtype="float")

    text_file = open("x2.txt", "r")
    x2 = text_file.read().split(' ')
    y = convertStringArray(x2)
    x2NP = np.array(y, dtype="float")

    text_file = open("x3.txt", "r")
    x3 = text_file.read().split(' ')
    y = convertStringArray(x3)
    x3NP = np.array(y, dtype="float")

    text_file = open("x4.txt", "r")
    x4 = text_file.read().split(' ')
    y = convertStringArray(x4)
    x4NP = np.array(y, dtype="float")

    text_file = open("x5.txt", "r")
    x5 = text_file.read().split(' ')
    y = convertStringArray(x5)
    x5NP = np.array(y, dtype="float")

    text_file = open("x6.txt", "r")
    x6 = text_file.read().split(' ')
    y = convertStringArray(x6)
    x6NP = np.array(y, dtype="float")

    text_file = open("x7.txt", "r")
    x7 = text_file.read().split(' ')
    y = convertStringArray(x7)
    x7NP = np.array(y, dtype="float")

    text_file = open("x8.txt", "r")
    x8 = text_file.read().split(' ')
    y = convertStringArray(x8)
    x8NP = np.array(y, dtype="float")

    text_file = open("x9.txt", "r")
    x9 = text_file.read().split(' ')
    y = convertStringArray(x9)
    x9NP = np.array(y, dtype="float")

    text_file = open("y1.txt", "r")
    y1 = text_file.read().split(' ')
    y = convertStringArray(y1)
    y1NP = np.array(y, dtype="float")

    text_file = open("y2.txt", "r")
    y2 = text_file.read().split(' ')
    y = convertStringArray(y2)
    y2NP = np.array(y, dtype="float")

    A0 = 0
    A1 = 0
    A2 = 0
    A3 = 0
    A11 = 0
    A12 = 0
    A13 = 0
    A21 = 0
    A22 = 0
    A23 = 0
    Y1Coord = 0
    Y2Coord = 0
    def countRegression(self):
        xLinear = np.array([self.x1NP, self.x2NP, self.x3NP], dtype="float").T
        xQuadro = np.array([self.x1NP, self.x2NP, self.x3NP, self.x4NP, self.x5NP, self.x6NP, self.x7NP, self.x8NP, self.x9NP], dtype="float").T
        R1 = [0,0]
        R2 = [0,0]
        R = 0
        FLAG = False

        model = sm.OLS(self.y1NP, sm.add_constant(xLinear))
        results = model.fit()
        print("Linear regression for first parameter Y")
        print(results.summary())
        R1[0] = results.rsquared

        model = sm.OLS(self.y2NP, sm.add_constant(xLinear))
        results = model.fit()
        print("Linear regression for second parameter Y")
        print(results.summary())
        R1[1] = results.rsquared


        model = sm.OLS(self.y1NP, sm.add_constant(xQuadro))
        results = model.fit()
        print("Quadratic regression for first parameter Y")
        print(results.summary())
        R2[0] = results.rsquared

        model = sm.OLS(self.y2NP, sm.add_constant(xQuadro))
        results = model.fit()
        print("Quadratic regression for second parameter Y")
        print(results.summary())
        R2[1] = results.rsquared

        for i in R1:
            if (i > R):
                R = i

        for i in R2:
            if (i > R):
                R = i
                FLAG = True

        bounds = [[np.amin(self.x1NP), np.amax(self.x1NP)], [np.amin(self.x2NP), np.amax(self.x2NP)], [np.amin(self.x3NP), np.amax(self.x3NP)]]

        #выбор модели
        print(FLAG)
        if(not FLAG):
            model = sm.OLS(self.y1NP, sm.add_constant(xLinear))
            results = model.fit()
            self.A0 = results.params[0]
            self.A1 = results.params[1]
            self.A2 = results.params[2]
            self.A3 = results.params[3]
            Res = differential_evolution(self.fLin, bounds)
            self.Y1Coord = Res.fun

            model = sm.OLS(self.y2NP, sm.add_constant(xLinear))
            results = model.fit()
            self.A0 = results.params[0]
            self.A1 = results.params[1]
            self.A2 = results.params[2]
            self.A3 = results.params[3]
            Res = differential_evolution(self.fLin, bounds)
            self.Y2Coord = Res.fun
        else:
            model = sm.OLS(self.y1NP, sm.add_constant(xQuadro))
            results = model.fit()
            self.A0 = results.params[0]
            self.A0 = results.params[0]
            self.A1 = results.params[1]
            self.A2 = results.params[2]
            self.A3 = results.params[3]
            self.A11 = results.params[4]
            self.A12 = results.params[5]
            self.A13 = results.params[6]
            self.A21 = results.params[7]
            self.A22 = results.params[8]
            self.A23 = results.params[9]
            Res = differential_evolution(self.fQuad, bounds)
            self.Y1Coord = Res.fun

            model = sm.OLS(self.y2NP, sm.add_constant(xQuadro))
            results = model.fit()
            self.A0 = results.params[0]
            self.A1 = results.params[1]
            self.A2 = results.params[2]
            self.A3 = results.params[3]
            self.A11 = results.params[4]
            self.A12 = results.params[5]
            self.A13 = results.params[6]
            self.A21 = results.params[7]
            self.A22 = results.params[8]
            self.A23 = results.params[9]
            Res = differential_evolution(self.fQuad, bounds)
            self.Y2Coord = Res.fun
            



    def fLin(self, solution):
        X1, X2, X3 = solution
        return self.A0 + self.A1 * float(X1) + self.A2 * float(X2) + self.A3 * float(X3)


    def fQuad(self, solution):
        X1, X2, X3 = solution

        return (self.A0 + self.A1 * float(X1) + self.A2 * float(X2) + self.A3 * float(X3)
                + self.A11 * pow(X1,2) + self.A12 * X1 * X2 + self.A13 * X1 * X3
                + self.A21 * pow(X2,2)+ self.A22 * X2 * X3 + self.A23 * pow(X3,2))

    def draw(self):
        self.optimal = [str(-self.Y1Coord), str(-self.Y2Coord)]
        plt.scatter(self.y1, self.y2, label='Показатели выборки')
        plt.scatter(self.optimal[0], self.optimal[1], marker='x', label='Оптимальные значения')
        plt.xlabel('y1')
        plt.ylabel('y2')
        plt.legend()
        plt.grid()
        plt.show()

l = Lab2()
l.countRegression()
l.draw()





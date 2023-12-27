import numpy as np
from scipy.optimize import differential_evolution

def constraint_function(x, r1, r2, a):
    return a - x[0] * r1 - x[1] * r2

def objective_function(x, r1, r2, f_target):
    # x[0] - это x1, x[1] - это x2
    f_calculated = x[0] * r1 + x[1] * r2

    # Рассчитываем отклонение
    deviation = f_calculated - f_target

    # Вычисляем сумму отклонений
    total_deviation = np.sum(deviation ** 2)

    return total_deviation

# Пример данных
r1 = np.array([1, 2, 3])
r2 = np.array([4, 5, 6])
f_target = np.array([7, 8, 9])
a = np.array([10, 11, 12])

# Определение диапазона значений x1 и x2 для метода differential_evolution
bounds = [(0, a[0]), (0, a[1])]

# Определение ограничений
constraints = ({'type': 'ineq', 'fun': constraint_function, 'args': (r1, r2, a)})

# Запуск дифференциальной эволюции с учетом ограничений
result = differential_evolution(objective_function, bounds, constraints=constraints, args=(r1, r2, f_target))

# Получение оптимальных значений x1 и x2
optimal_x1, optimal_x2 = result.x


print(optimal_x1 * r1[0] + optimal_x2 * r2[0], " <= " , a[0])
print(optimal_x1 * r1[1] + optimal_x2 * r2[1], " <= " , a[1])
print(optimal_x1 * r1[2] + optimal_x2 * r2[2], " <= " , a[2])

print("Optimal x1:", optimal_x1)
print("Optimal x2:", optimal_x2)
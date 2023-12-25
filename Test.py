import numpy as np
from scipy.optimize import differential_evolution


def objective_function(x, r1, r2, f_target, a):
    # x[0] - это x1, x[1] - это x2
    f_calculated = x[0] * r1 + x[1] * r2

    # Рассчитываем отклонение и учитываем ограничения
    deviation = f_calculated - f_target
    deviation[deviation > 0] = 0  # Если f_calculated > f_target, устанавливаем отклонение в 0

    # Вычисляем сумму отклонений
    total_deviation = -np.sum(deviation)  # Минимизируем отрицательную сумму отклонений

    return total_deviation

# Пример данных
r1 = np.array([4, 3, 2])
r2 = np.array([3, 4, 4])
f_target = np.array([220, 487, 369])
a = np.array([220, 487, 369])

# Определение диапазона значений x1 и x2 для метода differential_evolution
bounds = [(0, a[0]), (0, a[1])]

# Запуск дифференциальной эволюции
result = differential_evolution(objective_function, bounds, args=(r1, r2, f_target, a))

# Получение оптимальных значений x1 и x2
optimal_x1, optimal_x2 = result.x

print(optimal_x1 * r1[0] + optimal_x2 * r2[0], " <= " , a[0])
print(optimal_x1 * r1[1] + optimal_x2 * r2[1], " <= " , a[1])
print(optimal_x1 * r1[2] + optimal_x2 * r2[2], " <= " , a[2])

print("Optimal x1:", optimal_x1)
print("Optimal x2:", optimal_x2)
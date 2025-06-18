import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры симуляции
g = 9.81  # ускорение свободного падения, м/с^2
dt = 0.05  # шаг по времени, с
total_time = 2  # общее время симуляции, с

# Начальные условия
x0, y0 = 0, 10  # начальная позиция
vx0, vy0 = 2, 0  # начальная скорость

# Списки для хранения траектории
x, y = [x0], [y0]
vx, vy = vx0, vy0

# Симуляция движения
for _ in np.arange(0, total_time, dt):
    vy -= g * dt
    x.append(x[-1] + vx * dt)
    y.append(y[-1] + vy * dt)
    if y[-1] < 1:
        y[-1] = -1
        break

# Визуализация
fig, ax = plt.subplots()
ax.set_xlim(0, max(x) + 1)
ax.set_ylim(0, max(y) + 1)
line, = ax.plot([], [], 'bo-', lw=2)

def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(x), interval=50, blit=True)
plt.title("Симуляция движения объекта")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

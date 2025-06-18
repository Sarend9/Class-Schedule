max_height = max(y)
flight_time = len(x) * dt
range_ = x[-1]
vy_last = vy0 - g * dt * (len(x) - 1)
landing_speed = np.sqrt(vx0**2 + vy_last**2)

print(f"Максимальная высота: {max_height:.2f} м")
print(f"Время полёта: {flight_time:.2f} с")
print(f"Дальность полёта: {range_:.2f} м")
print(f"Скорость при приземлении: {landing_speed:.2f} м/с")

def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit
celsius_temp = 25
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp} градусов Цельсия равно {fahrenheit_temp} градусам Фаренгейта")
try:
    celsius_input = float(input("Введите температуру в градусах Цельсия: "))
    fahrenheit_output = celsius_to_fahrenheit(celsius_input)
    print(f"{celsius_input} градусов Цельсия равно {fahrenheit_output} градусам Фаренгейта")
except ValueError:
    print("Ошибка: Пожалуйста, введите числовое значение для температуры.")

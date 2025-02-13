def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit
celsius_temp = 25
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp} �������� ������� ����� {fahrenheit_temp} �������� ����������")
try:
    celsius_input = float(input("������� ����������� � �������� �������: "))
    fahrenheit_output = celsius_to_fahrenheit(celsius_input)
    print(f"{celsius_input} �������� ������� ����� {fahrenheit_output} �������� ����������")
except ValueError:
    print("������: ����������, ������� �������� �������� ��� �����������.")

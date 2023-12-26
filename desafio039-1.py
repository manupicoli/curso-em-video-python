from datetime import date

data = date.today()

print(data)

data2 = data.strftime('%d/%m/%Y')

print(data2)

data3 = data.strftime('%Y')

print(data3)
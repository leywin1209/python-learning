```python
#1
while True:
    try:
        a = int(input('Введите число: '))
        if a % 2 == 0:
            print('Число четное')

        else:
            print("Число не четное")
        break
    except ValueError:
        print('ВВедите число')

#2
words = ["python", "go", "git", "sql", "docker"]
print([n.upper() for n in words if len(n) > 2])

#3
prices = {
    "яблоко": 50,
    "хлеб": 30,
    "молоко": 80
}

price = []

for key, value in prices.items():
    if value > 40:
        price.append(key)

print(price)

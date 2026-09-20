import random

# 1
print(f"Привіт {input('Ім\'я: ')}, тобі {input('Вік: ')}!")

# 2
print("Вхід дозволено!" if int(input("Вік: ")) > 18 else "Вхід заборонено!")

# 3
print("Гра Вгадай число:")
print("Ви вгадали!" if any(print("Менше" if g > t else "Більше") or False for t in [random.randint(1, 10)] for g in [int(input("Число (1-10): "))] if g == t) else "Спроби вичерпано")

# 4
print(*range(int(input("З: ")), int(input("По: ")) + 1))

# 5
print(*filter(lambda x: x % 2 == 0, range(int(input("n: ")), 0, -1)))

# 6
import math
print(math.prod(range(1, int(input("n: ")) + 1)))

# 7
print((["незадовільно"]*50 + ["задовільно"]*20 + ["добре"]*20 + ["відмінно"]*11)[int(input("Бали (0-100): "))])

# 8
print("Ділення на нуль" if (op := input("Дія (+ - * /): ")) == "/" and (b := float(input("b: "))) == 0 else eval(f"{float(input('a: '))}{op}{b if 'b' in locals() else float(input('b: '))}\n"))
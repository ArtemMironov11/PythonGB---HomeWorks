# Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
# не (X и Y) или Z

print("x | y | z | F")
for x in range(0,2):
  for y in range(0,2):
    for z in range(0,2):
        F = not (x and y) or z
        print(f"{x} | {y} | {z} | {int(F)}")


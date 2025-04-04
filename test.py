def euler(f, x0, y0, x_end, step):
  x = x0
  y = y0
  solution = [(x, y)]

  while x < x_end:
      y = y + step * f(x, y)  # Formule de la méthode d'Euler
      x = x + step
      solution.append((x, y))

  return solution

def user_equation(x, y):
  return x - y  # Modifie ici l'équation que tu veux résoudre


x0 = float(input("Entrer x0 (valeur initiale de x) : "))
y0 = float(input("Entrer y0 (valeur initiale de y) : "))
x_end = float(input("Entrer la valeur finale de x : "))
step = float(input("Entrer le pas de discrétisation (ex: 0.1) : "))

solution = euler(user_equation, x0, y0, x_end, step)

print("\nSolutions (x, y) :")
for x, y in solution:
  print(f"x = {x:.2f}, y = {y:.5f}")
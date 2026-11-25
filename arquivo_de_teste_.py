
import sys
sys.path.insert(0, "src")

from Lab_vetores.vetores import Vector


# Teste de norma e versor
v = Vector([3, 4])

print("Norma:", v.norma())
print("Versor:", v.versor())


# Teste de soma
u = Vector([2, 3])
w = Vector([4, 5])

resultado = u.somar(w)

print("Soma:", resultado)

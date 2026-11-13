import numpy as np

class Vector:

    def __init__(self, components):
        self.components = np.array(components, dtype=float)

        if self.components.ndim != 1: #valide para ver se o vetor é tridimensional ou que seja bidimensional 
            raise ValueError("o valor desse vetor não é valido, possui apenas uma dimensão")

        if self.components.size == 0: #n.dim verifica quantas "dimensões" o array relacionado possui 
            raise ValueError ("o vetor não pode estar vazio")

    def __repr__(self):
        return f"Vector({self.components.tolist()})"

# como teste useu esse comando - python -c "import sys; sys.path.insert(0, 'src'); from Lab_vetores.vetores import Vector; v = Vector([3, 4, 5]); print(v); print(v.components.ndim); print(v.components.size)"
# nele a gente cria os valotres dos vetores e retorna o n. dim (quantas dimensões ele tem) e size (quantos elementos tem dentro desse array)
    
    # vamos calcular o versor modular do vetor criando essa função como "regra"
    
    def norma(self):
       return np.sqrt(np.sum(self.components ** 2)) # a ideia é elevar cada veror ao quadrado, somar eles e usar sqrt para calcular a raiz deles
    

# codigo base de teste - python -c "import sys; sys.path.insert(0, 'src'); from Lab_vetores.vetores import Vector; v = Vector([1, 2, 2]); print('Norma:', v.norma())"
    def versor(self):
        modulo = self.norma()

        if modulo == 0:
            raise ValueError("não é possivel calcular o versor de cada vetor sendo nulo")

        return self.components / modulo # formula base 

v = Vector([3, 4])

print("Norma:", v.norma())
print("Versor:", v.versor())
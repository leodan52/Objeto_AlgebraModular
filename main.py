# Descripcion

from TOOLS.ciclon import *

def main():
	r = (1,12)

	print("Definir un álgebra modular entre 1 y 12 ---álgebra de reloj---:\n")

	h = Modular(9)
	g = Modular(7)

	print(f'Con {g} y {h} objetos de esta álgebra\n')

	print(f'Suma:')
	print(f'{g} + {h} = {g + h}\n')
	print(f'Resta:')
	print(f'{g} - {h} = {g - h}')
	print(f'{h} - {g} = {h - g}')



def main2():

	r = (5,50)
	conm = 0
	e = []
	asocia = 0
	lista = list(range(r[0], r[1] + 1))
	nlen = len(lista)

	print("Conjunto =", lista)
	print("Tiene", len(lista), "elementos")



	for i in lista:
		i = Modular(i,r)
		for j in lista:
			j = Modular(j,r)
			for k in lista:
				k = Modular(k,r)

				if i+(k+j) == (i+j)+k:
					asocia +=1



	for i in lista:
		i = Modular(i,r)
		for j in lista:
			j = Modular(j,r)

			k = i + j
			k_ = j + i

			if k == k_:
				conm += 1
			else:
				continue

			if k == j and i not in e:
				e.append(i)

	if len(e) == 1:
		print("Entidad unica", e)
	else:
		print("Entidad no única", e)

	e_ = e[0]

	for i in lista:
		i = Modular(i,r)
		for j in lista:
			j = Modular(j,r)

			k = i + j
			k_ = j + i

			if k != k_:
				print("Falló")
				continue

			try:
				if k == e_:
					print(i, "+", j, "=", k)
			except IndexError:
				pass


	print(f'{nlen}*{nlen}*{nlen} =', asocia, f'{nlen}*{nlen} =', conm, e)




main()

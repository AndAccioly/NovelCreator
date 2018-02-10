import os
from src.GameObjetos import Sprite, Cena
	
erro_formatacao =  "Erro: expressao número {} incorreta. Use Dialogo, Background ou Atores."

class Processamento():
	def processa_dir_scripts():
		lista = []
		dir = 'scripts'
		for filename in os.listdir(dir):
			filename = "scripts/" + filename
			print(filename)
			lista = lista + [filename]
		return lista
		
	def processa_dir_sprites():
		tupla_lista = []
		dir = 'sprites'
		for filename in os.listdir(dir):
			filename = "sprites/" + filename
			sprite = Sprite(filename, [0,0])
			tupla_lista = tupla_lista + [(filename, sprite)]

		return tupla_lista

	def proxima_cena(lista_cenas, lista_sprites):
		lista_partes = []
		parte = ""
		contador_expressao = 1
		arq = lista_cenas[0]
		#print(arq)
		cenaArq = open(arq)
		with cenaArq as f:
			lista_linha = list(f)

		for linha in lista_linha:
			parte = parte + linha
			if "}" in parte:
				lista_partes.append(parte.replace("}\n","}"))
				parte = ""

		for parte in lista_partes:
			parte = parte.replace("{", "").replace("}", "")

			if "Titulo" in parte:
				print("TITULO:", parte)

			elif "Background" in parte:
				print("BG:", parte)

			elif "Atores" in parte:
				print("ATORES: ", parte)

			elif "Dialogo" in parte:
				print("DIALOGO: ", parte)

			else:
				print(erro_formatacao.format(contador_expressao))

			contador_expressao = contador_expressao + 1
		bg = ""
		atores = ""
		ordem_dialogos = ""
		cena = Cena(bg, atores, ordem_dialogos)
		return cena



	
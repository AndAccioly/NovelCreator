import os
from src.GameObjetos import Sprite, Cena
	
erro_formatacao =  "Erro: expressao número {} incorreta. Use Dialogo, Background ou Atores."
sprites = "sprites/"

class Processamento():
	def processa_dir_scripts():
		lista = []
		dir = 'scripts'
		for filename in os.listdir(dir):
			filename = "scripts/" + filename
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



	def proxima_cena(lista_cenas):
		lista_partes = []
		titulo = ""
		bg = []
		atores = []
		ordem_dialogos = []
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
				titulo = parte.replace("Titulo|", "").strip()

			elif "Background" in parte:
				bg = Processamento.processa_bg(parte)

			elif "Atores" in parte:
				atores = Processamento.processa_atores(parte)

			elif "Dialogo" in parte:
				print("DIALOGO: ", parte)
				ordem_dialogos =  ordem_dialogos + Processamento.processa_dialogos(parte)

			else:
				print(erro_formatacao.format(contador_expressao))

			contador_expressao = contador_expressao + 1

		cena = Cena(titulo, bg, atores, ordem_dialogos)
		#print(">>>>>", titulo)
		#print(">>>>>", bg)
		#print(">>>>>", atores)
		#print(">>>>>", ordem_dialogos)
		return cena



	def processa_bg(parte):
		bg = []
		bg_nome = ""
		bg_caminho = ""
		caminho_ou_nome = "nome"
		for c in parte.replace("Background|", ""):
			if "nome" in caminho_ou_nome:
				bg_nome = bg_nome + c
			else:
				bg_caminho = bg_caminho + c
			if c == '|':
				caminho_ou_nome = "caminho"
			elif c == ']':
				caminho_ou_nome = "nome"
				bg_nome = bg_nome.replace("[","").replace("|","").replace("]","")
				bg_caminho = bg_caminho.replace("[","").replace("|","").replace("]","")
				bg.append((bg_nome.strip(), sprites + bg_caminho.strip()))
				break

		return bg



	def processa_atores(parte):
		atores = []
		ator_nome = ""
		ator_caminho = ""
		caminho_ou_nome = "nome"
		for c in parte.replace("Atores|", ""):
			if "nome" in caminho_ou_nome:
				ator_nome = ator_nome + c
			else:
				ator_caminho = ator_caminho + c
			if c == '|':
				caminho_ou_nome = "caminho"
			elif c == ']':
				caminho_ou_nome = "nome"
				ator_nome = ator_nome.replace("[","").replace("|","").replace("]","")
				ator_caminho = ator_caminho.replace("[","").replace("|","").replace("]","")
				atores.append((ator_nome.strip(), sprites + ator_caminho.strip()))
				ator_nome = ""
				ator_caminho = ""

		return atores



	def processa_dialogos(parte):
		dialogos = []
		locutor = ""
		texto = ""
		texto_ou_nome = "nome"
		for c in parte.replace("Dialogo|", ""):
			if "nome" in texto_ou_nome:
				locutor = locutor + c
			else:
				texto = texto + c

			if c == '|':
				texto_ou_nome = "texto"
			elif c == ']':
				texto_ou_nome = "nome"
				locutor = locutor.replace("[","").replace("|","").replace("]","")
				texto = texto.replace("[","").replace("|","").replace("]","")
				dialogos.append((locutor.strip(), texto.strip()))
				locutor = ""
				texto = ""

		return dialogos
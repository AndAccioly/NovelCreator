import os
from src.GameObjetos import Sprite, Cena
	
erro_formatacao =  "Erro: expressao número {} incorreta. Use Dialogo, Background ou Atores."

class Processamento():
	#Faz a leitura de todos os arquivos da pasta script
	def processa_dir_scripts():
		lista = []
		dir = 'scripts'
		for filename in os.listdir(dir):
			filename = "scripts/" + filename
			print(filename)
			lista = lista + [filename]
		return lista
		
	#Faz a leitura de todas as sprites da pasta Sprites. A ideia seria associar o nome da Sprite ao caminho dela. Isso será usado mais pra frente
	def processa_dir_sprites():
		tupla_lista = []
		dir = 'sprites'
		for filename in os.listdir(dir):
			filename = "sprites/" + filename
			sprite = Sprite(filename, [0,0])
			tupla_lista = tupla_lista + [(filename, sprite)]

		return tupla_lista

	def proxima_cena(cena):
		bg = None
		atores = []
		lista_partes = []
		dialogos = []
		parte = ""
		contador_expressao = 1
		arq = cena
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
				conteudo = parte.replace("]", "").replace("[", "").split("|")
				bg =  Sprite(conteudo[2], [0,0])


			elif "Atores" in parte:
				print("ATORES: ", parte)
				conteudo = parte.replace("]", "").replace("[", "").split("|")
				tam = len(conteudo)
				for i in range (1, tam):
					if i%2 == 0:
						atores.append((conteudo[i-1], Sprite(conteudo[i], [75*i*i,300])))

			elif "Dialogo" in parte:
				print("DIALOGO: ", parte)
				conteudo = parte.replace("]", "").replace("[", "").split("|")
				print(conteudo)
				dialogos.append((conteudo[1], conteudo[2]))

			else:
				print(erro_formatacao.format(contador_expressao))

			contador_expressao = contador_expressao + 1

		cena = Cena(bg, atores, dialogos)
		return cena
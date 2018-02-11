import pygame
from src.Processamento import Processamento
from src.GameObjetos import Sprite, Cena
from src.GerenciadorInput import GerenciadorInput

pygame.init() #Lista de tuplas do tipo (String, Sprite)

game_objetos = []
	#Lista de cenas
	#tupla de nome com Sprite ou caminho de Sprite
script_teste = "scripts/primeira_parte.txt"
background_teste = "sprites/bg_teste2.jpg"

class GameLoop():
	def __init__(self, screen, bg_color = (255, 255, 255), bg = None, cenaAtual = None, trocaCena = False, lista_cenas = [], lista_sprites = []):
		self.screen = screen
		self.bg_color = bg_color
		self.clock = pygame.time.Clock()
		self.bg = bg
		self.cenaAtual = cenaAtual
		self.trocaCena = trocaCena
		self.gerenciadorInput = GerenciadorInput()
		self.lista_cenas = lista_cenas
		self.lista_sprites = lista_sprites

	def run(self):
		script = open(script_teste)
		self.lista_cenas = Processamento.processa_dir_scripts()
		self.lista_sprites = Processamento.processa_dir_sprites()

		print("Iniciando main loop")
		mainLoop = True
		while mainLoop:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			self.update()
			self.render()
			self.clock.tick(50)

	def render(self):
		#self.bg.render(self.screen)
		for objeto in game_objetos:
			objeto[1].render(self.screen)
		pygame.display.flip()

	def update(self):
		#troca a cena atual se tiver terminado a cena anterior OU se nao tiver nenhuma cena carregada
		if self.trocaCena == True or self.cenaAtual == None:
			self.cenaAtual = Processamento.proxima_cena(self.lista_cenas)
			self.trocaCena = False
			self.bg = Sprite(self.cenaAtual.getBg()[0][1], [0,0])
			self.screen.blit(self.bg.image, self.bg.rect)
			self.remover_item_lista_objetos("Background")
			self.adicionar_objeto("Background", self.bg)

		self.gerenciadorInput.update()

		for objeto in game_objetos:
			objeto[1].update()
		
	def adicionar_objeto(self, tipo, objeto):
		game_objetos.append((tipo, objeto))

	def remover_item_lista_objetos(self, tipo):
		for elem in game_objetos:
			if tipo in elem[0]:
				game_objetos.remove(elem)


		

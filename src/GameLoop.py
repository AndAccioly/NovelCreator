import pygame
from src.Processamento import Processamento
from src.GameObjetos import Sprite, Cena
from src.GerenciadorInput import GerenciadorInput

pygame.init()

game_objetos = []
	#Lista de cenas
	#tupla de nome com Sprite ou caminho de Sprite
script_teste = "scripts/primeira_parte.txt"

class GameLoop():
	def __init__(self, screen, bg_color = (255, 255, 255), bg = None, cenaAtual = Cena(None, None, None), trocaCena = True, lista_cenas = [], lista_sprites = []):
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
		if self.cenaAtual.getBg() != None:
			self.screen.blit(self.cenaAtual.getBg().image, self.cenaAtual.getBg().rect)
		if self.cenaAtual.getAtores() != None:
			for ator in self.cenaAtual.getAtores():
				ator.render(self.screen)

		pygame.display.flip()

	def update(self):
		if self.trocaCena == True or self.cenaAtual == None:
			self.cenaAtual = Processamento.proxima_cena(self.lista_cenas)
			self.trocaCena = False

		self.gerenciadorInput.update()
		for objeto in game_objetos:
			objeto.update()
		
	def adicionar_objeto(self, objeto):
		game_objetos.append(objeto)

		

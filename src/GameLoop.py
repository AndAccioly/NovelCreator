import pygame
from src.Processamento import Processamento
from src.GameObjetos import Sprite, Cena
from src.GerenciadorInput import GerenciadorInput

pygame.init()
pygame.font.init()
fonte = pygame.font.SysFont('Comic Sans MS', 30)

script_teste = "scripts/primeira_parte.txt"

class GameLoop():
	def __init__(self, screen, bg_color = (255, 255, 255), bg = None, cenaAtual = Cena(None, None, None), trocaCena = True, lista_cenas = [], lista_sprites = [], dialogoAtual = None, texto = None, locutor = None, telaAltura = None, 
		telaLargura = None, fimDoDialogo = False):
		self.screen = screen
		self.bg_color = bg_color
		self.clock = pygame.time.Clock()
		self.bg = bg
		self.cenaAtual = cenaAtual
		self.trocaCena = trocaCena
		self.gerenciadorInput = GerenciadorInput()
		self.lista_cenas = lista_cenas
		self.lista_sprites = lista_sprites
		self.dialogoAtual = dialogoAtual
		self.texto = texto
		self.locutor = locutor
		self.fimDoDialogo = fimDoDialogo

	#loop principal do main game
	def run(self, telaLargura, telaAltura):
		self.telaAltura = telaAltura
		self.telaLargura = telaLargura
		script = open(script_teste)
		self.lista_cenas = Processamento.processa_dir_scripts()
		self.lista_sprites = Processamento.processa_dir_sprites()

		print("Iniciando main loop")
		
		mainLoop = True
		while mainLoop:
			self.update()	
			self.render()
			self.clock.tick(50)

	def render(self):
		#renderiza background
		if self.cenaAtual.getBg() != None:
			self.screen.blit(self.cenaAtual.getBg().image, self.cenaAtual.getBg().rect)

		#renderiza os atores. Aquele que esta como locutor é redimensionado para um tamanho maior
		if self.cenaAtual.getAtores() != None:
			for ator in self.cenaAtual.getAtores():
				if self.dialogoAtual != None:
					if self.locutor != None and ator[0] == self.dialogoAtual[0]:
						ator[1].scale(1.1)
					else:
						ator[1].arrumar()

				ator[1].render(self.screen)

		#renderiza texto
		if self.locutor != None and self.texto != None:
			self.screen.blit(self.locutor, (self.telaLargura*0.1, self.telaAltura*0.8))
			self.screen.blit(self.texto, (self.telaLargura*0.1, self.telaAltura*0.85))

		pygame.display.flip()


	def update(self):
		#faz a troca de cena caso a cena tenha sido encerrada
		if self.trocaCena == True or self.cenaAtual == None:
			if len(self.lista_cenas) > 0:
				self.cenaAtual = Processamento.proxima_cena(self.lista_cenas[0])
				del self.lista_cenas[0]
				self.trocaCena = False

		self.gerenciadorInput.update()

		#faz a atualizacao do jogo seguindo cada tecla
		if self.gerenciadorInput.getFoiPressionado() == "ESPACO":
			if self.fimDoDialogo == True and len(self.lista_cenas) == 0:
				pygame.quit()
				quit()
		
			if self.cenaAtual.getDialogos() != None:
				self.dialogoAtual = self.cenaAtual.getDialogoAtual()
				if self.dialogoAtual != None:
					print(self.dialogoAtual)
					self.locutor = fonte.render(self.dialogoAtual[0], False, (0, 0, 0))
					self.texto = fonte.render(self.dialogoAtual[1], False, (0, 0, 0))
				else:
					self.locutor = fonte.render("", False, (0, 0, 0))
					self.texto = fonte.render("", False, (0, 0, 0))
					self.fimDoDialogo = True



	
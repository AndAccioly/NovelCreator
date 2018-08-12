import pygame

PRESSIONADO = "PRESSIONADO"
ESPACO = "ESPACO"

class GerenciadorInput():
	def __init__(self, pressionado = None):
		self.pressionado = None
		
	
	def getFoiPressionado(self):
		pressionado = self.pressionado
		self.pressionado = None
		return pressionado

	#
	def update(self):
		for evento in pygame.event.get():
			if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
				self.pressionado = ESPACO
			if evento.type == pygame.QUIT:
				pygame.quit()
				quit()
		
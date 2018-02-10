import pygame

pygame.init()

class Cena():
	#background
	#dialogo associado a sprite = tupla
	def __init__(self, bg, atores, ordem_dialogos):
		self.bg = bg
		self.atores = atores
		self.ordem_dialogos = ordem_dialogos
	def a():
		print("a")
	

class Sprite():
	#sprites
	def __init__(self, arquivo_imagem, coordenada):
		pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
		self.image = pygame.image.load(arquivo_imagem)
		self.rect = self.image.get_rect()
		self.posX, self.posY = coordenada

	def setPos(self, coordenada):
		self.posX, self.posY = coordenada

	def getPos(self):
		return self.posX, self.posY

	def update(self):
		self.rect.x, self.rect.y = self.posX, self.posY

	def render(self, screen):
		screen.blit(self.image, self.rect)
import pygame

pygame.init()

class Cena():
	#background
	#dialogo associado a sprite = tupla
	def __init__(self, bg = None, atores = None, ordem_dialogos = None):
		self.bg = bg
		self.atores = atores
		self.ordem_dialogos = ordem_dialogos
	def getBg(self):
		return self.bg
	def getAtores(self):
		return self.atores
	

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
		screen.blit(self.image, [self.posX, self.posY])

class Texto():
	def __init__(self, texto = "Falta texto"):
		self.texto = texto

	def getTexto(self):
		return self.texto

	def setTexto(self, texto):
		self.texto = texto
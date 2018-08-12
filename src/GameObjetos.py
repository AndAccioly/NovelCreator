import pygame

pygame.init()

class Cena():
	#background
	#dialogo associado a sprite = tupla
	def __init__(self, bg = None, atores = None, dialogos = None):
		self.bg = bg
		self.atores = atores
		self.dialogos = dialogos
	def getBg(self):
		return self.bg

	def getAtores(self):
		return self.atores

	def getDialogos(self):
		return self.dialogos

	def getDialogoAtual(self):
		dialogo = None
		if len(self.dialogos) > 0:
			dialogo = self.dialogos.pop(0)
		return dialogo

	def aindaTemDialogo(self):
		if len(self.dialogos) > 0:
			return True
		return False
	

class Sprite():
	#sprites
	def __init__(self, arquivo_imagem, coordenada):
		pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
		self.image = pygame.image.load(arquivo_imagem)
		self.rect = self.image.get_rect()
		self.posX, self.posY = coordenada
		self.dimOriginal = self.image.get_size()

	def setPos(self, coordenada):
		self.posX, self.posY = coordenada

	def getPos(self):
		return self.posX, self.posY

	def update(self):
		self.rect.x, self.rect.y = self.posX, self.posY

	def render(self, screen):
		screen.blit(self.image, [self.posX, self.posY])

	def arrumar(self):
		dimensoes = self.image.get_size()
		if(dimensoes[0] != self.dimOriginal[0] and dimensoes[1] != self.dimOriginal[1]):
			self.image = pygame.transform.scale(self.image, self.dimOriginal)	

	def scale(self, escala):
		dimensoes = self.image.get_size()
		if(dimensoes[0] == self.dimOriginal[0] and dimensoes[1] == self.dimOriginal[1]):
			self.image = pygame.transform.scale(self.image, (int(dimensoes[0]*escala), int(dimensoes[1]*escala)))	

#Nao usado
class Texto():
	def __init__(self, texto = "Falta texto"):
		self.texto = texto

	def getTexto(self):
		return self.texto

	def setTexto(self, texto):
		self.texto = texto
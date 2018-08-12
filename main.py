import sys
import pygame
from src.GameLoop import GameLoop

telaLargura = 1920
telaAltura = 1080

def main():
	pygame.display.init()
	gameDisplay = pygame.display.set_mode((telaLargura, telaAltura), 0, 0)
	pygame.display.set_caption('Novel Creator')

	gl = GameLoop(gameDisplay)
	gl.run(telaLargura, telaAltura)
	
if __name__=="__main__":
	main()
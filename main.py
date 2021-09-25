import pygame
import sys
from random import choice
import time

alphabet = 'abcdefghijklmnopqrstuvwxyz '

words = []

with open('words.txt','r') as f:
	for word in f.readlines():
		words += [word[:-1]]

pygame.init()

DIS = [800,600]
cx,cy = DIS[0]//2,DIS[1]//2
root = pygame.display.set_mode(DIS)

TITLEFONT = pygame.font.Font('open-sans/OpenSans-Bold.ttf',48)
TEXTFONT = pygame.font.Font('open-sans/OpenSans-Regular.ttf',32)

FPS = 60

def main():

	running = True

	clock = pygame.time.Clock()

	text = ''
	target = choice(words)
	score = 0

	title = TITLEFONT.render('Typing Test',True,(0,0,0))
	title.set_colorkey((0,0,0,0))
	titlePos = title.get_rect()
	titlePos.center = (cx,cy-200)
	textBox = pygame.Rect((0,0),(400,48))
	textBox.center = (cx,cy)
	wpmSurf = pygame.Surface((0,0))

	ending = False

	start = None

	t = 0
	wpm = 0

	while running:

		if start:
			t = round((time.time()-start)/60,2)
			wpm = round(score/((time.time()-start+0.0001)/60),2)

		keys = pygame.key.get_pressed()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False

				if pygame.key.name(event.key) in alphabet:
					if not start:
						start = time.time()
					if not ending:
						if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
							text += pygame.key.name(event.key).upper()
						else:
							text += pygame.key.name(event.key)

				if event.key == pygame.K_BACKSPACE:
					text = text[:-1]

		if text == target:
			target = choice(words)
			score += 1
			text = ''

		if score == 30:
			ending = True

		textSurf = TEXTFONT.render(text,True,(0,0,0))
		targetSurf = TEXTFONT.render(target,True,(0,0,0))
		scoreSurf = TEXTFONT.render(str(score),True,(0,0,0))
		scoreRect = scoreSurf.get_rect()
		scoreRect.topright = (textBox.topright[0],textBox.topright[1]-40)
		if not ending:
			wpmSurf = TEXTFONT.render(str(t)+'    wpm:'+str(wpm),True,(0,0,0))
		wpmRect = wpmSurf.get_rect()
		wpmRect.topleft = (textBox.bottomleft[0],textBox.bottomleft[1])

		root.fill((255,255,255))
		root.blit(title,titlePos)
		pygame.draw.rect(root,(0,0,0),textBox,5)
		root.blit(textSurf,(textBox.topleft[0]+10,textBox.topleft[1]))
		root.blit(targetSurf,(textBox.topleft[0]+10,textBox.topleft[1]-40))
		root.blit(scoreSurf,scoreRect)
		root.blit(wpmSurf,wpmRect)

		clock.tick(FPS)
		pygame.display.flip()

	return


if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		pygame.quit()
		raise e

	pygame.quit()
	sys.exit()


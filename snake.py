import pygame, random, os
from pygame.math import Vector2 


pygame.init()

#tamaño de la ventana
ANCHO = 720
ALTO = 480

#imagen de la manzana  
manzanaD = pygame.transform.scale(pygame.image.load(os.path.join(r"man.png")),(20,20))
pantalla = pygame.display.set_mode((ANCHO,ALTO))


#tamaño de la letra 
texto_vida = pygame.font.SysFont("Russo One ",20)
texto_puntaje = pygame.font.SysFont("Russo One",20)


#Esto es una prueba apara el repositorio

#clase de la Snake
class Snake:

    #constructor
	def __init__(self):
		self.body = [Vector2(20,100),Vector2(20,110),Vector2(20,120)]
		self.direction = Vector2(0,-20)
		self.add = False

    #dibujo de la Snake
	def dibujo(self):
		for bloque in self.body:
			pygame.draw.rect(pantalla,(0,0,255),(bloque.x,bloque.y,10,10))

		

	def mover(self):
		
		#[0,1,2] --> [0,1] --> [None,0,1] --> [-1,0,1]
        #crece la Snake o incrementa el tamaño
		if self.add == True:
			body_copy = self.body
			body_copy.insert(0,body_copy[0]+self.direction)
			self.body = body_copy[:]
			self.add = False
		else:
			body_copy = self.body[:-1]
			body_copy.insert(0,body_copy[0]+self.direction)
			self.body = body_copy[:]

    #funciones de mover a la Snake
	def mover_arriba(self):
		self.direction = Vector2(0,-20)

	def mover_abajo(self):
		self.direction = Vector2(0,20)

	def mover_derecha(self):
		self.direction = Vector2(20,0)

	def mover_izquierda(self):
		self.direction = Vector2(-20,0)

    #funcione colisión de la snake con los bordes
	def colision(self):
		if self.body[0].x >= ANCHO+10 or self.body[0].y >= ALTO+10 or self.body[0].x <= -10 or self.body[0].y <= -10:
			return True

		#colisión  si se toca asi misma
		for i in self.body[1:]:
			if self.body[0] == i:
				return True
    

#clase de la manzana
class Manzana:
	def __init__(self):
		self.generate()

    #funcion de la manzana
	def dibujarM(self):
		pantalla.blit(manzanaD,(self.pos.x,self.pos.y))

    #donde se genera aleatoriamente en la pantalla
	def generate(self):
		self.x = random.randrange(0,ANCHO/20)
		self.y = random.randrange(0,ALTO/20)
		self.pos = Vector2(self.x*20,self.y*20)

    #funcion donde conecta la Snake con la manzana
	def come_comida(self,snake):

		if snake.body[0] == self.pos:
			self.generate()
			snake.add = True

			return True

        #choca con una manzana se genera otra
		for bloque in snake.body[1:]:
			if self.pos == bloque:
				self.generate()

		return False


#funcion de ejecución
def main():

    #llama a las clase
	snake = Snake()
	manzana = Manzana()
	puntos = 0
	vida=3

    #velocidad de la vivorita
	fps = pygame.time.Clock()

	while True:
        #veleidad
		fps.tick(5)

		for event in pygame.event.get():

            #funcion de la ventana de salir
			if event.type == pygame.QUIT:
				quit()
            
            #funcion de los teclado 

			if event.type == pygame.KEYDOWN and snake.direction.y != 20:
				if event.key == pygame.K_UP:
					snake.mover_arriba()

			if event.type == pygame.KEYDOWN and snake.direction.y != -20:
				if event.key == pygame.K_DOWN:
					snake.mover_abajo()


			if event.type == pygame.KEYDOWN and snake.direction.x != -20:
				if event.key == pygame.K_RIGHT:
					snake.mover_derecha()

			if event.type == pygame.KEYDOWN and snake.direction.x != 20:
				if event.key == pygame.K_LEFT:
					snake.mover_izquierda()



		#fondo de pantalla			
		pantalla.fill((175,215,70))
        #llama a las funciones
		snake.dibujo()
		manzana.dibujarM()

		snake.mover()

        #donde se incrementa la vivorita al comer una manzana
		if manzana.come_comida(snake):
			puntos+=1
			
        #donde se ejecuta colisión
		snake.colision()
		if snake.colision():
			vida -=1

        #muestra la posición del puntaje en la pantalla

		texto_v= texto_vida.render("vida : "+ str (vida),True, (255,255, 255))

		pantalla.blit(texto_v,(10,10))
		
		text = texto_puntaje.render("puntuación: {}".format(puntos),1,(255,255,255))
		pantalla.blit(text,(ANCHO-text.get_width()-20,20))

		pygame.display.update()

main()
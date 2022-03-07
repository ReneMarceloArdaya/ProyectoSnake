
import pygame, sys, random
from pygame.math import Vector2

#clase serpiente
class SNAKE:
    def __init__(self):
        self.nuevo_bloque = False
        
        #constructor de la serpiente inicial
        self.cuerpo = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        #dirección inicial
        self.direccion = Vector2(1,0) # (x , y) 
        
       
        #cuerpo de la serpiente
        #cabeza
        self.cabeza_arriba = pygame.transform.scale(pygame.image.load('asset/Snake_body/cabeza_arriba.png').convert_alpha(),(celda_size,celda_size))
        self.cabeza_derecha = pygame.transform.scale(pygame.image.load('asset/Snake_body/cabeza_derecha.png').convert_alpha(),(celda_size,celda_size))
        self.cabeza_izquierda = pygame.transform.scale(pygame.image.load('asset/Snake_body/cabeza_izquierda.png').convert_alpha(),(celda_size,celda_size))
        self.cabeza_abajo = pygame.transform.scale(pygame.image.load('asset/Snake_body/cabeza_abajo.png').convert_alpha(),(celda_size,celda_size))
        #cola
        self.cola_arriba = pygame.transform.scale(pygame.image.load('asset/Snake_body/cola_arriba.png').convert_alpha(),(celda_size,celda_size))
        self.cola_derecha = pygame.transform.scale(pygame.image.load('asset/Snake_body/cola_derecha.png').convert_alpha(),(celda_size,celda_size))
        self.cola_izquierda = pygame.transform.scale(pygame.image.load('asset/Snake_body/cola_izquierda.png').convert_alpha(),(celda_size,celda_size))
        self.cola_abajo = pygame.transform.scale(pygame.image.load('asset/Snake_body/cola_abajo.png').convert_alpha(),(celda_size,celda_size))
        #cuerpo
        self.cuerpo_vertical = pygame.transform.scale(pygame.image.load('asset/Snake_body/arriba_abajo.png').convert_alpha(),(celda_size,celda_size))
        self.cuerpo_horizontal = pygame.transform.scale(pygame.image.load('asset/Snake_body/izquierda_derecha.png').convert_alpha(),(celda_size,celda_size))
        #cuerpo movimiento
        self.cuerpo_Dup = pygame.transform.scale(pygame.image.load('asset/Snake_body/derecha_arriba.png').convert_alpha(),(celda_size,celda_size))
        self.cuerpo_Ddown = pygame.transform.scale(pygame.image.load('asset/Snake_body/derecha_abajo.png').convert_alpha(),(celda_size,celda_size))
        self.cuerpo_Iup = pygame.transform.scale(pygame.image.load('asset/Snake_body/izquierda_arriba.png').convert_alpha(),(celda_size,celda_size))
        self.cuerpo_Idown = pygame.transform.scale(pygame.image.load('asset/Snake_body/izquierda_abajo.png').convert_alpha(),(celda_size,celda_size))
        #sonido de la serpiente comiendo
        self.crunch_sound = pygame.mixer.Sound('songs/Crunch.wav')


    def dibuja_snake(self):
        self.update_cabeza()
        self.update_cola()
        
        for indice,bloque in enumerate(self.cuerpo):
            
            #crear rectángulo para posicionamiento
            x_pos = bloque.x * celda_size
            y_pos = bloque.y * celda_size
            block_rect = pygame.Rect(x_pos,y_pos,celda_size,celda_size)
            
            #dibujar dirección de la serpiente para la animacion
            if indice == 0: # cabeza de la serpiente
                ventana.blit(self.cabeza,block_rect)
            elif indice == len(self.cuerpo) - 1: # cola de la serpiente
                ventana.blit(self.cola,block_rect)
            else:
                previous_block = self.cuerpo[indice + 1] - bloque            
                next_block = self.cuerpo[indice - 1] - bloque               
                if previous_block.x == next_block.x:                        
                    ventana.blit(self.cuerpo_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    ventana.blit(self.cuerpo_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        ventana.blit(self.cuerpo_Iup,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        ventana.blit(self.cuerpo_Idown,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        ventana.blit(self.cuerpo_Dup,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        ventana.blit(self.cuerpo_Ddown,block_rect)
    
    def update_cabeza(self):
        cabeza_relacion = self.cuerpo[1] - self.cuerpo[0] #orientación cabeza de la serpiente
        if cabeza_relacion == Vector2(1,0): self.cabeza = self.cabeza_izquierda
        elif cabeza_relacion == Vector2(-1,0): self.cabeza = self.cabeza_derecha
        elif cabeza_relacion == Vector2(0,1): self.cabeza = self.cabeza_arriba
        elif cabeza_relacion == Vector2(0,-1): self.cabeza = self.cabeza_abajo

    def update_cola(self):
        cola_relacion = self.cuerpo[-2] - self.cuerpo[-1] #orientación cola de la serpiente
        if cola_relacion == Vector2(1,0): self.cola = self.cola_izquierda
        elif cola_relacion == Vector2(-1,0): self.cola = self.cola_derecha
        elif cola_relacion == Vector2(0,1): self.cola = self.cola_arriba
        elif cola_relacion == Vector2(0,-1): self.cola = self.cola_abajo



    # mover serpiente y crear nuevo bloque de cuerpo
    def mover_snake(self):
        if self.nuevo_bloque == True:
            cuerpo_copia = self.cuerpo[:]
            cuerpo_copia.insert(0,cuerpo_copia[0] + self.direccion)
            self.cuerpo = cuerpo_copia[:]
            self.nuevo_bloque = False
        else:
            cuerpo_copia = self.cuerpo[:-1]
            cuerpo_copia.insert(0,cuerpo_copia[0] + self.direccion)
            self.cuerpo = cuerpo_copia[:]

    def añadir_bloque(self):
        self.nuevo_bloque = True

    def reproducir_comiendo(self):
        self.crunch_sound.play()
#clase fruta
class FRUTA:
    def __init__(self):
        self.frutarandom()
        self.manzana = pygame.transform.scale(pygame.image.load('asset/manzana.png').convert_alpha(),(celda_size,celda_size))
    
    def dibujar_fruta(self):
        #crear rectángulo
        fruit_rect = pygame.Rect(self.pos.x * celda_size , self.pos.y * celda_size, celda_size ,celda_size)
        #dibujar manzana
        ventana.blit(self.manzana,fruit_rect)

    #mueve la fruta a una posición ramdon, menos en la celda donde esta el final de la ventana
    def frutarandom(self):
        self.x = random.randint(3,celda_numero - 3)
        self.y = random.randint(3,celda_numero - 3)
        self.pos = Vector2(self.x,self.y)

# parte lógica del juego
class MAIN:
    
    def __init__(self):
        self.snake = SNAKE()
        self.fruta = FRUTA()
        self.vida = vidas
        self.score = 0  
        self.fin_juego = False      

    #actualizar acciones del juego
    def update(self):
        self.snake.mover_snake()
        self.check_colisión()
        self.check_fail() #condición de perdida

    #dibujar elementos
    def dibujar_elementos(self):
        self.dibujar_hierba()
        self.fruta.dibujar_fruta()
        self.snake.dibuja_snake()
        self.dibujar_score()
        self.dibujar_vida()
        if self.fin_juego == True:
            self.dibujar_FinDelJuego()
     
        
    #colisión
    def check_colisión(self):
        
        # colicion de la cabeza con la fruta
        if self.fruta.pos == self.snake.cuerpo[0]:
            #si la fruta colisiona(aparece) en el cuerpo e cola y no en la cabeza de la serpiente que la mueva la fruta otra parte 
            for block in self.snake.cuerpo[1:]:
                if block == self.fruta.pos:
                     self.fruta.frutarandom()
            
            self.score += 10
            #reposición de la fruta
            self.fruta.frutarandom()
            #crecimiento de la serpiente
            self.snake.añadir_bloque()
            #sonido de serpiente comiendo
            self.snake.reproducir_comiendo()
         
                 
    #condiciones de perdida
    def check_fail(self):
        #serpiente choca ventana
        if not 0 <= self.snake.cuerpo[0].x < celda_numero or not 0 <= self.snake.cuerpo[0].y < celda_numero:
            self.intentos()
        #serpiente choca en si misma
        for block in self.snake.cuerpo[1:]:
            if block == self.snake.cuerpo[0]:
                self.intentos()
    
    #vidas
    def intentos(self):
        if self.vida < 1:
            self.fin_juego = True #activa el fin del juego
        else:
            self.vida -= 1
            self.snake = SNAKE() #reinicia la serpiente
            self.fruta = FRUTA() #reinicia la fruta

    #fin del juego 
    def dibujar_FinDelJuego(self):
        game_font = pygame.font.Font('font/animeace2_bld.ttf',40)
        pygame.time.set_timer(VENTANA_UPDATE , 130) #Pausa el juego
        fin = game_font.render("Fin del juego",False,(56,74,12))     #True o False pixeleado de letra
        reinicio = game_font.render("Para reiniciar presione ",False,(56,74,12))
        reintentar = game_font.render("la letra [R]",False,(56,74,12))
        #centro de la pantalla (x) y (y)
        centro_x = (celda_size * celda_numero // 2)
        centro_y = (celda_size * celda_numero // 2) 
        #definir posion de cada mensaje a imprimir
        fin_position = fin.get_rect(center = (centro_x , centro_y - 200))
        reinicio_position = reinicio.get_rect(center = (centro_x , centro_y - 100))
        reintentar_position = reintentar.get_rect(center = (centro_x , centro_y))
        #dibuja en la ventana 
        ventana.blit(fin,fin_position)
        ventana.blit(reinicio,reinicio_position)
        ventana.blit(reintentar,reintentar_position)

    #añadir hierba 
    def dibujar_hierba(self):
        color_hierba = (167,209,61) #verde claro un poco mas oscuro
        for row in range(celda_numero): 
             if row % 2 == 0: #filas pares
                 for col in range(celda_numero):
                     if col % 2 == 0: #columnas pares
                         hierba_rect = pygame.Rect(col * celda_size,row * celda_size, celda_size, celda_size) 
                         pygame.draw.rect(ventana,color_hierba,hierba_rect) 
             else:
                 for col in range(celda_numero):
                     if col % 2 != 0:
                         hierba_rect = pygame.Rect(col * celda_size,row * celda_size, celda_size, celda_size)
                         pygame.draw.rect(ventana,color_hierba,hierba_rect)

    #dibujar puntos ganados
    def dibujar_score(self):
        score_font = pygame.font.Font('font/barcadbold.ttf',38) #fuente de letra para el score
        score_surface = score_font.render("(Total de Puntos: " + str(self.score) +")",False,(56,74,12))  #True o False pixeleado de letra
        score_x = (celda_size * celda_numero - 680) 
        score_y = (celda_size * celda_numero - 870)
        score_Posición = score_surface.get_rect(center = (score_x , score_y)) #definimos la position del texto
        ventana.blit(score_surface, score_Posición) #dibujamos el texto en pantalla
    
    def dibujar_vida(self):
        corazón_vivo = pygame.transform.scale(pygame.image.load('asset/corazon vivo.png').convert_alpha(),(40,40)) #importamos la imagen en una variable
        corazón_muerto = pygame.transform.scale(pygame.image.load('asset/corazon muerto.png').convert_alpha(),(40,40))
        vida_x = (celda_size * celda_numero - 30) 
        vida_y = (celda_size * celda_numero - 870)
        if self.vida == 3:
            #ajustamos la posición de cada corazón
            vida_posición1 = corazón_vivo.get_rect(center = (vida_x,vida_y)) 
            vida_posición2 = corazón_vivo.get_rect(center = (vida_x - 50,vida_y))
            vida_posición3 = corazón_vivo.get_rect(center = (vida_x - 100,vida_y))
            #dibujamos en pantalla los corazones
            ventana.blit(corazón_vivo,vida_posición1)
            ventana.blit(corazón_vivo,vida_posición2)
            ventana.blit(corazón_vivo,vida_posición3)
        elif self.vida == 2:
            vida_posición1 = corazón_vivo.get_rect(center = (vida_x,vida_y))
            vida_posición2 = corazón_vivo.get_rect(center = (vida_x - 50,vida_y))
            vida_posición3 = corazón_muerto.get_rect(center = (vida_x - 100,vida_y))
            ventana.blit(corazón_vivo,vida_posición1)
            ventana.blit(corazón_vivo,vida_posición2)
            ventana.blit(corazón_muerto,vida_posición3)
        elif self.vida == 1:
            vida_posición1 = corazón_vivo.get_rect(center = (vida_x,vida_y))
            vida_posición2 = corazón_muerto.get_rect(center = (vida_x - 50,vida_y))
            vida_posición3 = corazón_muerto.get_rect(center = (vida_x - 100,vida_y))
            ventana.blit(corazón_vivo,vida_posición1)
            ventana.blit(corazón_muerto,vida_posición2)
            ventana.blit(corazón_muerto,vida_posición3)
        elif self.vida == 0:
            vida_posición1 = corazón_muerto.get_rect(center = (vida_x,vida_y))
            vida_posición2 = corazón_muerto.get_rect(center = (vida_x - 50,vida_y))
            vida_posición3 = corazón_muerto.get_rect(center = (vida_x - 100,vida_y))
            ventana.blit(corazón_muerto,vida_posición1)
            ventana.blit(corazón_muerto,vida_posición2)
            ventana.blit(corazón_muerto,vida_posición3)

# parecido al RGB 
#          frecuencia , tamaño , canales , bufe 
pygame.mixer.pre_init(44100,-16,2,512) #sincronizar sonidos del juego
pygame.init()

vidas = 3 # 3 vidas
celda_size = 30 #tamaño de cada celda
celda_numero = 30 # cantidad de cedas n x n total = 900 celdas -30 pixel cada una, total 900 X 900 pixeles 
ventana = pygame.display.set_mode((celda_numero * celda_size , celda_numero * celda_size)) #crear la ventana del juego en pixeles
reloj = pygame.time.Clock() #definir reloj para los fps
main_game = MAIN() #definir variable que llame a todo la parte lógica del juego

musica =  pygame.mixer.music.load('songs/Musica.wav') #cargamos la música
pygame.mixer.music.play(-1) #reproducimos la música en bucle

#definir variable de stop de frame para las teclas
move_tik = 0

VENTANA_UPDATE = pygame.USEREVENT #creamos una variable que sera un temporizador de eventos
pygame.time.set_timer(VENTANA_UPDATE , 130) #velocidad de de la serpiente - menor sea el numero mas rápido sera la serpiente

#eventos y prosesos que se ejecutan 
while True:
    for evento in pygame.event.get():
        # cerrar el juego
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()     #borrar rastros en el sistema
        #activar velocidad de la serpiente 
        if evento.type == VENTANA_UPDATE:
            main_game.update()
            
        
        #Definir las teclas de movimiento
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w or evento.key == pygame.K_UP: # arriba
                if move_tik == 0:
                    move_tik = 8
                    if main_game.snake.direccion.y != 1:
                        main_game.snake.direccion = Vector2(0,-1)
                
            if evento.key == pygame.K_s or evento.key == pygame.K_DOWN: # abajo
                if move_tik == 0:
                    move_tik = 8
                    if main_game.snake.direccion.y != -1:
                        main_game.snake.direccion = Vector2(0,1)
                  
            if evento.key == pygame.K_d or evento.key == pygame.K_RIGHT: # derecha
                if move_tik == 0:
                    move_tik = 8
                    if main_game.snake.direccion.x != -1:
                        main_game.snake.direccion = Vector2(1,0)
             
            if evento.key == pygame.K_a or evento.key == pygame.K_LEFT: # izquierda
                if move_tik == 0:
                    move_tik = 8
                    if main_game.snake.direccion.x != 1:
                        main_game.snake.direccion = Vector2(-1,0)
                    
            #tecla de reinicio
            if evento.key == pygame.K_r:
                main_game.__init__()
    
    if move_tik > 0:
        move_tik -= 1
           
    ventana.fill((172,215,70)) #color verde claro
    main_game.dibujar_elementos()   #muestras todos los elemento que se mostraran en la pantalla                                            
    pygame.display.update()  #actualisa el juego
    reloj.tick(60) # 60 fps(frame) por segundos 

    
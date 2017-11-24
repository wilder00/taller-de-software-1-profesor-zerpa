import pygame, sys
from pygame import*
import random

#datos extra para la pantalla y mas
cantidadEnemigos    = 2 #indica la cantidad por cada tipo de enemigo
imagenBala          = 'Recursos/bala.png'
background_image    = 'Recursos/fondo.jpg'
song                = 'Recursos/song.mp3'
BLACK               = (0, 0, 0)
WHITE               = (255,255,255)
BLUE                = (0,0,255)
FPS                 = 120
#Constantes
alto                = 680
ancho               = 1100

x, y        = 150, 353
MOVE_RIGHT  = 1
MOVE_LEFT   = 2
MOVE_UP     = 1
MOVE_DOWN   = 2
directionx  = 0
directiony  = 0
#Recursos en file

imagenOpciones  = 'Recursos/Menu.png'
imagenIniciar   = 'Recursos/Menu_iniciar.png'
imagenAyuda     = 'Recursos/Menu_ayuda.png'
imagenCredito   = 'Recursos/Menu_creditos.png'
imagenSalir     = 'Recursos/Menu_salir.png'
fondo           = 'Recursos/fondo.jpg'
imagenSalir_o_no= 'Recursos/salir_o_no.png'
imagenFin       =  'Recursos/game_over.png'
imagen_ayuda    =  'Recursos/ayuda.png'
imagen_creditos =  'Recursos/creditos.png'


ruta_nave0           = "Recursos/nave0.png"
ruta_nave1           = "Recursos/nave1.png"
ruta_nave2           = "Recursos/nave2.png"
ruta_nave3           = "Recursos/nave3.png"
ruta_nave4           = "Recursos/nave4.png"
ruta_nave5           = "Recursos/nave5.png"
#creando Surface
nave0           =  pygame.image.load(ruta_nave0)
nave1           =  pygame.image.load(ruta_nave1)
nave2           =  pygame.image.load(ruta_nave2)
nave3           =  pygame.image.load(ruta_nave3)
nave4           =  pygame.image.load(ruta_nave4)
nave5           =  pygame.image.load(ruta_nave5)
vidas           =  pygame.image.load(ruta_nave0)
opciones        =  pygame.image.load(imagenOpciones)
opcionIniciar   =  pygame.image.load(imagenIniciar)
opcionAyuda     =  pygame.image.load(imagenAyuda)
opcionCredito   =  pygame.image.load(imagenCredito)
opcionSalir     =  pygame.image.load(imagenSalir)
salir_o_no      =  pygame.image.load(imagenSalir_o_no)
fondoMenu       =  pygame.image.load(fondo)
bala            =  pygame.image.load(imagenBala)
background      =  pygame.image.load(background_image)#.convert()
game_over       =  pygame.image.load(imagenFin)
vistaAyuda      =  pygame.image.load(imagen_ayuda)
vistaCreditos        =  pygame.image.load(imagen_creditos)
#transformando las imagenes a tamanio de pantalla
vidas           =   pygame.transform.rotozoom(nave0, 125, 0.10)
opciones        =   pygame.transform.scale(opciones,(ancho,alto))
opcionIniciar   =   pygame.transform.scale(opcionIniciar,(ancho,alto))
opcionAyuda     =   pygame.transform.scale(opcionAyuda,(ancho,alto))
opcionCredito   =   pygame.transform.scale(opcionCredito,(ancho,alto))
opcionSalir     =   pygame.transform.scale(opcionSalir,(ancho,alto))
fondoMenu       =   pygame.transform.scale(fondoMenu,(ancho,alto))
background      =   pygame.transform.scale(background,(ancho,alto))
salir_o_no      =   pygame.transform.scale(salir_o_no,(ancho,alto))
game_over       =  pygame.transform.scale(game_over,(ancho,alto))
vistaAyuda           =  pygame.transform.scale(vistaAyuda,(ancho,alto))
vistaCreditos        =  pygame.transform.scale(vistaCreditos ,(ancho,alto))
# variable (algunos globales) que permiten la logica del juego
modoMenu    = True
cerrar      = False
iniciar     = False
ayuda       = False
credito     = False
######Clases#####
#Nave
class Player(pygame.sprite.Sprite):
    #Sprite del jugador
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Falta escalar
        #self.image = pygame.image.load(nave0).convert_alpha()
        self.image          =  pygame.transform.rotozoom(nave0, 125, 0.30)
        self.rect           = self.image.get_rect()
        self.radius         = 35
        self.lives          = 6
        self.rect.center    = (ancho/2,(10*alto)/11)
        self.speedx         = 0
        self.speedy         = 0
    def update(self):
        #Movimientos
        self.speedx         = 0
        self.speedy         = 0
        estadoteclas        = pygame.key.get_pressed()
        #Mejorar velocidad
        if estadoteclas[pygame.K_LEFT]:
            self.speedx     = -15
        if estadoteclas[pygame.K_RIGHT]:
            self.speedx     = 15
        if estadoteclas[pygame.K_UP]:
            self.speedy     = -15
        if estadoteclas[pygame.K_DOWN]:
            self.speedy     = 15

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        #Bordes
        if self.rect.right > ancho+100:
            self.rect.right = x-ancho-100
            self.rect.left  = 0-100
        if self.rect.left <0 -100:
            self.rect.left  = x+ancho+100
            self.rect.right = ancho+100
        if self.rect.top < 0-110:
            self.rect.top       = y+alto+110
            self.rect.bottom    = alto+110
        if self.rect.bottom > alto+110:
            self.rect.bottom    = x-alto-110
            self.rect.top       = 0-110

    def reiniciarTodo(self):
        self.image          =  pygame.transform.rotozoom(nave0, 125, 0.30)
        self.rect           = self.image.get_rect()
        self.lives          = 6
        self.rect.center    = (ancho/2,(10*alto)/11)
        self.speedx         = 0
        self.speedy         = 0

#Enemigo 1
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image  =  pygame.transform.rotozoom(nave1, 315, 0.15)
        self.rect   = self.image.get_rect()
        self.rect.y = - self.rect.height-10#random.randrange(alto - self.rect.height)
        self.rect.x = random.randrange(ancho - self.rect.width)
        self.speedy = random.randrange(1, 3)
        self.speedx = 0#random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > alto + 10 or self.rect.left < -25 or self.rect.right > ancho + 20:
            self.rect.x = random.randrange(ancho - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1,3)
            self.speedx = 0#random.randrange(-2,4)



#Enemigo 2


class Mob2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image  = pygame.transform.rotozoom(nave2, 270, 0.10)
        self.rect   = self.image.get_rect()
        self.radius         = 35
        self.rect.y = - self.rect.height-10#random.randrange(alto - self.rect.height)
        self.rect.x = random.randrange(ancho - self.rect.width)
        self.speedy = random.randrange(1, 4)
        self.speedx = random.randrange(-3, 3)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > alto + 10 or self.rect.left < -25 or self.rect.right > ancho + 20:
            self.rect.x = random.randrange(ancho - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1,5)
            self.speedx = 0#random.randrange(1,4)



#Enemigo 3
class Mob3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.transform.rotozoom(nave3, 45, 0.27)
        self.rect   = self.image.get_rect()
        self.radius         = 35
        self.rect.y = - self.rect.height-10#random.randrange(alto - self.rect.height)
        self.rect.x = random.randrange(ancho - self.rect.width)
        self.speedy = random.randrange(1, 3)
        self.speedx = 0#random.randrange(-3, 3)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > alto + 10 or self.rect.left < -25 or self.rect.right > ancho + 20:
            self.rect.x = random.randrange(ancho - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1,5)
            self.speedx = 0#random.randrange(1,4)


#Enemigo 4
class Mob4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image  =  pygame.transform.rotozoom(nave4, 270, 0.10)
        self.rect   = self.image.get_rect()
        self.radius         = 35
        self.rect.y = - self.rect.height-10#random.randrange(alto - self.rect.height)
        self.rect.x = random.randrange(ancho - self.rect.width)
        self.speedy = random.randrange(1, 4)
        self.speedx = random.randrange(-3, 3)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > alto + 10 or self.rect.left < -25 or self.rect.right > ancho + 20:
            self.rect.x = random.randrange(ancho - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1,3)
            self.speedx = 0#random.randrange(-3,4)



#Enemigo 5
class Mob5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image  =  pygame.transform.rotozoom(nave5, 270, 0.10)
        self.rect   = self.image.get_rect()
        self.radius         = 35
        self.rect.y = - self.rect.height-10#random.randrange(alto - self.rect.height)
        self.rect.x = random.randrange(ancho - self.rect.width)
        self.speedy = random.randrange(1, 5)
        self.speedx = 0#random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > alto + 10 or self.rect.left < -25 or self.rect.right > ancho + 20:
            self.rect.x = random.randrange(ancho - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1,4)
            self.speedx = random.randrange(1,4)



#Balas
class Bala(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bala,(10,10))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        #Desaparecer
        if self.rect.bottom<0:
            self.kill()


#Menu
def menu():
    #global es para mostrar que estas variables no son exclusivas de la funcion
    global ancho,alto,screen,modoMenu,iniciar,ayuda,credito,cerrar
    #creado la Ventana
    blanco  = (255,255,255) # color blanco en RGB
    contador = 0
    #LOOP PRINCIPAL
    while modoMenu :
        #recorro todos los eventos producidos
        #en realidad es una lista

        for event in pygame.event.get():

            # si el evento es del tipo
            # pygame.QUIT( cruz de la ventana)
            if event.type == pygame.QUIT :
                cerrar      = True
                modoMenu    = False
                iniciar     = False
                ayuda       = False
                credito     = False
                contador    = 0
                #pygame.quit()
                break


            elif event.type == KEYDOWN:
                print event.key
                if event.key == K_DOWN:
                    contador=contador+1
                    if contador>4:
                        contador=1



                if event.key == K_UP:
                    contador=contador-1
                    if contador<1:
                        contador=4


                if event.key == 13 or event.key == K_x: #el numero 13 representa la tecla enter (no encontre el nombre)

                    if contador == 1:
                        iniciar = True
                        modoMenu = False
                        break

                    elif contador == 2:
                        ayuda = True
                        modoMenu = False
                        break

                    elif contador == 3:
                        credito = True
                        modoMenu = False
                        break

                    elif contador == 4:
                        cerrar      = True
                        modoMenu    = False
                        iniciar     = False
                        ayuda       = False
                        credito     = False
                        contador    = 0

                        break


        #reloj1.tick(20)#operacion para que todo corra a 20fps
        pygame.display.update() #actualizo el display
        screen.fill(blanco) # pinto la superficie de blanco

        screen.blit(fondoMenu.convert(),(0,0))
        if contador   == 1:
            screen.blit(opcionIniciar,(0,0))
        elif contador == 2:
            screen.blit(opcionAyuda,(0,0))
        elif contador == 3:
            screen.blit(opcionCredito,(0,0))
        elif contador == 4:
            screen.blit(opcionSalir,(0,0))
        else:
            screen.blit(opciones,(0,0))










#Vidas de jugador
def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)
#Texto de score
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, 55)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

#Inicializadores
pygame.init()
pygame.mixer.init()
#musica
pygame.mixer.music.load(song)
pygame.mixer.music.play(-1)
#Ventana
SCREEN_SIZE = (ancho, alto)
screen = pygame.display.set_mode(SCREEN_SIZE)
#Titulo
pygame.display.set_caption("COLOR GUNNER")
#Reloj
clock = pygame.time.Clock()
#Grupo de Sprites
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
balas= pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#Aparicion de enemigos
objetivo    =pygame.sprite.Group()
noObjetivo  =pygame.sprite.Group()
def crearNaves():
    global a,b,c,d,e,all_sprites,objetivo,noObjetivo
    for i in range(cantidadEnemigos):
        a = Mob()
        b = Mob2()
        c = Mob3()
        d = Mob4()
        e = Mob5()
        all_sprites.add(a)
        all_sprites.add(b)
        all_sprites.add(c)
        all_sprites.add(d)
        all_sprites.add(e)
        objetivo.add(a)
        objetivo.add(b)
        objetivo.add(d)
        noObjetivo.add(c)
        noObjetivo.add(e)
        mobs.add(a)
        mobs.add(b)
        mobs.add(c)
        mobs.add(d)
        mobs.add(e)
crearNaves()


def verificarSalirONo():
    global iniciar,modoMenu,all_sprites,score
    regresar = False
    while not regresar:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == 32:
                    regresar = True
                    break

                elif event.key == 13:
                    iniciar=False
                    modoMenu=True
                    regresar = True

                    player.reiniciarTodo()
                    all_sprites.remove(mobs)
                    score = 0
                    crearNaves()



                    #all_sprites.update()
                    break



        screen.blit(salir_o_no, (0,0))
        pygame.display.flip()

def gameover():
    global iniciar,modoMenu,all_sprites,score,gameover
    regresar = False
    while not regresar:

        for event in pygame.event.get():
            if event.type == KEYDOWN:


                if event.key == 13:
                    iniciar=False
                    modoMenu=True
                    regresar = True

                    player.reiniciarTodo()
                    all_sprites.remove(mobs)
                    score = 0
                    crearNaves()



                    #all_sprites.update()
                    break


        screen.blit(game_over , (0,0))
        pygame.display.flip()



#Score
score = 0
turnoNave=0
while not cerrar:
    while modoMenu:
        menu()
    while iniciar:
        #Reloj
        #clock.tick(FPS)
        #Inputs

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #exit()
                cerrar      = True
                modoMenu    = False
                iniciar     = False
                ayuda       = False
                credito     = False
            #Teclas presionadas
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    directionx = MOVE_LEFT
                elif event.key == K_RIGHT:
                    directionx = MOVE_RIGHT
                elif event.key == K_UP:
                    directiony = MOVE_UP
                elif event.key == K_DOWN:
                    directiony = MOVE_DOWN

                elif event.key == K_ESCAPE:

                    verificarSalirONo()

                if event.key == K_SPACE or event.key == K_x:

                    disparoFuego = Bala(player.rect.centerx-15,player.rect.y+50)
                    all_sprites.add(disparoFuego)
                    balas.add(disparoFuego)

            #Teclas sin presionar
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    directionx = 0
                elif event.key == K_RIGHT:
                    directionx = 0
                elif event.key == K_UP:
                    directiony = 0
                elif event.key == K_DOWN:
                    directiony = 0

        all_sprites.update()

        #colision de jugador-enemigo
        #colision de jugador-enemigo
        hits = pygame.sprite.spritecollide(player,mobs,True,pygame.sprite.collide_circle)
        if hits:
            player.lives -= 1
            if player.lives==0:
               gameover()


        #colision bala-enemigo
        for disparoFuego in balas:
            lista_enemigos_alcanzados=pygame.sprite.spritecollide(disparoFuego,objetivo,True)
            for a in lista_enemigos_alcanzados:
                balas.remove(disparoFuego)
                all_sprites.remove(disparoFuego)
                score  += 10
            lista_no_enemigos_alcanzados=pygame.sprite.spritecollide(disparoFuego,noObjetivo,True)
            for j in lista_no_enemigos_alcanzados:
                balas.remove(disparoFuego)
                all_sprites.remove(disparoFuego)
                player.lives -= 1
                if player.lives==0:
                   gameover()

        while len(mobs)< cantidadEnemigos*5: #esta establecido la cantidad de clases de enemigos 5
            turnoNave = random.randrange(1,6)
            print turnoNave
            if turnoNave == 1:
                a = Mob()
                all_sprites.add(a)
                mobs.add(a)
                objetivo.add(a)

            elif turnoNave == 2:
                b = Mob2()
                all_sprites.add(b)
                mobs.add(b)
                objetivo.add(b)

            elif turnoNave == 3:
                c = Mob3()
                all_sprites.add(c)
                mobs.add(c)

                noObjetivo.add(c)

            elif turnoNave == 4:
                d = Mob4()
                all_sprites.add(d)
                mobs.add(d)
                objetivo.add(d)

            elif turnoNave == 5:
                e = Mob5()
                all_sprites.add(e)
                mobs.add(e)
                noObjetivo.add(e)
            else:
                turnoNave = 1

        # Creaci0n de las naves
        #if all_sprites.sprite()==2:
         #   crearNaves()

#esto estuve intentando para la colision de enemigo y player pero no sale creo la estructura esta mal
##        for player in mobs:
##            choque_enemigo_player=pygame.sprite.spritecollide(player,mobs,True)
##            for player in choque_enemigo_player:
##                mobs.remove(player)
##                all_sprites.remove(player)


        #Renderizar

        screen.fill(BLACK)
        screen.blit(background, (0,0))
        all_sprites.draw(screen)
        draw_text(screen, str(score), 18, ancho / 2, 10)
        draw_lives(screen, ancho - 200, 3, player.lives, vidas)
        pygame.display.flip()



    while ayuda:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    ayuda    = False
                    modoMenu = True
                    break
        screen.blit(vistaAyuda, (0,0))
        pygame.display.flip()
    while credito:



        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    credito  = False
                    modoMenu = True
                    break
        screen.blit(vistaCreditos, (0,0))
        pygame.display.flip()





pygame.quit()

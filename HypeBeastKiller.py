# encoding: UTF-8
# Sebastian Morales Martin
# HypeBeastKiller: Destruye las marcas mainstream!

import pygame
from random import randint as ran
from getpass import getuser as get


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
ROJO2 = (196, 60, 45)
user = get()
def dibujarmenu(fondo,boton1, ventana, letra): #dibuja la interaz de menu
    ventana.blit(fondo,(0,0))
    ventana.blit(boton1.image, boton1.rect)
    titulo = letra.render('Hype Beast Killer.py', 100, ROJO)
    ventana.blit(titulo, (50, 25))
def dibujarTutorial(fondo, boton1,  ventana, letra): # dibuja un pequeño tutorial en el cual muestra que tienes que hacer en el juego
    ventana.blit(fondo, (0,0))
    ventana.blit(boton1.image, boton1.rect)
    mensaje = letra.render('¡Acaba con los enemigos!', 100, NEGRO)
    mensaje2 = letra.render('Usa las flechas DERECHA e IZQUIERDA', 50, NEGRO)
    mensaje3 = letra.render('para moverte. ESPACIO para disparar.', 50, NEGRO)
    mensaje4 = letra.render('¡DIVIERTETE!', 50, NEGRO)
    mensaje5 = letra.render('Obten 5000 puntos para ganar!', 50, NEGRO)
    mensaje6 = letra.render('Hola %s !' % user, 50, NEGRO)
    ventana.blit(mensaje, (50, 100))
    ventana.blit(mensaje2, (50, 150))
    ventana.blit(mensaje3, (50, 200))
    ventana.blit(mensaje4, (50, 250))
    ventana.blit(mensaje5, (50, 300))
    ventana.blit(mensaje6, (50, 50))
def dibujarJuego(fondo, ventana):               # dibuja el juego
    ventana.blit(fondo, (0,0))


def dibujarEE(ventana, fondo):                 # dibuja un pequeño "easter egg" dentro del juego
    ventana.blit(fondo, (0,0))

def crearEnemigos(lista, malo):                   #crea 60 enemigos y los agrega a la lista
    for renglon in range(1, 6):
        for columna in range(1, 13):
            enemigo = pygame.sprite.Sprite()
            enemigo.image = malo
            enemigo.rect = malo.get_rect()
            enemigo.rect.left = columna * (58)
            enemigo.rect.top = renglon * (60)
            lista.append(enemigo)

def dibujarEnemigos(lista, ventana):            # dibuja los enemigos en pantalla
    for enemigo in lista:
        ventana.blit(enemigo.image, enemigo.rect)
    for indiceEnemigo in range( -len(lista)-1, -1, -1):
        enemigo = lista[indiceEnemigo]
        while enemigo.rect.top + enemigo.rect.height < 750:
            enemigo.rect.top += 10


# Estructura básica de un programa que usa pygame para dibujar


def crearBalas(lista, sprite, nave):
    spriteBala = pygame.sprite.Sprite()
    spriteBala.image = sprite
    spriteBala.rect = sprite.get_rect()
    spriteBala.rect.left = nave.rect.left + (nave.rect.width//2)
    spriteBala.rect.top = ALTO - (nave.rect.height + 20)
    lista.append(spriteBala)


def dibujarBalas(lista, ventana):
    for bala in lista:
        ventana.blit(bala.image, bala.rect)
    for bala in lista:
        bala.rect.top -= 10
        for k in range(len(lista)-1 ,-1, -1):
            bala = lista[k]
            if bala.rect.top <= - bala.rect.height:
                lista.remove(bala)


def eliminarEnemigos(listaBalas, listaEnemigos, efecto):
    contador = 0
    for iB in range(len(listaBalas)-1, -1, -1):
        bala = listaBalas[iB]
        for iE in range(len(listaEnemigos)-1, -1, -1):
            enemigo = listaEnemigos[iE]
            xb, yb, anchoB, altoB = bala.rect
            xe, ye, anchoE, altoE = enemigo.rect
            if xb >= xe and xb <= xe + anchoE and yb >= ye and yb <= ye + altoE:
                efecto.play()
                listaBalas.remove(bala)
                listaEnemigos.remove(enemigo)
                contador +=1
                break
    return contador


def dibujarVictoria(imgEE, consolas, ventana):
    ventana.blit(imgEE, (0,0))
    victoria = consolas.render('Victoria!', 1, BLANCO)
    ventana.blit(victoria, (50, 250))


def generaBalaEnemigo(listaEnemigos,listaBalasEnemigos, imgBala):
    while len(listaEnemigos) > 1:
        disparo = listaEnemigos[ran(0, len(listaEnemigos))]
        spriteBala = pygame.sprite.Sprite()
        spriteBala.image = imgBala
        spriteBala.rect = imgBala.get_rect()
        spriteBala.rect.top = disparo.rect.top + disparo.rect.height
        spriteBala.rect.left = disparo.rect.left + (disparo.rect.width // 2)
        listaBalasEnemigos.append(spriteBala)
def dibujarBalaEnemigos(listaBalasEnemigos, ventana):
    for bala in listaBalasEnemigos:
        ventana.blit(bala.image, bala.rect)
    while bala < ALTO + bala.rect.height:
        bala.rect.top += 10



def dibujar():

    # Inicializa el motor de pygame
    pygame.init()
    pygame.mixer.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock()     # Para limitar los fps
    termina = False                 # Bandera para saber si termina la ejecución
    pygame.font.init()

    #Fuente
    consolas = pygame.font.SysFont('consolas', 50)
    ubuntu = pygame.font.SysFont('ubuntu', 100)


    #Estados
    estado = 'menu'
    # Imágenes
    imgFondo = pygame.image.load("fondo.jpg")
    imgBtnSupreme = pygame.image.load("supreme.png")
    imgBtnHelp = pygame.image.load("help.png")
    imgGame = pygame.image.load('fondoGame.png')
    imgBtnPlay = pygame.image.load('play.png')
    imgEE = pygame.image.load('ee.jpg')
    imgEnemigo =pygame.image.load('enemigo.png')
    imgNave = pygame.image.load('nave.png')
    imgBala = pygame.image.load('bala.png')
    imgJuego = pygame.image.load('battlefield.jpg')
    imgNiceMeme = pygame.image.load('nice meme.png')

    #Boton "supreme" para iniciar el juego
    spriteBtnSupreme = pygame.sprite.Sprite()
    spriteBtnSupreme.image = imgBtnSupreme
    spriteBtnSupreme.rect = imgBtnSupreme.get_rect()
    spriteBtnSupreme.rect.left = ANCHO//2 - 128
    spriteBtnSupreme.rect.top = 250
    #------------------------  AYUDA (posiblemente lo quite mas tarde)
    #spriteBtnHelp = pygame.sprite.Sprite()
    #spriteBtnHelp.image = imgBtnHelp
    #spriteBtnHelp.rect = imgBtnHelp.get_rect()
    #spriteBtnHelp.rect.left = ANCHO//2 - 128
    #spriteBtnHelp.rect.top = 200
    #------------------------
    # boton de play en la pagina de tutorial
    spriteBtnPlay = pygame.sprite.Sprite()
    spriteBtnPlay.image = imgBtnPlay
    spriteBtnPlay.rect = imgBtnPlay.get_rect()
    spriteBtnPlay.rect.left = ANCHO//2 - 128
    spriteBtnPlay.rect.top = 400
    #------------------------  NAVE
    spriteNave = pygame.sprite.Sprite()
    spriteNave.image = imgNave
    spriteNave.rect = imgNave.get_rect()
    spriteNave.rect.left = ANCHO//2 - 24
    spriteNave.rect.top = ALTO - spriteNave.rect.height


    #Sonidos
    pygame.mixer.music.load('intermission.mp3')
    pygame.mixer.music.play(-1)


    #Efectos de sonido
    efecto = pygame.mixer.Sound("shoot.wav")
    boton = pygame.mixer.Sound('disparo.wav')

    boton.set_volume(1)

    # implementacion de los enemigos
    listaEnemigos = []
    crearEnemigos(listaEnemigos, imgEnemigo)

    # implementación de las balas
    listaBalas = []     # al empezar no hay balas
    listaBalasEnemigos = [] # no hay balas empezando

    #pantakka de victoria
    puntos= 0
    vidas = 3
    timer = 1/60

    while not termina:              # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if estado == "menu":

                    xb, yb, anchoB, altoB = spriteBtnSupreme.rect
                    #xd, yd, anchoD, altoD = spriteBtnHelp.rect

                    if mouseX >= xb and mouseX <= xb + anchoB:
                        if mouseY >= yb and mouseY <= yb + altoB:
                            boton.play()
                            estado = "Tutorial"

                elif estado == "Tutorial":
                    xc, yc, anchoC, altoC = spriteBtnPlay.rect
                    if mouseX >= xc and mouseX <= xc + anchoC:
                        if mouseY >= yc and mouseY <= yc + altoC:
                            boton.play()
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load("juego.mp3")            #NOTA: si haces clic rápido en la pantalla puede que la cancion no se ejecute
                            pygame.mixer.music.set_volume(.75)
                            pygame.mixer.music.play(-1)
                            estado = 'juego'

                elif estado == 'gana':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('hydrogen.mp3')
                    pygame.mixer.music.play(-1)

            elif evento.type == pygame.KEYDOWN and estado == 'juego':           #Eventos de teclado dentro del juego
                if evento.key == pygame.K_LEFT:
                    spriteNave.rect.left -= 10
                elif evento.key == pygame.K_RIGHT:
                    spriteNave.rect.left += 10
                elif evento.key == pygame.K_SPACE:
                    efecto.play()
                    crearBalas(listaBalas, imgBala, spriteNave)



        # Borrar pantalla
        ventana.fill(NEGRO)

        while timer < 2 and estado == 'juego':
            timer += 1 / 60
            if timer == 30 / 60:
                generaBalaEnemigo(listaEnemigos, listaBalasEnemigos, imgBala)
                dibujarBalaEnemigos(listaBalasEnemigos, ventana)
            elif timer == 1:
                timer = 1 / 60

        # Dibujar, aquí haces todos los trazos que requieras
        pygame.display.set_caption('')
        if estado == 'menu':
            dibujarmenu(imgFondo, spriteBtnSupreme, ventana, ubuntu)
        elif estado == 'Tutorial':
            dibujarTutorial(imgGame, spriteBtnPlay, ventana, consolas)
        elif estado == 'juego':
            dibujarJuego(imgJuego, ventana)
            dibujarEnemigos(listaEnemigos, ventana)
            ventana.blit(spriteNave.image, spriteNave.rect)
            dibujarBalas(listaBalas, ventana)
            #verificacion de colisiones
            destruidos = eliminarEnemigos(listaBalas, listaEnemigos, boton)
            puntos += destruidos *100
            puntaje = consolas.render('Puntos: %d'% puntos, 100, NEGRO)
            resistencia = consolas.render('Resistencia: %d' % vidas, 100, NEGRO)
            ventana.blit(puntaje, (50, 20))
            ventana.blit(resistencia, (500, 20))
            if puntos >= 300:
                estado = 'gana'
        elif estado == 'gana':
            dibujarVictoria(imgEE, consolas, ventana)
            ventana.blit(imgNiceMeme, (300, 150))



        pygame.display.flip()   # Actualiza trazos
        reloj.tick(60)         # 60 fps

    # Después del ciclo principal
    pygame.quit()   # termina pygame


def main():
    dibujar()


main()
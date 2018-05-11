#Autor: Jossian Abimelec García Quijano
# encoding: UTF-8
#Juego llamado KURSK
from random import randint
import pygame
pygame.font.init()
import time

ANCHO = 800
ALTO = 600
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)


def dibujarEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image,enemigo.rect)


def crearEnemigos(listaEnemigos, imgEnemigo):
    for renglon in range(3,8):
        for columna in range(1,4):
            enemigo=pygame.sprite.Sprite()
            enemigo.image=imgEnemigo
            enemigo.rect=imgEnemigo.get_rect()
            enemigo.rect.left=columna*(randint(0,400))
            enemigo.rect.top=renglon*75#100
            listaEnemigos.append(enemigo)


def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image,bala.rect)


def actualizarBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.top += 12
    for k in range(len(listaBalas)-1,-1,-1):
         bala=listaBalas[k]
         if bala.rect.top<=bala.rect.height:
            listaBalas.remove(bala)


def checarColisiones(listaBalas, listaEnemigos, efectoDestruye):
    destruidos = 0
    for iB in range(len(listaBalas)-1,-1,-1):
        bala=listaBalas[iB]
        for iE in range(len(listaEnemigos)-1,-1,-1):
            enemigo=listaEnemigos[iE]
            xb,yb,ab,alb=bala.rect
            xe,ye,ae,ale=enemigo.rect
            if xb+ab>=xe and xb<=xe+ae and yb>=ye and yb<=ye+ale :
                listaBalas.remove(bala)
                listaEnemigos.remove(enemigo)
                efectoDestruye.play()
                destruidos+=1
                break
    return destruidos


def crearBalasEnemigo( listaBalasEnemigos,listaEnemigos,imgBalaEnemigo):
    tiempo = pygame.time.get_ticks()
    if tiempo >= 3000:
      for enemigo in listaEnemigos:
            rangodisparo=3
            if randint(0,200)<rangodisparo:
                balaE = pygame.sprite.Sprite()
                balaE.image = imgBalaEnemigo
                balaE.rect = imgBalaEnemigo.get_rect()
                balaE.rect.left = enemigo.rect.left +enemigo.rect.width // 2
                balaE.rect.top = enemigo.rect.top -balaE.rect.height
                listaBalasEnemigos.append(balaE)


def dibujarEnemigo(listaBalasEnemigos,ventana):
       for balae in listaBalasEnemigos:
           ventana.blit(balae.image,balae.rect)


def actualizarBalasEnemigo(listaBalasEnemigos):
         for balaE in listaBalasEnemigos:
             balaE.rect.top -= 5
         for k in range(len(listaBalasEnemigos)-1,-1,-1):
              balaE=listaBalasEnemigos[k]
              if balaE.rect.top<=balaE.rect.height:#si la y de la bala es menor a menos la altura de la bala
                 listaBalasEnemigos.remove(balaE)


def checharColisionDestructor(listaBalasEnemigos, destructor,estadoJuego, efectoDestruye,listaVidas):
    destruido=0
    for iB in range(len(listaBalasEnemigos)-1,-1,-1):
        balaE=listaBalasEnemigos[iB]
        xb,yb,ab,alb=balaE.rect
        xe,ye,ae,ale=destructor.rect
        if xb+ab>=xe and xb<=xe+ae and yb>=ye and yb<=ye+ale :
            listaBalasEnemigos.remove(balaE)
            efectoDestruye.play()
            destruido += 1
            break
    return destruido


def leerHighScore(puntos):
    entrada=open("highScore.txt","r",encoding="UTF-8")
    linea=entrada.readline()
    dato = linea.split(" ")
    highSocre=dato[0]
    return highSocre


def compararhighScore(puntos):
    entrada = open("highScore.txt", "r", encoding="UTF-8")
    linea = entrada.readline()
    dato = linea.split(" ")
    highSocre = dato[0]
    if int(highSocre) < puntos:
        salida = open("highScore.txt", "w", encoding="UTF-8")
        lineasalida = puntos
        salida.write(str(lineasalida))
        salida.close()

def dibujar():
    imgFondo = pygame.image.load("kursk.jpg")
    imgOceano = pygame.image.load("oceano.jpg")
    imgBtnJugar = pygame.image.load("buttonJugar.png")
    imgBtnAcercaDe = pygame.image.load("button_acerca-de.png")
    imgAcerca_de = pygame.image.load("Acerca.jpg")
    imgGANA = pygame.image.load("GANA.jpg")
    imgPIERDE = pygame.image.load("PIERDE.jpg")
    imgHorizonte = pygame.image.load("horizonte.jpg")

    spriteBtnJugar = pygame.sprite.Sprite()
    spriteBtnJugar.image = imgBtnJugar
    spriteBtnJugar.rect = imgBtnJugar.get_rect()
    spriteBtnJugar.rect.left = ANCHO // 2 - spriteBtnJugar.rect.width // 2  # coordenadax
    spriteBtnJugar.rect.top = 600-(ALTO // 2)  # coordenaday

    spriteBtnAcercaDe = pygame.sprite.Sprite()
    spriteBtnAcercaDe.image = imgBtnAcercaDe
    spriteBtnAcercaDe.rect = imgBtnAcercaDe.get_rect()
    spriteBtnAcercaDe.rect.left = ANCHO // 2 - spriteBtnAcercaDe.rect.width // 2
    spriteBtnAcercaDe.rect.top = 600-(ALTO // 4)


    #DESTRUCTOR
    imgDestructor = pygame.image.load("destructor.png")
    destructor = pygame.sprite.Sprite()
    destructor.image = imgDestructor
    destructor.rect = imgDestructor.get_rect()
    destructor.rect.left = ANCHO//2
    destructor.rect.top =ALTO//8
    destruido=False


    #BALAS
    imgBala = pygame.image.load("torpedo.png")
    listaBalas = []


    #BALAS ENEMIGOS
    imgBalaEnemigo = pygame.image.load("tor.png")
    listaBalasEnemigos = []


    #SONIDOS
    pygame.mixer.init()
    efectoDestruye=pygame.mixer.Sound("explosion.wav")
    pygame.mixer.music.load("musica.mp3")


    #ENEMIGOS(SUBMARINOS)
    imgEnemigo = pygame.image.load("sub.png")
    listaEnemigos=[]
    crearEnemigos(listaEnemigos, imgEnemigo)


    #PANTALLA GANAS
    puntos=0
    fuente = pygame.font.SysFont("monospace", 76)

    #BARRA VIDA
    imgVida = pygame.image.load("vidas.png")
    listaVidas = []

    for vid in range(0,3):
        vida=pygame.sprite.Sprite()
        vida.image=imgVida
        vida.rect=imgVida.get_rect()
        vida.rect.left=0+vida.rect.width*vid######################
        vida.rect.top=25
        listaVidas.append(vida)
    muertos=0
    MENU=1
    JUEGO=2
    ACERCA_DE=3
    GANA=4
    PIERDE=5

    estadoJuego=MENU
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución
    pygame.mixer.music.play()
    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            if evento.type==pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego == MENU:  # SOLO CUANDO ESTA EN EL MENU

                    xbj, ybj, abj, albj = spriteBtnJugar.rect
                    xba, yba, aba, alba = spriteBtnAcercaDe.rect

                    if xm >= xbj and xm <= xbj + abj:
                        if ym >= ybj and ym <= ybj + albj:
                            estadoJuego=JUEGO

                    if xm >= xba and xm <= xba + aba:
                        if ym >= yba and ym <= yba + alba:
                            estadoJuego=ACERCA_DE

            if evento.type == pygame.KEYDOWN and estadoJuego == JUEGO:  # si oprimio una tecla
                if evento.key == pygame.K_LEFT:
                    destructor.rect.left -= 25
                elif evento.key == pygame.K_RIGHT:
                    destructor.rect.left += 25

                elif evento.key == pygame.K_SPACE:
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = destructor.rect.left +destructor.rect.width // 2
                    bala.rect.top = destructor.rect.top -bala.rect.height
                    listaBalas.append(bala)

        ventana.fill(AZUL)

        if estadoJuego==MENU:
            ventana.blit(imgFondo, (0, 0))
            ventana.blit(spriteBtnJugar.image, spriteBtnJugar.rect)
            ventana.blit(spriteBtnAcercaDe.image,spriteBtnAcercaDe.rect)


        elif estadoJuego==JUEGO:
            ventana.blit(imgHorizonte, (0,0))
            ventana.blit(imgOceano, (0,ALTO//8+30))
            dibujarEnemigos(ventana, listaEnemigos)
            dibujarBalas(ventana,listaBalas)
            crearBalasEnemigo( listaBalasEnemigos,listaEnemigos,imgBalaEnemigo)
            dibujarEnemigo(listaBalasEnemigos,ventana)
            actualizarBalasEnemigo(listaBalasEnemigos)
            ventana.blit(destructor.image,destructor.rect)
            actualizarBalas(listaBalas)
            destruido=checharColisionDestructor(listaBalasEnemigos,destructor,estadoJuego, efectoDestruye, listaVidas)
            muertos+=destruido
            if muertos==1:
                ventana.blit(listaVidas[2].image, listaVidas[2].rect)
            elif muertos==2:
                ventana.blit(listaVidas[2].image, listaVidas[2].rect)
                ventana.blit(listaVidas[1].image, listaVidas[1].rect)
            elif muertos==3:
                ventana.blit(listaVidas[2].image, listaVidas[2].rect)
                ventana.blit(listaVidas[1].image, listaVidas[1].rect)
                ventana.blit(listaVidas[0].image, listaVidas[0].rect)
                estadoJuego=PIERDE

            destruidos=checarColisiones(listaBalas, listaEnemigos, efectoDestruye)
            puntos += destruidos
            if puntos >= 15:
                estadoJuego = GANA
            compararhighScore(puntos)


        elif estadoJuego == PIERDE:
            ventana.blit(imgPIERDE, (0, 0))
            pygame.mixer.music.stop()
            texto = fuente.render("PERDISTE :C",4, BLANCO)
            ventana.blit(texto, (ANCHO // 2 - 200, ALTO // 4))


        elif estadoJuego==GANA:
            ventana.blit(imgGANA, (0, 0))
            texto = fuente.render("¡GANASTE!", 4, BLANCO)
            ventana.blit(texto, (ANCHO // 2 - 200, ALTO // 4))


        elif estadoJuego==ACERCA_DE:
            highScore = leerHighScore(puntos)
            ventana.blit(imgAcerca_de, (0, 0))
            texto = fuente.render("PUNTAJE MÁS ALTO: ", 6, BLANCO)
            ventana.blit(texto, (0, ALTO // 4))
            texto = fuente.render(str(highScore), 10, AZUL)
            ventana.blit(texto, (0, ALTO // 2))


        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def main():
    dibujar()


main()
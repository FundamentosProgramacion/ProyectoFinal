import pygame
import random
import winsound

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0,0,0)
YELLOW =(255,247,0)
mousewidth = 150
yFondo = 0



# Estructura básica de un programa que usa pygame para dibujar

# Dibuja TODOS LOS ENEMIGOS SOBRE LA VENTANA

def dibujarTrampa1(ventana,trap,randomStartx,direction):
    ventana.blit(trap, (randomStartx, direction))

def dibujarTrampa2(ventana,trap2,randomStartx2,direction2):
    ventana.blit(trap2, (randomStartx2,direction2))

def dibujarMonedas(ventana,imgCoin,randomstartx3,direction3):
    ventana.blit(imgCoin , (randomstartx3,direction3 ))

def checarColisionesTrampa1(mouse,trap,randomStartx,direccion):
    xm, ym, am, alm = mouse.rect
    xt, yt, at, alt = trap.rect
    yt = direccion
    xt = randomStartx

    if xm >= xt and xm <= xt + at and ym >= yt and ym <= yt + alt:
        return True
    elif xm+75 >= xt and xm+75 <= xt + at and ym >= yt and ym <= yt + alt:
        return True
    elif xm+mousewidth >= xt and xm+mousewidth <= xt + at and ym >= yt and ym <= yt + alt:
        return True

def checarColisionesTrampa2(mouse,trap2,randomStartx2,direccion2):
    xm, ym, am, alm = mouse.rect
    xt, yt, at, alt = trap2.rect
    yt = direccion2
    xt = randomStartx2
    if xm >= xt and xm <= xt + at and ym >= yt and ym <= yt + alt:
        return True
    elif xm+75 >= xt and xm+75 <= xt + at and ym >= yt and ym <= yt + alt:
        return True
    elif xm+mousewidth >= xt and xm+mousewidth <= xt + at and ym >= yt and ym <= yt + alt:
        return True

def checarColisionesBITCOIN(ventana,mouse,coin,imgCoin,randomStartx3,direction3):
    xm, ym, am, alm = mouse.rect
    xt, yt, at, alt = coin.rect
    yt = direction3
    xt = randomStartx3
    if xm >= xt and xm <= xt + at and ym >= yt and ym <= yt + alt:

        return True
    elif xm + 75 >= xt and xm + 75 <= xt + at and ym >= yt and ym <= yt + alt:

        return True
    elif xm + mousewidth >= xt and xm + mousewidth <= xt + at and ym >= yt and ym <= yt + alt:

        return True

    else:
        return False


def checarColisionesGato(mouse,cat,xCat,randomStarty,cattt):
    xm, ym, am, alm = mouse.rect
    xt, yt, at, alt = cat.rect
    yt = randomStarty
    xt = xCat
    if xm >= xt and xm <= xt + at and ym >= yt and ym <= yt + alt:
        cattt.play()
        return True
    elif xm + 75 >= xt and xm + 75 <= xt + at and ym >= yt and ym <= yt + alt:
        cattt.play()
        return True
    elif xm + mousewidth >= xt and xm + mousewidth <= xt + at and ym >= yt and ym <= yt + alt:
        cattt.play()
        return True

def checarColisionesBala(cat,bala,xCat,randomStarty,listaBalas):
    xb, yb, ab, alb = bala.rect
    xe, ye, ae, ale = cat.rect
    yt = randomStarty
    xt = xCat
    if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + ale:
        print("colisionBALA")

def dibujarFlama(ventana,imgFlama,x,y):
    ventana.blit(imgFlama,(100,100))

def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución


    #Imagenes
    imgFondo = pygame.image.load("kaw.jpg")
    imgBtnJugar = pygame.image.load("button_jugar.png")
    imgGameOver = pygame.image.load("dead.jpg")
    spriteBtnJugar = pygame.sprite.Sprite()
    spriteBtnJugar.image = imgBtnJugar
    spriteBtnJugar.rect = imgBtnJugar.get_rect()
    spriteBtnJugar.rect.left = ANCHO//2 - spriteBtnJugar.rect.width//2
    spriteBtnJugar.rect.top = ANCHO//2 - spriteBtnJugar.rect.height//2

    #BOTON PLAYAGIAN
    imgBtnReintentar = pygame.image.load("button_reintentar.png")
    spriteReintentar = pygame.sprite.Sprite()
    spriteReintentar.image = imgBtnReintentar
    spriteReintentar.rect = imgBtnReintentar.get_rect()
    spriteReintentar.rect.left = ANCHO//2 - spriteReintentar.rect.width//2
    spriteReintentar.rect.top = ANCHO//2 - spriteReintentar.rect.height//2

    #ESTADOS de juego
    MENU  = 1
    JUEGO = 2
    GATOMUERTO = 3
    GATOVIVO =4
    GANA = 5
    CHOQUE = 6
    yFondo = 0
    bitnotcollected = 8

    estadoJuego = MENU      #juego, acerca de

    #PERSONAJE. RATON
    imgMouse = pygame.image.load("muss.png")
    mouse = pygame.sprite.Sprite()
    mouse.image = imgMouse
    mouse.rect = imgMouse.get_rect()
    mouse.rect.left = ANCHO//2 - mouse.rect.width//2
    mouse.rect.top = ALTO - mouse.rect.height-30
    xm,ym,am,alm = mouse.rect
    #ym = mouse.rect.top

    #IMAGEN DE TRAMPA
    imgTrap = pygame.image.load("MOUSETRAP1.jpg")
    trap = pygame.sprite.Sprite()
    trap.image = imgTrap
    trap.rect = imgTrap.get_rect()
    randomStartx = random.randint(0, ANCHO)
    trap.rect.left = randomStartx
    trap.top = -600
    trap.rect.top = ALTO // 2

    #IMG TRAMPA2
    imgTrap2 = pygame.image.load("MOUSETRAP2.jpg")
    trap2 = pygame.sprite.Sprite()
    trap2.image = imgTrap2
    trap2.rect = imgTrap2.get_rect()
    randomStartx2 = random.randint(0, ANCHO)
    trap2.rect.left = randomStartx2
    trap2.top = -600
    trap2.rect.top = ALTO // 2


    #IMAGEN. BITCOIN
    imgCoin = pygame.image.load("bitcoin.png")
    coin = pygame.sprite.Sprite()
    coin.image = imgCoin
    coin.rect = imgCoin.get_rect()
    randomStartx3 = random.randint(0, ANCHO)
    coin.rect.left = randomStartx3
    coin.top = -300
    coin.rect.top = ALTO//2

    #PERSONAJE. GATO(derecho)
    randomStarty = random.randint(0,ALTO)
    imgCat = pygame.image.load("catright.png")
    cat = pygame.sprite.Sprite()
    cat.image = imgCat
    cat.rect = imgCat.get_rect()
    cat.rect.left = randomStartx
    cat.rect.top = randomStarty
    xCat = -200
    yCat = random.randint(0,ALTO)

    #Fondo durante juego
    imgPiso = pygame.image.load("floor.jpg")
    #Fondo Cuando Ganas
    imgWinner= pygame.image.load("winner.jpg")

    #SONIDO efecto al destruir un enemigo
    pygame.mixer.init()
    sound = pygame.mixer.Sound("chaching.wav")
    squ1 = pygame.mixer.Sound("squ1.wav")
    cattt= pygame.mixer.Sound("catsound.wav")
    winsound.PlaySound("SONG.wav", winsound.SND_ASYNC)
    #Pantalla BLANCA, letrero GANAS...
    puntos = 0      #   Naves destruidos
    fuente = pygame.font.SysFont("moonspace",60)
    direction = -150
    direction2 = 100
    direction3 = -600
    direction4 = 500
    bitC = 0
    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            if evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego ==MENU:
                    xbj, ybj, abj ,albj = spriteBtnJugar.rect
                    if xm >= xbj and xm<= xbj+abj:
                        if ym>= ybj and ym<=ybj + albj:
                            estadoJuego = JUEGO     #Cambia de estado

            if evento.type == pygame.KEYDOWN and estadoJuego == JUEGO:
                if evento.key == pygame.K_LEFT:
                    mouse.rect.left -= 60
                elif evento.key == pygame.K_RIGHT:
                    mouse.rect.left += 60
                elif evento.key == pygame.K_UP:
                    mouse.rect.top -= 60
                elif evento.key == pygame.K_DOWN:
                    mouse.rect.top += 60
                elif evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                        mouse.rect.left = 0
                if mouse.rect.left > ANCHO -70 or mouse.rect.left < -135 or mouse.rect.top > ALTO-100:
                    estadoJuego = CHOQUE


        # Borrar pantalla
        ventana.fill(NEGRO)
        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        if estadoJuego == MENU:
            ventana.blit(imgFondo,(0,0))
            ventana.blit(spriteBtnJugar.image,(spriteBtnJugar.rect))
        elif estadoJuego == JUEGO:
            Fondo = yFondo % imgPiso.get_rect().height
            ventana.blit(imgPiso, (0, Fondo - imgPiso.get_rect().height))
            if Fondo < ALTO:
                ventana.blit(imgPiso, (0, Fondo))
            yFondo += 5
            #dibujarBalas(ventana, listaBalas)
            font = pygame.font.SysFont("moonspace", 40)
            text = font.render("BitCoin en Pesos Mexicanos $" + str(bitC), True, YELLOW)
            ventana.blit(text, (0, 0))
            ventana.blit(mouse.image,mouse.rect)
            ventana.blit(imgCat,(xCat,randomStarty))
            #song.play()
            if xCat <= ANCHO:
                xCat += 10
            if xCat >= ANCHO:
                xCat = -200
                randomStarty = random.randint(0,ALTO)

            dibujarTrampa1(ventana, imgTrap, randomStartx, direction)
            if direction <= ALTO:
                direction += 8
            if direction >= 600:
                direction = -200
                randomStartx = random.randint(0,ANCHO)

            dibujarTrampa2(ventana, imgTrap2, randomStartx2, direction2)
            if direction2 <= ALTO:
                direction2 += 8
            if direction2 >= 600:
                direction2 = -200
                randomStartx2 = random.randint(0,ANCHO)

            #VerificaPUNTOS
            xm, ym, am, alm = mouse.rect
            xt, yt, at, alt = coin.rect
            yt = direction3
            xt = randomStartx3
            if xm >= xt and xm <= xt + at and ym >= yt and ym <= yt + alt:

                bitcollected = True
            elif xm + 75 >= xt and xm + 75 <= xt + at and ym >= yt and ym <= yt + alt:

                bitcollected = True
            elif xm + mousewidth >= xt and xm + mousewidth <= xt + at and ym >= yt and ym <= yt + alt:

                bitcollected = True
            else:
                bitcollected = False

            if bitcollected == False and ym >= yt:
                    dibujarMonedas(ventana, imgCoin, randomStartx3, direction3)
            if direction3 <= ALTO:
                direction3 += 8
            if direction3 >= ALTO:
                direction3 = -200
                randomStartx3 = random.randint(0,ANCHO)



            # Verificar Colisiones

            #checarColisionesBITCOIN(ventana,mouse,coin,yt,randomStartx3,direction3)
            checarColisionesBITCOIN(ventana, mouse, coin,imgCoin,randomStartx3, direction3)
            if checarColisionesBITCOIN(ventana, mouse, coin,imgCoin,randomStartx3, direction3) == True:
                sound.play()
                if pygame.mixer.get_busy() == True:
                    bitC +=float(179000.00)
            if bitC >= 1790000.00:
                estadoJuego = GANA
            checarColisionesTrampa1(mouse,trap,randomStartx,direction)
            if checarColisionesTrampa1(mouse,trap,randomStartx,direction) == True:
                squ1.play()
                estadoJuego = CHOQUE

            checarColisionesTrampa2(mouse,trap2,randomStartx2,direction2)
            if checarColisionesTrampa2(mouse,trap2,randomStartx2,direction2) == True:
                squ1.play()
                estadoJuego = CHOQUE

            checarColisionesGato(mouse,cat,xCat,randomStarty,cattt)
            if checarColisionesGato(mouse,cat,xCat,randomStarty,cattt) == True:
                estadoJuego = CHOQUE

        elif estadoJuego == GANA:
            #Texto GANA
            ventana.blit(imgWinner,(0,0))
            texto = fuente.render("¡Felicidades, eres millonario!",1,BLANCO)
            ventana.blit(texto, (ANCHO//2-380,25))
        elif estadoJuego == CHOQUE:
            ventana.blit(imgGameOver, (0, 0))
            texto = fuente.render("GAME OVER",1,NEGRO)
            ventana.blit(texto, (ANCHO//2-120,ALTO//2))
            texto1 = fuente.render("Juego creado por CORNEJO",1,NEGRO)
            ventana.blit(texto1, (ANCHO//4,550))
        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    dibujar()


main()
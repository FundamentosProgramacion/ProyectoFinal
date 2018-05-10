import pygame
import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 122)





# Estructura básica de un programa que usa pygame para dibujar
def crearEnemi(listaEnemi, imgEnemi1):
    for renglon in range(1, 8):  # 1..5
        for columna in range(7,10):

            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgEnemi1
            enemigo.rect = imgEnemi1.get_rect()
            enemigo.rect.left = columna * 60
            enemigo.rect.top = renglon * 70
            listaEnemi.append(enemigo)
#PC
def crearEnemi2(listaEnemi2, imgEnemi2):
    for renglon in range(1, 8):  # 1..5
        for columna in range(3,6):

            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgEnemi2
            enemigo.rect = imgEnemi2.get_rect()
            enemigo.rect.left = columna * 60
            enemigo.rect.top = renglon * 70
            listaEnemi2.append(enemigo)


# Dibuja Todos los discos del jugador sobre la ventana
def dibujarEnemi(ventana, listaEnemi):
    for enemigo in listaEnemi:
        ventana.blit(enemigo.image, enemigo.rect)

#PC
def dibujarEnemi2(ventana, listaEnemi2):
    for enemigo in listaEnemi2:
        ventana.blit(enemigo.image, enemigo.rect)


def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)



#Lista de balas
def actualizarBalas(listaBalas):
    # MOVER
    for bala in listaBalas:
        bala.rect.left -= 20
    # BORRAR   #NO usar iterador cuando borran datos de la lista
    for k in range(len(listaBalas) - 1, -1, -1):
        bala = listaBalas[k]
        if bala.rect.left <= bala.rect.width:
            listaBalas.remove(bala)
#PC
def actualizarBalas2(listaBalas2):
    # MOVER
    for bala in listaBalas2:
        bala.rect.left += 20
    # BORRAR   #NO usar iterador cuando borran datos de la lista
    for k in range(len(listaBalas2) - 1, -1, -1):
        bala = listaBalas2[k]
        if bala.rect.right <= (bala.rect.width-14):
            listaBalas2.remove(bala)

#Checa colisiones del juador
def checarcolisiones(listaBalas, listaEnemi):
    destruidos = 0

    for ib in range(len(listaBalas) - 1, -1, -1):
        bala = listaBalas[ib]
        for ie in range(len(listaEnemi) - 1, -1, -1):
            enemigo = listaEnemi[ie]
            xb, yb, ab, alb = bala.rect
            xe, ye, ae, ale = enemigo.rect
            if (xb >= xe and xb <= xe + ae and yb >= ye and yb  <= ye + ale) or (xb >= xe and xb <= xe + ae and (yb+alb) >= ye and (yb+alb)  <= ye + ale):
                listaBalas.remove(bala)
                listaEnemi.remove(enemigo)
                # listaEnemi[ie].image = imgEnemi #papa enseño a poner otra imagen
                destruidos += 1
                # efecto de sonido
                break
    return destruidos

def checarcolisiones2(listaBalas, Get):
    golpe = 0

    for ib in range(len(listaBalas) - 1, -1, -1):
        bala = listaBalas[ib]
        xb, yb, ab, alb = bala.rect
        xe, ye, ae, ale =Get
        if (xb >= xe and xb <= xe + ae and yb >= ye and yb  <= ye + ale) or (xb >= xe and xb <= xe + ae and (yb+alb) >= ye and (yb+alb)  <= ye + ale):
            listaBalas.remove(bala)
                # listaEnemi[ie].image = imgEnemi #papa enseño a poner otra imagen
            golpe += 1
                # efecto de sonido
            break
    return golpe


def quitarPuntos(puntos):
    menos= 21-puntos
    quitar= (menos*2)
    return quitar




def dibujar(nombreJugador):
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución


#IMG Cargadas
    imgFondo = pygame.image.load("MWfondo.png")
    imgBtnJugar = pygame.image.load("bPlay.png")
    imgMenu = pygame.image.load("bHow.png")
    imgInfo= pygame.image.load("bInfo.png")
    imgHero= pygame.image.load("bWin.png")
    imgCFondo = pygame.image.load("fondoRojo.jpg")
    imgHFondo= pygame.image.load("podio.jpg")
    imgIFondo = pygame.image.load("fondoRojo.jpg")



 #Boton menu
    spriteBtnJugar = pygame.sprite.Sprite()
    spriteBtnJugar.image = imgBtnJugar
    spriteBtnJugar.rect = imgBtnJugar.get_rect()  # rectangulo, (x,y),whith,height
    spriteBtnJugar.rect.left = ANCHO // 2 - spriteBtnJugar.rect.width // 2  # x
    spriteBtnJugar.rect.top = ALTO // 3 - spriteBtnJugar.rect.height // 2  # y

#Boton Como jugar
    spriteBtnMenu = pygame.sprite.Sprite()
    spriteBtnMenu.image = imgMenu
    spriteBtnMenu.rect = imgMenu.get_rect()
    spriteBtnMenu.rect.left = ANCHO//2 - spriteBtnMenu.rect.width // 2
    spriteBtnMenu.rect.top = (200 - spriteBtnJugar.rect.height // 2)+50
#Boton Info
    spriteBtnInfo = pygame.sprite.Sprite()
    spriteBtnInfo.image = imgInfo
    spriteBtnInfo.rect = imgMenu.get_rect()
    spriteBtnInfo.rect.left = 0
    spriteBtnInfo.rect.top = 556
#Boton mejores jugadores
    spriteBtnHero = pygame.sprite.Sprite()
    spriteBtnHero.image = imgHero
    spriteBtnHero.rect = imgMenu.get_rect()
    spriteBtnHero.rect.left = 684
    spriteBtnHero.rect.top = 556

 #Musica
    pygame.mixer.init()
    music = pygame.mixer.Sound("musicaFondo.wav")


    # Estados del juego
    MENU = 1
    JUEGO = 2
    COMOJUGAR = 3
    INFO= 5
    HERO= 6
    Gana = 4
    Nivel2= 7


    estadoJuego = MENU  # juego, menu

    # enemigos
    imgEnemi1 = pygame.image.load("GoldenD.png")
    listaEnemi = []
    crearEnemi(listaEnemi, imgEnemi1)
    imgEnemi2 = pygame.image.load("SilverD.png")
    listaEnemi2 = []
    crearEnemi2(listaEnemi2, imgEnemi2)

    # Soldado Nivel 1
    imgSol = pygame.image.load("Soldado.png")
    sold = pygame.sprite.Sprite()
    sold.image = imgSol
    sold.rect = imgSol.get_rect()
    sold.rect.right = ANCHO- sold.rect.width//2
    sold.rect.top = ALTO//2 - sold.rect.width//2

    # Soldado PC Nivel 1
    imgSol2 = pygame.image.load("Soldado2.png")
    sold2 = pygame.sprite.Sprite()
    sold2.image = imgSol2
    sold2.rect = imgSol2.get_rect()
    sold2.rect.right = 150
    sold2.rect.top = ALTO // 2 - sold2.rect.width // 2

    #GuitarMan Nivel 2


    imgGuita= pygame.image.load("Hero/hero0.png")
    Guita = pygame.sprite.Sprite()
    Guita.image = imgGuita
    Guita.rect = imgGuita.get_rect()
    Guita.rect.left = 550
    Guita.rect.top = ALTO // 2 - Guita.rect.width // 2

    imgGuitab = pygame.image.load("Hero/hero1.png")
    Guitab = pygame.sprite.Sprite()
    Guitab.image = imgGuitab
    Guitab.rect = imgGuitab.get_rect()
    Guitab.rect.left = 550
    Guitab.rect.top = ALTO // 2 - Guitab.rect.width // 2

    #GuitarManNivel 2
    imgGuita2 = pygame.image.load("Hero2/heroIzq0.png")
    Guita2 = pygame.sprite.Sprite()
    Guita2.image = imgGuita2
    Guita2.rect = imgGuita2.get_rect()
    Guita2.rect.left = 0
    Guita2.rect.top = ALTO // 2 - Guita2.rect.width // 2

    imgGuita2b = pygame.image.load("Hero2/heroIzq1.png")
    Guita2b = pygame.sprite.Sprite()
    Guita2b.image = imgGuita2b
    Guita2b.rect = imgGuita2b.get_rect()
    Guita2b.rect.left = 0
    Guita2b.rect.top = ALTO // 2 - Guita2b.rect.width // 2

    # Bala
    imgBala = pygame.image.load("balaNota.png")
    listaBalas = []  # Al inicio hay balas
    imgBala2 = pygame.image.load("balaNotaIzq.png")
    listaBalas2 = []  # Al inicio hay balas

    # Sonido


    # PantallaFin(gana)
    # Pantalla Blana, letrero ganas
    puntos = 0  # Enemi destruidos
    puntos2 = 0
    puntosVida=100
    puntosVidaPC=100
    JugadorGanador= 3
    fuente = pygame.font.SysFont("monospace", 76)
    fuente2 = pygame.font.SysFont("AgencyFB", 50)






    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            #Menu Teclas
            if evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego == MENU:
                    xbi, ybi, abi, albi= spriteBtnInfo.rect
                    xbh, ybh, abh, albh= spriteBtnHero.rect
                    xbm, ybm, abm, albm= spriteBtnMenu.rect
                    xbj, ybj, abj, albj = spriteBtnJugar.rect  # xBtnJugar, y , ancho, alto
                    if xm >= xbj and xm <= xbj + abj:
                        if ym >= ybj and ym <= ybj + albj:
                            estadoJuego = JUEGO
                    if xm >= xbm and xm <= xm + abm:
                        if ym >= ybm and ym <= ybm + albm:
                            estadoJuego = INFO

                    elif xm >= xbi and xm <= xbi + abi:
                        if ym >= ybi and ym <= ybi + albi:
                            estadoJuego = INFO
                    elif xm >= xbh and xm <= xbh + abh:
                        if ym >= ybh and ym <= ybh + albh:
                            estadoJuego = HERO

            #Juego Nivel 1 teclas

            if evento.type == pygame.KEYDOWN and estadoJuego == JUEGO:
                if (evento.key == pygame.K_UP) and sold.rect.top >= 0:
                        sold.rect.top -= 15
                elif (evento.key == pygame.K_DOWN) and sold.rect.top <= 518:
                        sold.rect.top += 15
                elif evento.key == pygame.K_LEFT:
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = sold.rect.left - 5
                    bala.rect.top = sold.rect.top + 15
                    listaBalas.append(bala)

            #Juego Nivel 2
            if evento.type == pygame.KEYDOWN and estadoJuego == Nivel2:
                if evento.key == pygame.K_LEFT:
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = Guita.rect.left - bala.rect.width
                    bala.rect.top = Guita.rect.top+ 50
                    listaBalas.append(bala)

        # Borrar pantalla
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)

        # Menu
        if estadoJuego == MENU:
            ventana.blit(imgFondo, (0, 0))
            ventana.blit(spriteBtnJugar.image, spriteBtnJugar.rect)
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
            ventana.blit(spriteBtnInfo.image, spriteBtnInfo.rect)
            ventana.blit(spriteBtnHero.image, spriteBtnHero.rect)

        #Juego Nivel 1
        elif estadoJuego == JUEGO:
            music.play()
            nombre = fuente2.render(nombreJugador, 1, BLANCO)
            ventana.blit(nombre, (500, 40))
            PC = fuente2.render("PC", 1, BLANCO)
            ventana.blit(PC, (100, 40))
            dibujarEnemi(ventana, listaEnemi)
            dibujarBalas(ventana, listaBalas)
            dibujarEnemi2(ventana, listaEnemi2)

            ventana.blit(sold.image, sold.rect)
            ventana.blit(sold2.image, sold2.rect)

            #MOVIMIENTO SOLDADO PC
            accion= random.randint(0,10)
            if (accion == 0 or accion== 3 or accion== 6 ) and sold2.rect.top >= 0:
                sold2.rect.top -= 15
            elif (accion== 1 or accion== 4 or accion== 7 )and sold2.rect.top <= 518:
                sold2.rect.top += 15
            elif accion == 2 or accion== 10 or accion== 9:
                bala2 = pygame.sprite.Sprite()
                bala2.image = imgBala2
                bala2.rect = imgBala2.get_rect()
                bala2.rect.left = sold2.rect.right - 5
                bala2.rect.top = sold2.rect.top + 15
                listaBalas2.append(bala2)

            dibujarBalas(ventana, listaBalas2)
            # Actualizar
            actualizarBalas(listaBalas)
            actualizarBalas2(listaBalas2)
            # verificarclisiones
            destruidos = checarcolisiones(listaBalas, listaEnemi)
            destruidos2 = checarcolisiones(listaBalas2, listaEnemi2)
            puntos += destruidos
            puntos2 += destruidos2
            if puntos >= 21:
                JugadorGanador= 0
                menos = quitarPuntos(puntos2)
                puntosVida = puntosVida + menos
                estadoJuego = Gana  # termina por que gana
            elif puntos2>= 21:
                JugadorGanador = 1

                menos= quitarPuntos(puntos)
                puntosVidaPC= puntosVidaPC + menos
                estadoJuego = Gana
            elif puntos>= 21 and puntos2>=21:
                estadoJuego = Gana


        #Juego Nivel 2
        elif estadoJuego == Nivel2:

            #Lineas de Vida
            nombre = fuente2.render(nombreJugador, 1, BLANCO)
            ventana.blit(nombre, (500, 40))
            PC = fuente2.render("PC", 1, BLANCO)
            ventana.blit(PC, (100, 40))
            pygame.draw.line(ventana,VERDE,(100,100),((100+puntosVida),100),20)
            pygame.draw.line(ventana, VERDE, (501, 100), ((500+puntosVidaPC), 100),20)

            ventana.blit(Guita.image, Guita.rect)
            ventana.blit(Guita2.image, Guita2.rect)
            dibujarBalas(ventana, listaBalas)
            actualizarBalas(listaBalas)

            puntosMenos = checarcolisiones2(listaBalas,  Guita.rect)
            puntosMenos2 = checarcolisiones2(listaBalas2,  Guita2.rect)

            puntosVida= puntosVida-puntosMenos2
            puntosVidaPC = puntosVidaPC - puntosMenos

            if puntosVida== 0:
                JugadorGanador = 0
                estadoJuego= Gana
            elif puntosVidaPC== 0:
                JugadorGanador = 1
                estadoJuego = Gana






        elif estadoJuego == Gana:
            music.stop()
            if JugadorGanador== 1:
                 # texto gana
                texto = fuente.render(("Gano Jugador"), 1, BLANCO)
                ventana.blit(texto, (ANCHO // 2 - 200, ALTO // 2))
                salida = open("hero.txt", "w", encoding='UTF-8')
                lineaSalida = "%s,%s" % (nombreJugador, puntosVida)
                salida.write(lineaSalida)
                salida.write("\n")
                salida.close()

            elif JugadorGanador== 2:
                 # texto gana
                texto = fuente.render("Gano PC", 1, BLANCO)
                ventana.blit(texto, (ANCHO // 2 - 200, ALTO // 2))

        elif estadoJuego == COMOJUGAR:

            # texto COMO JUGAR
            ventana.blit(imgCFondo, (0, 0))
            texto = fuente.render("¡Como jugar, dispara con flecha izq\n muevete con flechas arriba y abajo!", 1, BLANCO)
            ventana.blit(texto, (ANCHO // 2 - 400, ALTO // 2))
        elif estadoJuego == INFO:

            # texto INFO
            ventana.blit(imgIFondo, (0, 0))
            texto = fuente.render("Mirna Zertuche\n A01373852", 1, BLANCO)
            ventana.blit(texto, (ANCHO // 2 - 200, ALTO // 2))
        elif estadoJuego == HERO:
            ventana.blit(imgHFondo, (0, 0))
            entrada = open("hero.txt", "r", encoding='UTF-8')

            # leer lineaxlinea
            linea = entrada.readline()
            while linea != "":
                print(linea)
            entrada.close()


        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    nombreJugador= input("Nombre de Jugador: ")
    dibujar(nombreJugador)



main()
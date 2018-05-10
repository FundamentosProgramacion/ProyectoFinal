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
def formatearNombre(datos):
    nombre= datos[0]
    return nombre

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
            if ((xb >= xe and xb <= xe + ae and yb >= ye and yb  <= ye + ale) or (xb >= xe and xb <= xe + ae and (yb+alb) >= ye and (yb+alb)  <= ye + ale)):
                listaBalas.remove(bala)
                listaEnemi.remove(enemigo)
                # listaEnemi[ie].image = imgEnemi #papa enseño a poner otra imagen
                destruidos += 1
            elif xb in range(390, 410):
                listaBalas.remove(bala)

                # efecto de sonido
                break
    return destruidos

def checarcolisiones2(listaBalas, get):
    golpe = 0

    for ib in range(len(listaBalas) - 1, -1, -1):
        bala = listaBalas[ib]
        xb, yb, ab, alb = bala.rect
        xe, ye, ae, ale = get
        if (xb >= xe and xb <= (xe + ae)-ab and yb >= ye and yb  <= ye + ale) or (xb >= xe and xb <= (xe + ae)-ab and (yb+alb) >= ye and (yb+alb)  <= ye + ale):
            listaBalas.remove(bala)
                # listaEnemi[ie].image = imgEnemi #papa enseño a poner otra imagen
            golpe += 1
                # efecto de sonido
            break
    return golpe
def checarcolisiones3(listaBalas, get):
    golpe = 0

    for ib in range(len(listaBalas) - 1, -1, -1):
        bala = listaBalas[ib]
        xb, yb, ab, alb = bala.rect
        xe, ye, ae, ale = get
        print(xe)
        print(ye)
        print(ae)
        print(ale)
        if (xb >= xe+145 and xb <= 750 and yb >= ye and yb  <= ye + ale) or (xb >= xe+145  and xb <= 750  and (yb+alb) >= ye and (yb+alb)  <= ye + ale):
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


def puntaje(datos):
    Puntos = datos[1]
    return Puntos


def crearLista(datos):
    listaPuntajes=[]
    puntaje= int(datos)
    listaPuntajes.append(puntaje)
    listaPuntajes.sort()
    return listaPuntajes


def checarMejores(Puntaje, listaPuntaje):
    if Puntaje == listaPuntaje[0] or Puntaje == listaPuntaje[1] or Puntaje == listaPuntaje[3]:
        return True
    else:
        return False


def crearListaBest(nombre, Puntaje):
    listaBest=[]
    listaBest.append(nombre)
    listaBest.append(Puntaje)
    return listaBest


def dibujar(nombreJugador):
    # Inicializa el motor de pygame
    pygame.mixer.pre_init(44100,16,2,4096)
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
    imgbMenu = pygame.image.load("bHome.png")
    imgCFondo = pygame.image.load("fondoRojo.jpg")
    imgHFondo= pygame.image.load("podio.jpg")
    imgIFondo = pygame.image.load("fondoRojo.jpg")



 #Boton Jugar
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
    spriteBtnInfo.rect = imgInfo.get_rect()
    spriteBtnInfo.rect.left = 0
    spriteBtnInfo.rect.top = 556
#Boton mejores jugadores
    spriteBtnHero = pygame.sprite.Sprite()
    spriteBtnHero.image = imgHero
    spriteBtnHero.rect = imgHero.get_rect()
    spriteBtnHero.rect.left = 684
    spriteBtnHero.rect.top = 556
#Botn a Menu
    spriteBtnHome = pygame.sprite.Sprite()
    spriteBtnHome.image = imgbMenu
    spriteBtnHome.rect = imgMenu.get_rect()
    spriteBtnHome.rect.left = 766
    spriteBtnHome.rect.top = 556

 #Musica




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
    Guita.rect.right = 550+ Guita.rect.width // 2
    Guita.rect.top = ALTO // 2 - Guita.rect.width // 2

    imgGuitab = pygame.image.load("Hero/hero1.png")
    Guitab = pygame.sprite.Sprite()
    Guitab.image = imgGuitab
    Guitab.rect = imgGuitab.get_rect()
    Guitab.rect.left = 550- Guita.rect.width // 2
    Guitab.rect.top = ALTO // 2 - Guitab.rect.width // 2

    #GuitarManNivel 2
    imgGuita2 = pygame.image.load("Hero2/heroIzq0.png")
    Guita2 = pygame.sprite.Sprite()
    Guita2.image = imgGuita2
    Guita2.rect = imgGuita2.get_rect()
    Guita2.rect.right = 150 +Guita.rect.width // 2
    Guita2.rect.top = ALTO // 2 - Guita2.rect.width // 2

    imgGuita2b = pygame.image.load("Hero2/heroIzq1.png")
    Guita2b = pygame.sprite.Sprite()
    Guita2b.image = imgGuita2b
    Guita2b.rect = imgGuita2b.get_rect()
    Guita2b.rect.left = - Guita2b.rect.width // 2
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
    fuente3 = pygame.font.SysFont("AgencyFB", 25)






    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                if JugadorGanador == 1:
                    salida = open("PUNTAJE.txt", "a", encoding='UTF-8')
                    lineaSalida = "%s,%s" % (nombreJugador, puntosVida)
                    salida.write(lineaSalida)
                    salida.write("\n")
                    salida.close()
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
                            estadoJuego = COMOJUGAR

                    if xm >= xbi and xm <= xbi + abi:
                        if ym >= ybi and ym <= ybi + albi:
                            estadoJuego = INFO

                    if xm >= xbh and xm <= xbh + abh:
                        if ym >= ybh and ym <= ybh + albh:
                            estadoJuego = HERO
                if estadoJuego == HERO or estadoJuego == INFO or estadoJuego == COMOJUGAR or estadoJuego == JUEGO or estadoJuego == Nivel2 or estadoJuego == Gana:
                    xbo, ybo, abo, albo = spriteBtnHome.rect
                    if xm >= xbo and xm <= xbo + abo:
                        if ym >= ybo and ym <= ybo + albo:
                            estadoJuego = MENU




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
                    bala.rect.top = Guita.rect.top+ 75
                    listaBalas.append(bala)

        # Borrar pantalla
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)

        # Menu
        if estadoJuego == MENU:
            pygame.mixer.music.load('SNA.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            ventana.blit(imgFondo, (0, 0))
            ventana.blit(spriteBtnJugar.image, spriteBtnJugar.rect)
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
            ventana.blit(spriteBtnInfo.image, spriteBtnInfo.rect)
            ventana.blit(spriteBtnHero.image, spriteBtnHero.rect)

        #Juego Nivel 1
        elif estadoJuego == JUEGO:

            dibujarEnemi(ventana, listaEnemi)
            dibujarBalas(ventana, listaBalas)
            dibujarEnemi2(ventana, listaEnemi2)

            ventana.blit(sold.image, sold.rect)
            ventana.blit(sold2.image, sold2.rect)
            ventana.blit(spriteBtnHome.image, spriteBtnHome.rect)

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

                menos = quitarPuntos(puntos2)
                puntosVidaPC = puntosVidaPC - menos
                estadoJuego = Nivel2  # termina por que gana
            elif puntos2>= 21:

                menos= quitarPuntos(puntos)
                puntosVida= puntosVida - menos
                estadoJuego = Nivel2
            elif puntos>= 21 and puntos2>=21:
                estadoJuego = Nivel2


        #Juego Nivel 2
        elif estadoJuego == Nivel2:



            #Lineas de Vida
            nombre = fuente2.render(nombreJugador, 1, BLANCO)
            ventana.blit(nombre, (500, 40))
            PC = fuente2.render("PC", 1, BLANCO)
            ventana.blit(PC, (100, 40))
            pygame.draw.line(ventana, ROJO, (100, 100), ((200), 100), 20)
            pygame.draw.line(ventana, ROJO, (490, 100), ((590), 100), 20)
            pygame.draw.line(ventana,VERDE,(100,100),((100+puntosVidaPC),100),20)
            pygame.draw.line(ventana, VERDE, (490, 100), ((490+puntosVida), 100),20)

            ventana.blit(Guita.image, Guita.rect)
            ventana.blit(Guita2.image, Guita2.rect)
            dibujarBalas(ventana, listaBalas)
            actualizarBalas(listaBalas)
            ventana.blit(spriteBtnHome.image, spriteBtnHome.rect)


            accion2= random.randint(0,30)
            if accion2== 10 or accion2== 20 or accion2 == 30:
                bala2 = pygame.sprite.Sprite()
                bala2.image = imgBala2
                bala2.rect = imgBala2.get_rect()
                bala2.rect.left = Guita2.rect.right - 5
                bala2.rect.top = Guita2b.rect.top + 15
                listaBalas2.append(bala2)
            dibujarBalas(ventana, listaBalas2)
            # Actualizar
            actualizarBalas(listaBalas)
            actualizarBalas2(listaBalas2)


            puntosMenos = checarcolisiones2(listaBalas,  Guita2.rect)
            puntosMenos2 = checarcolisiones3(listaBalas2,  Guita.rect)

            puntosVida= puntosVida-puntosMenos2
            puntosVidaPC = puntosVidaPC - puntosMenos

            if puntosVida== 0:
                JugadorGanador = 0
                estadoJuego= Gana
            elif puntosVidaPC== 0:
                JugadorGanador = 1
                estadoJuego = Gana






        elif estadoJuego == Gana:
            ventana.blit(spriteBtnHome.image, spriteBtnHome.rect)
            pygame.mixer.music.stop()
            if JugadorGanador== 1:
                 # texto gana
                texto = fuente.render(("Gano Jugador"), 1, BLANCO)
                ventana.blit(texto, (ANCHO // 2 - 200, ALTO // 2))

            elif JugadorGanador== 0:
                 # texto gana
                texto = fuente.render("Gano PC", 1, BLANCO)
                ventana.blit(texto, (ANCHO // 2 - 200, ALTO // 2))

        elif estadoJuego == COMOJUGAR:


            # texto COMO JUGAR
            ventana.blit(imgCFondo, (0, 0))
            ventana.blit(spriteBtnHome.image, spriteBtnHome.rect)
            texto = fuente2.render("Como jugar: dispara con flecha izquierda", 1, BLANCO)
            texto1 = fuente2.render("muevete con flechas arriba y abajo", 1,
                                    BLANCO)
            texto2 = fuente2.render("¡DIVIERTETE!", 1,
                                    BLANCO)
            ventana.blit(texto, (0, ALTO // 2-100))
            ventana.blit(texto1, (0, ALTO // 2))
            ventana.blit(texto2, (0, ALTO // 2+100))

        elif estadoJuego == HERO:

            entrada = open("PUNTAJE.txt", "r", encoding='UTF-8')
            linea = entrada.readline()
            while linea != "":
                datos = linea.split(",")
                nombre = formatearNombre(datos)
                Puntaje = puntaje(datos)
                listaPuntaje = crearLista(Puntaje)
                Mejor = checarMejores(Puntaje,listaPuntaje)
                if Mejor == True:
                    listaNombrePuntos= crearListaBest(nombre,Puntaje)
                    texto = fuente2.render((listaNombrePuntos[0],listaNombrePuntos[1]), 1, BLANCO)
                    texto1 = fuente2.render((listaNombrePuntos[2],listaNombrePuntos[3]), 1, BLANCO)
                    texto2 = fuente2.render((listaNombrePuntos[4],listaNombrePuntos[5]), 1, BLANCO)
                    ventana.blit(texto, (ANCHO//2, ALTO // 2 - 100))
                    ventana.blit(texto1, (ANCHO//2, ALTO // 2))
                    ventana.blit(texto2, (ANCHO//2, ALTO // 2 + 100))
                if Mejor == False:
                    texto2 = fuente2.render("No eres parte de los mejores", 1, BLANCO)
                    ventana.blit(texto2, (ANCHO // 2, ALTO // 2 + 100))
            salida.close()

            # texto INFO


        elif estadoJuego == INFO:
            ventana.blit(imgIFondo, (0, 0))
            ventana.blit(spriteBtnHome.image, spriteBtnHome.rect)
            texto = fuente2.render("Mirna Zertuche", 1, BLANCO)
            texto1 = fuente2.render(" A01373852", 1, BLANCO)
            texto2 = fuente2.render("Fundamentos de la programación", 1, BLANCO)
            ventana.blit(texto, (0, ALTO // 2 - 100))
            ventana.blit(texto1, (0, ALTO // 2))
            ventana.blit(texto2, (0, ALTO // 2 + 100))




        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    nombreJugador= input("Nombre de Jugador: ")
    dibujar(nombreJugador)



main()
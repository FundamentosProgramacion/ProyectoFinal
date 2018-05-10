# Autor: Andrés Reyes Rangel.
# Reproduce el juego de space invaders.

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)


# Movimiento enemigos
Derecha = True
Bajar = False
ayudita = 0
nlineas = 0

# Crea 60 enemigos en la lista
def crearEnemigos(listaEnemigos, imgEnemigo):
    for columna in range(1,13): # 1...12
        for renglon in range(1,8): # 1..5
            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgEnemigo
            enemigo.rect = imgEnemigo.get_rect()
            enemigo.rect.left = columna*58
            enemigo.rect.top = renglon*60
            listaEnemigos.append(enemigo)



def dibujarEnemigos(ventana, listaEnemigos):
    global Bajar, Derecha, estadoJuego, PIERDE
    PIERDE = 5
    for enemigo in listaEnemigos:
        if Bajar:
            enemigo.rect.top += 20
        if Derecha:
            enemigo.rect.left += 2
        else:
            enemigo.rect.left -= 2
    Bajar = False
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)
        xe, ye, ae, ale = enemigo.rect
        if xe == 0:
            Derecha = True
            Bajar = True
        if xe == ANCHO - ae:
            Derecha = False
            Bajar = True
        if ye >= ALTO - ale:
            estadoJuego = PIERDE


def dibujarBalas(ventana, listaBala):
    for bala in listaBala:
        ventana.blit(bala.image, bala.rect)


def actualizarBalas(listaBala):
    # MOVER BALAS
    for bala in listaBala:
        bala.rect.top -= 5
    # NO USAR ITERADOR CUANDO BORRO DATOS DE UNA LISTA
    # BORRAR
    for k in range(len(listaBala)-1, -1,-1):
        bala = listaBala[k]
        if bala.rect.top <= - bala.rect.height:
            listaBala.remove(bala)


def checarColisiones(listaBala, listaEnemigos):
    destruidos = 0
    for iB in range(len(listaBala)-1, -1, -1):
        bala = listaBala[iB]
        for iE in range(len(listaEnemigos)-1,-1,-1):
            enemigo = listaEnemigos[iE]
            xb, yb, ab, alb = bala.rect
            xe, ye, ae, ale = enemigo.rect
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + ale:
                listaBala.remove(bala)
                listaEnemigos.remove(enemigo)
                # CONTAR ENEMIGOS DESTRUIDOS
                destruidos += 1
                break
    return destruidos


def checarColisionNave(listaEnemigos, nave):
    destruidos = 0
    for iE in range(len(listaEnemigos) - 1, -1, -1):
        enemigo = listaEnemigos[iE]
        xn, yn, an, aln = nave.rect
        xe, ye, ae, ale = enemigo.rect
        if xn <= xe + ae <= xn + an:
            if yn <= ye <= yn + aln:
                listaEnemigos.remove(enemigo)
                # CONTAR ENEMIGOS DESTRUIDOS
                destruidos += 1
    return destruidos


# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    imgFondo = pygame.image.load("fondoMenu.png")
    imgFondoJuego = pygame.image.load("fondoEspacio.png")
    imgFondoPerdiste = pygame.image.load("fondoPerdiste.jpg")
    imgBtnJugar = pygame.image.load("Boton_jugar.png")
    imgBtnAyuda = pygame.image.load("Boton_Ayuda.png")
    imgBtnVolver = pygame.image.load("Boton_Volver.png")
    imgBtnMenu = pygame.image.load("Boton_Menu.png")
    imgBtnSalir = pygame.image.load("Boton_Salir.png")


    spriteBtnSalir = pygame.sprite.Sprite()
    spriteBtnSalir.image = imgBtnSalir
    spriteBtnSalir.rect = imgBtnSalir.get_rect()
    spriteBtnSalir.rect.left = 680
    spriteBtnSalir.rect.top = 550

    spriteBtnJugar = pygame.sprite.Sprite()
    spriteBtnJugar.image = imgBtnJugar
    spriteBtnJugar.rect = imgBtnJugar.get_rect()
    spriteBtnJugar.rect.left = 50
    spriteBtnJugar.rect.top = 500

    spriteBtnAyuda = pygame.sprite.Sprite()
    spriteBtnAyuda.image = imgBtnAyuda
    spriteBtnAyuda.rect = imgBtnAyuda.get_rect()
    spriteBtnAyuda.rect.left = 370
    spriteBtnAyuda.rect.top = 500

    spriteBtnVolver = pygame.sprite.Sprite()
    spriteBtnVolver.image = imgBtnVolver
    spriteBtnVolver.rect = imgBtnVolver.get_rect()
    spriteBtnVolver.rect.left = 570
    spriteBtnVolver.rect.top = 550

    spriteBtnMenu = pygame.sprite.Sprite()
    spriteBtnMenu.image = imgBtnMenu
    spriteBtnMenu.rect = imgBtnMenu.get_rect()
    spriteBtnMenu.rect.left = 550
    spriteBtnMenu.rect.top = 1

    # Estados
    MENU = 1
    JUEGO = 2
    AYUDA = 3
    GANA = 4
    PIERDE = 5
    estadoJuego = MENU

    # ENEMIGOS
    imgEnemigo = pygame.image.load("enemigoAbajo.png")
    listaEnemigos = []
    crearEnemigos(listaEnemigos, imgEnemigo)

    # PERSONAJE.NAVE
    imgNave = pygame.image.load("nave.png")
    nave = pygame.sprite.Sprite()
    nave.image = imgNave
    nave.rect = imgNave.get_rect()
    nave.rect.left = ANCHO // 2 - nave.rect.width // 2
    nave.rect.top = ALTO - nave.rect.height

    # PROYECTILES
    imgBala = pygame.image.load("bala.png")
    listaBala = []  # Al inicio  no hay balas

    # SONIDO AL DESTRUIR UN ENEMIGO
    pygame.mixer.init()
    efectoDestruye = pygame.mixer.Sound("shoot.wav")
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play()

    # PANTALLA FIN (GANA)
    # PANTALLA BLANCA, LETRERO GANAS...
    puntos = 0  # Naves destruidas
    fuente = pygame.font.SysFont("monospaced", 70)

    # TEXTO AYUDA
    ayudita = 0
    nlineas = 0

    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            if evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego == MENU:
                    xbj, ybj, abj, albj = spriteBtnJugar.rect
                    xba, yba, aba, alba = spriteBtnAyuda.rect
                    if xbj <= xm <= xbj + abj:
                        if ybj <= ym <= ybj+albj:
                            estadoJuego = JUEGO  # Cambia de estado
                    elif xba <= xm <= xba + aba:
                        if yba <= ym <= yba + alba:
                            estadoJuego = AYUDA
            if evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego == PIERDE or estadoJuego == GANA:
                    xbv, ybv, abv, albv = spriteBtnSalir.rect
                    if xbv <= xm <= xbv + abv:
                        if ybv <= ym <= ybv + albv:
                            termina = True
            if evento.type == pygame.KEYDOWN and estadoJuego == JUEGO:
                xn, yn, an, aln = nave.rect
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                    if xn > 0:
                        nave.rect.left -= 20
                elif evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                    if xn + an < ANCHO:
                        nave.rect.left += 20
                elif evento.key == pygame.K_UP or evento.key == pygame.K_SPACE or evento.key == pygame.K_w: # DISPARA
                    efectoDestruye.play()
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = nave.rect.left + nave.rect.width//2
                    bala.rect.top = nave.rect.top + bala.rect.height//4
                    listaBala.append(bala)
            if evento.type == pygame.KEYDOWN and estadoJuego == AYUDA:
                if evento.key == pygame.K_UP and ayudita > 0:
                    ayudita -= 1
                if evento.key == pygame.K_DOWN and ayudita < nlineas - 1:
                    ayudita += 1
            if evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego == AYUDA:
                    xbm, ybm, abm, albm = spriteBtnMenu.rect
                    if xbm <= xm <= xbm + abm:
                        if ybm <= ym <= ybm + albm:
                            estadoJuego = MENU

        # Borrar pantalla
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)

        if estadoJuego == MENU:
            ventana.blit(imgFondo, (0,0))
            ventana.blit(spriteBtnJugar.image, spriteBtnJugar.rect)
            ventana.blit(spriteBtnAyuda.image, spriteBtnAyuda.rect)
        elif estadoJuego == JUEGO:
            ventana.blit(imgFondoJuego, (0,0))
            dibujarEnemigos(ventana, listaEnemigos)
            dibujarBalas(ventana, listaBala)
            ventana.blit(nave.image, nave.rect)
            # ACTUALIZACIÓN
            actualizarBalas(listaBala)
            # VERIFICAR COLISIONES
            destruidos = checarColisiones(listaBala, listaEnemigos)
            naveDestruida = checarColisionNave(listaEnemigos, nave)
            puntos += destruidos
            if puntos >= 84:
                estadoJuego = GANA  # TERMINA EL JUEGO, GANA
            elif naveDestruida == 1:
                estadoJuego = PIERDE
            texto = fuente.render("Puntuación: " + str(puntos), 1, BLANCO) # MUESTRA EN LA PANTALLA LA PUNTUACIÓN DEL USUARIO.
            ventana.blit(texto, (0,0))
        elif estadoJuego == GANA:
            ventana.blit(imgFondoPerdiste, (0, 0))
            ventana.blit(spriteBtnSalir.image, spriteBtnSalir.rect)
            # TEXTO GANA
            texto = fuente.render("¡FELICIDADES HAS GANADO!", 1, BLANCO)
            ventana.blit(texto, (55,270))
        elif estadoJuego == PIERDE:
            ventana.blit(imgFondoPerdiste, (0, 0))
            ventana.blit(spriteBtnSalir.image, spriteBtnSalir.rect)
            texto = fuente.render("¡GAME OVER!", 1, ROJO)
            texto2 = fuente.render("PUNTUACION: " + str(puntos), 1, ROJO)
            ventana.blit(texto2, (220,350))
            ventana.blit(texto, (240, 270))
        elif estadoJuego == AYUDA:
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
            # Archivo para poner las instrucciones
            nlineas = len(open('ayuda.txt').readlines())
            ayuda = open("ayuda.txt", "r", encoding="UTF-8")
            ayuda.seek(0)
            for i in range(0,ayudita):
                ayuda.readline()
            linea = ayuda.readline()
            cadena = linea.split(",")
            y = 70
            for i in range(0,len(cadena)):
                texto = fuente.render(cadena[i], 1, BLANCO)
                ventana.blit(texto, (10, y))
                y += 40
            texto = fuente.render(str(ayudita + 1) + " / " + str(nlineas), 1, BLANCO)
            ventana.blit(texto, (ANCHO - 100, ALTO - 40))
            ayuda.close()


        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    dibujar()


main()
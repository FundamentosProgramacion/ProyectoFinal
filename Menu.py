# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

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


# Estructura básica de un programa que usa pygame para dibujar

# Crea 60 enemigos y los agrega a la lista
def crearEnemigos(listaEnemigos, imgEnemigo):
    for renglon in range(1,6):  # 1..5
        for columna in range(1,13): # 1..12
            enemigo = pygame.sprite.Sprite()
            enemigo.image = imgEnemigo
            enemigo.rect = imgEnemigo.get_rect()
            enemigo.rect.left = columna*58
            enemigo.rect.top = renglon*60
            listaEnemigos.append(enemigo)


# Dibuja TODOS los enemigos sobre la ventana
def dibujarEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)


def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def actualizarBalas(listaBalas):
    # MOVER
    for bala in listaBalas:
        bala.rect.top -= 20

    # BORRAR. No USAR iterador cuando borran datos de la lista
    for k in range(len(listaBalas)-1, -1, -1):  # al revés
        bala = listaBalas[k]
        if bala.rect.top <= - bala.rect.height:
            listaBalas.remove(bala)


def checarColisiones(listaBalas, listaEnemigos, efecto):
    destruidos = 0
    for iB in range(len(listaBalas)-1, -1, -1):
        bala = listaBalas[iB]
        for iE in range(len(listaEnemigos)-1, -1, -1):
            enemigo = listaEnemigos[iE]
            xb, yb, ab, alb = bala.rect
            xe, ye, ae, ale = enemigo.rect
            if xb>=xe and xb<=xe+ae and yb>=ye and yb<=ye+ale:
                listaBalas.remove(bala)
                listaEnemigos.remove(enemigo)
                # Contarlo
                destruidos += 1
                # efecto de sonido
                efecto.play()
                break

    return destruidos

def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    # Imágenes
    imgFondo = pygame.image.load("fondoMenu.jpg")
    imgBtnJugar = pygame.image.load("jugar.png")
    imgBtnAcercaDe = pygame.image.load("acercaDe.png")

    spriteBtnJugar = pygame.sprite.Sprite()
    spriteBtnJugar.image = imgBtnJugar
    spriteBtnJugar.rect = imgBtnJugar.get_rect()
    spriteBtnJugar.rect.left = ANCHO//2 - spriteBtnJugar.rect.width//2
    spriteBtnJugar.rect.top = ALTO//3 - spriteBtnJugar.rect.height//2

    spriteBtnAcercaDe = pygame.sprite.Sprite()
    spriteBtnAcercaDe.image = imgBtnAcercaDe
    spriteBtnAcercaDe.rect = imgBtnAcercaDe.get_rect()
    spriteBtnAcercaDe.rect.left = ANCHO//2 - spriteBtnAcercaDe.rect.width//2
    spriteBtnAcercaDe.rect.top = 2*ALTO//3

    # ESTADOS del juego
    MENU = 1
    JUEGO = 2
    ACERCA_DE = 3
    GANA = 4
    estadoJuego = MENU      # JUEGO, ACERCA_DE

    # ENEMIGOS
    imgEnemigo = pygame.image.load("enemigoAbajo.png")
    listaEnemigos = []
    crearEnemigos(listaEnemigos, imgEnemigo)

    # Personaje. NAVE
    imgNave = pygame.image.load("nave.png")
    nave = pygame.sprite.Sprite()
    nave.image = imgNave
    nave.rect = imgNave.get_rect()
    nave.rect.left = ANCHO//2
    nave.rect.top = ALTO - nave.rect.height

    # BALAS
    imgBala = pygame.image.load("bala.png")
    listaBalas = []     # Al inicio no hay balas

    # SONIDO efecto al destruir un enemigo
    pygame.mixer.init()
    efectoDestruye = pygame.mixer.Sound("shoot.wav")

    # Pantalla FIN (Gana)
    # Pantalla BLANCA, letrero GANAS...
    puntos = 0      # Naves destruidas
    fuente = pygame.font.SysFont("monospace", 76)


    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego == MENU:
                    xbj, ybj, abj, albj = spriteBtnJugar.rect
                    if xm>=xbj and xm<=xbj+abj:
                        if ym>=ybj and ym<=ybj+albj:
                            estadoJuego = JUEGO # Cambia de estado
            if evento.type == pygame.KEYDOWN and estadoJuego==JUEGO:
                if evento.key == pygame.K_LEFT:
                    nave.rect.left -= 10
                elif evento.key == pygame.K_RIGHT:
                    nave.rect.left += 10
                elif evento.key == pygame.K_SPACE:
                    # dispara
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = nave.rect.left + nave.rect.width//2
                    bala.rect.top = nave.rect.top
                    listaBalas.append(bala)

        # Borrar pantalla
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        if estadoJuego == MENU:
            ventana.blit(imgFondo, (0,0))
            ventana.blit(spriteBtnJugar.image, spriteBtnJugar.rect)
            ventana.blit(spriteBtnAcercaDe.image, spriteBtnAcercaDe.rect)
        elif estadoJuego == JUEGO:
            dibujarEnemigos(ventana, listaEnemigos)
            dibujarBalas(ventana, listaBalas)
            ventana.blit(nave.image, nave.rect)
            # Actualizar
            actualizarBalas(listaBalas)
            # Verificar colisiones
            destruidos = checarColisiones(listaBalas, listaEnemigos, efectoDestruye)
            puntos += destruidos
            if puntos >= 3:
                estadoJuego = GANA     # termina el juego, GANA
        elif estadoJuego == GANA:
            # Texto GANA
            texto = fuente.render("¡GANASTE!",1,BLANCO)
            ventana.blit(texto, (ANCHO//2-200,ALTO//2))

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    dibujar()


main()
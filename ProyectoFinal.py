import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
Imagenes=2
TiempoFrames=0.1
TiempoTotal=Imagenes*TiempoFrames


#Crea al personaje
def crearListaSprites():
    lista = []
    for i in range (Imagenes):
        nombre = "Sprite/Sprite-" + str (i) + ".png"
        imagen = pygame.image.load (nombre)
        spriteAnimacion = pygame.sprite.Sprite ()
        spriteAnimacion.image = imagen
        spriteAnimacion.rect = imagen.get_rect ()
        spriteAnimacion.rect.left = ANCHO - 780
        spriteAnimacion.rect.top = ALTO / 1.25
        lista.append (spriteAnimacion)
    return lista


#Crea el tiempo en que las imágenes se cambian y crean la animación
def obtenerFrame(timerAnimacion, listaSprites):
    indice = int (timerAnimacion /TiempoFrames)
    return listaSprites[indice]

#Delimita al jugador de solo moverse en cierto espacio
def moverJugador(dx, listaSprites):

    for k in listaSprites:
        if k.rect.left > 10 and k.rect.left + k.rect.width < 790:
            if k.rect.left + dx > 10 and k.rect.left + dx + k.rect.width < 790:
                listaSprites[0].rect.left += dx
                listaSprites[1].rect.left += dx
#Dibuja los items
def generarChilaquil(listaItems, imgItems):
    cx = randint (20, ANCHO - 128)
    cy = 0
    chilaquil = pygame.sprite.Sprite ()
    chilaquil.image = imgItems
    chilaquil.rect = imgItems.get_rect ()
    chilaquil.rect.left = cx
    chilaquil.rect.top = cy
    listaItems.append (chilaquil)

#Dibuja los enemigos
def generarSesentaynueve(lista69, img69):
    cx = randint (20, ANCHO - 128)
    cy = 0
    sesentaynueve = pygame.sprite.Sprite ()
    sesentaynueve.image = img69
    sesentaynueve.rect = img69.get_rect ()
    sesentaynueve.rect.left = cx
    sesentaynueve.rect.top = cy
    lista69.append (sesentaynueve)
#Hace que el chilaquil caiga
def caerChilaquil(listaItems):

    for chilaquil in (listaItems):
        chilaquil.rect.top += 10
        if chilaquil.rect.top < 0:
            listaItems.remove (chilaquil)
#Hace que el 69 caiga
def caersesentanueve(lista69):
    for sesentaynueve in (lista69):
        sesentaynueve.rect.top += 10
        if sesentaynueve.rect.top < 0:
            lista69.remove (sesentaynueve)
#Dibuja el chilaquil y el 69
def dibujarJuego(ventana, listaObstaculos, lista69):
    for enemigo in listaObstaculos:
        ventana.blit (enemigo.image, enemigo.rect)

    for k in lista69:
        ventana.blit (k.image, k.rect)


#Hace las colisiones del personaje y los 69's
def hacerColisionesEnemigo(listaSprites,lista69):
    destruidos = 0
    for iB in range ( len ( listaSprites)):
        bala = listaSprites[iB]
        for iE in range ( len ( lista69) ):
            enemigo = lista69[iE]
            xb, yb, ab, alb = bala.rect
            xe, ye, ae, ale = enemigo.rect
            if xb > xe and xb <= xe + ae and yb >= ye and yb <= ye + ale:
                lista69.remove ( enemigo )
                destruidos += 1
    return destruidos
#Hace las colisiones del personaje y  el chilaquil
def hacerColisionesItem(listaSprites,listaItems):
    puntuacion = 0
    for i in range ( len ( listaSprites)):
        Sprite = listaSprites[i]
        for k in range ( len ( listaItems) ):
            chilaquil = listaItems[k]
            xb, yb, ab, alb = Sprite.rect
            xe, ye, ae, ale = chilaquil.rect
            if xb > xe and xb <= xe + ae and yb >= ye and yb <= ye + ale:
                listaItems.remove ( chilaquil )
                puntuacion += 1
    return puntuacion

# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Inicializa el motor de pygame
    pygame.init ()
    ventana = pygame.display.set_mode ( (ANCHO, ALTO) )  # Crea la ventana de dibujo
    reloj = pygame.time.Clock ()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución
    # estados
    Menu = 1
    Jugando = 2
    Informacion = 3
    Gana = 4
    Pierde = 5
    estado = Menu
    # Animación
    listaSprites = crearListaSprites()
    timerAnimacion = 0
    #Movimiento
    x=0
    mover = False
    #puntaje
    puntos = 0
    reprobado=0

    #Fuente
    fuente = pygame.font.SysFont ( "monospace", 54 )
    # Imágenes
    # Fondo
    Fondo = pygame.image.load ( "Fondojuego.png" )
    informacion=pygame.image.load ("Informacion.jpg" )
    FondoJuego = pygame.image.load ( "Fondo2.jpg" )
    FondoGana=pygame.image.load("BogoAzul.png")
    FondoPierde=pygame.image.load("Perder.jpg")
    # Botón Jugar
    Jugar = pygame.image.load ( "button_jugar.png" )
    botonJugar = pygame.sprite.Sprite ()
    botonJugar.image = Jugar
    botonJugar.rect = Jugar.get_rect ()
    botonJugar.rect.left = ANCHO // 2 - botonJugar.rect.width // 2
    botonJugar.rect.top = ALTO // 2 - botonJugar.rect.height // 2
    # Botón información
    Info = pygame.image.load ( "button_informacion.png" )
    botonInformacion = pygame.sprite.Sprite ()
    botonInformacion.image = Info
    botonInformacion.rect = Info.get_rect ()
    botonInformacion.rect.left = ANCHO // 2 - botonJugar.rect.width / 2.5
    botonInformacion.rect.top = ALTO / (1.3) - botonJugar.rect.height // 3
    # Botón atrás
    botonAtras = pygame.image.load ( "button_atras.png" )
    Atras = pygame.sprite.Sprite ()
    Atras.image = botonAtras
    Atras.rect = botonAtras.get_rect ()
    Atras.rect.left = ANCHO // (40)
    Atras.rect.top = 0
    #Botón regresar menú
    botonMenu= pygame.image.load ( "button_menu.png" )
    Men = pygame.sprite.Sprite ()
    Men.image = botonMenu
    Men.rect = botonAtras.get_rect ()
    Men.rect.left = ANCHO // (40)
    Men.rect.top = 0
    #Enemigo
    lista69=[]
    imgEnemigo=pygame.image.load("Enemigo.png")
    generarSesentaynueve(lista69,imgEnemigo)

    #Items
    listaItems=[]
    imgItems=pygame.image.load("Item.png")
    generarChilaquil(listaItems,imgItems)




    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get ():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos ()
                if estado == Menu:
                    xb, yb, anchoB, altoB = botonInformacion.rect
                if xm >= xb and xm <= xb + anchoB:
                    if ym >= yb and ym <= yb + altoB:
                        estado=Informacion
                        if estado==Informacion:
                            xb, yb, anchoB, altoB = Atras.rect
                        if xm >= xb and xm <= xb + anchoB:
                            if ym >= yb and ym <= yb + altoB:
                                estado = Menu
                if estado == Menu:
                    xb, yb, anchoB, altoB = botonJugar.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            estado = Jugando
                if estado == Jugando:
                    xb, yb, anchoB, altoB = Men.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            estado = Menu







            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_RIGHT:
                    x = 10

                    mover = True

                if evento.key == pygame.K_LEFT:
                    x = -10

                    mover = True

            elif evento.type == pygame.KEYUP:

                if evento.key == pygame.K_RIGHT:
                    mover = False

                if evento.key == pygame.K_LEFT:
                    mover = False

        # Borrar pantalla
        ventana.fill ( BLANCO )

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        if estado == Menu:
            ventana.blit ( Fondo, (0, 0) )
            ventana.blit ( botonJugar.image, botonJugar.rect )
            ventana.blit ( botonInformacion.image, botonInformacion.rect )

        elif estado== Informacion:
            ventana.blit(informacion,(0,0))
            ventana.blit ( Atras.image, Atras.rect )



        elif estado==Jugando:
            ventana.blit(FondoJuego,(0,0))
            frameActual = obtenerFrame ( timerAnimacion, listaSprites)
            ventana.blit ( frameActual.image, frameActual.rect )
            ventana.blit(Men.image,Men.rect)
            dibujarJuego ( ventana, listaItems, lista69 )
            if mover:
                moverJugador ( x, listaSprites )

            if puntos<1 :
                caersesentanueve(lista69)
                caerChilaquil(listaItems)
            puntuacion=hacerColisionesItem(listaSprites,listaItems)
            reprobar=hacerColisionesEnemigo(listaSprites,lista69)
            puntos += puntuacion
            reprobado+=reprobar

            if puntos >= 1:
                estado = Gana

            elif reprobado>=1:
                estado=Pierde


        elif estado==Gana:
            ventana.blit(FondoGana,(0,0))

        elif estado==Pierde:
            ventana.blit(FondoPierde,(0,0))

        pygame.display.flip ()  # Actualiza trazos
        timerAnimacion += reloj.tick ( 40 ) / 1000
        if timerAnimacion >= TiempoTotal:
            timerAnimacion = 0
        reloj.tick ( 40 )  # 40 fps

    # Después del ciclo principal
    pygame.quit ()  # termina pygame


def main():
    dibujar ()


main ()

# Fernando Sebastian Silva Miramontes
# DK Elevator

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

BLANCO = (255, 255, 255)


# Dibuja las plataformas
def dibujarPlataformas(ventana, lista):
    for plataforma in lista:
        ventana.blit(plataforma.image, plataforma.rect)


# Crea una lista con las posiciones de las plataformas
def crearListaPlataformas(imgPlataformas, lista):
    for altura in range(600, 0, -300):
        plataforma = pygame.sprite.Sprite()
        plataforma.image = imgPlataformas
        plataforma.rect = imgPlataformas.get_rect()
        plataforma.rect.left = 100
        plataforma.rect.top = altura - plataforma.rect.height
        lista.append(plataforma)


def lugarCanon(imgcanon, ventana, plataforma):
    for cuenta in range(1, 3):
        canon = pygame.sprite.Sprite()
        canon.image = imgcanon
        canon.rect = imgcanon.get_rect()
        if cuenta == 1:
            canon.rect.left = 700 - canon.rect.width
            canon.rect.top = (600 - plataforma.rect.height) - canon.rect.height
            ventana.blit(canon.image, canon.rect)
        else:
            canon.rect.left = 100
            canon.rect.top = (600 - plataforma.rect.height) - 300 - canon.rect.height
            ventana.blit(canon.image, canon.rect)


def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    # EDOS DE JUEGO
    MENU = 1
    ACERCA_DE = 2
    JUEGO = 3
    PUNTAJES = 4
    estadoJuego = JUEGO

    # PLATAFORMAS
    imgPlataformas = pygame.image.load("plataforma_Alfa.png")
    plataforma = pygame.sprite.Sprite()
    plataforma.image = imgPlataformas
    plataforma.rect = imgPlataformas.get_rect()
    listaPlataformas = []

    # PERSONAJE
    imgPersonaje = pygame.image.load("Personaje_Alfa.png")
    personaje = pygame.sprite.Sprite()
    personaje.image = imgPersonaje
    personaje.rect = imgPersonaje.get_rect()
    personaje.rect.left = 150
    personaje.rect.top = (600 - plataforma.rect.height) - personaje.rect.height

    # CAÑON
    imgcanon = pygame.image.load("canon_Alfa.png")

    # ESCALERA
    imgescalera = pygame.image.load("escaleras_Alfa.png")
    escalera = pygame.sprite.Sprite()
    escalera.image = imgescalera
    escalera.rect = imgescalera.get_rect()
    escalera.rect.left = 550
    escalera.rect.top = (600 - plataforma.rect.height) - escalera.rect.height

    # BOOLEANOS
    moverPersonajeD = False
    moverPersonajeL = False
    estaSaltando = False
    puedeEscalar = False
    estaEscalando = False
    subeEscalera = False
    bajaEscalera = False

     # Timer de fps
    pygame.time.set_timer(pygame.USEREVENT+1, 25)

    #Contador
    contador = 0



    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            if estadoJuego == JUEGO:
                # Revisa si la tecla especifica ESTA siendo presionada
                if evento.type == pygame.KEYDOWN:
                    #Para Movimiento X
                    if evento.key == pygame.K_LEFT:
                        moverPersonajeL = True
                    elif evento.key == pygame.K_RIGHT:
                        moverPersonajeD = True
                    #Para el salto
                    elif evento.key == pygame.K_SPACE and not estaSaltando:
                        estaSaltando = True
                        contador = 0
                        y0 = personaje.rect.bottom
                    # Para Movimiento escalera
                    elif evento.key == pygame.K_UP and puedeEscalar:
                        estaEscalando = True
                        subeEscalera = True
                    elif evento.key == pygame.K_DOWN and puedeEscalar:
                        estaEscalando = True
                        bajaEscalera = True


                # Revisa si la tecla especifica NO ESTA siendo presionada
                elif evento.type == pygame.KEYUP:
                    #Para movimiento X
                    if evento.key == pygame.K_LEFT:
                        moverPersonajeL = False
                    elif evento.key == pygame.K_RIGHT:
                        moverPersonajeD = False
                    # Para Movimiento Y en Escalera
                    elif evento.key == pygame.K_UP and estaEscalando:  # -OJO-  BUG DE ESCALERA INFINITA
                        subeEscalera = False
                    elif evento.key == pygame.K_DOWN and puedeEscalar:
                        bajaEscalera = False

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Fondos y Estados en el Que esta el Juego
        edoDeJuego = JUEGO
        # BUSCAR FONDO Y BOTONES!!!!
        if edoDeJuego == MENU:
            pass
        if edoDeJuego == JUEGO:
            # Creacion de las  Plataformas
            crearListaPlataformas(imgPlataformas, listaPlataformas)
            dibujarPlataformas(ventana, listaPlataformas)

            # Dibujo de Cañon
            lugarCanon(imgcanon, ventana, plataforma)  # Es una funcion para vers. ALFA.. Ponerlos manuales?

            # Dibujo de Escaleras
            ventana.blit(escalera.image, escalera.rect)
            areaMediaEscalera = escalera.rect.left+20, escalera.rect.left+40

            # Dibujo de personaje
            ventana.blit(personaje.image, personaje.rect)
            mitadPersonaje = (personaje.rect.left + personaje.rect.right)/2



            # Revisa si el presonaje esta en posicion de escalar
            if mitadPersonaje in range(areaMediaEscalera[0], areaMediaEscalera[1]) and not estaSaltando:
                puedeEscalar = True
            if personaje.rect.bottom == escalera.rect.top or personaje.rect.bottom == escalera.rect.bottom:
                estaEscalando = False
            if subeEscalera and not personaje.rect.bottom == escalera.rect.top:
                personaje.rect.bottom -= 2
            if bajaEscalera and not personaje.rect.bottom == escalera.rect.bottom:
                personaje.rect.bottom += 2
            if estaEscalando:
                personaje.rect.left = escalera.rect.left
                moverPersonajeL = False
                moverPersonajeD = False

            if personaje.rect.bottom == escalera.rect.top:
                puedeEscalar = False

            # Movimiento del personaje Derecha izquierda
            if moverPersonajeL:
                personaje.rect.left -= 3
            if moverPersonajeD:
                personaje.rect.left += 3

            #Utiliza la ecacion de fisica para calcular su altura en un momento determinado. Cuanta con Gravedad y Vo
            if estaSaltando:
                moveVertical = 4.1097*contador-.5*0.25*contador**2 # goriginal = .221 VO original = 4.99
                personaje.rect.bottom = y0 - int(moveVertical)
                if y0 < personaje.rect.bottom:
                    personaje.rect.bottom = y0
                    estaSaltando = False

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps
        contador += 1


    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    dibujar()


main()

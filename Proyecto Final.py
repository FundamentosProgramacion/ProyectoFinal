# Fernando Sebastian Silva Miramontes
# DK Elevator

import pygame


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

BLANCO = (255,255,255)

# Dibuja las plataformas
def dibujarPlataformas(ventana, lista):
    for plataforma in lista:
        ventana.blit(plataforma.image, plataforma.rect)


# Crea una lista con las posiciones de las plataformas
def crearListaPlataformas (imgPlataformas, lista):
    for altura in range(600, -1 , -300):
        plataforma = pygame.sprite.Sprite()
        plataforma.image = imgPlataformas
        plataforma.rect = imgPlataformas.get_rect()
        plataforma.rect.left = 100
        plataforma.rect.top = altura - plataforma.rect.height
        lista.append(plataforma)


def lugarCanon(imgcanon, ventana, plataforma):
    for cuenta in range(1,3):
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

    #PLATAFORMAS
    imgPlataformas = pygame.image.load("plataforma_Alfa.png")
    plataforma = pygame.sprite.Sprite()
    plataforma.image = imgPlataformas
    plataforma.rect = imgPlataformas.get_rect()
    listaPlataformas =[]

    #PERSONAJE
    imgPersonaje = pygame.image.load("Personaje_Alfa.png")
    personaje = pygame.sprite.Sprite()
    personaje.image = imgPersonaje
    personaje.rect = imgPersonaje.get_rect()
    personaje.rect.left = 150
    personaje.rect.top = (600-plataforma.rect.height) - personaje.rect.height

    #CAÑON
    imgcanon = pygame.image.load("canon_Alfa.png")


    #ESCALERA
    imgescalera = pygame.image.load("escaleras_Alfa.png")
    escalera = pygame.sprite.Sprite()
    escalera.image = imgescalera
    escalera.rect = imgescalera.get_rect()
    escalera.rect.left = 550
    escalera.rect.top = (600 - plataforma.rect.height) - escalera.rect.height




    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Fondos y Estados en el Que esta el Juego
        edoDeJuego = JUEGO
        # BUSCAR FONDO Y BOTONES
        if edoDeJuego == MENU:
            pass
        if edoDeJuego == JUEGO:
            # Creacion de las  Plataformas
            crearListaPlataformas(imgPlataformas, listaPlataformas)
            dibujarPlataformas(ventana, listaPlataformas)

            # Dibujo de Cañon
            lugarCanon(imgcanon, ventana, plataforma) # Es una funcion para vers. ALFA

            # Dibujo de Escaleras
            ventana.blit(escalera.image, escalera.rect)

            # Dibujo de personaje
            ventana.blit(personaje.image, personaje.rect)





        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    dibujar()


main()
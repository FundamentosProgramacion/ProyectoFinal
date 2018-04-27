#Karla Fabiola Ramirez Martinez
#Proyecto final, Videojuego Apple Rush

import pygame
import math
import random
# Dimensiones de la pantalla
ANCHO = 800
ALTO =600


# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)

reloj = pygame.time.Clock()
def crearManzanas(listaManzana, imgManzana,cantidad):
    contador = 0
    for manzanita in range(1,cantidad):  # 1..5



        manzana = pygame.sprite.Sprite()
        manzana.image = imgManzana
        manzana.rect = imgManzana.get_rect()
        manzana.rect.left = manzanita*(random.randint(1,40))
        numeroR=random.randint(0,3000)
        manzana.rect.top = 0 - numeroR

        listaManzana.append(manzana)
        contador += 1

    return listaManzana

# Dibuja TODOS los enemigos sobre la ventana
def dibujarManzanas(ventana, listaManzana):
    for manzana in listaManzana:
        ventana.blit(manzana.image, manzana.rect)





def actualizarManzanas(listaManzana,imgManzana,):
    # MOVER
    contador=0
    for manzana in listaManzana:
        manzana.rect.top += random.randint(1,8)
  #REVISAR EL CICLO QUE INTENTABAS HACER PERO VALIO CHETO
    # BORRAR. No USAR iterador cuando borran datos de la lista
    for k in range(len(listaManzana)-1, -1, -1):  # al revés
        manzana = listaManzana[k]


        if 800+manzana.rect.top <= -(800+ manzana.rect.height):
            listaManzana.remove(manzana)



# de momento no hace nada , hay que ver como actualziarla con el juego que haras
def checarColisiones(listaManzana, canasta):
    atrapadas = 0
    for iB in range(len(listaManzana)-1, -1, -1):
        apple = listaManzana[iB]
        xb, yb, ab, alb = canasta.rect
        xe, ye, ae, ale = apple.rect
        if xe>=xb-ae+5 and xe+ae<=xb+ab+ae-5 and yb>=ye and yb<=ye+ale:
            listaManzana.remove(apple)

                # Contarlo

                # efecto de sonido




def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    # Imágenes/Fondo
    imgFondo = pygame.image.load("Menu.png")
    imgBtnJugar = pygame.image.load("button_jugar.png")
    imgBtnAcercaDe = pygame.image.load("button_instrucciones.png")
    imgBtnCreditos= pygame.image.load("button_creditos.png")
    imgBtnPuntajes=pygame.image.load("button_puntajes.png")
    imgBtnTitulo=pygame.image.load("Titulo.png")
    imgBtnVolver=pygame.image.load("VolverMenu.png")
    imgBtnInst=pygame.image.load("InInstrucc.png")


#Imagen pantalla ganar
    imgPersonajeGanar=pygame.image.load("PantallaGanar.png")
#Boton jugar
    spriteBtnJugar = pygame.sprite.Sprite()
    spriteBtnJugar.image = imgBtnJugar
    spriteBtnJugar.rect = imgBtnJugar.get_rect()
    spriteBtnJugar.rect.left = ANCHO-180 - spriteBtnJugar.rect.width//2
    spriteBtnJugar.rect.top = ALTO//3 - spriteBtnJugar.rect.height+80+10
#Boton de instrucciones/pendiente cambiar nombre
    spriteBtnAcercaDe = pygame.sprite.Sprite()
    spriteBtnAcercaDe.image = imgBtnAcercaDe
    spriteBtnAcercaDe.rect = imgBtnAcercaDe.get_rect()
    spriteBtnAcercaDe.rect.left = ANCHO-180 - spriteBtnAcercaDe.rect.width//2
    spriteBtnAcercaDe.rect.top = 2*ALTO//3-50-10-10-15-2
#Para el sprite de creditos
    spriteBtnCreditos = pygame.sprite.Sprite()
    spriteBtnCreditos.image = imgBtnCreditos
    spriteBtnCreditos.rect = imgBtnCreditos.get_rect()
    spriteBtnCreditos.rect.left = ANCHO - 180 - spriteBtnCreditos.rect.width // 2
    spriteBtnCreditos.rect.top =ALTO // 3 - spriteBtnCreditos.rect.height // 2+350
#Para el sprite de puntajes
    spriteBtnPuntajes = pygame.sprite.Sprite()
    spriteBtnPuntajes.image = imgBtnPuntajes
    spriteBtnPuntajes.rect = imgBtnPuntajes.get_rect()
    spriteBtnPuntajes.rect.left = ANCHO - 180 - spriteBtnPuntajes.rect.width // 2
    spriteBtnPuntajes.rect.top =  ALTO // 3 - spriteBtnPuntajes.rect.height // 2 +250

#Para el titulo
    spriteBtnTitulo = pygame.sprite.Sprite()
    spriteBtnTitulo.image = imgBtnTitulo
    spriteBtnTitulo.rect = imgBtnTitulo.get_rect()
    spriteBtnTitulo.rect.left = ANCHO - 180 - spriteBtnTitulo.rect.width // 2-20
    spriteBtnTitulo.rect.top = ALTO // 3 - spriteBtnTitulo.rect.height-40

#Boton de volver
    spriteBtnVolver = pygame.sprite.Sprite()
    spriteBtnVolver.image = imgBtnVolver
    spriteBtnVolver.rect = imgBtnVolver.get_rect()
    spriteBtnVolver.rect.left = ANCHO - spriteBtnVolver.rect.width
    spriteBtnVolver.rect.top = 600 - spriteBtnVolver.rect.height
#Instrucciones dentro de intrucciones
    spriteBtnInst = pygame.sprite.Sprite()
    spriteBtnInst.image = imgBtnInst
    spriteBtnInst.rect = imgBtnInst.get_rect()
    spriteBtnInst.rect.left = ANCHO - spriteBtnInst.rect.width-40
    spriteBtnInst.rect.top = 40 + spriteBtnInst.rect.height

#TExtos
    fuente = pygame.font.SysFont("meiryomeiryomeiryouimeiryouiitalic", 60)

    # ESTADOS del juego

    MENU = 1
    JUEGO = 2
    INSTRUCCIONES = 3
    GANA = 4
    PIERDE=5
    CREDITOS=6
    PUNTAJES=7
    estadoJuego = MENU
    # JUEGO, ACERCA_DE

  #Todos los objetos dentro del juego


    # Manzanas
    imgManzana = pygame.image.load("M.png")
    imgManzanaP=pygame.image.load("MP.png")
    listaManzana = []
    listaManzanaP= []
    crearManzanas(listaManzana,imgManzana,1000)
    crearManzanas(listaManzanaP, imgManzanaP,20)
    # Personaje. Canasta
    imgCanasta = pygame.image.load("Canasta.png")

    canasta = pygame.sprite.Sprite()
    canasta.image = imgCanasta
    canasta.rect = imgCanasta.get_rect()
    canasta.rect.left = ANCHO // 2
    canasta.rect.top = ALTO - canasta.rect.height
    movercanasta= False


#PEGA QUI LO QUE quitaste


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

            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego == MENU:
                    xbj, ybj, abj, albj = spriteBtnAcercaDe.rect
                    if xm >= xbj and xm <= xbj + abj:
                        if ym >= ybj and ym <= ybj + albj:
                            estadoJuego = INSTRUCCIONES
            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego == INSTRUCCIONES:
                    xbj, ybj, abj, albj = spriteBtnVolver.rect
                    if xm >= xbj and xm <= xbj + abj:
                        if ym >= ybj and ym <= ybj + albj:
                            estadoJuego = MENU

            if evento.type == pygame.KEYDOWN and estadoJuego==JUEGO:
                if evento.key == pygame.K_LEFT:
                    longitud=-10
                    movercanasta= True


                if evento.key == pygame.K_RIGHT:
                    longitud=10
                    movercanasta = True
            if evento.type==pygame.KEYUP:
                movercanasta= False



        # Borrar pantalla
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        if estadoJuego == MENU:
            ventana.blit(imgFondo, (0,-150))
            ventana.blit(spriteBtnJugar.image, spriteBtnJugar.rect)
            ventana.blit(spriteBtnAcercaDe.image, spriteBtnAcercaDe.rect)
            ventana.blit(spriteBtnCreditos.image, spriteBtnCreditos.rect)
            ventana.blit(spriteBtnPuntajes.image, spriteBtnPuntajes.rect)
            ventana.blit(spriteBtnTitulo.image, spriteBtnTitulo.rect)
        elif estadoJuego == JUEGO:
            if movercanasta:
                canasta.rect.left += longitud
            ventana.blit(canasta.image, canasta.rect)
            dibujarManzanas(ventana, listaManzana)

            actualizarManzanas(listaManzana,imgManzana,)
            checarColisiones(listaManzana, canasta)

            dibujarManzanas(ventana, listaManzanaP)
            actualizarManzanas(listaManzanaP, imgManzanaP)
            checarColisiones(listaManzanaP,canasta)
        elif estadoJuego==INSTRUCCIONES:
            ventana.blit(imgPersonajeGanar, (0, -150))
            ventana.blit(spriteBtnInst.image, spriteBtnInst.rect)

            ventana.blit(spriteBtnVolver.image, spriteBtnVolver.rect)


            # Actualizar

            # Verificar colisiones
            #Estado juego pegar lo que quitaste


        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    dibujar()


main()
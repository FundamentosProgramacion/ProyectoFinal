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

def moreApples(ventana,tiempo,listaManzana,imgManzana,cantidad):
    contador=0
    while tiempo>=10:
        contador+=1
        if contador%15==0:

            newlist=crearManzanas(listaManzana, imgManzana, cantidad)
    return  newlist




def creaCreditos(ventana,lista):
    fuente = pygame.font.SysFont("meiryomeiryomeiryouimeiryouiitalic", 14)
    xOrigen=80
    yOrigen=100

    for dato in lista:
        datox=fuente.render(dato,1,BLANCO)
        ventana.blit(datox, (xOrigen, yOrigen))
        yOrigen+=30



def calcularPuntos(puntos,numero):
    Puntos=len(puntos)
    score=Puntos*numero
    return score







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


def puntosTotal(puntosM,puntosMP):
    puntos = puntosM - (puntosMP)
    return puntos

# Dibuja TODOS los enemigos sobre la ventana
def dibujarManzanas(ventana, listaManzana):
    for manzana in listaManzana:
        ventana.blit(manzana.image, manzana.rect)





def actualizarManzanas(listaManzana,imgManzana):
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


#Funcion que trasnforma los creditos a string
def regresarCreditos(archivo):
    listaCreditos=[]
    entrada = open(archivo, "r",encoding="UTF-8")
    for linea in entrada:
        lineax=linea.rstrip("\n")
        listaCreditos.append(lineax)

    entrada.close()
    return listaCreditos





# de momento no hace nada , hay que ver como actualziarla con el juego que haras
def checarColisiones(listaManzana,canasta,puntos):


    for iB in range(len(listaManzana)-1, -1, -1):
        apple = listaManzana[iB]
        xb, yb, ab, alb = canasta.rect
        xe, ye, ae, ale = apple.rect

        if xe>=xb-ae+5 and xe+ae<=xb+ab+ae-5 and yb>=ye and yb<=ye+ale:
            listaManzana.remove(apple)
            puntos.append(1)
                # Contarlo

                # efecto de sonido




def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución
#Timer



    # Imágenes/Fondo
    imgFondo = pygame.image.load("Menu.png")
    imgFondoJuego = pygame.image.load("fondoJuego.jpg")
    imgBtnJugar = pygame.image.load("button_jugar.png")
    imgBtnAcercaDe = pygame.image.load("button_instrucciones.png")
    imgBtnCreditos= pygame.image.load("button_creditos.png")
    imgBtnPuntajes=pygame.image.load("button_puntajes.png")
    imgBtnTitulo=pygame.image.load("Titulo.png")
    imgBtnVolver=pygame.image.load("VolverMenu.png")
    imgBtnInst=pygame.image.load("InInstrucc.png")
    imgBtnTCreditos= pygame.image.load("TCreditos.png")
    imgBtnPerdiste=pygame.image.load("button_perdiste.png")
    imgBtnGanaste=pygame.image.load("button_ganaste.png")
    imgBtnPuntaje=pygame.image.load("button_puntajeTitulo.png")
#Sonido
    pygame.mixer.init()
    cancionFondoJuego = pygame.mixer.Sound("Cancion.mp3")
    cancionMenu=pygame.mixer.Sound("Menu.wav")



#Imagen pantalla ganar
    imgPersonajeGanar=pygame.image.load("PantallaGanar.png")
    imgPerder=pygame.image.load("Perder.png")
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
    spriteBtnTitulo.rect.left = ANCHO - 180 - spriteBtnTitulo.rect.width // 2-20-5
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
    spriteBtnInst.rect.top = 20 + spriteBtnInst.rect.height
#Titulo de creditos
    spriteBtnTCreditos = pygame.sprite.Sprite()
    spriteBtnTCreditos.image = imgBtnTCreditos
    spriteBtnTCreditos.rect = imgBtnTCreditos.get_rect()
    spriteBtnTCreditos.rect.left = ANCHO//2 -spriteBtnTCreditos.rect.width
    spriteBtnTCreditos.rect.top = 30

#Boton ganaste
    spriteBtnPerdiste = pygame.sprite.Sprite()
    spriteBtnPerdiste.image = imgBtnPerdiste
    spriteBtnPerdiste.rect = imgBtnPerdiste.get_rect()
    spriteBtnPerdiste.rect.left = ANCHO // 2 - spriteBtnPerdiste.rect.width+150
    spriteBtnPerdiste.rect.top = 30
#Boton perdiste
    spriteBtnGanaste = pygame.sprite.Sprite()
    spriteBtnGanaste .image = imgBtnGanaste
    spriteBtnGanaste .rect = imgBtnGanaste .get_rect()
    spriteBtnGanaste .rect.left = ANCHO // 2 - spriteBtnGanaste .rect.width+300
    spriteBtnGanaste .rect.top = 30

#Titulo en puntajes
    spriteBtnPuntaje = pygame.sprite.Sprite()
    spriteBtnPuntaje.image = imgBtnPuntaje
    spriteBtnPuntaje.rect = imgBtnPuntaje.get_rect()
    spriteBtnPuntaje.rect.left = ANCHO - 180 - spriteBtnPuntaje.rect.width // 2
    spriteBtnPuntaje.rect.top = ALTO // 3 - spriteBtnPuntaje.rect.height // 2 + 250
#TExtos
    fuente = pygame.font.SysFont("meiryomeiryomeiryouimeiryouiitalic", 18)

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
#Se que de esta manera no es la mas eficeinte , sin embargo no me salia de otra manera para generar el tiempo en las que se
    #generaban todas las manzana TwT

    listaNew=[]
    crearManzanas(listaNew, imgManzana, 900)
    listaN2=[]
    crearManzanas(listaN2, imgManzana, 700)
    listaN3 = []
    crearManzanas(listaN3, imgManzana, 900)
    listaN4 = []
    crearManzanas(listaN4, imgManzana, 900)
    listaN5 = []
    crearManzanas(listaN5, imgManzana, 300)
    listaN6 = []
    crearManzanas(listaN6, imgManzana, 900)
    listaN7 = []
    crearManzanas(listaN7, imgManzana, 900)
    #POISON
    listaNewP = []
    crearManzanas(listaNew, imgManzanaP, 200)
    listaN2P = []
    crearManzanas(listaN2, imgManzanaP, 50)
    listaN3P = []
    crearManzanas(listaN3, imgManzanaP, 10)
    listaN4P = []
    crearManzanas(listaN4, imgManzanaP, 20)
    listaN5P = []
    crearManzanas(listaN5, imgManzanaP, 40)
    listaN6P = []
    crearManzanas(listaN6, imgManzanaP, 90)
    listaN7P = []
    crearManzanas(listaN7, imgManzanaP, 10)



    #Manzanas para instrucciones
    # Manzanas
    manzana = pygame.sprite.Sprite()
    manzana.image = imgManzana
    manzana.rect = imgManzana.get_rect()
    manzana.rect.left = 400
    manzana.rect.top = 480
    manzanaP = pygame.sprite.Sprite()
    manzanaP.image = imgManzanaP
    manzanaP.rect = imgManzanaP.get_rect()
    manzanaP.rect.left = 400
    manzanaP.rect.top = 420
    # Personaje. Canasta
    imgCanasta = pygame.image.load("Canasta.png")

    canasta = pygame.sprite.Sprite()
    canasta.image = imgCanasta
    canasta.rect = imgCanasta.get_rect()
    canasta.rect.left = ANCHO // 2
    canasta.rect.top = ALTO - canasta.rect.height
    movercanasta= False
    #Lista para los puntos
    puntos=[]
    puntosP=[]

    puntosT=[]
    puntosX=[]
    puntosY=[]
    puntosZ=[]
    puntosA=[]
    puntosB=[]
    puntosC=[]


    puntosTP = []
    puntosXP= []
    puntosYP = []
    puntosZP = []
    puntosAP = []
    puntosBP = []
    puntosCP = []



    #Timers
    counter, text = 3250, '3250'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

    timeri = 105


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
                if estadoJuego == MENU:
                    xbj, ybj, abj, albj = spriteBtnCreditos.rect
                    if xm >= xbj and xm <= xbj + abj:
                        if ym >= ybj and ym <= ybj + albj:
                            estadoJuego = CREDITOS
            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego == MENU:
                    xbj, ybj, abj, albj = spriteBtnPuntajes.rect
                    if xm >= xbj and xm <= xbj + abj:
                        if ym >= ybj and ym <= ybj + albj:
                            estadoJuego = PUNTAJES
            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego == CREDITOS:
                    xbj, ybj, abj, albj = spriteBtnVolver.rect
                    if xm >= xbj and xm <= xbj + abj:
                        if ym >= ybj and ym <= ybj + albj:
                            estadoJuego = MENU
            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego == PUNTAJES:
                    xbj, ybj, abj, albj = spriteBtnVolver.rect
                    if xm >= xbj and xm <= xbj + abj:
                        if ym >= ybj and ym <= ybj + albj:
                            estadoJuego = MENU
            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego == INSTRUCCIONES:
                    xbj, ybj, abj, albj = spriteBtnVolver.rect
                    if xm >= xbj and xm <= xbj + abj:
                        if ym >= ybj and ym <= ybj + albj:
                            estadoJuego = MENU
            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego == GANA:
                    xbj, ybj, abj, albj = spriteBtnVolver.rect
                    if xm >= xbj and xm <= xbj + abj:
                        if ym >= ybj and ym <= ybj + albj:
                            estadoJuego = MENU
                            counter, text = 3250, '3250'.rjust(3)
                            pygame.time.set_timer(pygame.USEREVENT, 1000)
            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego == PIERDE:
                    xbj, ybj, abj, albj = spriteBtnVolver.rect
                    if xm >= xbj and xm <= xbj + abj:
                        if ym >= ybj and ym <= ybj + albj:
                            estadoJuego = MENU
                            counter, text = 3250, '3250'.rjust(3)
                            pygame.time.set_timer(pygame.USEREVENT, 1000)

            if evento.type == pygame.KEYDOWN and estadoJuego==JUEGO:

                if evento.key == pygame.K_LEFT :
                    longitud=-10
                    movercanasta= True


                if evento.key == pygame.K_RIGHT:
                    longitud=10
                    movercanasta = True


            if evento.type==pygame.KEYUP :
                movercanasta= False

                # Timer




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
            cancionMenu.play()

        elif estadoJuego == JUEGO:
            cancionFondoJuego.play()
            ventana.blit(imgFondoJuego, (0,0))

            font = pygame.font.SysFont('Consolas', 30)


            if movercanasta :
                canasta.rect.left += longitud
            ventana.blit(canasta.image, canasta.rect)
            #manzana normales
            dibujarManzanas(ventana, listaManzana)
            actualizarManzanas(listaManzana,imgManzana)
            checarColisiones(listaManzana,canasta,puntos)


            #Manzanas envenenadas
            dibujarManzanas(ventana, listaManzanaP)
            actualizarManzanas(listaManzanaP, imgManzanaP)
            checarColisiones(listaManzanaP,canasta,puntosP)


            counter -= 1
            newcounter = counter // 27
            text = str(newcounter).rjust(3) if newcounter > 0 else '¡Time Over!'
            ventana.blit(font.render("Tiempo", True, (255, 255, 255)), (32, 28))
            ventana.blit(font.render(text, True, (255, 255, 255)), (32, 58))

            puntosM = calcularPuntos(puntos, 50)

            puntosMP = calcularPuntos(puntosP, 500)
            #Manzana NORMALES <3
            #Se supone esto calcula mas manzanas , no pude hacer que tambien creara mas manzanas verdes y
            #Las contara como debe ser en el puntaje, sin embargo ammm aun asi crea manzanas verdes
            if newcounter <= timeri:

                dibujarManzanas(ventana, listaNew)
                actualizarManzanas(listaNew, imgManzana)
                checarColisiones(listaNew, canasta, puntosT)

                puntosM+= calcularPuntos(puntosT, 50)

            if newcounter <= timeri-15:
                dibujarManzanas(ventana, listaN2)
                actualizarManzanas(listaN2, imgManzana)
                checarColisiones(listaN2, canasta, puntosX)
                puntosM += calcularPuntos(puntosX, 50)


            if newcounter <= timeri - 30:
                dibujarManzanas(ventana, listaN3)
                actualizarManzanas(listaN3, imgManzana)
                checarColisiones(listaN3, canasta, puntosY)
                puntosM += calcularPuntos(puntosY, 50)

            if newcounter <= timeri-45:
                dibujarManzanas(ventana, listaN4)
                actualizarManzanas(listaN4, imgManzana)
                checarColisiones(listaN4, canasta, puntosZ)
                puntosM += calcularPuntos(puntosZ, 50)


            if newcounter <= timeri-60:
                dibujarManzanas(ventana, listaN5)
                actualizarManzanas(listaN5, imgManzana)
                checarColisiones(listaN5, canasta, puntosA)
                puntosM += calcularPuntos(puntosA, 50)


            if newcounter <= timeri-75:
                dibujarManzanas(ventana, listaN6)
                actualizarManzanas(listaN6, imgManzana)
                checarColisiones(listaN6, canasta, puntosB)
                puntosM += calcularPuntos(puntosB, 50)

            if newcounter <= timeri-88:
                dibujarManzanas(ventana, listaN7)
                actualizarManzanas(listaN7, imgManzana)
                checarColisiones(listaN7, canasta, puntosC)
                puntosM += calcularPuntos(puntosC, 50)



            #Poion APPLE


            pTotales = str(puntosTotal(puntosM, puntosMP))

            textoPuntos = fuente.render(pTotales, 10, BLANCO)
            textoPuntos2 = fuente.render("Puntos", 10, BLANCO)
            ventana.blit(textoPuntos, (30, 140))
            ventana.blit(textoPuntos2, (30, 120))


            if newcounter==0:
                if int(pTotales)<0:
                    estadoJuego=PIERDE
                else:
                    estadoJuego=GANA







        elif estadoJuego==INSTRUCCIONES:

            ventana.blit(imgPersonajeGanar, (-20, -150))
            ventana.blit(spriteBtnInst.image, spriteBtnInst.rect)
            texto = fuente.render("Atrapa todas las manzanas que puedas ", 1, BLANCO)
            texto2=fuente.render("durante 120 segundos, si atrapas manzanas",1,BLANCO)
            texto3=fuente.render("envenenadas no te preocupes, no perderas",1,BLANCO)
            texto4=fuente.render("automaticamente pero perderas puntos.",1,BLANCO)
            texto5=fuente.render("¡Buena suerte!",1,BLANCO)
            ventana.blit(texto, (400, 200))
            ventana.blit(texto2, (400,240))
            ventana.blit(texto3, (400, 280))
            ventana.blit(texto4, (400,320 ))
            ventana.blit(texto5, (400,360 ))
#Manzanas
            ventana.blit(manzana.image, manzana.rect)
            ventana.blit(manzanaP.image, manzanaP.rect)
            textoM = fuente.render("+ 50 puntos",3,BLANCO)
            textoMP=fuente.render("-500 puntos",3,BLANCO)
            ventana.blit(textoM, (450, 490))
            ventana.blit(textoMP, (450, 430))

            ventana.blit(spriteBtnVolver.image, spriteBtnVolver.rect)



        elif estadoJuego==CREDITOS:
            ventana.blit(spriteBtnVolver.image, spriteBtnVolver.rect)
            ventana.blit(spriteBtnTCreditos.image, spriteBtnTCreditos.rect)
            listaC=regresarCreditos("Referencias")
            creaCreditos(ventana,listaC)
        elif estadoJuego==PIERDE:
            font1 = pygame.font.SysFont('Consolas', 80)
            ventana.blit(imgPerder, (0,0))
            ventana.blit(spriteBtnPerdiste.image, spriteBtnPerdiste.rect)

            textoPuntos = font1.render(pTotales, 3, BLANCO)
            ventana.blit(textoPuntos, (300, 150))
            ventana.blit(spriteBtnVolver.image, spriteBtnVolver.rect)
        elif estadoJuego == GANA:

            font1 = pygame.font.SysFont('Consolas', 100)
            ventana.blit(imgPersonajeGanar, (0, -150))
            ventana.blit(spriteBtnGanaste.image, spriteBtnGanaste.rect)


            textoPuntos = font1.render(pTotales, 3, BLANCO)

            ventana.blit(textoPuntos, (450, 200))
            ventana.blit(spriteBtnVolver.image, spriteBtnVolver.rect)
        elif estadoJuego == PUNTAJES:
            ventana.blit(spriteBtnPuntaje.image, spriteBtnPuntaje.rect)
            listaD = regresarCreditos("Puntajes")
            ventana.blit(spriteBtnVolver.image, spriteBtnVolver.rect)
            creaCreditos(ventana, listaD)


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

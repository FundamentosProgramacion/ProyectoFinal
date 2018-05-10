################################### DAVID MEDINA MEDINA ###########################################################
######################################## A01653311 #####################################################################
######################################## PROYECTO FINAL PYGAME #########################################################
######################################## BLACKJACK #####################################################################


######################################### IMPORTACIONES DE PYGAME Y RANDOM #############################################
from random import *
import pygame

##################################### DIMENSIONES DE LA PANTALLA #######################################################
ANCHO = 800
ALTO = 600
negro = (0,0,0)
blanco = (255,255,255)

##################################### CORDENADAS DE CARATS #############################################################
cartaCrupierx1 = 360
cartaCrupiery1 = 60
cartaCrupierx2 = 400
cartaCrupiery2 = 85
cartaCrupierx3 = 440
cartaCrupiery3 = 110
cartaCrupierx4 = 480
cartaCrupiery4 = 135
cartaCrupierx5 = 520
cartaCrupiery5 = 170
cartaCrupierx6 = 360
cartaCrupiery6 = 205

yox1 = 360
yoy1 = 430
yox2 = 400
yoy2 = 405
yox3 = 440
yoy3 = 380
yox4 = 480
yoy4 = 355
yox5 = 520
yoy5 = 320
yox6 = 560
yoy6 = 295



###################################### FUNCION PARA DIBUJADO DE CARTAS #################################################
def dibujarCarta(ventana,n,x,y):
    if n ==2:
        return ventana.blit(CN2, (x, y))
    if n == 3:
        return ventana.blit(CN3, (x, y))
    if n == 3:
        return ventana.blit(CN3, (x, y))
    if n == 4:
        return ventana.blit(CN4, (x, y))
    if n == 5:
        return ventana.blit(CN5, (x, y))
    if n == 6:
        return ventana.blit(CN6, (x, y))
    if n == 7:
        return ventana.blit(CN7, (x, y))
    if n == 8:
        return ventana.blit(CN8, (x, y))
    if n == 9:
        return ventana.blit(CN9, (x, y))
    if n == 10:
        return ventana.blit(CN10, (x, y))
    if n == 11:
        return ventana.blit(CNAs, (x, y))


######################################## FUNCION CARTA 1 ###############################################################
def miPrimeraCarta(ventana, n ,x, y):
    dibujarCarta(ventana,n, x, y)



######################################## FUNCION CARTA 2 ###############################################################
def miSegundaCarta(ventana,n, x , y):
    dibujarCarta(ventana, n, x, y)



######################################## FUNCION CARTA 3 ###############################################################
def miTerceraCarta(ventana,n, x , y):
    dibujarCarta(ventana, n, x, y)



######################################## FUNCION CARTA 4 ###############################################################
def miCuartaCarta(ventana,n, x , y):
    dibujarCarta(ventana, n, x, y)



######################################## FUNCION CARTA 5 ###############################################################
def miQuintaCarta(ventana,n, x , y):
    dibujarCarta(ventana, n, x, y)


######################################## FUNCION CARTA 6 ###############################################################
def miSextaCarta(ventana,n, x , y):
    dibujarCarta(ventana, n, x, y)
    pass


######################################## FUNCIONPARA SUMAR 3 CARTAS ####################################################
def suma(val1,val2):
    total = val1+val2
    strtotal = str(total)
    if total >21:
        totalAs = total-10
        strtotal = str(totalAs)
        return strtotal
    return strtotal


def suma3cartas(carta1, carta2, carta3):
    total = carta1 + carta2 + carta3
    strTotal = str(total)
    listaCartas = [carta1, carta2, carta3]
    AS = 0
    for ases in listaCartas:
        if ases == 11:
            AS+=1
    if AS !=0 and total > 21:
        x = total-10
        if x > 21 and AS >1:
            y = str(total-20)
            strtotalAS2 = (y)
            return strtotalAS2
        strtotal1 = str(x)
        return strtotal1
    return strTotal


def suma4cartas(carta1, carta2, carta3, carta4):
    total = carta1 + carta2 + carta3 + carta4
    strTotal = str(total)
    listaCartas = [carta1, carta2, carta3, carta4]
    AS = 0
    for ases in listaCartas:
        if ases == 11:
            AS+=1
    if AS !=0 and total > 21:
        x = total-10
        if x > 21 and AS >1:
            y = str(total-20)
            strtotalAS2 = (y)
            return strtotalAS2
        strtotal1 = str(x)
        return strtotal1
    return strTotal


def suma5cartas(carta1, carta2, carta3, carta4, carta5):
    total = carta1 + carta2 + carta3 + carta4 + carta5
    strTotal = str(total)
    listaCartas = [carta1, carta2, carta3, carta4, carta5]
    AS = 0
    for ases in listaCartas:
        if ases == 11:
            AS+=1
    if AS !=0 and total > 21:
        x = total-10
        if x > 21 and AS >1:
            y = str(total-20)
            strtotalAS2 = (y)
            return strtotalAS2
        strtotal1 = str(x)
        return strtotal1
    return strTotal


def suma6cartas(carta1, carta2, carta3, carta4, carta5, carta6):
    total = carta1 + carta2 + carta3 + carta4 + carta5 + carta6
    strTotal = str(total)
    listaCartas = [carta1, carta2, carta3, carta4, carta5, carta6]
    AS = 0
    for ases in listaCartas:
        if ases == 11:
            AS+=1
    if AS !=0 and total > 21:
        x = total-10
        if x > 21 and AS >1:
            y = str(total-20)
            strtotalAS2 = (y)
            return strtotalAS2
        strtotal1 = str(x)
        return strtotal1
    return strTotal

######################################## FUNCION PARA PUNTOS ###########################################################
def puntos(n):
    puntos = int(n)
    return puntos


######################################## FUNCION PARA CARTA CRUPIER ####################################################
def cartaCrupier1(ventana, cartaCrupier1, cartaCrupierx1, cartaCrupiery1):
    dibujarCarta(ventana, cartaCrupier1, cartaCrupierx1, cartaCrupiery1)


def cartaCrupier2(ventana, cartaCrup2, cartaCrupierx2, cartaCrupiery2):
    dibujarCarta(ventana, cartaCrup2, cartaCrupierx2, cartaCrupiery2)


def cartaCrupier3(ventana, cartaCrup3, cartaCrupierx3, cartaCrupiery3):
    dibujarCarta(ventana, cartaCrup3, cartaCrupierx3, cartaCrupiery3)


def cartaCrupier4(ventana, cartaCrup4, cartaCrupierx4, cartaCrupiery4):
    dibujarCarta(ventana, cartaCrup4, cartaCrupierx4, cartaCrupiery4)


def cartaCrupier5(ventana, cartaCrup5, cartaCrupierx5, cartaCrupiery5):
    dibujarCarta(ventana, cartaCrup5, cartaCrupierx5, cartaCrupiery5)


def cartaCrupier6(ventana, cartaCrup6, cartaCrupierx6, cartaCrupiery6):
    dibujarCarta(ventana, cartaCrup6, cartaCrupierx6, cartaCrupiery6)


######################################## FUNCION PARA SELECCION DE CARTAS ##############################################
def seleccionarCarta():
    listaCartas = choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    return listaCartas

######################################## FUNCION PRINCIPAL DE DIBUJADO #################################################
def dibujar(linea):
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

######################################## SONIDOS DEL VIDEOJUEGO ########################################################
    pygame.mixer.init()
    efectoClick = pygame.mixer.Sound("toqueMenu.wav")
    efectoFichas = pygame.mixer.Sound("fichas.wav")
    efectoEmpezar = pygame.mixer.Sound("empezar.wav")
    efectoDinero = pygame.mixer.Sound("dinero.wav")


######################################## IMPORTACION DE IMAGENES #######################################################
    imgFondoJuego = pygame.image.load("blackjack.jpg")
    imgFondoMenu = pygame.image.load("bjmenu.jpg")
    imgFondoAcercaDe = pygame.image.load("imgFondoAD.jpg")

    imgBtnJugar = pygame.image.load("jugar.png")
    imgBtnAcercaDe = pygame.image.load("acercaDe.png")
    imgBtnAyuda = pygame.image.load("ayuda.png")
    imgBtnRegresar = pygame.image.load("regresar.png")

    imgBtnPedir = pygame.image.load("pedir.png")
    imgBtnPlantarse = pygame.image.load("plantarse.png")
    imgBtnRendirse = pygame.image.load("rendirse.png")
    imgBtnDoblar = pygame.image.load("doblar.png")
    imgBtnMenu = pygame.image.load("menu.png")
    imgBtnReapostar = pygame.image.load("reapostar.png")

    imgBtn50 = pygame.image.load("cincuenta.png")
    imgBtn100 = pygame.image.load("cien.png")
    imgBtn200 = pygame.image.load("doscientos.png")
    imgBtn500 = pygame.image.load("quinientos.png")
    imgBtnmasDinero = pygame.image.load("masDinero.png")

    imgBtnEmpezar = pygame.image.load("empezar.png")

######################################## IMPORTACION DE CARTAS #########################################################
    global CNAs
    CNAs = pygame.image.load("AsCorNeg.jpg")
    global CN2
    CN2 = pygame.image.load("2corNeg.jpg")
    global CN3
    CN3 = pygame.image.load("3corNeg.jpg")
    global CN4
    CN4 = pygame.image.load("4corNeg.jpg")
    global CN5
    CN5 = pygame.image.load("5corNeg.jpg")
    global CN6
    CN6 = pygame.image.load("6corNeg.jpg")
    global CN7
    CN7 = pygame.image.load("7corNeg.jpg")
    global CN8
    CN8 = pygame.image.load("8corNeg.jpg")
    global CN9
    CN9 = pygame.image.load("9corNeg.jpg")
    global CN10
    CN10 = pygame.image.load("10corNeg.jpg")
    global CNJ
    CNJ = pygame.image.load("JCorNeg.jpg")
    global CNQ
    CNQ = pygame.image.load("QCorNeg.jpg")
    global CNK
    CNK = pygame.image.load("KCorNeg.jpg")

######################################## SPRITES ######################################################################
    spriteBtnJugar = pygame.sprite.Sprite()
    spriteBtnJugar.image = imgBtnJugar
    spriteBtnJugar.rect = imgBtnJugar.get_rect()
    spriteBtnJugar.rect.left = (ANCHO//2-spriteBtnJugar.rect.width//2)+5
    spriteBtnJugar.rect.top = 480

    spriteBtnAcercaDe = pygame.sprite.Sprite()
    spriteBtnAcercaDe.image = imgBtnAcercaDe
    spriteBtnAcercaDe.rect = imgBtnAcercaDe.get_rect()
    spriteBtnAcercaDe.rect.left = 20
    spriteBtnAcercaDe.rect.top = 30

    spriteBtnRegresar = pygame.sprite.Sprite()
    spriteBtnRegresar.image = imgBtnRegresar
    spriteBtnRegresar.rect = imgBtnRegresar.get_rect()
    spriteBtnRegresar.rect.left = ANCHO- 280
    spriteBtnRegresar.rect.top = 490

    spriteBtnAyuda = pygame.sprite.Sprite()
    spriteBtnAyuda.image = imgBtnAyuda
    spriteBtnAyuda.rect = imgBtnAyuda.get_rect()
    spriteBtnAyuda.rect.left = ANCHO- 270
    spriteBtnAyuda.rect.top = 30

    spriteBtnPedir = pygame.sprite.Sprite()
    spriteBtnPedir.image = imgBtnPedir
    spriteBtnPedir.rect = imgBtnPedir.get_rect()
    spriteBtnPedir.rect.left = 630
    spriteBtnPedir.rect.top = 350

    spriteBtnPlantarse = pygame.sprite.Sprite()
    spriteBtnPlantarse.image = imgBtnPlantarse
    spriteBtnPlantarse.rect = imgBtnPlantarse.get_rect()
    spriteBtnPlantarse.rect.left = 630
    spriteBtnPlantarse.rect.top = 420

    spriteBtnRendirse = pygame.sprite.Sprite()
    spriteBtnRendirse.image = imgBtnRendirse
    spriteBtnRendirse.rect = imgBtnRendirse.get_rect()
    spriteBtnRendirse.rect.left = 20
    spriteBtnRendirse.rect.top = 350

    spriteBtnDoblar = pygame.sprite.Sprite()
    spriteBtnDoblar.image = imgBtnDoblar
    spriteBtnDoblar.rect = imgBtnDoblar.get_rect()
    spriteBtnDoblar.rect.left = 20
    spriteBtnDoblar.rect.top = 420

    spriteBtnMenu = pygame.sprite.Sprite()
    spriteBtnMenu.image = imgBtnMenu
    spriteBtnMenu.rect = imgBtnMenu.get_rect()
    spriteBtnMenu.rect.left = 660
    spriteBtnMenu.rect.top = 550

    spriteBtnReapostar = pygame.sprite.Sprite()
    spriteBtnReapostar.image = imgBtnReapostar
    spriteBtnReapostar.rect = imgBtnReapostar.get_rect()
    spriteBtnReapostar.rect.left = 21
    spriteBtnReapostar.rect.top = 550

    spriteBtn50 = pygame.sprite.Sprite()
    spriteBtn50 .image = imgBtn50
    spriteBtn50 .rect = imgBtn50 .get_rect()
    spriteBtn50 .rect.left = 350
    spriteBtn50 .rect.top = 380

    spriteBtn100 = pygame.sprite.Sprite()
    spriteBtn100 .image = imgBtn100
    spriteBtn100 .rect = imgBtn100 .get_rect()
    spriteBtn100 .rect.left = 410
    spriteBtn100 .rect.top = 380

    spriteBtn200  = pygame.sprite.Sprite()
    spriteBtn200.image = imgBtn200
    spriteBtn200.rect = imgBtn200.get_rect()
    spriteBtn200.rect.left = 350
    spriteBtn200.rect.top = 440

    spriteBtn500 = pygame.sprite.Sprite()
    spriteBtn500.image = imgBtn500
    spriteBtn500.rect = imgBtn500.get_rect()
    spriteBtn500.rect.left = 410
    spriteBtn500.rect.top = 440

    spriteBtnmasDinero = pygame.sprite.Sprite()
    spriteBtnmasDinero.image = imgBtnmasDinero
    spriteBtnmasDinero.rect = imgBtnmasDinero.get_rect()
    spriteBtnmasDinero.rect.left = 20
    spriteBtnmasDinero.rect.top = 480

    spriteBtnEmpezar = pygame.sprite.Sprite()
    spriteBtnEmpezar.image = imgBtnEmpezar
    spriteBtnEmpezar.rect = imgBtnEmpezar.get_rect()
    spriteBtnEmpezar.rect.left = 340
    spriteBtnEmpezar.rect.top = 500

######################################## ESTADOS DEL JUEGO #############################################################
    MENU = 1
    ACERCA_DE = 2
    AYUDA = 3
    JUEGO = 4
    EMPIEZA = 5
    JUEGO3CARTAS = 6
    JUEGO4CARTAS = 7
    JUEGO5CARTAS = 8
    JUEGO6CARTAS = 9
    JUEGO7CARTAS = 10
    EMPIEZAPLANTADO = 11
    JUEGO3CARTASPLANTADO = 12
    JUEGO4CARTASPLANTADO = 13
    JUEGO5CARTASPLANTADO = 14
    JUEGO6CARTASPLANTADO = 15
    JUEGODOBLADO = 17
    JUEGORENDIDO = 18
    estadoJuego = MENU

######################################## MENSAJE FONT ##################################################################
    fuente = pygame.font.SysFont("monospace", 24)

######################################## dinero ########################################################################
    dineroInicial = 1000
    dI = str(dineroInicial)
    entrada = open("dinero.txt", "w", encoding="UTF-8")
    lineaSalida = (dI)
    entrada.write(lineaSalida)
    entrada.close()


######################################## SELECCION DE CARTAS ###########################################################

    global carta1
    carta1 = seleccionarCarta()
    global carta2
    carta2 = seleccionarCarta()
    global carta3
    carta3 = seleccionarCarta()
    global carta4
    carta4 = seleccionarCarta()
    global carta5
    carta5 = seleccionarCarta()
    global carta6
    carta6 = seleccionarCarta()
    global cartaCrup1
    cartaCrup1 = seleccionarCarta()
    global cartaCrup2
    cartaCrup2 = seleccionarCarta()
    global cartaCrup3
    cartaCrup3 = seleccionarCarta()
    global cartaCrup4
    cartaCrup4 = seleccionarCarta()
    global cartaCrup5
    cartaCrup5 = seleccionarCarta()
    global cartaCrup6
    cartaCrup6 = seleccionarCarta()

######################################## CICLO PRINCIPAL ###############################################################
    while not termina:

######################################## PROCESION DE EVENTOS QUE RECIBE EL PROGRAMA ###################################
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

            if evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego == MENU:
                    xbj, ybj, abj, albj = spriteBtnJugar.rect
                    xbAD, ybAD, abAD, albAD = spriteBtnAcercaDe.rect
                    xbA, ybA, abA, albA = spriteBtnAyuda.rect
                    if xm>=xbj and xm<=xbj+abj and ym>=ybj and ym<=ybj+albj:
                        efectoClick.play()
                        estadoJuego = JUEGO
                    elif xm>=xbAD and xm<=xbAD+abAD and ym>=ybAD and ym<=ybAD+albAD:
                        efectoClick.play()
                        estadoJuego = ACERCA_DE
                    elif xm>=xbA and xm<=xbA+abA and ym>=ybA and ym<=ybA+albA:
                        efectoClick.play()
                        estadoJuego = AYUDA

                elif estadoJuego == ACERCA_DE:
                    xbR, ybR, abR, albR = spriteBtnRegresar.rect
                    if xm >= xbR and xm <= xbR + abR and ym >= ybR and ym <= ybR + albR:
                        efectoClick.play()
                        estadoJuego = MENU

                elif estadoJuego == AYUDA:
                    xbR, ybR, abR, albR = spriteBtnRegresar.rect
                    if xm >= xbR and xm <= xbR + abR and ym >= ybR and ym <= ybR + albR:
                        efectoClick.play()
                        estadoJuego = MENU

                elif estadoJuego == JUEGO:
                    entrada = open("dinero.txt", "r", encoding="UTF-8")
                    linea = entrada.readline()
                    entrada.close()
                    xb50, yb50, ab50, alb50 = spriteBtn50.rect
                    xb100, yb100, ab100, alb100 = spriteBtn100.rect
                    xb200, yb200, ab200, alb200 = spriteBtn200.rect
                    xb500, yb500, ab500, alb500 = spriteBtn500.rect
                    xbE, ybE, abE, albE = spriteBtnEmpezar.rect
                    xbDin, ybDin, abDin, albDin = spriteBtnmasDinero.rect
                    xbM, ybM, abM, albM = spriteBtnMenu.rect
                    if xm >= xbDin and xm <= xbDin + abDin and ym >= ybDin and ym <= ybDin + albDin:
                        efectoDinero.play()
                    if xm >= xb50 and xm <= xb50 + ab50 and ym >= yb50 and ym <= yb50 + alb50:
                        efectoFichas.play()
                    if xm >= xb100 and xm <= xb100 + ab100 and ym >= yb100 and ym <= yb100 + alb100:
                        efectoFichas.play()
                    if xm >= xb200 and xm <= xb200 + ab200 and ym >= yb200 and ym <= yb200 + alb200:
                        efectoFichas.play()
                    if xm >= xb500 and xm <= xb500 + ab500 and ym >= yb500 and ym <= yb500 + alb500:
                        efectoFichas.play()
                    if xm >= xbDin and xm <= xbDin + abDin and ym >= ybDin and ym <= ybDin + albDin:
                        dinero = str(1000)
                        entrada = open("dinero.txt", "w", encoding="UTF-8")
                        lineaSalida = (dinero)
                        entrada.write(lineaSalida)
                        entrada.close()
                    if xm >= xbE and xm <= xbE + abE and ym >= ybE and ym <= ybE + albE:
                        efectoEmpezar.play()
                        estadoJuego = EMPIEZA
                    if xm >= xbM and xm <= xbM + abM and ym >= ybM and ym <= ybM + albM:
                        efectoClick.play()
                        estadoJuego = MENU

                elif estadoJuego == EMPIEZA:
                    xbM, ybM, abM, albM = spriteBtnMenu.rect
                    xbP, ybP, abP, albP = spriteBtnPedir.rect
                    xbD, ybD, abD, albD = spriteBtnDoblar.rect
                    xbR, ybR, abR, albR = spriteBtnRendirse.rect
                    xbPl, ybPl, abPl, albPl = spriteBtnPlantarse.rect
                    xbRe, ybRe, abRe, albRe = spriteBtnReapostar.rect
                    if xm >= xbM and xm <= xbM + abM and ym >= ybM and ym <= ybM + albM:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        estadoJuego = MENU
                    if xm >= xbD and xm <= xbD + abD and ym >= ybD and ym <= ybD + albD:
                        efectoClick.play()
                        estadoJuego = JUEGODOBLADO
                    if xm >= xbP and xm <= xbP + abP and ym >= ybP and ym <= ybP + albP:
                        efectoClick.play()
                        estadoJuego = JUEGO3CARTAS
                    if xm >= xbR and xm <= xbR + abR and ym >= ybR and ym <= ybR + albR:
                        efectoClick.play()
                        estadoJuego = JUEGORENDIDO
                    if xm >= xbPl and xm <= xbPl + abPl and ym >= ybPl and ym <= ybPl + albPl:
                        efectoClick.play()
                        estadoJuego = EMPIEZAPLANTADO
                    if xm >= xbRe and xm <= xbRe + abRe and ym >= ybRe and ym <= ybRe + albRe:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        estadoJuego = JUEGO


                elif estadoJuego == EMPIEZAPLANTADO:
                    xbM, ybM, abM, albM = spriteBtnMenu.rect
                    xbRe, ybRe, abRe, albRe = spriteBtnReapostar.rect
                    if xm >= xbM and xm <= xbM + abM and ym >= ybM and ym <= ybM + albM:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        #entrada = open("dinero.txt", "r", encoding="UTF-8")
                        #linea = entrada.readline()

                       # entrada.close()
                        estadoJuego = MENU
                    if xm >= xbRe and xm <= xbRe + abRe and ym >= ybRe and ym <= ybRe + albRe:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        #entrada = open("dinero.txt", "r", encoding="UTF-8")
                        #linea = entrada.readline()
                        #entrada.close()
                        estadoJuego = JUEGO

                elif estadoJuego == JUEGODOBLADO:
                    xbM, ybM, abM, albM = spriteBtnMenu.rect
                    xbRe, ybRe, abRe, albRe = spriteBtnReapostar.rect
                    if xm >= xbM and xm <= xbM + abM and ym >= ybM and ym <= ybM + albM:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        entrada = open("dinero.txt", "r", encoding="UTF-8")
                        linea = entrada.readline()

                        entrada.close()
                        estadoJuego = MENU
                    if xm >= xbRe and xm <= xbRe + abRe and ym >= ybRe and ym <= ybRe + albRe:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        entrada = open("dinero.txt", "r", encoding="UTF-8")
                        linea = entrada.readline()

                        entrada.close()
                        estadoJuego = JUEGO

                elif estadoJuego == JUEGORENDIDO:
                    xbM, ybM, abM, albM = spriteBtnMenu.rect
                    xbRe, ybRe, abRe, albRe = spriteBtnReapostar.rect
                    if xm >= xbM and xm <= xbM + abM and ym >= ybM and ym <= ybM + albM:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        entrada = open("dinero.txt", "r", encoding="UTF-8")
                        linea = entrada.readline()

                        entrada.close()
                        estadoJuego = MENU
                    if xm >= xbRe and xm <= xbRe + abRe and ym >= ybRe and ym <= ybRe + albRe:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        entrada = open("dinero.txt", "r", encoding="UTF-8")
                        linea = entrada.readline()

                        entrada.close()
                        estadoJuego = JUEGO

                elif estadoJuego == JUEGO3CARTAS:
                    xbM, ybM, abM, albM = spriteBtnMenu.rect
                    xbP, ybP, abP, albP = spriteBtnPedir.rect
                    xbPl, ybPl, abPl, albPl = spriteBtnPlantarse.rect
                    xbRe, ybRe, abRe, albRe = spriteBtnReapostar.rect
                    if xm >= xbM and xm <= xbM + abM and ym >= ybM and ym <= ybM + albM:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        entrada = open("dinero.txt", "r", encoding="UTF-8")
                        linea = entrada.readline()

                        entrada.close()
                        estadoJuego = MENU
                    if xm >= xbP and xm <= xbP + abP and ym >= ybP and ym <= ybP + albP and puntos(suma3cartas(carta1, carta2, carta3)) < 22:
                        efectoClick.play()
                        estadoJuego = JUEGO4CARTAS
                    if xm >= xbPl and xm <= xbPl + abPl and ym >= ybPl and ym <= ybPl + albPl and puntos(suma3cartas(carta1, carta2, carta3)) < 22:
                        efectoClick.play()
                        estadoJuego = JUEGO3CARTASPLANTADO
                    if xm >= xbRe and xm <= xbRe + abRe and ym >= ybRe and ym <= ybRe + albRe:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        entrada = open("dinero.txt", "r", encoding="UTF-8")
                        linea = entrada.readline()

                        entrada.close()
                        estadoJuego = JUEGO


                elif estadoJuego == JUEGO3CARTASPLANTADO:
                    xbM, ybM, abM, albM = spriteBtnMenu.rect
                    xbRe, ybRe, abRe, albRe = spriteBtnReapostar.rect
                    if xm >= xbM and xm <= xbM + abM and ym >= ybM and ym <= ybM + albM:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        entrada = open("dinero.txt", "r", encoding="UTF-8")
                        linea = entrada.readline()

                        entrada.close()
                        estadoJuego = MENU
                    if xm >= xbRe and xm <= xbRe + abRe and ym >= ybRe and ym <= ybRe + albRe:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        entrada = open("dinero.txt", "r", encoding="UTF-8")
                        linea = entrada.readline()

                        entrada.close()
                        estadoJuego = JUEGO


                elif estadoJuego == JUEGO4CARTAS:
                    xbM, ybM, abM, albM = spriteBtnMenu.rect
                    xbP, ybP, abP, albP = spriteBtnPedir.rect
                    xbPl, ybPl, abPl, albPl = spriteBtnPlantarse.rect
                    xbRe, ybRe, abRe, albRe = spriteBtnReapostar.rect
                    if xm >= xbM and xm <= xbM + abM and ym >= ybM and ym <= ybM + albM:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        entrada = open("dinero.txt", "r", encoding="UTF-8")
                        linea = entrada.readline()
                        entrada.close()
                        estadoJuego = MENU
                    if xm >= xbP and xm <= xbP + abP and ym >= ybP and ym <= ybP + albP and puntos(suma4cartas(carta1, carta2, carta3, carta4)) < 22:
                        efectoClick.play()
                        estadoJuego = JUEGO5CARTAS
                    if xm >= xbPl and xm <= xbPl + abPl and ym >= ybPl and ym <= ybPl + albPl and puntos(suma4cartas(carta1, carta2, carta3, carta4)) < 22:
                        efectoClick.play()
                        estadoJuego = JUEGO4CARTASPLANTADO
                    if xm >= xbRe and xm <= xbRe + abRe and ym >= ybRe and ym <= ybRe + albRe:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        entrada = open("dinero.txt", "r", encoding="UTF-8")
                        linea = entrada.readline()
                        entrada.close()
                        estadoJuego = JUEGO


                elif estadoJuego == JUEGO4CARTASPLANTADO:
                    xbM, ybM, abM, albM = spriteBtnMenu.rect
                    xbRe, ybRe, abRe, albRe = spriteBtnReapostar.rect
                    if xm >= xbM and xm <= xbM + abM and ym >= ybM and ym <= ybM + albM:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        estadoJuego = MENU
                    if xm >= xbRe and xm <= xbRe + abRe and ym >= ybRe and ym <= ybRe + albRe:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        estadoJuego = JUEGO

                elif estadoJuego == JUEGO5CARTAS:
                    xbM, ybM, abM, albM = spriteBtnMenu.rect
                    xbP, ybP, abP, albP = spriteBtnPedir.rect
                    xbPl, ybPl, abPl, albPl = spriteBtnPlantarse.rect
                    xbRe, ybRe, abRe, albRe = spriteBtnReapostar.rect
                    if xm >= xbM and xm <= xbM + abM and ym >= ybM and ym <= ybM + albM:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        estadoJuego = MENU
                    if xm >= xbP and xm <= xbP + abP and ym >= ybP and ym <= ybP + albP and puntos(suma5cartas(carta1, carta2, carta3, carta4, carta5)) < 22:
                        efectoClick.play()
                        estadoJuego = JUEGO6CARTAS
                    if xm >= xbPl and xm <= xbPl + abPl and ym >= ybPl and ym <= ybPl + albPl and puntos(suma5cartas(carta1, carta2, carta3, carta4, carta5)) < 22:
                        efectoClick.play()
                        estadoJuego = JUEGO5CARTASPLANTADO
                    if xm >= xbRe and xm <= xbRe + abRe and ym >= ybRe and ym <= ybRe + albRe:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        estadoJuego = JUEGO


                elif estadoJuego == JUEGO5CARTASPLANTADO:
                    xbM, ybM, abM, albM = spriteBtnMenu.rect
                    xbRe, ybRe, abRe, albRe = spriteBtnReapostar.rect
                    if xm >= xbM and xm <= xbM + abM and ym >= ybM and ym <= ybM + albM:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        estadoJuego = MENU
                    if xm >= xbRe and xm <= xbRe + abRe and ym >= ybRe and ym <= ybRe + albRe:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        estadoJuego = JUEGO

                elif estadoJuego == JUEGO6CARTAS:
                    xbM, ybM, abM, albM = spriteBtnMenu.rect
                    xbPl, ybPl, abPl, albPl = spriteBtnPlantarse.rect
                    xbRe, ybRe, abRe, albRe = spriteBtnReapostar.rect
                    if xm >= xbM and xm <= xbM + abM and ym >= ybM and ym <= ybM + albM:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        estadoJuego = MENU
                    if xm >= xbPl and xm <= xbPl + abPl and ym >= ybPl and ym <= ybPl + albPl and puntos(suma6cartas(carta1, carta2, carta3, carta4, carta5, carta6)) < 22:
                        efectoClick.play()
                        estadoJuego = JUEGO6CARTASPLANTADO
                    if xm >= xbRe and xm <= xbRe + abRe and ym >= ybRe and ym <= ybRe + albRe:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        efectoClick.play()
                        estadoJuego = JUEGO


                elif estadoJuego == JUEGO6CARTASPLANTADO:
                    xbM, ybM, abM, albM = spriteBtnMenu.rect
                    xbRe, ybRe, abRe, albRe = spriteBtnReapostar.rect
                    if xm >= xbM and xm <= xbM + abM and ym >= ybM and ym <= ybM + albM:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        estadoJuego = MENU
                    if xm >= xbRe and xm <= xbRe + abRe and ym >= ybRe and ym <= ybRe + albRe:
                        carta1 = seleccionarCarta()
                        carta2 = seleccionarCarta()
                        carta3 = seleccionarCarta()
                        carta4 = seleccionarCarta()
                        carta5 = seleccionarCarta()
                        carta6 = seleccionarCarta()
                        cartaCrup1 = seleccionarCarta()
                        cartaCrup2 = seleccionarCarta()
                        cartaCrup3 = seleccionarCarta()
                        cartaCrup4 = seleccionarCarta()
                        cartaCrup5 = seleccionarCarta()
                        cartaCrup6 = seleccionarCarta()
                        estadoJuego = JUEGO


######################################## BORRADO DE PANTALLA ###########################################################
        ventana.fill(negro)

######################################## AQUI SE DIBUJAN TODOS LOS TRAZOS REQUERIDOS ###################################
        if estadoJuego == MENU:
            ventana.blit(imgFondoMenu,(0,0))
            ventana.blit(spriteBtnJugar.image, spriteBtnJugar.rect)
            ventana.blit(spriteBtnAcercaDe.image, spriteBtnAcercaDe.rect)
            ventana.blit(spriteBtnAyuda.image, spriteBtnAyuda.rect)

######################################## ESTADO DEL JUEGO: JUEGO #######################################################
        if estadoJuego == JUEGO:
            ventana.blit(imgFondoJuego, (0, 0))
            ventana.blit(spriteBtnmasDinero.image, spriteBtnmasDinero.rect)
            dineroApostado = 0
            xb50, yb50, ab50, alb50 = spriteBtn50.rect
            xb100, yb100, ab100, alb100 = spriteBtn100.rect
            xb200, yb200, ab200, alb200 = spriteBtn200.rect
            xb500, yb500, ab500, alb500 = spriteBtn500.rect
            if xm >= xb50 and xm <= xb50 + ab50 and ym >= yb50 and ym <= yb50 + alb50:
                dineroApostado += 50
            elif xm >= xb100 and xm <= xb100 + ab100 and ym >= yb100 and ym <= yb100 + alb100:
                dineroApostado += 100
            elif xm >= xb200 and xm <= xb200 + ab200 and ym >= yb200 and ym <= yb200 + alb200:
                dineroApostado += 200
            elif xm >= xb500 and xm <= xb500 + ab500 and ym >= yb500 and ym <= yb500 + alb500:
                dineroApostado += 500
            global strdinero
            strdinero = str(dineroApostado)
            entrada = open("dinero.txt", "r", encoding="UTF-8")
            linea = entrada.readline()
            entrada.close()
            texto1 = fuente.render("DINERO: $" + linea, 1, blanco)
            texto2 = fuente.render("DINERO APOSTADO: $" + strdinero, 1, blanco)
            texto3 = fuente.render("¡SELECCIONE UNA FICHA PARA APOSTAR Y SELECCIONE BOTON EMPEZAR  ", 1, blanco)
            texto4 = fuente.render("PARA INICIAR EL JUEGO O SELECCIONE MENU (ABAJO Y DERECHA) PARA " ,1, blanco)
            texto5 = fuente.render("VOVLER AL MENU PRINCIPAL!", 1, blanco)
            texto6 = fuente.render("¡SI YA NO TIENES DINERO PRESIONAR", 1, blanco)
            texto7 = fuente.render("BOTON [+$$$] Y TU DINERO SERA $1000!", 1, blanco)
            ventana.blit(texto1, (10, 31))
            ventana.blit(texto2, (10, 71))
            ventana.blit(texto3, (20, 321))
            ventana.blit(texto4, (20, 351))
            ventana.blit(texto5, (20, 381))
            ventana.blit(texto6, (20, 411))
            ventana.blit(texto7, (20, 441))
            ventana.blit(spriteBtn50.image, spriteBtn50.rect)
            ventana.blit(spriteBtn100.image, spriteBtn100.rect)
            ventana.blit(spriteBtn200.image, spriteBtn200.rect)
            ventana.blit(spriteBtn500.image, spriteBtn500.rect)
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
            if dineroApostado !=0:
                ventana.blit(spriteBtnEmpezar.image, spriteBtnEmpezar.rect)

######################################## ESTADO DEL JUEGO: EMPIEZA #####################################################
        if estadoJuego == EMPIEZA:
            ventana.blit(imgFondoJuego, (0, 0))
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
            suma(carta1, carta2)
            dIint = int(dI)
            apuesta = int(strdinero)
            lineaInt = int(linea)
            dineroActual = str(lineaInt-apuesta)
            #print(dineroActual)
            gananciaBj = ((apuesta//2) + apuesta)
            dineroActualBj = str(lineaInt + gananciaBj)
            gananciaBjstr = str(gananciaBj)

            din = (lineaInt-apuesta)
            dinstr = str(din)
            texto2 = fuente.render("DINERO APOSTADO: $" + strdinero, 1, blanco)
            texto3 = fuente.render("MIS PUNTOS: " + suma(carta1, carta2), 1, blanco)
            ventana.blit(texto2, (10, 71))
            ventana.blit(texto3, (10, 111))
            if carta1+carta2 ==21:
                texto1 = fuente.render("¡¡¡FELICIDADES BLACKJACK!!!", 1, blanco)
                texto2 = fuente.render("GANASTE :$"+ gananciaBjstr, 1, blanco)
                texto3 = fuente.render("DINERO: $" + dineroActualBj, 1, blanco)
                ventana.blit(texto3, (10, 31))
                ventana.blit(texto1, ((ANCHO // 2) - 120, 350))
                ventana.blit(texto2, ((ANCHO // 2) - 60, 380))
                cartaCrupier1(ventana, cartaCrup1, cartaCrupierx1, cartaCrupiery1)
                miPrimeraCarta(ventana, carta1, yox1, yoy1)
                miSegundaCarta(ventana, carta2, yox2, yoy2)
                ventana.blit(spriteBtnReapostar.image, spriteBtnReapostar.rect)
                entrada = open("dinero.txt", "w", encoding="UTF-8")
                lineaSalida = (dineroActualBj)
                entrada.write(lineaSalida)
                entrada.close()
            else:
                ventana.blit(spriteBtnPedir.image, spriteBtnPedir.rect)
                ventana.blit(spriteBtnPlantarse.image, spriteBtnPlantarse.rect)
                ventana.blit(spriteBtnDoblar.image, spriteBtnDoblar.rect)
                ventana.blit(spriteBtnRendirse.image, spriteBtnRendirse.rect)
                ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
                cartaCrupier1(ventana, cartaCrup1, cartaCrupierx1, cartaCrupiery1)
                miPrimeraCarta(ventana,carta1, yox1, yoy1)
                miSegundaCarta(ventana,carta2, yox2, yoy2)
                texto1 = fuente.render("DINERO: $" + dineroActual, 1, blanco)
                ventana.blit(texto1, (10, 31))
                entrada = open("dinero.txt", "w", encoding="UTF-8")
                lineaSalida = (dineroActual)
                entrada.write(lineaSalida)
                entrada.close()



######################################## ESTADO DEL JUEGO: EMPIEZAPLANTADO #############################################
        if estadoJuego == EMPIEZAPLANTADO:
            ventana.blit(imgFondoJuego, (0, 0))
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
            ventana.blit(spriteBtnReapostar.image, spriteBtnReapostar.rect)
            cartaCrupier1(ventana, cartaCrup1, cartaCrupierx1, cartaCrupiery1)
            cartaCrupier2(ventana, cartaCrup2, cartaCrupierx2, cartaCrupiery2)
            miPrimeraCarta(ventana,carta1, yox1, yoy1)
            miSegundaCarta(ventana,carta2, yox2, yoy2)
            puntosCrupier = str(cartaCrup1+ cartaCrup2)
            puntosCrupierInt = int(puntosCrupier)
            suma(carta1, carta2)
            puntosMios = int(suma(carta1, carta2))
            lineaInt = int(linea)
            dIint = int(dI)
            apuesta = int(strdinero)
            dineroActual = str(lineaInt - apuesta)
            archivoperdido = dineroActual
            archivoGanado = str(lineaInt+apuesta)

            texto1 = fuente.render("DINERO: $" + dineroActual, 1, blanco)
            texto2 = fuente.render("DINERO APOSTADO: $" + strdinero, 1, blanco)
            texto3 = fuente.render("MIS PUNTOS: " + suma(carta1, carta2), 1, blanco)
            #texto4 = fuente.render("PUNTOSCRUPIER: " + puntosCrupier, 1, blanco)
            ventana.blit(texto1, (10, 31))
            ventana.blit(texto2, (10, 71))
            #ventana.blit(texto4, (10, 111))
            ventana.blit(texto3, (10, 111))
            puntosCrupier2 = cartaCrup1+cartaCrup2
            if puntosCrupier2 >16:
                if puntosCrupier2 > puntosMios and puntosCrupier2<22:
                    texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                    entrada = open("dinero.txt", "w", encoding="UTF-8")
                    lineaSalida = (archivoperdido)
                    entrada.write(lineaSalida)
                    entrada.close()
                elif puntosCrupier2 < puntosMios or puntosCrupier2>21:
                    texto1 = fuente.render("GANASTE!!!", 1, blanco)
                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                    entrada = open("dinero.txt", "w", encoding="UTF-8")
                    lineaSalida = (archivoGanado)
                    entrada.write(lineaSalida)
                    entrada.close()
                elif puntosCrupier2 == puntosMios:
                    texto1 = fuente.render("EMPATE!!!", 1, blanco)
                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
            elif puntosCrupier2 <17:
                cartaCrupier3(ventana, cartaCrup3, cartaCrupierx3, cartaCrupiery3)
                puntosCrupier3 = cartaCrup1+cartaCrup2+cartaCrup3
                if puntosCrupier3 >16:
                    if puntosCrupier3 > puntosMios and puntosCrupier3<22:
                        texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                        ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                        entrada = open("dinero.txt", "w", encoding="UTF-8")
                        lineaSalida = (archivoperdido)
                        entrada.write(lineaSalida)
                        entrada.close()
                    elif puntosCrupier3 < puntosMios or puntosCrupier3 > 21:
                        texto1 = fuente.render("GANASTE!!!", 1, blanco)
                        ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                        entrada = open("dinero.txt", "w", encoding="UTF-8")
                        lineaSalida = (archivoGanado)
                        entrada.write(lineaSalida)
                        entrada.close()
                    elif puntosCrupier3 == puntosMios:
                        texto1 = fuente.render("EMPATE!!!", 1, blanco)
                        ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                elif puntosCrupier3 <17:
                    cartaCrupier4(ventana, cartaCrup4, cartaCrupierx4, cartaCrupiery4)
                    puntosCrupier4 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4
                    if puntosCrupier4 >16:
                        if puntosCrupier4 > puntosMios and puntosCrupier4<22:
                            texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                            ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                            entrada = open("dinero.txt", "w", encoding="UTF-8")
                            lineaSalida = (archivoperdido)
                            entrada.write(lineaSalida)
                            entrada.close()
                        elif puntosCrupier4 < puntosMios or puntosCrupier4 > 21:
                            texto1 = fuente.render("GANASTE!!!", 1, blanco)
                            ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                            entrada = open("dinero.txt", "w", encoding="UTF-8")
                            lineaSalida = (archivoGanado)
                            entrada.write(lineaSalida)
                            entrada.close()
                        elif puntosCrupier4 == puntosMios:
                            texto1 = fuente.render("EMPATE!!!", 1, blanco)
                            ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                    elif puntosCrupier4 <17:
                        cartaCrupier5(ventana, cartaCrup5, cartaCrupierx5, cartaCrupiery5)
                        puntosCrupier5 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4 + cartaCrup5
                        if puntosCrupier5 >16:
                            if puntosCrupier5 > puntosMios and puntosCrupier5<22:
                                texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoperdido)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier5 < puntosMios or puntosCrupier5 > 21:
                                texto1 = fuente.render("GANASTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoGanado)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier5 == puntosMios:
                                texto1 = fuente.render("EMPATE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                        elif puntosCrupier5 <17:
                            cartaCrupier6(ventana, cartaCrup6, cartaCrupierx6, cartaCrupiery6)
                            puntosCrupier6 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4 + cartaCrup5 + cartaCrup6
                            if puntosCrupier6 > puntosMios and puntosCrupier6<22:
                                texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoperdido)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier6 < puntosMios or puntosCrupier6 > 21:
                                texto1 = fuente.render("GANASTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoGanado)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier6 == puntosMios:
                                texto1 = fuente.render("EMPATE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))


######################################## ESTADO DEL JUEGO: JUEGO DOBLADO ###############################################
        if estadoJuego == JUEGODOBLADO :
            ventana.blit(imgFondoJuego, (0, 0))
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
            ventana.blit(spriteBtnReapostar.image, spriteBtnReapostar.rect)
            cartaCrupier1(ventana, cartaCrup1, cartaCrupierx1, cartaCrupiery1)
            #cartaCrupier2(ventana, cartaCrup2, cartaCrupierx2, cartaCrupiery2)

            miPrimeraCarta(ventana, carta1, yox1, yoy1)
            miSegundaCarta(ventana, carta2, yox2, yoy2)
            miTerceraCarta(ventana, carta3, yox3, yoy3)
            puntosCrupier = str(cartaCrup1)
            dIint = int(dI)
            lineaInt = int(linea)
            apuesta = int(strdinero)
            dineroDoblado = str(apuesta*2)
            dineroActual = str(lineaInt - apuesta*2)
            dineroActualGanado = str(dIint + apuesta*2)
            dineroActualEmpate = str(dIint)
            suma3cartas(carta1, carta2, carta3)
            puntosMios =int(suma3cartas(carta1, carta2, carta3))
            puntos(suma3cartas(carta1, carta2, carta3))
            archivoperdido = dineroActual
            archivoGanado = str(lineaInt + apuesta*2)

            texto2 = fuente.render("DINERO APOSTADO: $" + dineroDoblado, 1, blanco)
            texto3 = fuente.render("MIS PUNTOS: " + suma3cartas(carta1, carta2, carta3), 1, blanco)
            puntosCrupier2 = cartaCrup1 + cartaCrup2
            ventana.blit(texto2, (10, 71))
            ventana.blit(texto3, (10, 111))

            if puntos(suma3cartas(carta1, carta2, carta3)) > 21:
                texto1 = fuente.render("DINERO: $" + dineroActual, 1, blanco)
                texto2 = fuente.render("PERDISTE, MAS DE 21 PUNTOS!", 1, blanco)
                ventana.blit(texto2, ((ANCHO // 2) - 125, 330))
                ventana.blit(texto1, (10, 31))
                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                entrada = open("dinero.txt", "w", encoding="UTF-8")
                lineaSalida = (archivoperdido)
                entrada.write(lineaSalida)
                entrada.close()
            elif puntos(suma3cartas(carta1, carta2, carta3)) < 22:
                cartaCrupier2(ventana, cartaCrup2, cartaCrupierx2, cartaCrupiery2)
                puntosCrupier2 = cartaCrup1 + cartaCrup2
                if puntosCrupier2 > 16:
                    if puntosCrupier2 > puntosMios and puntosCrupier2 <22:
                        texto1 = fuente.render("DINERO: $" + dineroActual, 1, blanco)
                        texto2 = fuente.render("PERDISTE!!!", 1, blanco)
                        ventana.blit(texto1, (10, 31))
                        ventana.blit(texto2, ((ANCHO // 2) - 50, 350))

                        entrada = open("dinero.txt", "w", encoding="UTF-8")
                        lineaSalida = (archivoperdido)
                        entrada.write(lineaSalida)
                        entrada.close()
                    elif puntosCrupier2 < puntosMios:
                        texto1 = fuente.render("DINERO: $" + dineroActualGanado, 1, blanco)
                        texto2 = fuente.render("GANASTE!!!", 1, blanco)
                        ventana.blit(texto1, (10, 31))
                        ventana.blit(texto2, ((ANCHO // 2) - 50, 350))
                        entrada = open("dinero.txt", "w", encoding="UTF-8")
                        lineaSalida = (archivoGanado)
                        entrada.write(lineaSalida)
                        entrada.close()
                    elif puntosCrupier2 == puntosMios:
                        texto1 = fuente.render("DINERO: $" + linea, 1, blanco)
                        texto2 = fuente.render("EMPATE!!!", 1, blanco)
                        ventana.blit(texto1, (10, 31))
                        ventana.blit(texto2, ((ANCHO // 2) - 50, 350))
                elif puntosCrupier2 < 17:
                    cartaCrupier3(ventana, cartaCrup3, cartaCrupierx3, cartaCrupiery3)
                    puntosCrupier3 = cartaCrup1 + cartaCrup2 + cartaCrup3
                    if puntosCrupier3 > 16:
                        if puntosCrupier3 > puntosMios and puntosCrupier3 <22:
                            texto1 = fuente.render("DINERO: $" + dineroActual, 1, blanco)
                            texto2 = fuente.render("PERDISTE!!!", 1, blanco)
                            ventana.blit(texto1, (10, 31))
                            ventana.blit(texto2, ((ANCHO // 2) - 50, 350))

                            entrada = open("dinero.txt", "w", encoding="UTF-8")
                            lineaSalida = (archivoperdido)
                            entrada.write(lineaSalida)
                            entrada.close()
                        elif puntosCrupier3 < puntosMios or puntosCrupier3 >21:
                            texto1 = fuente.render("DINERO: $" + dineroActualGanado, 1, blanco)
                            texto2 = fuente.render("GANASTE!!!", 1, blanco)
                            ventana.blit(texto1, (10, 31))
                            ventana.blit(texto2, ((ANCHO // 2) - 50, 350))
                            entrada = open("dinero.txt", "w", encoding="UTF-8")
                            lineaSalida = (archivoGanado)
                            entrada.write(lineaSalida)
                            entrada.close()
                        elif puntosCrupier3 == puntosMios:
                            texto1 = fuente.render("DINERO: $" + linea, 1, blanco)
                            texto2 = fuente.render("EMPATE!!!", 1, blanco)
                            ventana.blit(texto1, (10, 31))
                            ventana.blit(texto2, ((ANCHO // 2) - 50, 350))
                    elif puntosCrupier3 < 17:
                        cartaCrupier4(ventana, cartaCrup4, cartaCrupierx4, cartaCrupiery4)
                        puntosCrupier4 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4
                        if puntosCrupier4 > 16:
                            if puntosCrupier4 > puntosMios and puntosCrupier4 <22:
                                texto1 = fuente.render("DINERO: $" + dineroActual, 1, blanco)
                                texto2 = fuente.render("PERDISTE!!!", 1, blanco)
                                ventana.blit(texto1, (10, 31))
                                ventana.blit(texto2, ((ANCHO // 2) - 50, 350))

                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoperdido)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier4 < puntosMios or puntosCrupier4 >21:
                                texto1 = fuente.render("DINERO: $" + dineroActualGanado, 1, blanco)
                                texto2 = fuente.render("GANASTE!!!", 1, blanco)
                                ventana.blit(texto1, (10, 31))
                                ventana.blit(texto2, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoGanado)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier4 == puntosMios:
                                texto1 = fuente.render("DINERO: $" + linea, 1, blanco)
                                texto2 = fuente.render("EMPATE!!!", 1, blanco)
                                ventana.blit(texto1, (10, 31))
                                ventana.blit(texto2, ((ANCHO // 2) - 50, 350))
                        elif puntosCrupier4 < 17:
                            cartaCrupier5(ventana, cartaCrup5, cartaCrupierx5, cartaCrupiery5)
                            puntosCrupier5 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4 + cartaCrup5
                            if puntosCrupier5 > 16:
                                if puntosCrupier5 > puntosMios and puntosCrupier5 <22:
                                    texto1 = fuente.render("DINERO: $" + dineroActual, 1, blanco)
                                    texto2 = fuente.render("PERDISTE!!!", 1, blanco)
                                    ventana.blit(texto1, (10, 31))
                                    ventana.blit(texto2, ((ANCHO // 2) - 50, 350))

                                    entrada = open("dinero.txt", "w", encoding="UTF-8")
                                    lineaSalida = (archivoperdido)
                                    entrada.write(lineaSalida)
                                    entrada.close()
                                elif puntosCrupier5 < puntosMios or puntosCrupier5 >21:
                                    texto1 = fuente.render("DINERO: $" + dineroActualGanado, 1, blanco)
                                    texto2 = fuente.render("GANASTE!!!", 1, blanco)
                                    ventana.blit(texto1, (10, 31))
                                    ventana.blit(texto2, ((ANCHO // 2) - 50, 350))
                                    entrada = open("dinero.txt", "w", encoding="UTF-8")
                                    lineaSalida = (archivoGanado)
                                    entrada.write(lineaSalida)
                                    entrada.close()
                                elif puntosCrupier5 == puntosMios:
                                    texto1 = fuente.render("DINERO: $" + linea, 1, blanco)
                                    texto2 = fuente.render("EMPATE!!!", 1, blanco)
                                    ventana.blit(texto1, (10, 31))
                                    ventana.blit(texto2, ((ANCHO // 2) - 50, 350))
                            elif puntosCrupier5 < 17:
                                cartaCrupier6(ventana, cartaCrup6, cartaCrupierx6, cartaCrupiery6)
                                puntosCrupier6 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4 + cartaCrup5 + cartaCrup6
                                if puntosCrupier6 > puntosMios and puntosCrupier6 <22:
                                    texto1 = fuente.render("DINERO: $" + dineroActual, 1, blanco)
                                    texto2 = fuente.render("PERDISTE!!!", 1, blanco)
                                    ventana.blit(texto1, (10, 31))
                                    ventana.blit(texto2, ((ANCHO // 2) - 50, 350))

                                    entrada = open("dinero.txt", "w", encoding="UTF-8")
                                    lineaSalida = (archivoperdido)
                                    entrada.write(lineaSalida)
                                    entrada.close()
                                elif puntosCrupier6 < puntosMios or puntosCrupier6 >21:
                                    texto1 = fuente.render("DINERO: $" + dineroActualGanado, 1, blanco)
                                    texto2 = fuente.render("GANASTE!!!", 1, blanco)
                                    ventana.blit(texto1, (10, 31))
                                    ventana.blit(texto2, ((ANCHO // 2) - 50, 350))
                                    entrada = open("dinero.txt", "w", encoding="UTF-8")
                                    lineaSalida = (archivoGanado)
                                    entrada.write(lineaSalida)
                                    entrada.close()
                                elif puntosCrupier6 == puntosMios:
                                    texto1 = fuente.render("DINERO: $" + linea, 1, blanco)
                                    texto2 = fuente.render("EMPATE!!!", 1, blanco)
                                    ventana.blit(texto1, (10, 31))
                                    ventana.blit(texto2, ((ANCHO // 2) - 50, 350))

######################################## ESTADO DEL JUEGO: JUEGO RENDIDO ###############################################
        if estadoJuego == JUEGORENDIDO:
            ventana.blit(imgFondoJuego, (0, 0))
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
            ventana.blit(spriteBtnReapostar.image, spriteBtnReapostar.rect)
            cartaCrupier1(ventana, cartaCrup1, cartaCrupierx1, cartaCrupiery1)
            miPrimeraCarta(ventana, carta1, yox1, yoy1)
            miSegundaCarta(ventana, carta2, yox2, yoy2)
            puntosCrupier = str(cartaCrup1)
            suma(carta1, carta2)
            dIint = int(dI)
            lineaInt = int(linea)
            apuesta = int(strdinero)
            apuestaRendida = str(apuesta)
            apuestaRendidaP = str(apuesta//2)
            dineroActualRen = str(lineaInt - apuesta//2)
            archivoRendido = str(lineaInt - apuesta // 2)
            texto1 = fuente.render("DINERO: $" + dineroActualRen, 1, blanco)
            texto2 = fuente.render("DINERO APOSTADO: $" + apuestaRendida, 1, blanco)
            texto3 = fuente.render("MIS PUNTOS: " + suma(carta1, carta2), 1, blanco)
            #texto4 = fuente.render("PUNTOSCRUPIER: " + puntosCrupier, 1, blanco)
            ventana.blit(texto1, (10, 31))
            ventana.blit(texto2, (10, 71))
            ventana.blit(texto3, (10, 111))
            #ventana.blit(texto4, (10, 151))
            texto1 = fuente.render("TE RENDISTE, PIERDES $" + apuestaRendidaP , 1, blanco)
            ventana.blit(texto1, (280, 350))
            entrada = open("dinero.txt", "w", encoding="UTF-8")
            lineaSalida = (archivoRendido)
            entrada.write(lineaSalida)
            entrada.close()


######################################## ESTADO DEL JUEGO: JUEGO CON 3 CARTAS ##########################################
        if estadoJuego == JUEGO3CARTAS:
            ventana.blit(imgFondoJuego, (0, 0))
            ventana.blit(spriteBtnPedir.image, spriteBtnPedir.rect)
            ventana.blit(spriteBtnPlantarse.image, spriteBtnPlantarse.rect)
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
            cartaCrupier1(ventana, cartaCrup1, cartaCrupierx1, cartaCrupiery1)
            miPrimeraCarta(ventana, carta1, yox1, yoy1)
            miSegundaCarta(ventana, carta2, yox2, yoy2)
            miTerceraCarta(ventana, carta3, yox3, yoy3)
            puntosCrupier = str(cartaCrup1)
            dIint = int(dI)
            lineaInt = int(linea)
            apuesta = int(strdinero)
            dineroActual = str(lineaInt - apuesta)
            suma3cartas(carta1, carta2, carta3)
            puntos(suma3cartas(carta1, carta2, carta3))
            archivoperdido = dineroActual
            archivoGanado = str(lineaInt + apuesta)
            texto1 = fuente.render("DINERO: $" + dineroActual, 1, blanco)
            texto2 = fuente.render("DINERO APOSTADO: $" + strdinero, 1, blanco)
            texto3 = fuente.render("MIS PUNTOS: " + suma3cartas(carta1, carta2, carta3), 1, blanco)
            ventana.blit(texto1, (10, 31))
            ventana.blit(texto2, (10, 71))
            ventana.blit(texto3, (10, 111))
            if puntos(suma3cartas(carta1, carta2, carta3))> 21:
                ventana.blit(spriteBtnReapostar.image, spriteBtnReapostar.rect)
                texto1 = fuente.render("PERDISTE, MAS DE 21 PUNTOS!", 1, blanco)
                ventana.blit(texto1, (280, 350))
                entrada = open("dinero.txt", "w", encoding="UTF-8")
                lineaSalida = (archivoperdido)
                entrada.write(lineaSalida)
                entrada.close()

######################################## ESTADO DEL JUEGO: JUEGO CON 3 CARTAS PLANTADO #################################
        if estadoJuego == JUEGO3CARTASPLANTADO:
            ventana.blit(imgFondoJuego, (0, 0))
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
            ventana.blit(spriteBtnReapostar.image, spriteBtnReapostar.rect)
            cartaCrupier1(ventana, cartaCrup1, cartaCrupierx1, cartaCrupiery1)
            cartaCrupier2(ventana, cartaCrup2, cartaCrupierx2, cartaCrupiery2)
            miPrimeraCarta(ventana, carta1, yox1, yoy1)
            miSegundaCarta(ventana, carta2, yox2, yoy2)
            miTerceraCarta(ventana, carta3, yox3, yoy3)
            dIint = int(dI)
            lineaInt = int(linea)
            apuesta = int(strdinero)
            dineroActual = str(lineaInt - apuesta)
            suma3cartas(carta1, carta2, carta3)
            puntosMios =int(suma3cartas(carta1, carta2, carta3))
            puntos(suma3cartas(carta1, carta2, carta3))
            archivoperdido = dineroActual
            archivoGanado = str(lineaInt + apuesta)
            texto1 = fuente.render("DINERO: $" + dineroActual, 1, blanco)
            texto2 = fuente.render("DINERO APOSTADO: $" + strdinero, 1, blanco)
            texto3 = fuente.render("MIS PUNTOS: " + suma3cartas(carta1, carta2, carta3), 1, blanco)
            ventana.blit(texto1, (10, 31))
            ventana.blit(texto2, (10, 71))
            ventana.blit(texto3, (10, 111))
            if puntos(suma3cartas(carta1, carta2, carta3)) > 21:
                texto1 = fuente.render("PERDISTE, MAS DE 21 PUNTOS!", 1, blanco)
                ventana.blit(texto1, (280, 350))
                entrada = open("dinero.txt", "w", encoding="UTF-8")
                lineaSalida = (archivoperdido)
                entrada.write(lineaSalida)
                entrada.close()
            puntosCrupier2 = cartaCrup1 + cartaCrup2
            if puntosCrupier2 > 16:
                if puntosCrupier2 > puntosMios:
                    texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                    entrada = open("dinero.txt", "w", encoding="UTF-8")
                    lineaSalida = (archivoperdido)
                    entrada.write(lineaSalida)
                    entrada.close()
                elif puntosCrupier2 < puntosMios:
                    texto1 = fuente.render("GANASTE!!!", 1, blanco)
                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                    entrada = open("dinero.txt", "w", encoding="UTF-8")
                    lineaSalida = (archivoGanado)
                    entrada.write(lineaSalida)
                    entrada.close()
                elif puntosCrupier2 == puntosMios:
                    texto1 = fuente.render("EMPATE!!!", 1, blanco)
                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
            elif puntosCrupier2 < 17:
                cartaCrupier3(ventana, cartaCrup3, cartaCrupierx3, cartaCrupiery3)
                puntosCrupier3 = cartaCrup1 + cartaCrup2 + cartaCrup3
                if puntosCrupier3 > 16:
                    if puntosCrupier3 > puntosMios and puntosCrupier3 < 22:
                        texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                        ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                        entrada = open("dinero.txt", "w", encoding="UTF-8")
                        lineaSalida = (archivoperdido)
                        entrada.write(lineaSalida)
                        entrada.close()
                    elif puntosCrupier3 < puntosMios or puntosCrupier3 > 21:
                        texto1 = fuente.render("GANASTE!!!", 1, blanco)
                        ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                        entrada = open("dinero.txt", "w", encoding="UTF-8")
                        lineaSalida = (archivoGanado)
                        entrada.write(lineaSalida)
                        entrada.close()
                    elif puntosCrupier3 == puntosMios:
                        texto1 = fuente.render("EMPATE!!!", 1, blanco)
                        ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                elif puntosCrupier3 < 17:
                    cartaCrupier4(ventana, cartaCrup4, cartaCrupierx4, cartaCrupiery4)
                    puntosCrupier4 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4
                    if puntosCrupier4 > 16:
                        if puntosCrupier4 > puntosMios and puntosCrupier4 < 22:
                            texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                            ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                            entrada = open("dinero.txt", "w", encoding="UTF-8")
                            lineaSalida = (archivoperdido)
                            entrada.write(lineaSalida)
                            entrada.close()
                        elif puntosCrupier4 < puntosMios or puntosCrupier4 > 21:
                            texto1 = fuente.render("GANASTE!!!", 1, blanco)
                            ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                            entrada = open("dinero.txt", "w", encoding="UTF-8")
                            lineaSalida = (archivoGanado)
                            entrada.write(lineaSalida)
                            entrada.close()
                        elif puntosCrupier4 == puntosMios:
                            texto1 = fuente.render("EMPATE!!!", 1, blanco)
                            ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                    elif puntosCrupier4 < 17:
                        cartaCrupier5(ventana, cartaCrup5, cartaCrupierx5, cartaCrupiery5)
                        puntosCrupier5 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4 + cartaCrup5
                        if puntosCrupier5 > 16:
                            if puntosCrupier5 > puntosMios and puntosCrupier5 < 22:
                                texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoperdido)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier5 < puntosMios or puntosCrupier5 > 21:
                                texto1 = fuente.render("GANASTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoGanado)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier5 == puntosMios:
                                texto1 = fuente.render("EMPATE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                        elif puntosCrupier5 < 17:
                            cartaCrupier6(ventana, cartaCrup6, cartaCrupierx6, cartaCrupiery6)
                            puntosCrupier6 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4 + cartaCrup5 + cartaCrup6
                            if puntosCrupier6 > 16:
                                if puntosCrupier6 > puntosMios and puntosCrupier6 < 22:
                                    texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                    entrada = open("dinero.txt", "w", encoding="UTF-8")
                                    lineaSalida = (archivoperdido)
                                    entrada.write(lineaSalida)
                                    entrada.close()
                                elif puntosCrupier6 < puntosMios or puntosCrupier6 > 21:
                                    texto1 = fuente.render("GANASTE!!!", 1, blanco)
                                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                    entrada = open("dinero.txt", "w", encoding="UTF-8")
                                    lineaSalida = (archivoGanado)
                                    entrada.write(lineaSalida)
                                    entrada.close()
                                elif puntosCrupier6 == puntosMios:
                                    texto1 = fuente.render("EMPATE!!!", 1, blanco)
                                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))

######################################## ESTADO DEL JUEGO: JUEGO CON 4 CARTAS ##########################################
        if estadoJuego == JUEGO4CARTAS:
            ventana.blit(imgFondoJuego, (0, 0))
            ventana.blit(spriteBtnPedir.image, spriteBtnPedir.rect)
            ventana.blit(spriteBtnPlantarse.image, spriteBtnPlantarse.rect)
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
            cartaCrupier1(ventana, cartaCrup1, cartaCrupierx1, cartaCrupiery1)
            miPrimeraCarta(ventana, carta1, yox1, yoy1)
            miSegundaCarta(ventana, carta2, yox2, yoy2)
            miTerceraCarta(ventana, carta3, yox3, yoy3)
            miCuartaCarta(ventana, carta4, yox4, yoy4)
            dIint = int(dI)
            lineaInt = int(linea)
            apuesta = int(strdinero)
            dineroActual = str(lineaInt - apuesta)
            suma4cartas(carta1, carta2, carta3, carta4)
            puntos(suma4cartas(carta1, carta2, carta3, carta4))
            archivoperdido = dineroActual
            archivoGanado = str(lineaInt + apuesta)
            texto1 = fuente.render("DINERO: $" + dineroActual, 1, blanco)
            texto2 = fuente.render("DINERO APOSTADO: $" + strdinero, 1, blanco)
            texto3 = fuente.render("MIS  PUNTOS: " + suma4cartas(carta1, carta2, carta3, carta4), 1, blanco)
            ventana.blit(texto1, (10, 31))
            ventana.blit(texto2, (10, 71))
            ventana.blit(texto3, (10, 111))
            if puntos(suma4cartas(carta1, carta2, carta3, carta4)) > 21:
                ventana.blit(spriteBtnReapostar.image, spriteBtnReapostar.rect)
                texto1 = fuente.render("PERDISTE, MAS DE 21 PUNTOS!", 1, blanco)
                ventana.blit(texto1, (280, 320))
                entrada = open("dinero.txt", "w", encoding="UTF-8")
                lineaSalida = (archivoperdido)
                entrada.write(lineaSalida)
                entrada.close()

######################################## ESTADO DEL JUEGO: JUEGO CON 4 CARTAS PLANTADO #################################
        if estadoJuego == JUEGO4CARTASPLANTADO:
            ventana.blit(imgFondoJuego, (0, 0))
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
            ventana.blit(spriteBtnReapostar.image, spriteBtnReapostar.rect)
            cartaCrupier1(ventana, cartaCrup1, cartaCrupierx1, cartaCrupiery1)
            cartaCrupier2(ventana, cartaCrup2, cartaCrupierx2, cartaCrupiery2)
            miPrimeraCarta(ventana, carta1, yox1, yoy1)
            miSegundaCarta(ventana, carta2, yox2, yoy2)
            miTerceraCarta(ventana, carta3, yox3, yoy3)
            miCuartaCarta(ventana, carta4, yox4, yoy4)
            dIint = int(dI)
            lineaInt = int(linea)
            apuesta = int(strdinero)
            dineroActual = str(lineaInt - apuesta)
            suma4cartas(carta1, carta2, carta3, carta4)
            puntos(suma4cartas(carta1, carta2, carta3, carta4))
            puntosMios = int(suma4cartas(carta1, carta2, carta3, carta4))
            archivoperdido = dineroActual
            archivoGanado = str(lineaInt + apuesta)
            texto1 = fuente.render("DINERO: $" + dineroActual, 1, blanco)
            texto2 = fuente.render("DINERO APOSTADO: $" + strdinero, 1, blanco)
            texto3 = fuente.render("MIS PUNTOS: " + suma4cartas(carta1, carta2, carta3, carta4), 1, blanco)
            ventana.blit(texto1, (10, 31))
            ventana.blit(texto2, (10, 71))
            ventana.blit(texto3, (10, 111))
            if puntos(suma4cartas(carta1, carta2, carta3, carta4)) > 21:
                texto1 = fuente.render("PERDISTE, MAS DE 21 PUNTOS!", 1, blanco)
                ventana.blit(texto1, (280, 320))
                entrada = open("dinero.txt", "w", encoding="UTF-8")
                lineaSalida = (archivoperdido)
                entrada.write(lineaSalida)
                entrada.close()
            puntosCrupier2 = cartaCrup1 + cartaCrup2
            if puntosCrupier2 > 16:
                if puntosCrupier2 > puntosMios:
                    texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                    entrada = open("dinero.txt", "w", encoding="UTF-8")
                    lineaSalida = (archivoperdido)
                    entrada.write(lineaSalida)
                    entrada.close()
                elif puntosCrupier2 < puntosMios:
                    texto1 = fuente.render("GANASTE!!!", 1, blanco)
                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                    entrada = open("dinero.txt", "w", encoding="UTF-8")
                    lineaSalida = (archivoGanado)
                    entrada.write(lineaSalida)
                    entrada.close()
                elif puntosCrupier2 == puntosMios:
                    texto1 = fuente.render("EMPATE!!!", 1, blanco)
                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
            elif puntosCrupier2 < 17:
                cartaCrupier3(ventana, cartaCrup3, cartaCrupierx3, cartaCrupiery3)
                puntosCrupier3 = cartaCrup1 + cartaCrup2 + cartaCrup3
                if puntosCrupier3 > 16:
                    if puntosCrupier3 > puntosMios and puntosCrupier3 < 22:
                        texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                        ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                        entrada = open("dinero.txt", "w", encoding="UTF-8")
                        lineaSalida = (archivoperdido)
                        entrada.write(lineaSalida)
                        entrada.close()
                    elif puntosCrupier3 < puntosMios or puntosCrupier3 > 21:
                        texto1 = fuente.render("GANASTE!!!", 1, blanco)
                        ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                        entrada = open("dinero.txt", "w", encoding="UTF-8")
                        lineaSalida = (archivoGanado)
                        entrada.write(lineaSalida)
                        entrada.close()
                    elif puntosCrupier3 == puntosMios:
                        texto1 = fuente.render("EMPATE!!!", 1, blanco)
                        ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                        entrada = open("dinero.txt", "w", encoding="UTF-8")
                        lineaSalida = (archivoGanado)
                        entrada.write(lineaSalida)
                        entrada.close()
                elif puntosCrupier3 < 17:
                    cartaCrupier4(ventana, cartaCrup4, cartaCrupierx4, cartaCrupiery4)
                    puntosCrupier4 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4
                    if puntosCrupier4 > 16:
                        if puntosCrupier4 > puntosMios and puntosCrupier4 < 22:
                            texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                            ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                            entrada = open("dinero.txt", "w", encoding="UTF-8")
                            lineaSalida = (archivoperdido)
                            entrada.write(lineaSalida)
                            entrada.close()
                        elif puntosCrupier4 < puntosMios or puntosCrupier4 > 21:
                            texto1 = fuente.render("GANASTE!!!", 1, blanco)
                            ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                            entrada = open("dinero.txt", "w", encoding="UTF-8")
                            lineaSalida = (archivoGanado)
                            entrada.write(lineaSalida)
                            entrada.close()
                        elif puntosCrupier4 == puntosMios:
                            texto1 = fuente.render("EMPATE!!!", 1, blanco)
                            ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                    elif puntosCrupier4 < 17:
                        cartaCrupier5(ventana, cartaCrup5, cartaCrupierx5, cartaCrupiery5)
                        puntosCrupier5 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4 + cartaCrup5
                        if puntosCrupier5 > 16:
                            if puntosCrupier5 > puntosMios and puntosCrupier5 < 22:
                                texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoperdido)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier5 < puntosMios or puntosCrupier5 > 21:
                                texto1 = fuente.render("GANASTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoGanado)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier5 == puntosMios:
                                texto1 = fuente.render("EMPATE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                        elif puntosCrupier5 < 17:
                            cartaCrupier6(ventana, cartaCrup6, cartaCrupierx6, cartaCrupiery6)
                            puntosCrupier6 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4 + cartaCrup5 + cartaCrup6
                            if puntosCrupier6 > puntosMios and puntosCrupier6 < 22:
                                texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoperdido)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier6 < puntosMios or puntosCrupier6 > 21:
                                texto1 = fuente.render("GANASTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoGanado)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier6 == puntosMios:
                                texto1 = fuente.render("EMPATE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))

######################################## ESTADO DEL JUEGO: JUEGO CON 5 CARTAS ##########################################
        if estadoJuego == JUEGO5CARTAS:
            ventana.blit(imgFondoJuego, (0, 0))
            ventana.blit(spriteBtnPedir.image, spriteBtnPedir.rect)
            ventana.blit(spriteBtnPlantarse.image, spriteBtnPlantarse.rect)
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
            cartaCrupier1(ventana, cartaCrup1, cartaCrupierx1, cartaCrupiery1)
            miPrimeraCarta(ventana, carta1, yox1, yoy1)
            miSegundaCarta(ventana, carta2, yox2, yoy2)
            miTerceraCarta(ventana, carta3, yox3, yoy3)
            miCuartaCarta(ventana, carta4, yox4, yoy4)
            miQuintaCarta(ventana, carta5, yox5, yoy5)
            dIint = int(dI)
            lineaInt = int(linea)
            apuesta = int(strdinero)
            dineroActual = str(linea - apuesta)
            suma5cartas(carta1, carta2, carta3, carta4, carta5)
            puntos(suma5cartas(carta1, carta2, carta3, carta4, carta5))
            archivoperdido = dineroActual
            archivoGanado = str(lineaInt + apuesta)
            texto1 = fuente.render("DINERO: $" + dineroActual, 1, blanco)
            texto2 = fuente.render("DINERO APOSTADO: $" + strdinero, 1, blanco)
            texto3 = fuente.render("MISPUNTOS: " + suma5cartas(carta1, carta2, carta3, carta4, carta5), 1, blanco)
            ventana.blit(texto1, (10, 31))
            ventana.blit(texto2, (10, 71))
            ventana.blit(texto3, (10, 111))
            if puntos(suma5cartas(carta1, carta2, carta3, carta4, carta5)) > 21:
                ventana.blit(spriteBtnReapostar.image, spriteBtnReapostar.rect)
                texto1 = fuente.render("PERDISTE, MAS DE 21 PUNTOS!", 1, blanco)
                ventana.blit(texto1, (280, 300))
            entrada = open("dinero.txt", "w", encoding="UTF-8")
            lineaSalida = (archivoperdido)
            entrada.write(lineaSalida)
            entrada.close()

######################################## ESTADO DEL JUEGO: JUEGO CON 5 CARTAS PLANTADO #################################
        if estadoJuego == JUEGO5CARTASPLANTADO:
            ventana.blit(imgFondoJuego, (0, 0))
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
            ventana.blit(spriteBtnReapostar.image, spriteBtnReapostar.rect)
            cartaCrupier1(ventana, cartaCrup1, cartaCrupierx1, cartaCrupiery1)
            cartaCrupier2(ventana, cartaCrup2, cartaCrupierx2, cartaCrupiery2)
            miPrimeraCarta(ventana, carta1, yox1, yoy1)
            miSegundaCarta(ventana, carta2, yox2, yoy2)
            miTerceraCarta(ventana, carta3, yox3, yoy3)
            miCuartaCarta(ventana, carta4, yox4, yoy4)
            miQuintaCarta(ventana, carta5, yox5, yoy5)
            dIint = int(dI)
            lineaInt = int(linea)
            apuesta = int(strdinero)
            dineroActual = str(linea - apuesta)
            suma5cartas(carta1, carta2, carta3, carta4, carta5)
            puntos(suma5cartas(carta1, carta2, carta3, carta4, carta5))
            puntosMios = int(suma5cartas(carta1, carta2, carta3, carta4, carta5))
            archivoperdido = dineroActual
            archivoGanado = str(lineaInt + apuesta)
            texto1 = fuente.render("DINERO: $" + dineroActual, 1, blanco)
            texto2 = fuente.render("DINERO APOSTADO: $" + strdinero, 1, blanco)
            texto3 = fuente.render("MISPUNTOS: " + suma5cartas(carta1, carta2, carta3, carta4, carta5), 1,blanco)
            ventana.blit(texto1, (10, 31))
            ventana.blit(texto2, (10, 71))
            ventana.blit(texto3, (10, 111))
            if puntos(suma5cartas(carta1, carta2, carta3, carta4, carta5)) > 21:
                texto1 = fuente.render("PERDISTE, MAS DE 21 PUNTOS!", 1, blanco)
                ventana.blit(texto1, (280, 300))
                entrada = open("dinero.txt", "w", encoding="UTF-8")
                lineaSalida = (archivoperdido)
                entrada.write(lineaSalida)
                entrada.close()
            puntosCrupier2 = cartaCrup1 + cartaCrup2
            if puntosCrupier2 > 16:
                if puntosCrupier2 > puntosMios and puntosCrupier2 < 22:
                    texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                    entrada = open("dinero.txt", "w", encoding="UTF-8")
                    lineaSalida = (archivoperdido)
                    entrada.write(lineaSalida)
                    entrada.close()
                elif puntosCrupier2 < puntosMios or puntosCrupier2 > 21:
                    texto1 = fuente.render("GANASTE!!!", 1, blanco)
                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                    entrada = open("dinero.txt", "w", encoding="UTF-8")
                    lineaSalida = (archivoGanado)
                    entrada.write(lineaSalida)
                    entrada.close()
                elif puntosCrupier2 == puntosMios:
                    texto1 = fuente.render("EMPATE!!!", 1, blanco)
                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
            elif puntosCrupier2 < 17:
                cartaCrupier3(ventana, cartaCrup3, cartaCrupierx3, cartaCrupiery3)
                puntosCrupier3 = cartaCrup1 + cartaCrup2 + cartaCrup3
                if puntosCrupier3 > 16:
                    if puntosCrupier3 > puntosMios and puntosCrupier3 < 22:
                        texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                        ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                        entrada = open("dinero.txt", "w", encoding="UTF-8")
                        lineaSalida = (archivoperdido)
                        entrada.write(lineaSalida)
                        entrada.close()
                    elif puntosCrupier3 < puntosMios or puntosCrupier3 > 21:
                        texto1 = fuente.render("GANASTE!!!", 1, blanco)
                        ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                        entrada = open("dinero.txt", "w", encoding="UTF-8")
                        lineaSalida = (archivoGanado)
                        entrada.write(lineaSalida)
                        entrada.close()
                    elif puntosCrupier3 == puntosMios:
                        texto1 = fuente.render("EMPATE!!!", 1, blanco)
                        ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                elif puntosCrupier3 < 17:
                    cartaCrupier4(ventana, cartaCrup4, cartaCrupierx4, cartaCrupiery4)
                    puntosCrupier4 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4
                    if puntosCrupier4 > 16:
                        if puntosCrupier4 > puntosMios and puntosCrupier4 < 22:
                            texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                            ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                            entrada = open("dinero.txt", "w", encoding="UTF-8")
                            lineaSalida = (archivoperdido)
                            entrada.write(lineaSalida)
                            entrada.close()
                        elif puntosCrupier4 < puntosMios or puntosCrupier4 > 21:
                            texto1 = fuente.render("GANASTE!!!", 1, blanco)
                            ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                            entrada = open("dinero.txt", "w", encoding="UTF-8")
                            lineaSalida = (archivoGanado)
                            entrada.write(lineaSalida)
                            entrada.close()
                        elif puntosCrupier4 == puntosMios:
                            texto1 = fuente.render("EMPATE!!!", 1, blanco)
                            ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                    elif puntosCrupier4 < 17:
                        cartaCrupier5(ventana, cartaCrup5, cartaCrupierx5, cartaCrupiery5)
                        puntosCrupier5 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4 + cartaCrup5
                        if puntosCrupier5 > 16:
                            if puntosCrupier5 > puntosMios and puntosCrupier5 < 22:
                                texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoperdido)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier5 < puntosMios or puntosCrupier5 > 21:
                                texto1 = fuente.render("GANASTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoGanado)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier5 == puntosMios:
                                texto1 = fuente.render("EMPATE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                        elif puntosCrupier5 < 17:
                            cartaCrupier6(ventana, cartaCrup6, cartaCrupierx6, cartaCrupiery6)
                            puntosCrupier6 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4 + cartaCrup5 + cartaCrup6
                            if puntosCrupier6 > puntosMios and puntosCrupier6 < 22:
                                texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoperdido)
                                entrada.write(lineaSalida)
                                entrada.close()
                                ventana.blit(spriteBtnReapostar.image, spriteBtnReapostar.rect)
                            elif puntosCrupier6 < puntosMios or puntosCrupier6 > 21:
                                texto1 = fuente.render("GANASTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoGanado)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier6 == puntosMios:
                                texto1 = fuente.render("EMPATE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))

######################################## ESTADO DEL JUEGO: JUEGO CON 6 CARTAS ##########################################
        if estadoJuego == JUEGO6CARTAS:
            ventana.blit(imgFondoJuego, (0, 0))
            ventana.blit(spriteBtnPlantarse.image, spriteBtnPlantarse.rect)
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
            cartaCrupier1(ventana, cartaCrup1, cartaCrupierx1, cartaCrupiery1)
            miPrimeraCarta(ventana, carta1, yox1, yoy1)
            miSegundaCarta(ventana, carta2, yox2, yoy2)
            miTerceraCarta(ventana, carta3, yox3, yoy3)
            miCuartaCarta(ventana, carta4, yox4, yoy4)
            miQuintaCarta(ventana, carta5, yox5, yoy5)
            miSextaCarta(ventana, carta6, yox6, yoy6)
            apuesta = int(strdinero)
            dineroActual = str(linea - apuesta)
            archivoperdido = dineroActual
            archivoGanado = str(lineaInt + apuesta)
            dIint = int(dI)
            lineaInt = int(linea)
            suma5cartas(carta1, carta2, carta3, carta4, carta5)
            puntos(suma5cartas(carta1, carta2, carta3, carta4, carta5))
            texto1 = fuente.render("DINERO: $" + dineroActual, 1, blanco)
            texto2 = fuente.render("DINERO APOSTADO: $" + strdinero, 1, blanco)
            texto3 = fuente.render("MISPUNTOS: " + suma6cartas(carta1, carta2, carta3, carta4, carta5, carta6), 1, blanco)
            ventana.blit(texto1, (10, 31))
            ventana.blit(texto2, (10, 71))
            ventana.blit(texto3, (10, 111))
            if puntos(suma6cartas(carta1, carta2, carta3, carta4, carta5, carta6)) > 21:
                ventana.blit(spriteBtnReapostar.image, spriteBtnReapostar.rect)
                texto1 = fuente.render("PERDISTE, MAS DE 21 PUNTOS!", 1, blanco)
                ventana.blit(texto1, (280, 300))
                entrada = open("dinero.txt", "w", encoding="UTF-8")
                lineaSalida = (archivoperdido)
                entrada.write(lineaSalida)
                entrada.close()


######################################## ESTADO DEL JUEGO: JUEGO CON 6 CARTAS PLANTADO #################################
        if estadoJuego == JUEGO6CARTASPLANTADO:
            ventana.blit(imgFondoJuego, (0, 0))
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)
            ventana.blit(spriteBtnReapostar.image, spriteBtnReapostar.rect)
            cartaCrupier1(ventana, cartaCrup1, cartaCrupierx1, cartaCrupiery1)
            cartaCrupier2(ventana, cartaCrup2, cartaCrupierx2, cartaCrupiery2)
            miPrimeraCarta(ventana, carta1, yox1, yoy1)
            miSegundaCarta(ventana, carta2, yox2, yoy2)
            miTerceraCarta(ventana, carta3, yox3, yoy3)
            miCuartaCarta(ventana, carta4, yox4, yoy4)
            miQuintaCarta(ventana, carta5, yox5, yoy5)
            miSextaCarta(ventana, carta6, yox6, yoy6)
            lineaInt = int(linea)
            dIint = int(dI)
            apuesta = int(strdinero)
            dineroActual = str(linea - apuesta)
            suma6cartas(carta1, carta2, carta3, carta4, carta5, carta6)
            puntosMios = int(suma6cartas(carta1, carta2, carta3, carta4, carta5, carta6))
            puntos(suma5cartas(carta1, carta2, carta3, carta4, carta5))
            archivoperdido = dineroActual
            archivoGanado = str(lineaInt + apuesta)
            texto1 = fuente.render("DINERO: $" + dineroActual, 1, blanco)
            texto2 = fuente.render("DINERO APOSTADO: $" + strdinero, 1, blanco)
            texto3 = fuente.render("MISPUNTOS: " + suma6cartas(carta1, carta2, carta3, carta4, carta5, carta6),1, blanco)
            ventana.blit(texto1, (10, 31))
            ventana.blit(texto2, (10, 71))
            ventana.blit(texto3, (10, 111))
            if puntos(suma5cartas(carta1, carta2, carta3, carta4, carta5)) > 21:
                texto1 = fuente.render("PERDISTE, MAS DE 21 PUNTOS!", 1, blanco)
                ventana.blit(texto1, (280, 300))
                entrada = open("dinero.txt", "w", encoding="UTF-8")
                lineaSalida = (archivoperdido)
                entrada.write(lineaSalida)
                entrada.close()
            puntosCrupier2 = cartaCrup1 + cartaCrup2
            if puntosCrupier2 > 16:
                if puntosCrupier2 > puntosMios and puntosCrupier2 < 22:
                    texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                    entrada = open("dinero.txt", "w", encoding="UTF-8")
                    lineaSalida = (archivoperdido)
                    entrada.write(lineaSalida)
                    entrada.close()
                elif puntosCrupier2 < puntosMios or puntosCrupier2 > 21:
                    texto1 = fuente.render("GANASTE!!!", 1, blanco)
                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                elif puntosCrupier2 == puntosMios:
                    texto1 = fuente.render("EMPATE!!!", 1, blanco)
                    ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
            elif puntosCrupier2 < 17:
                cartaCrupier3(ventana, cartaCrup3, cartaCrupierx3, cartaCrupiery3)
                puntosCrupier3 = cartaCrup1 + cartaCrup2 + cartaCrup3
                if puntosCrupier3 > 16:
                    if puntosCrupier3 > puntosMios and puntosCrupier3 < 22:
                        texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                        ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                        entrada = open("dinero.txt", "w", encoding="UTF-8")
                        lineaSalida = (archivoperdido)
                        entrada.write(lineaSalida)
                        entrada.close()
                    elif puntosCrupier3 < puntosMios or puntosCrupier3 > 21:
                        texto1 = fuente.render("GANASTE!!!", 1, blanco)
                        ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                        entrada = open("dinero.txt", "w", encoding="UTF-8")
                        lineaSalida = (archivoGanado)
                        entrada.write(lineaSalida)
                        entrada.close()
                    elif puntosCrupier3 == puntosMios:
                        texto1 = fuente.render("EMPATE!!!", 1, blanco)
                        ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                elif puntosCrupier3 < 17:
                    cartaCrupier4(ventana, cartaCrup4, cartaCrupierx4, cartaCrupiery4)
                    puntosCrupier4 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4
                    if puntosCrupier4 > 16:
                        if puntosCrupier4 > puntosMios and puntosCrupier4 < 22:
                            texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                            ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                            entrada = open("dinero.txt", "w", encoding="UTF-8")
                            lineaSalida = (archivoperdido)
                            entrada.write(lineaSalida)
                            entrada.close()
                        elif puntosCrupier4 < puntosMios or puntosCrupier4 > 21:
                            texto1 = fuente.render("GANASTE!!!", 1, blanco)
                            ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                            entrada = open("dinero.txt", "w", encoding="UTF-8")
                            lineaSalida = (archivoGanado)
                            entrada.write(lineaSalida)
                            entrada.close()
                        elif puntosCrupier4 == puntosMios:
                            texto1 = fuente.render("EMPATE!!!", 1, blanco)
                            ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                    elif puntosCrupier4 < 17:
                        cartaCrupier5(ventana, cartaCrup5, cartaCrupierx5, cartaCrupiery5)
                        puntosCrupier5 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4 + cartaCrup5
                        if puntosCrupier5 > 16:
                            if puntosCrupier5 > puntosMios and puntosCrupier5 < 22:
                                texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoperdido)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier5 < puntosMios or puntosCrupier5 > 21:
                                texto1 = fuente.render("GANASTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoGanado)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier5 == puntosMios:
                                texto1 = fuente.render("EMPATE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                        elif puntosCrupier5 < 17:
                            cartaCrupier6(ventana, cartaCrup6, cartaCrupierx6, cartaCrupiery6)
                            puntosCrupier6 = cartaCrup1 + cartaCrup2 + cartaCrup3 + cartaCrup4 + cartaCrup5 + cartaCrup6
                            if puntosCrupier6 > puntosMios and puntosCrupier6 < 22:
                                texto1 = fuente.render("PERDISTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoperdido)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier6 < puntosMios or puntosCrupier6 > 21:
                                texto1 = fuente.render("GANASTE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))
                                entrada = open("dinero.txt", "w", encoding="UTF-8")
                                lineaSalida = (archivoGanado)
                                entrada.write(lineaSalida)
                                entrada.close()
                            elif puntosCrupier6 == puntosMios:
                                texto1 = fuente.render("EMPATE!!!", 1, blanco)
                                ventana.blit(texto1, ((ANCHO // 2) - 50, 350))

######################################## ESTADO DEL JUEGO: ACERCA DE #######################################################
        if estadoJuego == ACERCA_DE:
            ventana.blit(imgFondoAcercaDe, (0, 0))
            texto1 = fuente.render("PROYECTO FINAL: BLACKJACK UTILIZANDO PYGAME", 1, negro)
            texto2 = fuente.render("AUTOR: DAVID MEDINA MEDINA", 1, negro)
            texto3 = fuente.render("MATRICULA: A01653311", 1, negro)
            texto4 = fuente.render("¡¡¡ESTE JUEGO SE JUEGA CON LAS REGLAS OFICIALES DE BLACKJACK,", 1, negro)
            texto5 = fuente.render("SI NO SABE COMO JUGAR PRESIONAR BOTON AYUDA EN MENU!!!", 1, negro)
            ventana.blit(texto1, (11, 11))
            ventana.blit(texto2, (11, 61))
            ventana.blit(texto3, (11, 111))
            ventana.blit(texto4, (11, 161))
            ventana.blit(texto5, (11, 201))
            ventana.blit(spriteBtnRegresar.image, spriteBtnRegresar.rect)

######################################## ESTADO DEL JUEGO: AYUDA #######################################################
        if estadoJuego == AYUDA:
            ventana.blit(imgFondoAcercaDe, (0, 0))
            texto1 = fuente.render("REGLAS:", 1, negro)
            texto2 = fuente.render("PARA INICIAR JUEGO PRESIONAR BOTON [JUGAR] Y DESPUES HAZ CLICK SOBRE", 1, negro)
            texto3 = fuente.render("UNA DE LAS 4 FICHAS ROJAS QUE INDICARA LA CANTIDAD DE DINERO A APOSTAR,", 1, negro)
            texto4 = fuente.render("AL HACER ESO APARECERA EL BOTON [EMPEZAR], HACER CLICK EN ESTE PARA INICIAR", 1, negro)
            texto5 = fuente.render("JUEGO.", 1, negro)
            texto6 = fuente.render("EMPEZARAS CON DOS CARTAS Y SU VALOR ES SU NUMERO A EXEPCION DE ", 1, negro)
            texto7 = fuente.render("LA CARTA AS QUE VALDRA 1 O 11 SIENDO ESTE UN COMODIN (PERO SOLO PARA TI.)", 1, negro)
            texto8 = fuente.render("AL INICIO QUE EMPIECES CON TUS DOS CARTAS PODRAS PLANTARTE PARA JUGAR CON", 1, negro)
            texto9 = fuente.render("TUS CARTAS INICIALES CONTRA CRUPIER O PRESIONAR PEDIR PARA (TENER HASTA 5).", 1, negro)
            texto10 = fuente.render("PARA GANARLE AL CRUPIER TENDRAS QUE SACAR MEJORES VALORES QUE.", 1, negro)
            texto11 = fuente.render("EL, SIENDO ESTOS 21 O LO MAS CERCANO, SI TE PASAS PIERDES.", 1, negro)
            texto12 = fuente.render("EL CRUPIER PEDIRA CARTAS HASTA QUE OBTENGA VALORES DE 17 A 21,", 1, negro)
            texto13 = fuente.render("ARRIBA DE ESO PIERDE Y RECIBES LA MISMA CANTDAD APOSTADA,", 1, negro)
            texto14 = fuente.render("SI CON LAS PRIMERAS DOS CARTAS HACES 21 (UN AS Y UN 10) AUTOMATICAMENTE", 1, negro)
            texto15 = fuente.render("GANARAS Y RECIBIRAS 3 A 2 DE GANANCIAS.", 1, negro)
            texto16 = fuente.render("SI QUIERES DOBLAR PRESIONAR BOTON [DOBLAR], AUMENTARAS TU APUESTA AL DOBLE", 1, negro)
            texto17 = fuente.render("Y PODRAS TENER UNA TERCERA Y ULTIMA CARTA E IRAS CONTRA LAS CARTAS DEL CRUPIER.", 1, negro)
            texto18 = fuente.render("SI TIENES MAL JUEGO Y CREES QUE PERDERAS AL INICO DEL JUEGO PRESIONA EL BOTON", 1, negro)
            texto19 = fuente.render("[RENDIRSE] PARA RENDIRTE Y SOLO PERDERAS LA MITAD APOSTADA.", 1, negro)
            texto20 = fuente.render("AL ACABAR EL JUEGO PRESIONA EL BOTON [REAPOSTAR] PARA VOLVER A APOSTAR O", 1, negro)
            texto21 = fuente.render("PRESIONA BOTON [MENU] PARA REGRESAR AL MENU PRINCIPAL", 1, negro)
            texto22 = fuente.render("AL INICIO EMPESARAS CON $1000 PESOS, SI PIERDES Y QUIERES SEGUIR JUGANDO ", 1, negro)
            texto23 = fuente.render("PRESIONAR BOTON [+$$$] EN MENU DE APUESTA Y AUTOMATICAMENTE TU DINERO VOLVERA  ", 1, negro)
            texto24 = fuente.render("A SER $1000 (IGNORANDO TU DINERO ANTERIOR.)", 1, negro)
            texto25 = fuente.render("¡NOTA! LA UNICA DIFERENCIA DE REGLAS DE UN  BLACKJACK ", 1, negro)
            texto26 = fuente.render("NORMAL CON ESTE JUEGO ES QUE EL AS PARA CRUPIER", 1, negro)
            texto27 = fuente.render("NO ES COMODIN, SU VALOR ES 11 SOLAMENTE ", 1, negro)
            texto28 = fuente.render("¡¡¡DIVIERTANSE!!!", 1, negro)
            ventana.blit(texto1, (1, 6))
            ventana.blit(texto2, (1, 21+10))
            ventana.blit(texto3, (1, 41+10))
            ventana.blit(texto4, (1, 61+10))
            ventana.blit(texto5, (1, 81+10))
            ventana.blit(texto6, (1, 101+10))
            ventana.blit(texto7, (1, 121+10))
            ventana.blit(texto8, (1, 141+10))
            ventana.blit(texto9, (1, 161+10))
            ventana.blit(texto10, (1, 181+10))
            ventana.blit(texto11, (1, 201+10))
            ventana.blit(texto12, (1, 221+10))
            ventana.blit(texto13, (1, 241+10))
            ventana.blit(texto14, (1, 261+10))
            ventana.blit(texto15, (1, 281+10))
            ventana.blit(texto16, (1, 301+10))
            ventana.blit(texto17, (1, 321+10))
            ventana.blit(texto18, (1, 341+10))
            ventana.blit(texto19, (1, 361+10))
            ventana.blit(texto20, (1, 381+10))
            ventana.blit(texto21, (1, 401+10))
            ventana.blit(texto22, (1, 421+10))
            ventana.blit(texto23, (1, 441+10))
            ventana.blit(texto24, (1, 461+10))
            ventana.blit(texto25, (1, 481 + 10))
            ventana.blit(texto26, (1, 501 + 10))
            ventana.blit(texto27, (1, 521 + 10))
            ventana.blit(texto28, (1, 541 + 10))
            ventana.blit(spriteBtnRegresar.image, spriteBtnRegresar.rect)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

######################################## DESPUES DE CICLO PRINCIPAL ####################################################
    pygame.quit()  # termina pygame

######################################## FUNCION PRINCIPAL MAIN ########################################################
def main():
    entrada = open("dinero.txt", "r", encoding="UTF-8")
    linea = entrada.readline()
    dibujar(linea)
    entrada.close()

main()
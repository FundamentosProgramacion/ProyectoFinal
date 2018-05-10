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


# Dibuja la Bala 1
def dibujarBala1(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


# Dibuja la Bala 1
def dibujarBala2(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


# Agrega a la lista, Mueve la bala; Elimina la bala de la lista(Bala 1)
def actualizarBala1(listaBala1):
    # MOVER
    for bala in listaBala1:
        bala.rect.left -= 7

    for k in range(len(listaBala1) - 1, -1, -1):
        bala = listaBala1[k]
        if bala.rect.left <= - bala.rect.width:
            listaBala1.remove(bala)


# Agrega a la lista, Mueve la bala; Elimina la bala de la lista(Bala 2)
def actualizarBala2(listaBala2):
    for bala in listaBala2:
        bala.rect.left += 10

    for k in range(len(listaBala2) - 1, -1, -1):
        bala = listaBala2[k]
        if bala.rect.left >= 800:
            listaBala2.remove(bala)


# Crea las balas y la agraga a la lista que le corresponda
def creaBalas(ritmoBalas, imgBala, canon1, canon2, listaBala, efecto):
    efecto.set_volume(.1)
    efecto.play()
    if ritmoBalas % 2 == 0:
        bala1 = pygame.sprite.Sprite()
        bala1.image = imgBala
        bala1.rect = imgBala.get_rect()
        bala1.rect.left = canon1[0]
        bala1.rect.top = canon1[1]
        listaBala.append(bala1)
        return bala1

    else:
        bala2 = pygame.sprite.Sprite()
        bala2.image = imgBala
        bala2.rect = imgBala.get_rect()
        bala2.rect.left = canon2[0]
        bala2.rect.top = canon2[1]
        listaBala.append(bala2)

        return bala2


# Checa el impacto real.
def checarColisiones(listaBala1, listaBala2, personaje):
    impacto = False
    for tiro1 in range(len(listaBala1) - 1, -1, -1):
        bala1 = listaBala1[tiro1]
        xb, yb, ab, alb = bala1.rect
        xp, yp, ap, alp = personaje.rect
        if xp <= xb <= xp + ap and yp <= yb <= yp + alp:
            impacto = True

    for tiro2 in range(len(listaBala2) - 1, -1, -1):
        bala2 = listaBala2[tiro2]
        xb, yb, ab, alb = bala2.rect
        xp, yp, ap, alp = personaje.rect
        if xp <= xb <= xp + ap and yp <= yb <= yp + alp:
            impacto = True
    return impacto


def actualizarArchivo(vidas, puntuacion):
    if puntuacion == 0:
        pass
    else:
        dicc = {}
        dicc[puntuacion] = vidas
        scores = open("Puntajes.txt", "r+", encoding="UTF-8")
        linea = scores.readline()
        while linea != "":
            datos = linea.split(",")
            if len(datos)<1:
                pass
            else:
               dicc[int(datos[0])] = int(datos[1])
               linea = scores.readline()
               print(dicc)
        for crv in sorted(dicc,reverse=True):
            lineaSalida = "%i,%i" % (crv,dicc[crv])
            scores.write(lineaSalida)
            scores.write("\n")

        scores.close()




def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps

    termina = False  # Bandera para saber si termina la ejecución

    # EDOS DE JUEGO
    MENU = 1
    JUEGO = 3
    PUNTAJES = 4
    GAMEOVER = 5
    estadoDeJuego = MENU

    # FONDOS
    imgFondoJUEGO = pygame.image.load("fondo_JUEGO.png")
    imgFondoMENUS = pygame.image.load("fondo_MENU.png")
    imgFondoPUNTOS = pygame.image.load("fondo_PUNTOS.png")
    imgFondoGAMEOVER = pygame.image.load("fondo_GAMEOVER.png")

    #BOTTONES
    imgBtnJugar = pygame.image.load("button_jugar.png")
    spriteBtnJugar = pygame.sprite.Sprite()
    spriteBtnJugar.image = imgBtnJugar
    spriteBtnJugar.rect = imgBtnJugar.get_rect()
    spriteBtnJugar.rect.left = ANCHO // 2 - spriteBtnJugar.rect.width // 2
    spriteBtnJugar.rect.top = ALTO // 3 - spriteBtnJugar.rect.height // 2

    imgBtnPuntuaciones = pygame.image.load("button_puntuaciones.png")
    spriteBtnPuntuaciones = pygame.sprite.Sprite()
    spriteBtnPuntuaciones.image = imgBtnPuntuaciones
    spriteBtnPuntuaciones.rect = imgBtnPuntuaciones.get_rect()
    spriteBtnPuntuaciones.rect.left = ANCHO // 2 - spriteBtnPuntuaciones.rect.width // 2
    spriteBtnPuntuaciones.rect.top = spriteBtnJugar.rect.bottom + 10

    imgBtnSalir = pygame.image.load("button_salir.png")
    spriteBtnSalir = pygame.sprite.Sprite()
    spriteBtnSalir.image = imgBtnSalir
    spriteBtnSalir.rect = imgBtnSalir.get_rect()


    imgBtnMenu = pygame.image.load("button_menu.png")
    spriteBtnMenu = pygame.sprite.Sprite()
    spriteBtnMenu.image = imgBtnMenu
    spriteBtnMenu.rect = imgBtnMenu.get_rect()
    spriteBtnMenu.rect.left = 20
    spriteBtnMenu.rect.bottom = ALTO - 10


    # SFX
    pygame.mixer.init()
    efectoDanio = pygame.mixer.Sound("danio.wav")
    efectoSalto = pygame.mixer.Sound("salto.wav")
    efectoDisparo = pygame.mixer.Sound("shoot.wav")

    # MUSICA
    pygame.mixer.music.load("menus.wav")
    pygame.mixer.music.play(-1)

    # PLATAFORMAS
    imgPlataformas = pygame.image.load("plataforma.png")
    plataforma = pygame.sprite.Sprite()
    plataforma.image = imgPlataformas
    plataforma.rect = imgPlataformas.get_rect()
    listaPlataformas = []
    crearListaPlataformas(imgPlataformas, listaPlataformas)

    # PERSONAJE
    imgPersonaje = pygame.image.load("Personaje.png")
    personaje = pygame.sprite.Sprite()
    personaje.image = imgPersonaje
    personaje.rect = imgPersonaje.get_rect()
    personaje.rect.left = 150
    personaje.rect.top = (600 - plataforma.rect.height) - personaje.rect.height

    # CAÑON
    # El cañon
    imgcanon = pygame.image.load("canon.png")
    canon = pygame.sprite.Sprite()
    canon.image = imgcanon
    canon.rect = imgcanon.get_rect()

    # ESCALERA
    imgescalera = pygame.image.load("escaleras.png")
    escalera = pygame.sprite.Sprite()
    escalera.image = imgescalera
    escalera.rect = imgescalera.get_rect()
    escalera.rect.left = 550
    escalera.rect.top = (600 - plataforma.rect.height) - escalera.rect.height

    # BALAS
    imgBala = pygame.image.load("bala_Alfa.png")
    listaBala1 = []
    listaBala2 = []

    # BOOLEANOS
    # Movimiento
    moverPersonajeD = False
    moverPersonajeL = False
    # Salto
    estaSaltando = False
    # Escalar
    puedeEscalar = False
    estaEscalando = False
    subeEscalera = False
    bajaEscalera = False
    # Cañones
    dispara = False

    # Contadores
    # Es el que mide el tiempo para la formula de salto
    tiempoSalto = 0
    # Determina que cañon es el que esta disparando
    ritmoBalas = 0
    # Mide dirante cuantos FPS esta la bala en colision con el personaje
    impactoJuego = 0
    # Cuenta cuantas vidas hay.
    vidas = 5


    # Letras
    fuente = pygame.font.SysFont("monospace", 76)
    fuente2 = pygame.font.SysFont("blackoak std", 50)

    # Timer
    pygame.time.set_timer(pygame.USEREVENT, 500)

    while not termina:  # Ciclo principal
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            # Eventos en MENU

            if estadoDeJuego == MENU:
                spriteBtnSalir.rect.left = ANCHO // 2 - spriteBtnSalir.rect.width // 2
                spriteBtnSalir.rect.top = spriteBtnPuntuaciones.rect.bottom + 30
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    xm, ym = pygame.mouse.get_pos()
                    xbj, ybj, abj, albj = spriteBtnJugar.rect
                    if xbj <= xm <= xbj + abj:
                        if ybj <= ym <= ybj + albj:
                            cronometro = pygame.time.Clock()
                            estadoDeJuego = JUEGO
                            pygame.mixer.music.load("juego.mp3")
                            pygame.mixer.music.play(-1)

                    xbad, ybad, abad, albad = spriteBtnPuntuaciones.rect
                    if xbad <= xm <= xbad + abad:
                        if ybad <= ym <= ybad + albad:
                            estadoDeJuego = PUNTAJES

                    xbs, ybs, abs, albs = spriteBtnSalir.rect
                    if xbs <= xm <= xbs + abs:
                        if ybs <= ym <= ybs + albs:
                            termina = True

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        estadoDeJuego = GAMEOVER

            # Eventos en GAME OVER
            if estadoDeJuego == GAMEOVER:  # A PARTIR DE AQUI SON INSTRUCCIONES PARA EL -G O-

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    xm, ym = pygame.mouse.get_pos()
                    xbme, ybme, abme, albme = spriteBtnSalir.rect
                    if xbme <= xm <= xbme + abme:
                        if ybme <= ym <= ybme + albme:
                            termina = True
                    xbad, ybad, abad, albad = spriteBtnPuntuaciones.rect
                    if xbad <= xm <= xbad + abad:
                        if ybad <= ym <= ybad + albad:
                            pygame.mixer.music.load("menus.wav")
                            pygame.mixer.music.play(-1)
                            estadoDeJuego = PUNTAJES


            #if estadoDeJuego == PUNTAJES:


            # ----------Eventos del JUEGO.---------------------------------------------------------------------------------------

            if estadoDeJuego == JUEGO:
                # Indica cada cuento se dispara una bala.
                if evento.type == pygame.USEREVENT:
                    ritmoBalas += 1
                    # Dependiendo del ritmo es si se agrega la bala a la lista 1 o 2.
                    if ritmoBalas % 2 == 0:
                        bala1 = creaBalas(ritmoBalas, imgBala, canon1, canon2, listaBala1, efectoDisparo)
                    else:
                        bala2 = creaBalas(ritmoBalas, imgBala, canon1, canon2, listaBala2, efectoDisparo)
                    dispara = True
                # Revisa si la tecla especifica ESTA siendo presionada
                if evento.type == pygame.KEYDOWN:
                    # Para Movimiento X
                    if evento.key == pygame.K_LEFT:
                        moverPersonajeL = True
                    elif evento.key == pygame.K_RIGHT:
                        moverPersonajeD = True
                    # El evento de que quiera saltar,(No revisa si se mantiene apretado)
                    elif evento.key == pygame.K_SPACE and not estaSaltando:
                        efectoSalto.play()
                        estaSaltando = True
                        tiempoSalto = 0
                        y0 = personaje.rect.bottom
                    # Evento para subir o bajar escalera. (Si se revisa si se mantiene presionado o no.)
                    elif evento.key == pygame.K_UP and puedeEscalar:
                        subeEscalera = True
                        estaEscalando = True
                    elif evento.key == pygame.K_DOWN and puedeEscalar:
                        estaEscalando = True
                        bajaEscalera = True

                # Revisa si la tecla especifica NO ESTA siendo presionada
                elif evento.type == pygame.KEYUP:
                    # Para movimiento X
                    if evento.key == pygame.K_LEFT:
                        moverPersonajeL = False
                    elif evento.key == pygame.K_RIGHT:
                        moverPersonajeD = False
                    # Para Movimiento Y en Escalera
                    elif evento.key == pygame.K_UP and puedeEscalar:
                        subeEscalera = False
                        estaEscalando = True
                    elif evento.key == pygame.K_DOWN and puedeEscalar:
                        bajaEscalera = False
                        estaEscalando = True

        # Borrar pantalla
        ventana.fill((0,0,204))

        # Estados del Juego. (La mayoria de los dibujos se hacen aqui.)

        # Para MENU
        if estadoDeJuego == MENU:
            ventana.blit(imgFondoMENUS, (0, 0))
            # BOTTONES
            ventana.blit(imgBtnJugar, spriteBtnJugar.rect)
            ventana.blit(imgBtnPuntuaciones, spriteBtnPuntuaciones.rect)
            ventana.blit(imgBtnSalir, spriteBtnSalir.rect)

        if estadoDeJuego == PUNTAJES:
            ventana.blit(imgFondoPUNTOS, (0,0))
            lugar = 0
            scores = open("Puntajes.txt", "r", encoding="UTF-8")
            linea = scores.readline()
            while linea != "" and lugar<500:
                lista = linea.split(",")
                Tscore = fuente2.render("Vidas: %s  Puntuación: %s" % (lista[1], lista[0]), 1, BLANCO)
                ventana.blit(Tscore, (ANCHO // 2 - 200, 50 + lugar))
                lugar += 100
                linea = scores.readline()
            scores.close()




        # Para GAMEOVER
        if estadoDeJuego == GAMEOVER:
            spriteBtnSalir.rect.left = spriteBtnMenu.rect.left
            spriteBtnSalir.rect.top = spriteBtnMenu.rect.top
            spriteBtnPuntuaciones.rect.right = ANCHO - 10
            spriteBtnPuntuaciones.rect.bottom = ALTO - 10
            ventana.blit(imgFondoGAMEOVER, (0, 0))
            ventana.blit(imgBtnSalir, spriteBtnSalir.rect)
            ventana.blit(imgBtnPuntuaciones, spriteBtnPuntuaciones.rect)
            texto = fuente.render("GAME OVER", 1, BLANCO)
            ventana.blit(texto, (ANCHO // 2 - 200,30 ))
            TPuntaje = fuente2.render("Puntaje: %i" %puntuacion, 1, BLANCO)
            ventana.blit(TPuntaje, (ANCHO // 2-200, ALTO-50))




        # Para el JUEGO
        if estadoDeJuego == JUEGO:
            # Fondo
            ventana.blit(imgFondoJUEGO, (0, 0))
            Tvidas = fuente2.render("Vidas: %i" %vidas, 1, BLANCO)
            ventana.blit(Tvidas,(100,50))

            # Creacion de las  Plataformas
            dibujarPlataformas(ventana, listaPlataformas)

            # Dibujo y variables de la Escaleras
            ventana.blit(escalera.image, escalera.rect)
            areaMediaEscalera = escalera.rect.left + 20, escalera.rect.left + 40

            # EL CAÑON 1 Y BALA 1 SON LOS DE ABAJO ABAJO, EL CAÑON 2 Y BALA 2 SON LOS DE ARRIBA
            # Dibujo de Cañon 1
            canon.rect.left = 700 - canon.rect.width
            canon.rect.top = (600 - plataforma.rect.height) - canon.rect.height
            ventana.blit(canon.image, canon.rect)
            canon1 = (canon.rect.left, canon.rect.top)
            # Dibujo Cañon 2
            canon.rect.left = 100
            canon.rect.top = (600 - plataforma.rect.height) - 300 - canon.rect.height
            ventana.blit(canon.image, canon.rect)
            canon2 = (canon.rect.left, canon.rect.top)
            # Dibujo Balas
            if dispara:
                # Crea Balas 1
                dibujarBala1(ventana, listaBala1)
                actualizarBala1(listaBala1)
                # Crea balas 2
                dibujarBala2(ventana, listaBala2)
                actualizarBala2(listaBala2)

            # Dibujo y variebles del Personaje
            ventana.blit(personaje.image, personaje.rect)
            mitadPersonaje = (personaje.rect.left + personaje.rect.right) / 2

            # Revisa si el presonaje esta en posicion de escalar
            if mitadPersonaje in range(areaMediaEscalera[0], areaMediaEscalera[1]) and not estaSaltando:
                puedeEscalar = True
            else:
                puedeEscalar = False
            # Mueve al personaje Arriba o Abajo en la Escalera
            if subeEscalera and not personaje.rect.bottom == escalera.rect.top:
                personaje.rect.bottom -= 5
            if bajaEscalera and not personaje.rect.bottom == escalera.rect.bottom:
                personaje.rect.bottom += 5
            # Condicion para salir de la Escalera.
            if personaje.rect.bottom == escalera.rect.top or personaje.rect.bottom == escalera.rect.bottom:
                estaEscalando = False
            # Condiciones otras cuando esta en la escalera.
            if personaje.rect.bottom == escalera.rect.bottom + 1:
                estaEscalando = True
            if estaEscalando:
                personaje.rect.left = escalera.rect.left
                moverPersonajeL = False
                moverPersonajeD = False

            # Movimiento del personaje  a la derecha o izquierda
            if moverPersonajeL:
                personaje.rect.left -= 3
            if moverPersonajeD:
                personaje.rect.left += 3

            # Utiliza la ecacion de fisica para calcular su altura en un momento determinado. Cuanta con Gravedad y Vo
            if estaSaltando and not estaEscalando:
                # Formula fisica original: y = Vo*t - 1/2 a t**2 (se cambia 1/2)
                moveVertical = 6 * tiempoSalto - .8 * 0.25 * tiempoSalto ** 2
                personaje.rect.bottom = y0 - int(moveVertical)
                # Aterrizaje
                if y0 < personaje.rect.bottom:
                    personaje.rect.bottom = y0
                    estaSaltando = False
            # Revisa la colision entre Bala y Personaje
            impactoReal = checarColisiones(listaBala1, listaBala2, personaje)
            # Revisa las colisiones y resta vidas o da GAME OVER.
            # El impacto real es el instante en el que el personaje toca la bala.
            # El impacto juego es el que el juego reconoce como colision.
            if impactoReal:
                impactoJuego += 1
            if impactoJuego >= 5:
                vidas -= 1
                impactoJuego = 0
                efectoDanio.play(0, 500)
            if vidas <= 0:
                estadoDeJuego = GAMEOVER
                puntuacion = 0
            # Termina el JUEGO y da puntiacion final.
            if personaje.rect.left == canon2[0] + canon.rect.width:
                cronometro.tick()
                tiempoDeJuego = cronometro.get_rawtime()
                # La puntiacion consiste en el producto de las vidas restantes y el tiempo que se jugo -
                # A mas tiempo mas puntos.
                puntuacion = vidas * (tiempoDeJuego // 100)
                actualizarArchivo(vidas,puntuacion)
                estadoDeJuego = GAMEOVER




        pygame.display.flip()
        reloj.tick(40)
        tiempoSalto += 1

    pygame.quit()



def main():
    dibujar()



main()

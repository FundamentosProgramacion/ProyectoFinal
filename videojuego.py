#Autor: Jean Paul Esquivel Lobato
# Video Juego de Bob Esponja

import pygame # se importa la librerìa de pygame
from random import randint  # se importa la libreria de aleatorio

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (216, 15, 36)
AMARILLO = (255, 255, 0)

#Función que dibuja la pantalla
def dibujarAcerca(ventana):
    fuente = pygame.font.SysFont("Consolas", 35)                                     # crea la fuente
    fuente2 = pygame.font.SysFont("Courier", 25)
    fuente3 = pygame.font.SysFont("Courier", 30)
    fuente4 = pygame.font.SysFont("Courier", 20)
    fuente5 = pygame.font.SysFont("Courier", 60)
    fuentees = pygame.font.SysFont("Consolas", 28)

    texto = fuente.render("¡Hola! Soy Bob Esponja ", 1, AMARILLO)     # crea los textos
    texto2 = fuente2.render("¡Plankton quire robarse", 1, NEGRO)
    texto3 = fuente3.render("la fórmula secreta! ", 1, ROJO)
    texto4 = fuente2.render("Necesito tu ayuda compañero", 1, NEGRO)
    texto5 = fuente4.render("Usa las teclas  Arriba/Abajo", 1, NEGRO)
    texto6 = fuente4.render("para poder moverme", 1, NEGRO)
    texto7 = fuente5.render("Y",1,NEGRO)
    texto8 = fuente4.render("Usa la tecla espaciadora", 1, NEGRO)
    texto9 = fuente4.render("para poder disparar.", 1, NEGRO)
    textoim = fuentees.render("¡No dejes que se lleve la fórmula!", 1, AMARILLO)

    ventana.blit(texto, (360, 200))                   # dibuja los textos
    ventana.blit(texto2, (440, 250))
    ventana.blit(texto3, (450, 275))
    ventana.blit(texto4, (380, 310))
    ventana.blit(texto5, (450, 345))
    ventana.blit(texto6, (450, 365))
    ventana.blit(texto7, (670, 360))
    ventana.blit(texto8, (500, 410))
    ventana.blit(texto9, (555, 430))
    ventana.blit(textoim, (15, 550))

#Dibuja la pantalla de ganaste
def dibujarGanaste(ventana):
    fuente = pygame.font.SysFont("Consolas", 65)
    fuente2 = pygame.font.SysFont("Consolas", 35)
    texto = fuente.render("¡GANASTE!", 1, ROJO)
    texto1 = fuente2.render("Haz derrotado a Plakton", 1, BLANCO)
    texto2 = fuente2.render("...Eres el mejor...", 1, BLANCO)
    ventana.blit(texto, (400, 55))
    ventana.blit(texto1, (350, 145))
    ventana.blit(texto2,(430, 175))

#Dibuja la pantalla de perdiste
def dibujarPerdiste(ventana):
    fuente = pygame.font.SysFont("Consolas", 65)
    fuente1 = pygame.font.SysFont("Consolas", 30)
    texto = fuente.render("Rayos", 1, ROJO)
    ventana.blit(texto, (480, 180))
    texto1 = fuente1.render("Se ha llevado la fórmula", 1, NEGRO)
    ventana.blit(texto1, (370, 240))

#Dibuja las balas
def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)

#Acutaliza las balas
def actualizarBalas(listaBalas):
    # Mover cada bala
    for bala in listaBalas:
        bala.rect.left += 20
    # Remover las balas
    for k in range(len(listaBalas) - 1, -1, -1):  # al revés
        bala = listaBalas[k]
        if bala.rect.left > ANCHO:
            listaBalas.remove(bala)

#Crea todos los enemigos
def crearEnemigos(listaEnemigos, imgPlankton):
    cx = ANCHO                                             # genera coordenadas aleatorias en el eje x
    cy = randint(2, ALTO - 130)                            # genera coordenadas aleatorias en el eje y
    enemigo = pygame.sprite.Sprite()                       # crea el sprite del enemigo
    enemigo.img = imgPlankton                              # crea la imagen en sprite
    enemigo.rect = imgPlankton.get_rect()                  # obtiene los bordes de la imagen
    enemigo.rect.left = cx                                 # coordenada en el eje x
    enemigo.rect.top = cy                                  # coordenada en el eje y
    listaEnemigos.append(enemigo)                          # agrega los elementos a la lista

#Crea al enemigo especial
def crearEnemigosEs(listaEnemigoEs, imgKaren):
    cxn = ANCHO  # genera coordenadas aleatorias en el eje x
    cyn = randint(2, ALTO - 130)  # genera coordenadas aleatorias en el eje y
    enemigoEs = pygame.sprite.Sprite()  # crea el sprite del enemigo
    enemigoEs.img = imgKaren  # crea la imagen en sprite
    enemigoEs.rect = imgKaren.get_rect()  # obtiene los bordes de la imagen
    enemigoEs.rect.left = cxn  # coordenada en el eje x
    enemigoEs.rect.top = cyn  # coordenada en el eje y
    listaEnemigoEs.append(enemigoEs)  # agrega los elementos a la lista

# Dibuja TODOS los enemigos sobre la ventana
def dibujarEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.img, enemigo.rect)

# Dibuja TODOS los enemigos especiales sobre la ventana
def dibujarEnemigoEs(ventana, listaEnemigoEs):
    for enemigoEs in listaEnemigoEs:
        ventana.blit(enemigoEs.img, enemigoEs.rect)

# Mueve los enemigos
def moverEnemigos(listaEnemigos, efecto):  # desplaza a los enemigos por el eje x
    golpe = 0
    for enemigo in listaEnemigos:  # visita los elementos de la lista
        enemigo.rect.left -= 5     # lo mueve 50 unidades a la izquierda

    for k in range(len(listaEnemigos) - 1, -1, -1):  # visita la lista de enemigos
        enemigo = listaEnemigos[k]  # enemigo en indice k
        if enemigo.rect.left <  0:
            listaEnemigos.remove(enemigo)
            # Contarlo
            golpe += 1
            # efecto de sonido
            efecto.play()                    #reproduce el sonido
    return golpe

#mueve los enemigos especiales
def moverEnemigoEs(listaEnemigoEs, efecto):  # desplaza a los enemigos por el eje x
    golpe = 0
    for enemigoEs in listaEnemigoEs:  # visita los elementos de la lista
        enemigoEs.rect.left -= 10     # lo mueve 100 unidades a la izquierda

    for k in range(len(listaEnemigoEs) - 1, -1, -1):  # visita la lista de enemigos
        enemigoEs = listaEnemigoEs[k]  # enemigo en indice k
        if enemigoEs.rect.left <  0:
            listaEnemigoEs.remove(enemigoEs)
            # Contarlo
            golpe += 2
            # efecto de sonido
            efecto.play()                    #reproduce el sonido
    return golpe

#checa la colision del enemigo normal
def checarColisiones(listaBalas, listaEnemigos, efecto):
    destruidos = 0
    for iB in range(len(listaBalas) - 1, -1, -1):
        bala = listaBalas[iB]
        for iE in range(len(listaEnemigos) - 1, -1, -1):
            enemigo = listaEnemigos[iE]
            xb, yb, ab, alb = bala.rect
            xe, ye, ae, ale = enemigo.rect
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + ale:
                listaBalas.remove(bala)
                listaEnemigos.remove(enemigo)
                # Contarlo
                destruidos += 1
                # efecto de sonido
                efecto.play()  # reproduce el sonido
                efecto.set_volume(0.5)  # el volumen con el que se escuchará
                break
    return destruidos

def colisionEs(listaBalas, listaEnemigoEs, efecto):
    destruidosEs = 0
    for iB in range(len(listaBalas) - 1, -1, -1):
        bala = listaBalas[iB]
        for iEs in range(len(listaEnemigoEs) - 1, -1, -1):
            enemigoE = listaEnemigoEs[iEs]
            xb, yb, ab, alb = bala.rect
            xes, yes, aes, ales = enemigoE.rect
            if xb >= xes and xb <= xes + aes and yb >= yes and yb <= yes + ales:
                listaBalas.remove(bala)
                listaEnemigoEs.remove(enemigoE)
                # Contarlo
                destruidosEs += 3
                # efecto de sonido
                efecto.play()  # reproduce el sonido
                efecto.set_volume(0.5)  # el volumen con el que se escuchará
                break
    return destruidosEs

def mostrarPuntos(ventana, puntos): #muestra los puntos obtenidos
    fuente = pygame.font.SysFont("monospace",40)    #crea la fuente
    texto = fuente.render("Puntos: ",1,ROJO)  #crea el texto
    points = fuente.render(str(puntos),1,ROJO)    #guarda los puntos
    ventana.blit(texto,(10,30))     #dibuja el texto
    ventana.blit(points,(180,32))   #dibuja los puntos

def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    # imágenes
    # Pantallas
    imgFondo = pygame.image.load("pantallamenu.png")          # Pantalla del menú
    imgAD = pygame.image.load("pantallaacercade.png")         # Pantalla de acerca de
    imgJuego = pygame.image.load("pantallajuego.png")         # Pantalla del juego
    imgScore = pygame.image.load("pantallascore.png")         # Pantalla del score
    imgPerder = pygame.image.load("pantallaperdedor.png")     #Pantalla perdedor
    imgGanar = pygame.image.load("pantallaganador.png")       # Pantalla perdedor

    # Botones
    imgBtnJugar = pygame.image.load("jugar.png")  # botón de jugar
    imgBtnAcercaDe = pygame.image.load("acercade.png")  # botón de acerca de
    imgBtnScore = pygame.image.load("scores.png")  # botón de score
    imgBtnMenu = pygame.image.load("menu.png")  # botón de menú

    # Crea el spite del boton jugar
    spriteBtnJugar = pygame.sprite.Sprite()
    spriteBtnJugar.image = imgBtnJugar
    spriteBtnJugar.rect = imgBtnJugar.get_rect()
    spriteBtnJugar.rect.left = 280
    spriteBtnJugar.rect.top = 470

    # Crea el spite del boton acerca de
    spriteBtnAcercaDe = pygame.sprite.Sprite()
    spriteBtnAcercaDe.image = imgBtnAcercaDe
    spriteBtnAcercaDe.rect = imgBtnAcercaDe.get_rect()
    spriteBtnAcercaDe.rect.left = 10
    spriteBtnAcercaDe.rect.top = 470

    # Crea el spite del boton score
    spriteBtnScore = pygame.sprite.Sprite()
    spriteBtnScore.image = imgBtnScore
    spriteBtnScore.rect = imgBtnScore.get_rect()
    spriteBtnScore.rect.left = 540
    spriteBtnScore.rect.top = 470

    # Crea el sprite del botón menú
    spriteBtnMenu = pygame.sprite.Sprite()
    spriteBtnMenu.image = imgBtnMenu
    spriteBtnMenu.rect = imgBtnMenu.get_rect()
    spriteBtnMenu.rect.left = 550
    spriteBtnMenu.rect.top = 500

    # Personaje. Bob
    imgBob = pygame.image.load("bob.png")
    bob = pygame.sprite.Sprite()
    bob.image = imgBob
    bob.rect = imgBob.get_rect()
    bob.rect.left = 10  # posición x
    bob.rect.top = 300  # posición y
    vy = 0

    # Medusa
    imgBala = pygame.image.load("bala.png")
    listaBalas = []  # Al inicio no hay balas

    # ENEMIGOS
    # Enemigo1
    imgPlankton = pygame.image.load("enemigo.png")
    listaEnemigos = []
    # Enemigoespecial
    imgKaren = pygame.image.load("enemigo2.png")
    listaEnemigoEs = []

    # Canciones y sonidos
    pygame.mixer.init()
    pygame.mixer.music.load("cancionmenu.mp3")  # carga la cancion de menu
    pygame.mixer.music.play(-1)
    efectoDestruye = pygame.mixer.Sound("electrocutar.wav")
    efectoGolpe = pygame.mixer.Sound("golpe.wav")
    efectoGolpeK = pygame.mixer.Sound("golpekaren.wav")


    # ESTADOS del juego
    MENU = 1
    JUEGO = 2
    ACERCA_DE = 3
    SCORE = 4
    GANA = 5
    PIERDE = 7
    timer = 0
    timer2 = 0
    puntos = 0
    puntos2= 0
    fuente = pygame.font.SysFont("monospaced", 70)
    golpes = 0
    golpesE = 0
    upApretada, downApretada = False, False
    estadoJuego = MENU  # JUEGO, ACERCA_DE

    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:  # El usuario hizo click izquierdo al precionarlo
                xm, ym = pygame.mouse.get_pos()
                if estadoJuego == MENU:  # Estado juego
                    xbj, ybj, abj, albj = spriteBtnJugar.rect  # Lineas de jugar
                    if xm >= xbj and xm <= xbj + abj:
                        if ym >= ybj and ym <= ybj + albj:
                            estadoJuego = JUEGO  # Cambia al estado del juego
                            pygame.mixer.music.load("cancionjuego.mp3")  # carga la cancion del juego
                            pygame.mixer.music.play(-1)

                    xbac, ybac, abac, albac = spriteBtnAcercaDe.rect  # Lineas de acerca de
                    if xm >= xbac and xm <= xbac + abac:
                        if ym >= ybac and ym <= ybac + albac:
                            estadoJuego = ACERCA_DE  # Cambia al estado acerca de
                            pygame.mixer.music.load("cancionacercade.mp3")  # Carga la cancion de acerca de
                            pygame.mixer.music.play(-1)

                    xbsc, ybsc, absc, albsc = spriteBtnScore.rect  # Lineas de score
                    if xm >= xbsc and xm <= xbsc + absc:
                        if ym >= ybsc and ym <= ybsc + albsc:
                            estadoJuego = SCORE  # Cambia al estado score
                            pygame.mixer.music.load("cancionscore.mp3")  # carga la cancion de score
                            pygame.mixer.music.play(-1)

                elif estadoJuego == ACERCA_DE or estadoJuego == SCORE:
                    xbm, ybm, abm, albm = spriteBtnMenu.rect
                    if xm >= xbm and xm <= xbm + abm:
                        if ym >= ybm and ym <= ybm + albm:
                            estadoJuego = MENU
                            pygame.mixer.music.load("cancionmenu.mp3")  # carga la cancion de menu
                            pygame.mixer.music.play(-1)

            elif evento.type == pygame.KEYDOWN and estadoJuego == JUEGO:  # El usuario esta en el juego y presionó hacia arriba y hacia abajo
                # mover jugador
                if evento.key == pygame.K_UP:
                    if bob.rect.top > 5:
                        upApretada = True
                        vy -= 10
                    else:
                        vy = 0

                elif evento.key == pygame.K_DOWN:
                    if bob.rect.top < ALTO - 130:
                        downApretada = True
                        vy += 10
                    else:
                        vy = 0

            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_UP:
                    upApretada = False
                    if downApretada:
                        if bob.rect.top < ALTO - 130:
                            vy += 10
                        else:
                            vy = 0
                    else:
                        vy = 0

                elif evento.key == pygame.K_DOWN:
                    downApretada = False
                    if upApretada:
                        if bob.rect.top > 5:
                            vy -= 10
                        else:
                            vy = 0
                    else:
                        vy = 0

                        # dispara
                elif evento.key == pygame.K_SPACE:
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = ((bob.rect.left // 2) - 10) + bob.rect.width // 2
                    bala.rect.top = bob.rect.top
                    listaBalas.append(bala)

        bob.rect.move_ip(0, vy)
        # Borrar pantalla
        ventana.fill(NEGRO)

        # Dibuja todos los objetos que se necesita
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        if estadoJuego == MENU:  # Condición del menú
            ventana.blit(imgFondo, (0, 0))
            ventana.blit(spriteBtnJugar.image, spriteBtnJugar.rect)
            ventana.blit(spriteBtnAcercaDe.image, spriteBtnAcercaDe.rect)
            ventana.blit(spriteBtnScore.image, spriteBtnScore.rect)

        elif estadoJuego == ACERCA_DE:  # Condición de acerca de
            ventana.blit(imgAD, (0,0))
            dibujarAcerca(ventana)
            #ventana.blit(imgAD, (0, 0))
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)

        elif estadoJuego == SCORE:       # Condición de score
            ventana.blit(imgScore, (0, 0))
            ventana.blit(spriteBtnMenu.image, spriteBtnMenu.rect)

        elif estadoJuego == JUEGO:      # Condición de juego
            ventana.blit(imgJuego, (0, 0))
            ventana.blit(bob.image, bob.rect)
            # dibujar las balas
            dibujarBalas(ventana, listaBalas)
            # Actualizar
            actualizarBalas(listaBalas)
            # Dibujar enemigo
            if timer >= 1:  # si el timer es mayor o igual a 2
                crearEnemigos(listaEnemigos, imgPlankton)  # crea los enemigos
                timer = 0  # se reinicia el timer
            dibujarEnemigos(ventana, listaEnemigos)
            golpe1 = (moverEnemigos(listaEnemigos, efectoGolpe))
            golpes += golpe1

            if timer2 >= 5:  # si el timer es mayor o igual a 1
                crearEnemigosEs(listaEnemigoEs, imgKaren)  # crea los enemigo Especial
                timer2 = 0  # se reinicia el timer
            dibujarEnemigoEs(ventana, listaEnemigoEs)
            golpe2 =  (moverEnemigoEs(listaEnemigoEs, efectoGolpeK))
            golpesE += golpe2

            timer += 1 / 40  # se crea el timer y controla la rapidez en que aparece el enemigo
            timer2 += 1 / 80  # se crea el timer y controla la rapidez en que aparece el enemigo
            destruidos = checarColisiones(listaBalas, listaEnemigos, efectoDestruye)
            puntos += destruidos
            destruidosEs = colisionEs(listaBalas, listaEnemigoEs, efectoDestruye)
            puntos2 += destruidosEs

            totalGolpes = golpes + golpesE
            vida = pygame.image.load("vidas.png")  # carga la imagen
            fuente = pygame.font.SysFont("monospace", 30)  # crea la fuente
            texto = fuente.render("VIDAS: ", 1, BLANCO)  # crea el texto
            ventana.blit(texto, (10, 10))  # dibuja el texto

            if totalGolpes == 0:  # analiza las vidas
                ventana.blit(vida, (110, 10))
                ventana.blit(vida, (130, 10))
                ventana.blit(vida, (150, 10))
                ventana.blit(vida, (170, 10))
                ventana.blit(vida, (190, 10))
            elif totalGolpes == 1:
                ventana.blit(vida, (110, 10))
                ventana.blit(vida, (130, 10))
                ventana.blit(vida, (150, 10))
                ventana.blit(vida, (170, 10))
            elif totalGolpes == 2:
                ventana.blit(vida, (110, 10))
                ventana.blit(vida, (130, 10))
                ventana.blit(vida, (150, 10))
            elif totalGolpes == 3:
                ventana.blit(vida, (110, 10))
                ventana.blit(vida, (130, 10))
            elif totalGolpes == 4:
                ventana.blit(vida, (110, 10))
            elif totalGolpes >= 5:
                 estadoJuego = PIERDE

            totalpuntos = puntos + puntos2
            mostrarPuntos(ventana, totalpuntos)
            if totalpuntos >= 20:
                estadoJuego = GANA

        elif estadoJuego == GANA:        # Condición de gana
            ventana.blit(imgGanar, (0, 0))
            dibujarGanaste(ventana)

        elif estadoJuego == PIERDE:      # Condición de pierde
            ventana.blit(imgPerder, (0, 0))
            dibujarPerdiste(ventana)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def main():
    dibujar()

main()
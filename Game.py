# Autor: Guillermo Adrian Urbina Aguiñiiga
# Juego Megaman

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

def calcularTiempo():
    tiempo = pygame.time.get_ticks()
    return tiempo

def registrarPuntos(puntos):
    Hoja = open('Puntuaciones.txt', 'a')
    puntosFinales = str(puntos)
    Hoja.write('\n' + str(puntosFinales))
    Hoja.close()

def checarColisiones(listaBalas, listaEnemigos):
    for i in range(len(listaBalas) - 1, -1, -1):
        bala = listaBalas[i]
        xb, yb, ab, alb = bala.rect
        for l in range(len(listaEnemigos) - 1, -1, -1):
            enemigo = listaEnemigos[l]
            xe, ye, ae, ale = enemigo.rect
            if xb >= xe and yb <= ye and ab <= ae and alb >= ale:
                listaEnemigos.remove(enemigo)
                listaBalas.remove(bala)


def CrearBalas(ventana,listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)

def ActualizarBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.left += 15

    for i in range(len(listaBalas) - 1, -1, -1):
        bala = listaBalas[i]
        if bala.rect.height >= ANCHO:
            listaBalas.remove(bala)

def crearEnemigos(imgEnemigo, listaEnemigos):
    columna = 300
    fila = 200
    for i in range(1, 3, 1):
        for l in range(0, 3, 1):
            Enemigo = pygame.sprite.Sprite()
            Enemigo.image = imgEnemigo
            Enemigo.rect = imgEnemigo.get_rect()
            Enemigo.rect.left = 0 + columna * i
            Enemigo.rect.top = (100 + fila * l) - 47
            listaEnemigos.append(Enemigo)


def dibujarEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)

def crearPlataformas(imgPlataforma, listaPlataformas):
    columna = 300
    fila = 200
    for i in range (0,3,1):
        for l in range (0,3,1):
            Plataforma = pygame.sprite.Sprite()
            Plataforma.image = imgPlataforma
            Plataforma.rect = imgPlataforma.get_rect()
            Plataforma.rect.left = 0 + columna * i
            Plataforma.rect.top = 100 + fila * l
            listaPlataformas.append(Plataforma)

def dibujarPlataforma(ventana, listaPlataforma):
    for plataforma in listaPlataforma:
        ventana.blit(plataforma.image, plataforma.rect)


# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    # Estados Juego

    # Estados del juego
    Menu = 1
    Juego = 2
    Puntos = 3
    Final = 4
    EstadoJuego = Menu

    # Imagenes
    imgFondo = pygame.image.load("fondo menu.png")
    imgJugar = pygame.image.load("button_jugar.png")
    imgAcerca = pygame.image.load("button_puntuaciones.png")
    imgRegresar = pygame.image.load("button_regresar(1).png")
    imgsaludRoja = pygame.image.load("saludRoja.png")
    imgsaludverde = pygame.image.load("saludverde.png")
    imgFondoJuego = pygame.image.load("Fondo juego.png")
    imgSalir = pygame.image.load("button_salir.png")

    # Sprite Salir
    spriteSalir = pygame.sprite.Sprite()
    spriteSalir.image = imgSalir
    spriteSalir.rect = imgSalir.get_rect()
    spriteSalir.rect.left = 750
    spriteSalir.rect.top = 550

    # Sprite Salud Roja
    spriteSaludroja = pygame.sprite.Sprite()
    spriteSaludroja.image = imgsaludRoja
    spriteSaludroja.rect = imgsaludRoja.get_rect()
    spriteSaludroja.rect.left = 0
    spriteSaludroja.rect.top = 0

    # Sprite Salud Verde
    spriteSaludverde = pygame.sprite.Sprite()
    spriteSaludverde.image = imgsaludverde
    spriteSaludverde.rect = imgsaludverde.get_rect()
    spriteSaludverde.rect.left = 0
    spriteSaludverde.rect.top = 0

    # Sprite Jugar
    spriteBtnJugar = pygame.sprite.Sprite()
    spriteBtnJugar.image = imgJugar
    spriteBtnJugar.rect = imgJugar.get_rect()
    spriteBtnJugar.rect.left = 200
    spriteBtnJugar.rect.top = 200

    # Sprite Puntos
    spriteBtnPuntos = pygame.sprite.Sprite()
    spriteBtnPuntos.image = imgAcerca
    spriteBtnPuntos.rect = imgAcerca.get_rect()
    spriteBtnPuntos.rect.left = 600 - spriteBtnPuntos.rect.width // 2
    spriteBtnPuntos.rect.top = 200

    # Sprite Regresar
    spriteBtnRegresar = pygame.sprite.Sprite()
    spriteBtnRegresar.image = imgRegresar
    spriteBtnRegresar.rect = imgRegresar.get_rect()
    spriteBtnRegresar.rect.left = 100
    spriteBtnRegresar.rect.top = 500

    # Personaje
    imgMegaman = pygame.image.load("megaman parado.png")
    megaman = pygame.sprite.Sprite()
    megaman.image = imgMegaman
    megaman.rect = imgMegaman.get_rect()
    megaman.rect.left = 0
    megaman.rect.top = 450

    # Lista Balas
    imgBala = pygame.image.load("balas.png")
    listaBalas = []
    CrearBalas(imgBala, listaBalas)

    # Lista Enemigos
    imgEnemigo = pygame.image.load("enemigo.png")
    listaEnemigos = []
    crearEnemigos(imgEnemigo, listaEnemigos)


    # Lista Plataformas
    imgPlataforma = pygame.image.load("plataforma.png")
    listaPlataformas = []
    crearPlataformas(imgPlataforma, listaPlataformas)

    # Canción de fondos


    # Pantalla FIN (Gana)
    # Pantalla BLANCA, letrero GANAS...
    fuente = pygame.font.SysFont("monospace", 76)
    fuentetexto = pygame.font.SysFont("monospace", 15)

    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            if evento.type == pygame.KEYDOWN and EstadoJuego == Juego:
                if  evento.key == pygame.K_UP and EstadoJuego == Juego:
                    megaman.rect.top -= 200
                elif evento.key == pygame.K_DOWN and EstadoJuego == Juego:
                    megaman.rect.top += 200
                elif evento.key == pygame.K_SPACE:
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = megaman.rect.left + megaman.rect.width // 2
                    bala.rect.top = megaman.rect.top
                    listaBalas.append(bala)

            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if EstadoJuego == Menu:
                    xbj, ybj, abj, albj = spriteBtnJugar.rect
                    if xm >= xbj and xm <= xbj + abj:
                        if ym >= ybj and ym <= ybj + albj:
                            EstadoJuego = Juego

            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if EstadoJuego == Menu:
                    xbp, ybp, abp, albp = spriteBtnPuntos.rect
                    if xm >= xbp and xm <= xbp + abp:
                        if ym >= ybp and ym <= ybp + albp:
                            EstadoJuego = Puntos

            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if EstadoJuego == Puntos:
                    xbr, ybr, abr, albr = spriteBtnRegresar.rect
                    if xm >= xbr and xm <= xbr + abr:
                        if ym >= ybr and ym <= ybr + albr:
                            EstadoJuego = Menu

            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if EstadoJuego == Juego:
                    xbr, ybr, abr, albr = spriteSalir.rect
                    if xm >= xbr and xm <= xbr + abr:
                        if ym >= ybr and ym <= ybr + albr:
                            EstadoJuego = Final


        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        if EstadoJuego == Menu:
            ventana.blit(imgFondo, (0,0))
            ventana.blit(spriteBtnJugar.image, spriteBtnJugar.rect)
            ventana.blit(spriteBtnPuntos.image, spriteBtnPuntos.rect)

        elif EstadoJuego == Puntos:
            ventana.blit(imgFondo, (0,0))
            ventana.blit(spriteBtnRegresar.image, spriteBtnRegresar.rect)
            texto = fuentetexto.render("El objetivo del juego es la velocidad por lo que el juego empieza desde que activan el", 1, ROJO)
            texto2 = fuentetexto.render(" programa hasta que dan el voton de salir luego de haber matado a los", 1, ROJO)
            texto3 = fuentetexto.render("6 enemigos, columna por columna de abajo hacia arriba oprime el boton salir", 1, ROJO)
            texto4 = fuentetexto.render("y cierra el programa ve tu resultado, el objetivo es tener el menor puntaje, tu puntaje ", 1, ROJO)
            texto4 = fuentetexto.render(" y tu puntaje es el último resultado registrado", 1, ROJO)
            ventana.blit(texto, (10, 100))
            ventana.blit(texto2,(10, 200))
            ventana.blit(texto3,(10, 300))
            ventana.blit(texto4,(10, 400))

        elif EstadoJuego == Juego:
            ventana.blit(imgFondoJuego, (0, 0))
            pygame.mixer.music.load("24 Sigma Stage 1.mp3")
            pygame.mixer.music.play(1)
            ventana.blit(megaman.image, megaman.rect)
            ventana.blit(spriteSalir.image, spriteSalir.rect)
            dibujarEnemigos(ventana, listaEnemigos)
            dibujarPlataforma(ventana, listaPlataformas)
            CrearBalas(ventana, listaBalas)
            ActualizarBalas(listaBalas)
            checarColisiones(listaBalas, listaEnemigos)
            tiempo = calcularTiempo()
            registrarPuntos(tiempo)


        elif EstadoJuego == Final:
            tiempo = calcularTiempo()
            puntos = tiempo * 1
            ventana.blit(imgFondo, (0, 0))
            texto = fuente.render("Juego terminado, gracias por jugar", 1, BLANCO)
            textopuntuacion = fuente.render(str(puntos), 1, ROJO)
            ventana.blit(texto, ((ANCHO // 2)-350, ALTO // 2))
            ventana.blit(textopuntuacion, ((ANCHO//2)-50, ALTO-500))



        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    dibujar()


main()
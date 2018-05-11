import pygame
from random import randrange

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)

# Movimiento Objetos

movimiento = 2


def animarPacman(contadorAni):

    if contadorAni <= 1:
        imgPacman = pygame.image.load("Pacman2.png")
    elif 1 < contadorAni <= 3:
        imgPacman = pygame.image.load("Pacman3.png")
    elif 3 < contadorAni <= 5:
        imgPacman = pygame.image.load("Pacman4.png")
    elif 5 < contadorAni <= 7:
        imgPacman = pygame.image.load("Pacman5.png")
    elif 7 < contadorAni <= 9:
        imgPacman = pygame.image.load("Pacman1.png")

    contadorAni += 1
    if contadorAni == 10:
        contadorAni = 0

    return contadorAni, imgPacman


def movimientoPacman(pacman, direccion):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:  # and pacman.rect.left+30 < 795:
        direccion = 4

    elif keys[pygame.K_LEFT]:  # and 5 < pacman.rect.left:
        direccion = 2

    elif keys[pygame.K_DOWN]:  # and 595 > pacman.rect.top+30:
        direccion = 3

    elif keys[pygame.K_UP]:  # and 105 < pacman.rect.top:
        direccion = 1

    elif keys[pygame.K_SPACE]:
        direccion = 0

    if direccion == 4 and pacman.rect.left + pacman.rect.width < 795:  # Derecha
        if (not (130 < pacman.rect.top < 562)) or (162 < pacman.rect.top < 171 and (44 <= pacman.rect.left < 724)) or (524 < pacman.rect.top < 532 and (44 <= pacman.rect.left < 724)) or (202 < pacman.rect.top < 211 and (86 <= pacman.rect.left < 683)) or (482 < pacman.rect.top < 491 and (86 <= pacman.rect.left < 683)) or (242 < pacman.rect.top < 251 and (129 <= pacman.rect.left < 641)) or (442 < pacman.rect.top < 451 and (129 <= pacman.rect.left < 641)) or (402 < pacman.rect.top < 411 and (170 <= pacman.rect.left < 599)) or (282 < pacman.rect.top < 291 and (170 <= pacman.rect.left < 599)) or (322 < pacman.rect.top < 331 and (129 <= pacman.rect.left < 641)) or ((131 < pacman.rect.top < 163 or 212 < pacman.rect.top < 244 or 292 < pacman.rect.top < 324 or 452 < pacman.rect.top < 484 or 532 < pacman.rect.top < 564) and (379 <= pacman.rect.left < 388)):
             pacman.rect.left += movimiento
        elif (127 <= pacman.rect.top <= 130 or 562 <= pacman.rect.top <= 565) and (6 <= pacman.rect.left < 764):
            pacman.rect.left += movimiento
        elif 322 < pacman.rect.top < 331 and (44 <= pacman.rect.left < 95 or 128 <= pacman.rect.left < 641 or 675 <= pacman.rect.left < 724):
            pacman.rect.left += movimiento

    elif direccion == 2:  # Izquierda
        pacman.image = pygame.transform.flip(pacman.image, True, False)
        if (162 < pacman.rect.top < 171 and (45 < pacman.rect.left <= 725)) or (524 < pacman.rect.top < 532 and (45 < pacman.rect.left <= 725)) or (202 < pacman.rect.top < 211 and (87 < pacman.rect.left <= 684)) or (482 < pacman.rect.top < 491 and (87 < pacman.rect.left <= 684)) or (242 < pacman.rect.top < 251 and (130 < pacman.rect.left <= 642)) or (442 < pacman.rect.top < 451 and (130 < pacman.rect.left <= 642)) or (402 < pacman.rect.top < 411 and (171 < pacman.rect.left <= 600)) or (282 < pacman.rect.top < 291 and (171 < pacman.rect.left <= 600)) or (322 < pacman.rect.top < 331 and (130 < pacman.rect.left <= 642)) or ((131 < pacman.rect.top < 163 or 212 < pacman.rect.top < 244 or 292 < pacman.rect.top < 324 or 452 < pacman.rect.top < 484 or 532 < pacman.rect.top < 564) and (380 < pacman.rect.left <= 389)):
             pacman.rect.left -= movimiento
        elif (127 <= pacman.rect.top <= 130 or 562 <= pacman.rect.top <= 565) and (7 < pacman.rect.left <= 765):
            pacman.rect.left -= movimiento
        elif 322 < pacman.rect.top < 331 and (45 < pacman.rect.left <= 96 or 129 < pacman.rect.left <= 642 or 676 < pacman.rect.left <= 725):
            pacman.rect.left -= movimiento

    elif direccion == 3:  # Abajo
        pacman.image = pygame.transform.rotate(pacman.image, -90)
        if (126 <= pacman.rect.top < 564 and (759 <= pacman.rect.left <= 765 or 6 <= pacman.rect.left <= 12)) or (164 <= pacman.rect.top < 530 and (45 <= pacman.rect.left <= 53 or 717 <= pacman.rect.left <= 725)) or (204 <= pacman.rect.top < 488 and (87 <= pacman.rect.left <= 95 or 675 <= pacman.rect.left <= 683)) or (244 <= pacman.rect.top < 448 and (129 <= pacman.rect.left <= 137 or 633 <= pacman.rect.left <= 641)) or (284 <= pacman.rect.top < 408 and (171 <= pacman.rect.left <= 179 or 591 <= pacman.rect.left <= 599)) or (379 <= pacman.rect.left <= 389 and (525 <= pacman.rect.top < 564 or 126 <= pacman.rect.top < 168 or 205 <= pacman.rect.top < 247 or 284 <= pacman.rect.top < 326 or 444 <= pacman.rect.top < 488)):
            pacman.rect.top += movimiento

    elif direccion == 1:  # Arriba
        pacman.image = pygame.transform.rotate(pacman.image, 90)
        if (128 < pacman.rect.top <= 565 and (759 <= pacman.rect.left <= 765 or 6 <= pacman.rect.left <= 12)) or (165 < pacman.rect.top <= 531 and (45 <= pacman.rect.left <= 53 or 717 <= pacman.rect.left <= 725)) or (205 < pacman.rect.top <= 489 and (87 <= pacman.rect.left <= 95 or 675 <= pacman.rect.left <= 683)) or (245 < pacman.rect.top <= 449 and (129 <= pacman.rect.left <= 137 or 633 <= pacman.rect.left <= 641)) or (285 < pacman.rect.top <= 409 and (171 <= pacman.rect.left <= 179 or 591 <= pacman.rect.left <= 599)) or (379 <= pacman.rect.left <= 389 and (526 < pacman.rect.top <= 565 or 127 < pacman.rect.top <= 169 or 206 < pacman.rect.top <= 248 or 285 < pacman.rect.top <= 327 or 445 < pacman.rect.top <= 489)):
            pacman.rect.top -= movimiento

    elif direccion == 0:
        pacman.rect.left += 0
        pacman.rect.top += 0

    return pacman, direccion


def mapa(ventana):
    randBlue = randrange(100, 255)
    # Lineas Externas
    # Horizontales
    pygame.draw.line(ventana, (0, 0, randBlue), (0, 120), (799, 120), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (799, 599), (0, 599), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (3, 123), (796, 123), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (796, 596), (3, 596), 2)
    # Verticales
    # Derecha
    pygame.draw.line(ventana, (0, 0, randBlue), (798, 120), (798, 599), 2)
    # pygame.draw.line(ventana, (0, 0, 0), (798, 325), (798, 375), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (795, 123), (795, 596), 2)
    # pygame.draw.line(ventana, (0, 0, 0), (795, 325), (795, 375), 2)
    # Izquierda
    pygame.draw.line(ventana, (0, 0, randBlue), (0, 120), (0, 599), 2)
    # pygame.draw.line(ventana, (0, 0, 0), (0, 325), (0, 375), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (3, 123), (3, 596), 2)
    # pygame.draw.line(ventana, (0, 0, 0), (3, 325), (3, 375), 2)

    # Líneas internas
    # pygame.draw.line(ventana, (0, 0, randBlue), (,), (,), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (42, 161), (42, 561), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (756, 161), (756, 561), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (42, 161), (378, 161), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (420, 161), (756, 161), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (42, 561), (378, 561), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (420, 561), (756, 561), 2)

    pygame.draw.line(ventana, (0, 0, randBlue), (84, 201), (84, 321), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (84, 361), (84, 521), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (714, 201), (714, 321), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (714, 361), (714, 521), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (84, 201), (714, 201), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (84, 521), (714, 521), 2)

    pygame.draw.line(ventana, (0, 0, randBlue), (126, 241), (126, 481), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (672, 241), (672, 481), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (126, 241), (378, 241), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (420, 241), (672, 241), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (126, 481), (378, 481), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (420, 481), (672, 481), 2)

    pygame.draw.line(ventana, (0, 0, randBlue), (168, 281), (168, 321), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (168, 361), (168, 441), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (630, 281), (630, 321), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (630, 361), (630, 441), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (168, 281), (630, 281), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (168, 441), (630, 441), 2)

    pygame.draw.line(ventana, (0, 0, randBlue), (210, 321), (378, 321), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (420, 321), (588, 321), 2)

    # Caja de fantasmas

    pygame.draw.line(ventana, (0, 0, randBlue), (210, 361), (588, 361), 2)
    pygame.draw.line(ventana, (randBlue, randBlue, randBlue), (378, 361), (420, 361), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (210, 401), (588, 401), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (210, 361), (210, 401), 2)
    pygame.draw.line(ventana, (0, 0, randBlue), (588, 361), (588, 401), 2)


def puntaje(Font, score, fanA):
    scoreTitulo = Font.render("SCORE", False, BLANCO)
    # scoreTitulo = Font.render("%03d, %03d" % (fanA.rect.left, fanA.rect.top), False, BLANCO)
    scoreNum = Font.render("%04d" % score, False, BLANCO)

    return scoreTitulo, scoreNum


def crearDots(listaDots, imgDot):
    for x in range(21, 778, 21):  # Cada 35 px una columna nueva. Separación de dots = 15 px
        for y in range(141, 582, 20):
            if not ((y == 161 and (21 < x < 399 or 399 < x < 777)) or (y == 561 and (21 < x < 777)) or (y == 481 and (105 < x < 399 or 399 < x < 693)) or (y == 241 and (105 < x < 399 or 399 < x < 693)) or (y == 321 and (189 < x < 399 or 399 < x < 609)) or (y == 361 and (189 < x < 609))):
                if not ((y == 201 and (63 < x < 735)) or (y == 281 and (167 < x < 631)) or (y == 401 and (209 < x < 589)) or (y == 441 and (167 < x < 631)) or (y == 521 and (63 < x < 735)) or (y == 381 and 189 < x < 609)):
                    if not ((161 < y < 560 and x == 42) or (161 < y < 560 and x == 756) or (241 < y < 480 and x == 126) or (241 < y < 480 and x == 672)):
                        if not (((201 < y < 322 or 360 < y < 540) and x == 84) or ((281 < y < 322 or 360 < y < 441) and x == 168) or ((281 < y < 322 or 360 < y < 441) and x == 630) or ((201 < y < 322 or 360 < y < 540) and x == 714)):
                            dot = pygame.sprite.Sprite()
                            dot.image = imgDot
                            dot.rect = imgDot.get_rect()
                            dot.rect.left = x
                            dot.rect.top = y
                            listaDots.append(dot)


def dibujarDots(ventana, listaDots):

    for dot in listaDots:
        ventana.blit(dot.image, dot.rect)


def checaPuntaje(pacman, listaDots, copiaLista, score):
    copiaLista = listaDots[:]
    xPac = pacman.rect.left
    yPac = pacman.rect.top
    x2Pac = pacman.rect.left + pacman.rect.width
    y2Pac = pacman.rect.top + pacman.rect.height
    for dot in range(-1, -len(listaDots)-1, -1):
        xDot = listaDots[dot].rect.left
        yDot = listaDots[dot].rect.top
        if xPac < xDot < x2Pac and yPac < yDot < y2Pac:
            listaDots.remove(listaDots[dot])
            score += 10
            return score
    return score


def movimientoFantasmas(fanA, fanB, fanC, fanD, ticks):

    if fanA.rect.left < 385:
        fanA.rect.left += movimiento
    if ticks >= 180:
        if fanB.rect.left > 385:
            fanB.rect.left -= movimiento
    if ticks >= 360:
        if fanC.rect.left < 385:
            fanC.rect.left += movimiento
    if ticks >= 540:
        if fanD.rect.left > 385:
            fanD.rect.left -= movimiento
    ticks += 1
    return fanA, fanB, fanC, fanD, ticks


def movFanA(fanA, fanARanMov):
    if fanA.rect.left == 385 and 325 < fanA.rect.top == 365:
        fanA.rect.top -= movimiento
        fanARanMov = 1
    elif fanA.rect.left == 385 and fanA.rect.top == 325:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 385 and fanA.rect.top == 285:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 385 and fanA.rect.top == 245:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 385 and fanA.rect.top == 205:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 385 and fanA.rect.top == 165:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 385 and fanA.rect.top == 125:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 385 and fanA.rect.top == 445:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 385 and fanA.rect.top == 485:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 385 and fanA.rect.top == 525:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 385 and fanA.rect.top == 565:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 3 and fanA.rect.top == 125:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 3 and fanA.rect.top == 565:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 767 and fanA.rect.top == 125:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 767 and fanA.rect.top == 565:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 45 and fanA.rect.top == 165:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 45 and fanA.rect.top == 325:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 45 and fanA.rect.top == 525:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 725 and fanA.rect.top == 165:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 725 and fanA.rect.top == 325:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 725 and fanA.rect.top == 525:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 87 and fanA.rect.top == 205:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 87 and fanA.rect.top == 325:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 87 and fanA.rect.top == 485:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 683 and fanA.rect.top == 205:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 683 and fanA.rect.top == 325:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 683 and fanA.rect.top == 485:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 129 and fanA.rect.top == 245:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 129 and fanA.rect.top == 325:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 129 and fanA.rect.top == 445:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 641 and fanA.rect.top == 245:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 641 and fanA.rect.top == 325:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 641 and fanA.rect.top == 445:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 171 and fanA.rect.top == 285:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 171 and fanA.rect.top == 325:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 171 and fanA.rect.top == 405:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 599 and fanA.rect.top == 285:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 599 and fanA.rect.top == 325:
        fanARanMov = randrange(1, 5)
    elif fanA.rect.left == 599 and fanA.rect.top == 405:
        fanARanMov = randrange(1, 5)

    if 129 < fanA.rect.left < 385 and 285 < fanA.rect.top < 405:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
    elif 385 < fanA.rect.left < 641 and 285 < fanA.rect.top < 405:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
    elif 171 < fanA.rect.left < 599 and 285 < fanA.rect.top <= 365:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
        if fanA.rect.left != 325:
            if fanARanMov == 3:
                fanA.rect.top += movimiento
    elif 171 < fanA.rect.left < 599 and 285 <= fanA.rect.top < 325:
        if fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanA.rect.left != 385 and fanA.rect.top != 285:
            if fanARanMov == 1:
                fanA.rect.top -= movimiento
    elif 171 <= fanA.rect.left < 385 and 285 <= fanA.rect.top < 325:
        if fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanA.rect.left != 171 and fanA.rect.top != 285:
            if fanARanMov == 1:
                fanA.rect.top -= movimiento
            elif fanARanMov == 2:
                fanA.rect.left -= movimiento
    elif 171 < fanA.rect.left <= 599 and 325 < fanA.rect.top <= 405:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.left != 599 and fanA.rect.top != 405:
            if fanARanMov == 3:
                fanA.rect.top += movimiento
            elif fanARanMov == 4:
                fanA.rect.left += movimiento
    elif 171 <= fanA.rect.left < 599 and 325 < fanA.rect.top <= 405:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanA.rect.left != 171 and fanA.rect.top != 405:
            if fanARanMov == 3:
                fanA.rect.top += movimiento
            elif fanARanMov == 2:
                fanA.rect.left -= movimiento
    elif 129 <= fanA.rect.left < 385 and 285 <= fanA.rect.top < 325:
        if fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanA.rect.left != 129 and fanA.rect.top != 285:
            if fanARanMov == 1:
                fanA.rect.top -= movimiento
            elif fanARanMov == 2:
                fanA.rect.left -= movimiento
    elif 87 <= fanA.rect.left < 385 and 205 <= fanA.rect.top < 325:
        if fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanA.rect.left != 87 and fanA.rect.top != 205:
            if fanARanMov == 1:
                fanA.rect.top -= movimiento
            elif fanARanMov == 2:
                fanA.rect.left -= movimiento
    elif 45 <= fanA.rect.left < 385 and 165 <= fanA.rect.top < 325:
        if fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanA.rect.left != 45 and fanA.rect.top != 165:
            if fanARanMov == 1:
                fanA.rect.top -= movimiento
            elif fanARanMov == 2:
                fanA.rect.left -= movimiento
    elif 3 <= fanA.rect.left < 385 and 125 <= fanA.rect.top < 325:
        if fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanA.rect.left != 3 and fanA.rect.top != 125:
            if fanARanMov == 1:
                fanA.rect.top -= movimiento
            elif fanARanMov == 2:
                fanA.rect.left -= movimiento
    elif 129 <= fanA.rect.left < 385 and 325 < fanA.rect.top <= 445:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanA.rect.left != 129 and fanA.rect.top != 445:
            if fanARanMov == 3:
                fanA.rect.top += movimiento
            elif fanARanMov == 2:
                fanA.rect.left -= movimiento
    elif 87 <= fanA.rect.left < 385 and 325 < fanA.rect.top <= 485:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanA.rect.left != 87 and fanA.rect.top != 485:
            if fanARanMov == 3:
                fanA.rect.top += movimiento
            elif fanARanMov == 2:
                fanA.rect.left -= movimiento
    elif 45 <= fanA.rect.left < 385 and 325 < fanA.rect.top <= 525:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanA.rect.left != 45 and fanA.rect.top != 525:
            if fanARanMov == 3:
                fanA.rect.top += movimiento
            elif fanARanMov == 2:
                fanA.rect.left -= movimiento
    elif 3 <= fanA.rect.left < 385 and 325 < fanA.rect.top <= 565:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanA.rect.left != 3 and fanA.rect.top != 565:
            if fanARanMov == 3:
                fanA.rect.top += movimiento
            elif fanARanMov == 2:
                fanA.rect.left -= movimiento
    elif 385 < fanA.rect.left <= 641 and 325 < fanA.rect.top <= 445:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.left != 641 and fanA.rect.top != 445:
            if fanARanMov == 3:
                fanA.rect.top += movimiento
            elif fanARanMov == 4:
                fanA.rect.left += movimiento
    elif 385 < fanA.rect.left <= 683 and 325 < fanA.rect.top <= 485:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.left != 683 and fanA.rect.top != 485:
            if fanARanMov == 3:
                fanA.rect.top += movimiento
            elif fanARanMov == 4:
                fanA.rect.left += movimiento
    elif 385 < fanA.rect.left <= 725 and 325 < fanA.rect.top <= 525:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.left != 725 and fanA.rect.top != 525:
            if fanARanMov == 3:
                fanA.rect.top += movimiento
            elif fanARanMov == 4:
                fanA.rect.left += movimiento
    elif 385 < fanA.rect.left <= 767 and 325 < fanA.rect.top <= 565:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.left != 767 and fanA.rect.top != 565:
            if fanARanMov == 3:
                fanA.rect.top += movimiento
            elif fanARanMov == 4:
                fanA.rect.left += movimiento
    elif 385 < fanA.rect.left <= 599 and 285 <= fanA.rect.top < 325:
        if fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanA.rect.left != 599 and fanA.rect.top != 285:
            if fanARanMov == 1:
                fanA.rect.top -= movimiento
            elif fanARanMov == 4:
                fanA.rect.left += movimiento
    elif 385 < fanA.rect.left <= 641 and 245 <= fanA.rect.top < 325:
        if fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanA.rect.left != 641 and fanA.rect.top != 245:
            if fanARanMov == 1:
                fanA.rect.top -= movimiento
            elif fanARanMov == 4:
                fanA.rect.left += movimiento
    elif 385 < fanA.rect.left <= 683 and 205 <= fanA.rect.top < 325:
        if fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanA.rect.left != 683 and fanA.rect.top != 205:
            if fanARanMov == 1:
                fanA.rect.top -= movimiento
            elif fanARanMov == 4:
                fanA.rect.left += movimiento
    elif 385 < fanA.rect.left <= 725 and 165 <= fanA.rect.top < 325:
        if fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanA.rect.left != 725 and fanA.rect.top != 165:
            if fanARanMov == 1:
                fanA.rect.top -= movimiento
            elif fanARanMov == 4:
                fanA.rect.left += movimiento
    elif 385 < fanA.rect.left <= 767 and 125 <= fanA.rect.top < 325:
        if fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanA.rect.left != 767 and fanA.rect.top != 125:
            if fanARanMov == 1:
                fanA.rect.top -= movimiento
            elif fanARanMov == 4:
                fanA.rect.left += movimiento
    elif 45 <= fanA.rect.left < 87 and 165 < fanA.rect.top < 525:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanA.rect.left != 45:
            if fanARanMov == 2:
                fanA.rect.left -= movimiento
    elif 129 <= fanA.rect.left < 171 and 245 < fanA.rect.top < 445:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanA.rect.left != 129:
            if fanARanMov == 2:
                fanA.rect.left -= movimiento
    elif 683 <= fanA.rect.left < 725 and 205 < fanA.rect.top < 485:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanA.rect.left != 683:
            if fanARanMov == 2:
                fanA.rect.left -= movimiento
    elif 45 < fanA.rect.left <= 87 and 165 < fanA.rect.top < 525:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.left != 87:
            if fanARanMov == 4:
                fanA.rect.left += movimiento
    elif 599 < fanA.rect.left <= 641 and 245 < fanA.rect.top < 445:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.left != 641:
            if fanARanMov == 4:
                fanA.rect.left += movimiento
    elif 683 < fanA.rect.left <= 725 and 165 < fanA.rect.top < 525:
        if fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.left != 725:
            if fanARanMov == 4:
                fanA.rect.left += movimiento
    elif 3 < fanA.rect.left < 767 and 125 <= fanA.rect.top < 165:
        if fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.top != 125:
            if fanARanMov == 1:
                fanA.rect.top -= movimiento
    elif 87 < fanA.rect.left < 683 and 205 <= fanA.rect.top < 245:
        if fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.top != 205:
            if fanARanMov == 1:
                fanA.rect.top -= movimiento
    elif 3 < fanA.rect.left < 767 and 125 <= fanA.rect.top < 165:
        if fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.top != 125:
            if fanARanMov == 1:
                fanA.rect.top -= movimiento
    elif 129 < fanA.rect.left < 641 and 445 <= fanA.rect.top < 485:
        if fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.top != 445:
            if fanARanMov == 1:
                fanA.rect.top -= movimiento
    elif 45 < fanA.rect.left < 725 and 525 <= fanA.rect.top < 565:
        if fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanARanMov == 3:
            fanA.rect.top += movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.top != 525:
            if fanARanMov == 1:
                fanA.rect.top -= movimiento
    elif 3 < fanA.rect.left < 767 and 525 < fanA.rect.top <= 565:
        if fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.top != 565:
            if fanARanMov == 3:
                fanA.rect.top += movimiento
    elif 87 < fanA.rect.left < 683 and 445 < fanA.rect.top <= 485:
        if fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.top != 485:
            if fanARanMov == 3:
                fanA.rect.top += movimiento
    elif 129 < fanA.rect.left < 641 and 205 < fanA.rect.top <= 245:
        if fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.top != 245:
            if fanARanMov == 3:
                fanA.rect.top += movimiento
    elif 45 < fanA.rect.left < 725 and 125 < fanA.rect.top <= 165:
        if fanARanMov == 4:
            fanA.rect.left += movimiento
        elif fanARanMov == 1:
            fanA.rect.top -= movimiento
        elif fanARanMov == 2:
            fanA.rect.left -= movimiento
        elif fanA.rect.top != 165:
            if fanARanMov == 3:
                fanA.rect.top += movimiento

    return fanA, fanARanMov


def movFanB(fanB, fanBRanMov):
    if fanB.rect.left == 385 and 325 < fanB.rect.top == 365:
        fanB.rect.top -= movimiento
        fanBRanMov = 1
    elif fanB.rect.left == 385 and fanB.rect.top == 325:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 385 and fanB.rect.top == 285:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 385 and fanB.rect.top == 245:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 385 and fanB.rect.top == 205:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 385 and fanB.rect.top == 165:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 385 and fanB.rect.top == 125:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 385 and fanB.rect.top == 445:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 385 and fanB.rect.top == 485:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 385 and fanB.rect.top == 525:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 385 and fanB.rect.top == 565:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 3 and fanB.rect.top == 125:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 3 and fanB.rect.top == 565:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 767 and fanB.rect.top == 125:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 767 and fanB.rect.top == 565:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 45 and fanB.rect.top == 165:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 45 and fanB.rect.top == 325:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 45 and fanB.rect.top == 525:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 725 and fanB.rect.top == 165:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 725 and fanB.rect.top == 325:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 725 and fanB.rect.top == 525:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 87 and fanB.rect.top == 205:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 87 and fanB.rect.top == 325:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 87 and fanB.rect.top == 485:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 683 and fanB.rect.top == 205:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 683 and fanB.rect.top == 325:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 683 and fanB.rect.top == 485:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 129 and fanB.rect.top == 245:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 129 and fanB.rect.top == 325:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 129 and fanB.rect.top == 445:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 641 and fanB.rect.top == 245:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 641 and fanB.rect.top == 325:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 641 and fanB.rect.top == 445:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 171 and fanB.rect.top == 285:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 171 and fanB.rect.top == 325:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 171 and fanB.rect.top == 405:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 599 and fanB.rect.top == 285:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 599 and fanB.rect.top == 325:
        fanBRanMov = randrange(1, 5)
    elif fanB.rect.left == 599 and fanB.rect.top == 405:
        fanBRanMov = randrange(1, 5)

    if 129 < fanB.rect.left < 385 and 285 < fanB.rect.top < 405:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
    elif 385 < fanB.rect.left < 641 and 285 < fanB.rect.top < 405:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
    elif 171 < fanB.rect.left < 599 and 285 < fanB.rect.top <= 365:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
        if fanB.rect.left != 325:
            if fanBRanMov == 3:
                fanB.rect.top += movimiento
    elif 171 < fanB.rect.left < 599 and 285 <= fanB.rect.top < 325:
        if fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanB.rect.left != 385 and fanB.rect.top != 285:
            if fanBRanMov == 1:
                fanB.rect.top -= movimiento
    elif 171 <= fanB.rect.left < 385 and 285 <= fanB.rect.top < 325:
        if fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanB.rect.left != 171 and fanB.rect.top != 285:
            if fanBRanMov == 1:
                fanB.rect.top -= movimiento
            elif fanBRanMov == 2:
                fanB.rect.left -= movimiento
    elif 171 < fanB.rect.left <= 599 and 325 < fanB.rect.top <= 405:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.left != 599 and fanB.rect.top != 405:
            if fanBRanMov == 3:
                fanB.rect.top += movimiento
            elif fanBRanMov == 4:
                fanB.rect.left += movimiento
    elif 171 <= fanB.rect.left < 599 and 325 < fanB.rect.top <= 405:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanB.rect.left != 171 and fanB.rect.top != 405:
            if fanBRanMov == 3:
                fanB.rect.top += movimiento
            elif fanBRanMov == 2:
                fanB.rect.left -= movimiento
    elif 129 <= fanB.rect.left < 385 and 285 <= fanB.rect.top < 325:
        if fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanB.rect.left != 129 and fanB.rect.top != 285:
            if fanBRanMov == 1:
                fanB.rect.top -= movimiento
            elif fanBRanMov == 2:
                fanB.rect.left -= movimiento
    elif 87 <= fanB.rect.left < 385 and 205 <= fanB.rect.top < 325:
        if fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanB.rect.left != 87 and fanB.rect.top != 205:
            if fanBRanMov == 1:
                fanB.rect.top -= movimiento
            elif fanBRanMov == 2:
                fanB.rect.left -= movimiento
    elif 45 <= fanB.rect.left < 385 and 165 <= fanB.rect.top < 325:
        if fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanB.rect.left != 45 and fanB.rect.top != 165:
            if fanBRanMov == 1:
                fanB.rect.top -= movimiento
            elif fanBRanMov == 2:
                fanB.rect.left -= movimiento
    elif 3 <= fanB.rect.left < 385 and 125 <= fanB.rect.top < 325:
        if fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanB.rect.left != 3 and fanB.rect.top != 125:
            if fanBRanMov == 1:
                fanB.rect.top -= movimiento
            elif fanBRanMov == 2:
                fanB.rect.left -= movimiento
    elif 129 <= fanB.rect.left < 385 and 325 < fanB.rect.top <= 445:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanB.rect.left != 129 and fanB.rect.top != 445:
            if fanBRanMov == 3:
                fanB.rect.top += movimiento
            elif fanBRanMov == 2:
                fanB.rect.left -= movimiento
    elif 87 <= fanB.rect.left < 385 and 325 < fanB.rect.top <= 485:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanB.rect.left != 87 and fanB.rect.top != 485:
            if fanBRanMov == 3:
                fanB.rect.top += movimiento
            elif fanBRanMov == 2:
                fanB.rect.left -= movimiento
    elif 45 <= fanB.rect.left < 385 and 325 < fanB.rect.top <= 525:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanB.rect.left != 45 and fanB.rect.top != 525:
            if fanBRanMov == 3:
                fanB.rect.top += movimiento
            elif fanBRanMov == 2:
                fanB.rect.left -= movimiento
    elif 3 <= fanB.rect.left < 385 and 325 < fanB.rect.top <= 565:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanB.rect.left != 3 and fanB.rect.top != 565:
            if fanBRanMov == 3:
                fanB.rect.top += movimiento
            elif fanBRanMov == 2:
                fanB.rect.left -= movimiento
    elif 385 < fanB.rect.left <= 641 and 325 < fanB.rect.top <= 445:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.left != 641 and fanB.rect.top != 445:
            if fanBRanMov == 3:
                fanB.rect.top += movimiento
            elif fanBRanMov == 4:
                fanB.rect.left += movimiento
    elif 385 < fanB.rect.left <= 683 and 325 < fanB.rect.top <= 485:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.left != 683 and fanB.rect.top != 485:
            if fanBRanMov == 3:
                fanB.rect.top += movimiento
            elif fanBRanMov == 4:
                fanB.rect.left += movimiento
    elif 385 < fanB.rect.left <= 725 and 325 < fanB.rect.top <= 525:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.left != 725 and fanB.rect.top != 525:
            if fanBRanMov == 3:
                fanB.rect.top += movimiento
            elif fanBRanMov == 4:
                fanB.rect.left += movimiento
    elif 385 < fanB.rect.left <= 767 and 325 < fanB.rect.top <= 565:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.left != 767 and fanB.rect.top != 565:
            if fanBRanMov == 3:
                fanB.rect.top += movimiento
            elif fanBRanMov == 4:
                fanB.rect.left += movimiento
    elif 385 < fanB.rect.left <= 599 and 285 <= fanB.rect.top < 325:
        if fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanB.rect.left != 599 and fanB.rect.top != 285:
            if fanBRanMov == 1:
                fanB.rect.top -= movimiento
            elif fanBRanMov == 4:
                fanB.rect.left += movimiento
    elif 385 < fanB.rect.left <= 641 and 245 <= fanB.rect.top < 325:
        if fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanB.rect.left != 641 and fanB.rect.top != 245:
            if fanBRanMov == 1:
                fanB.rect.top -= movimiento
            elif fanBRanMov == 4:
                fanB.rect.left += movimiento
    elif 385 < fanB.rect.left <= 683 and 205 <= fanB.rect.top < 325:
        if fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanB.rect.left != 683 and fanB.rect.top != 205:
            if fanBRanMov == 1:
                fanB.rect.top -= movimiento
            elif fanBRanMov == 4:
                fanB.rect.left += movimiento
    elif 385 < fanB.rect.left <= 725 and 165 <= fanB.rect.top < 325:
        if fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanB.rect.left != 725 and fanB.rect.top != 165:
            if fanBRanMov == 1:
                fanB.rect.top -= movimiento
            elif fanBRanMov == 4:
                fanB.rect.left += movimiento
    elif 385 < fanB.rect.left <= 767 and 125 <= fanB.rect.top < 325:
        if fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanB.rect.left != 767 and fanB.rect.top != 125:
            if fanBRanMov == 1:
                fanB.rect.top -= movimiento
            elif fanBRanMov == 4:
                fanB.rect.left += movimiento
    elif 45 <= fanB.rect.left < 87 and 165 < fanB.rect.top < 525:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanB.rect.left != 45:
            if fanBRanMov == 2:
                fanB.rect.left -= movimiento
    elif 129 <= fanB.rect.left < 171 and 245 < fanB.rect.top < 445:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanB.rect.left != 129:
            if fanBRanMov == 2:
                fanB.rect.left -= movimiento
    elif 683 <= fanB.rect.left < 725 and 205 < fanB.rect.top < 485:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanB.rect.left != 683:
            if fanBRanMov == 2:
                fanB.rect.left -= movimiento
    elif 45 < fanB.rect.left <= 87 and 165 < fanB.rect.top < 525:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.left != 87:
            if fanBRanMov == 4:
                fanB.rect.left += movimiento
    elif 599 < fanB.rect.left <= 641 and 245 < fanB.rect.top < 445:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.left != 641:
            if fanBRanMov == 4:
                fanB.rect.left += movimiento
    elif 683 < fanB.rect.left <= 725 and 165 < fanB.rect.top < 525:
        if fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.left != 725:
            if fanBRanMov == 4:
                fanB.rect.left += movimiento
    elif 3 < fanB.rect.left < 767 and 125 <= fanB.rect.top < 165:
        if fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.top != 125:
            if fanBRanMov == 1:
                fanB.rect.top -= movimiento
    elif 87 < fanB.rect.left < 683 and 205 <= fanB.rect.top < 245:
        if fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.top != 205:
            if fanBRanMov == 1:
                fanB.rect.top -= movimiento
    elif 3 < fanB.rect.left < 767 and 125 <= fanB.rect.top < 165:
        if fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.top != 125:
            if fanBRanMov == 1:
                fanB.rect.top -= movimiento
    elif 129 < fanB.rect.left < 641 and 445 <= fanB.rect.top < 485:
        if fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.top != 445:
            if fanBRanMov == 1:
                fanB.rect.top -= movimiento
    elif 45 < fanB.rect.left < 725 and 525 <= fanB.rect.top < 565:
        if fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanBRanMov == 3:
            fanB.rect.top += movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.top != 525:
            if fanBRanMov == 1:
                fanB.rect.top -= movimiento
    elif 3 < fanB.rect.left < 767 and 525 < fanB.rect.top <= 565:
        if fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.top != 565:
            if fanBRanMov == 3:
                fanB.rect.top += movimiento
    elif 87 < fanB.rect.left < 683 and 445 < fanB.rect.top <= 485:
        if fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.top != 485:
            if fanBRanMov == 3:
                fanB.rect.top += movimiento
    elif 129 < fanB.rect.left < 641 and 205 < fanB.rect.top <= 245:
        if fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.top != 245:
            if fanBRanMov == 3:
                fanB.rect.top += movimiento
    elif 45 < fanB.rect.left < 725 and 125 < fanB.rect.top <= 165:
        if fanBRanMov == 4:
            fanB.rect.left += movimiento
        elif fanBRanMov == 1:
            fanB.rect.top -= movimiento
        elif fanBRanMov == 2:
            fanB.rect.left -= movimiento
        elif fanB.rect.top != 165:
            if fanBRanMov == 3:
                fanB.rect.top += movimiento

    return fanB, fanBRanMov


def movFanC(fanC, fanCRanMov):
    if fanC.rect.left == 385 and 325 < fanC.rect.top == 365:
        fanC.rect.top -= movimiento
        fanCRanMov = 1
    elif fanC.rect.left == 385 and fanC.rect.top == 325:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 385 and fanC.rect.top == 285:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 385 and fanC.rect.top == 245:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 385 and fanC.rect.top == 205:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 385 and fanC.rect.top == 165:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 385 and fanC.rect.top == 125:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 385 and fanC.rect.top == 445:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 385 and fanC.rect.top == 485:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 385 and fanC.rect.top == 525:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 385 and fanC.rect.top == 565:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 3 and fanC.rect.top == 125:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 3 and fanC.rect.top == 565:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 767 and fanC.rect.top == 125:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 767 and fanC.rect.top == 565:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 45 and fanC.rect.top == 165:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 45 and fanC.rect.top == 325:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 45 and fanC.rect.top == 525:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 725 and fanC.rect.top == 165:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 725 and fanC.rect.top == 325:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 725 and fanC.rect.top == 525:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 87 and fanC.rect.top == 205:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 87 and fanC.rect.top == 325:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 87 and fanC.rect.top == 485:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 683 and fanC.rect.top == 205:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 683 and fanC.rect.top == 325:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 683 and fanC.rect.top == 485:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 129 and fanC.rect.top == 245:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 129 and fanC.rect.top == 325:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 129 and fanC.rect.top == 445:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 641 and fanC.rect.top == 245:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 641 and fanC.rect.top == 325:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 641 and fanC.rect.top == 445:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 171 and fanC.rect.top == 285:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 171 and fanC.rect.top == 325:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 171 and fanC.rect.top == 405:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 599 and fanC.rect.top == 285:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 599 and fanC.rect.top == 325:
        fanCRanMov = randrange(1, 5)
    elif fanC.rect.left == 599 and fanC.rect.top == 405:
        fanCRanMov = randrange(1, 5)

    if 129 < fanC.rect.left < 385 and 285 < fanC.rect.top < 405:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
    elif 385 < fanC.rect.left < 641 and 285 < fanC.rect.top < 405:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
    elif 171 < fanC.rect.left < 599 and 285 < fanC.rect.top <= 365:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
        if fanC.rect.left != 325:
            if fanCRanMov == 3:
                fanC.rect.top += movimiento
    elif 171 < fanC.rect.left < 599 and 285 <= fanC.rect.top < 325:
        if fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanC.rect.left != 385 and fanC.rect.top != 285:
            if fanCRanMov == 1:
                fanC.rect.top -= movimiento
    elif 171 <= fanC.rect.left < 385 and 285 <= fanC.rect.top < 325:
        if fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanC.rect.left != 171 and fanC.rect.top != 285:
            if fanCRanMov == 1:
                fanC.rect.top -= movimiento
            elif fanCRanMov == 2:
                fanC.rect.left -= movimiento
    elif 171 < fanC.rect.left <= 599 and 325 < fanC.rect.top <= 405:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.left != 599 and fanC.rect.top != 405:
            if fanCRanMov == 3:
                fanC.rect.top += movimiento
            elif fanCRanMov == 4:
                fanC.rect.left += movimiento
    elif 171 <= fanC.rect.left < 599 and 325 < fanC.rect.top <= 405:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanC.rect.left != 171 and fanC.rect.top != 405:
            if fanCRanMov == 3:
                fanC.rect.top += movimiento
            elif fanCRanMov == 2:
                fanC.rect.left -= movimiento
    elif 129 <= fanC.rect.left < 385 and 285 <= fanC.rect.top < 325:
        if fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanC.rect.left != 129 and fanC.rect.top != 285:
            if fanCRanMov == 1:
                fanC.rect.top -= movimiento
            elif fanCRanMov == 2:
                fanC.rect.left -= movimiento
    elif 87 <= fanC.rect.left < 385 and 205 <= fanC.rect.top < 325:
        if fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanC.rect.left != 87 and fanC.rect.top != 205:
            if fanCRanMov == 1:
                fanC.rect.top -= movimiento
            elif fanCRanMov == 2:
                fanC.rect.left -= movimiento
    elif 45 <= fanC.rect.left < 385 and 165 <= fanC.rect.top < 325:
        if fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanC.rect.left != 45 and fanC.rect.top != 165:
            if fanCRanMov == 1:
                fanC.rect.top -= movimiento
            elif fanCRanMov == 2:
                fanC.rect.left -= movimiento
    elif 3 <= fanC.rect.left < 385 and 125 <= fanC.rect.top < 325:
        if fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanC.rect.left != 3 and fanC.rect.top != 125:
            if fanCRanMov == 1:
                fanC.rect.top -= movimiento
            elif fanCRanMov == 2:
                fanC.rect.left -= movimiento
    elif 129 <= fanC.rect.left < 385 and 325 < fanC.rect.top <= 445:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanC.rect.left != 129 and fanC.rect.top != 445:
            if fanCRanMov == 3:
                fanC.rect.top += movimiento
            elif fanCRanMov == 2:
                fanC.rect.left -= movimiento
    elif 87 <= fanC.rect.left < 385 and 325 < fanC.rect.top <= 485:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanC.rect.left != 87 and fanC.rect.top != 485:
            if fanCRanMov == 3:
                fanC.rect.top += movimiento
            elif fanCRanMov == 2:
                fanC.rect.left -= movimiento
    elif 45 <= fanC.rect.left < 385 and 325 < fanC.rect.top <= 525:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanC.rect.left != 45 and fanC.rect.top != 525:
            if fanCRanMov == 3:
                fanC.rect.top += movimiento
            elif fanCRanMov == 2:
                fanC.rect.left -= movimiento
    elif 3 <= fanC.rect.left < 385 and 325 < fanC.rect.top <= 565:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanC.rect.left != 3 and fanC.rect.top != 565:
            if fanCRanMov == 3:
                fanC.rect.top += movimiento
            elif fanCRanMov == 2:
                fanC.rect.left -= movimiento
    elif 385 < fanC.rect.left <= 641 and 325 < fanC.rect.top <= 445:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.left != 641 and fanC.rect.top != 445:
            if fanCRanMov == 3:
                fanC.rect.top += movimiento
            elif fanCRanMov == 4:
                fanC.rect.left += movimiento
    elif 385 < fanC.rect.left <= 683 and 325 < fanC.rect.top <= 485:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.left != 683 and fanC.rect.top != 485:
            if fanCRanMov == 3:
                fanC.rect.top += movimiento
            elif fanCRanMov == 4:
                fanC.rect.left += movimiento
    elif 385 < fanC.rect.left <= 725 and 325 < fanC.rect.top <= 525:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.left != 725 and fanC.rect.top != 525:
            if fanCRanMov == 3:
                fanC.rect.top += movimiento
            elif fanCRanMov == 4:
                fanC.rect.left += movimiento
    elif 385 < fanC.rect.left <= 767 and 325 < fanC.rect.top <= 565:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.left != 767 and fanC.rect.top != 565:
            if fanCRanMov == 3:
                fanC.rect.top += movimiento
            elif fanCRanMov == 4:
                fanC.rect.left += movimiento
    elif 385 < fanC.rect.left <= 599 and 285 <= fanC.rect.top < 325:
        if fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanC.rect.left != 599 and fanC.rect.top != 285:
            if fanCRanMov == 1:
                fanC.rect.top -= movimiento
            elif fanCRanMov == 4:
                fanC.rect.left += movimiento
    elif 385 < fanC.rect.left <= 641 and 245 <= fanC.rect.top < 325:
        if fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanC.rect.left != 641 and fanC.rect.top != 245:
            if fanCRanMov == 1:
                fanC.rect.top -= movimiento
            elif fanCRanMov == 4:
                fanC.rect.left += movimiento
    elif 385 < fanC.rect.left <= 683 and 205 <= fanC.rect.top < 325:
        if fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanC.rect.left != 683 and fanC.rect.top != 205:
            if fanCRanMov == 1:
                fanC.rect.top -= movimiento
            elif fanCRanMov == 4:
                fanC.rect.left += movimiento
    elif 385 < fanC.rect.left <= 725 and 165 <= fanC.rect.top < 325:
        if fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanC.rect.left != 725 and fanC.rect.top != 165:
            if fanCRanMov == 1:
                fanC.rect.top -= movimiento
            elif fanCRanMov == 4:
                fanC.rect.left += movimiento
    elif 385 < fanC.rect.left <= 767 and 125 <= fanC.rect.top < 325:
        if fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanC.rect.left != 767 and fanC.rect.top != 125:
            if fanCRanMov == 1:
                fanC.rect.top -= movimiento
            elif fanCRanMov == 4:
                fanC.rect.left += movimiento
    elif 45 <= fanC.rect.left < 87 and 165 < fanC.rect.top < 525:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanC.rect.left != 45:
            if fanCRanMov == 2:
                fanC.rect.left -= movimiento
    elif 129 <= fanC.rect.left < 171 and 245 < fanC.rect.top < 445:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanC.rect.left != 129:
            if fanCRanMov == 2:
                fanC.rect.left -= movimiento
    elif 683 <= fanC.rect.left < 725 and 205 < fanC.rect.top < 485:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanC.rect.left != 683:
            if fanCRanMov == 2:
                fanC.rect.left -= movimiento
    elif 45 < fanC.rect.left <= 87 and 165 < fanC.rect.top < 525:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.left != 87:
            if fanCRanMov == 4:
                fanC.rect.left += movimiento
    elif 599 < fanC.rect.left <= 641 and 245 < fanC.rect.top < 445:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.left != 641:
            if fanCRanMov == 4:
                fanC.rect.left += movimiento
    elif 683 < fanC.rect.left <= 725 and 165 < fanC.rect.top < 525:
        if fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.left != 725:
            if fanCRanMov == 4:
                fanC.rect.left += movimiento
    elif 3 < fanC.rect.left < 767 and 125 <= fanC.rect.top < 165:
        if fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.top != 125:
            if fanCRanMov == 1:
                fanC.rect.top -= movimiento
    elif 87 < fanC.rect.left < 683 and 205 <= fanC.rect.top < 245:
        if fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.top != 205:
            if fanCRanMov == 1:
                fanC.rect.top -= movimiento
    elif 3 < fanC.rect.left < 767 and 125 <= fanC.rect.top < 165:
        if fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.top != 125:
            if fanCRanMov == 1:
                fanC.rect.top -= movimiento
    elif 129 < fanC.rect.left < 641 and 445 <= fanC.rect.top < 485:
        if fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.top != 445:
            if fanCRanMov == 1:
                fanC.rect.top -= movimiento
    elif 45 < fanC.rect.left < 725 and 525 <= fanC.rect.top < 565:
        if fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanCRanMov == 3:
            fanC.rect.top += movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.top != 525:
            if fanCRanMov == 1:
                fanC.rect.top -= movimiento
    elif 3 < fanC.rect.left < 767 and 525 < fanC.rect.top <= 565:
        if fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.top != 565:
            if fanCRanMov == 3:
                fanC.rect.top += movimiento
    elif 87 < fanC.rect.left < 683 and 445 < fanC.rect.top <= 485:
        if fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.top != 485:
            if fanCRanMov == 3:
                fanC.rect.top += movimiento
    elif 129 < fanC.rect.left < 641 and 205 < fanC.rect.top <= 245:
        if fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.top != 245:
            if fanCRanMov == 3:
                fanC.rect.top += movimiento
    elif 45 < fanC.rect.left < 725 and 125 < fanC.rect.top <= 165:
        if fanCRanMov == 4:
            fanC.rect.left += movimiento
        elif fanCRanMov == 1:
            fanC.rect.top -= movimiento
        elif fanCRanMov == 2:
            fanC.rect.left -= movimiento
        elif fanC.rect.top != 165:
            if fanCRanMov == 3:
                fanC.rect.top += movimiento

    return fanC, fanCRanMov


def movFanD(fanD, fanDRanMov):
    if fanD.rect.left == 385 and 325 < fanD.rect.top == 365:
        fanD.rect.top -= movimiento
        fanDRanMov = 1
    elif fanD.rect.left == 385 and fanD.rect.top == 325:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 385 and fanD.rect.top == 285:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 385 and fanD.rect.top == 245:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 385 and fanD.rect.top == 205:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 385 and fanD.rect.top == 165:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 385 and fanD.rect.top == 125:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 385 and fanD.rect.top == 445:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 385 and fanD.rect.top == 485:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 385 and fanD.rect.top == 525:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 385 and fanD.rect.top == 565:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 3 and fanD.rect.top == 125:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 3 and fanD.rect.top == 565:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 767 and fanD.rect.top == 125:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 767 and fanD.rect.top == 565:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 45 and fanD.rect.top == 165:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 45 and fanD.rect.top == 325:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 45 and fanD.rect.top == 525:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 725 and fanD.rect.top == 165:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 725 and fanD.rect.top == 325:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 725 and fanD.rect.top == 525:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 87 and fanD.rect.top == 205:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 87 and fanD.rect.top == 325:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 87 and fanD.rect.top == 485:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 683 and fanD.rect.top == 205:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 683 and fanD.rect.top == 325:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 683 and fanD.rect.top == 485:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 129 and fanD.rect.top == 245:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 129 and fanD.rect.top == 325:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 129 and fanD.rect.top == 445:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 641 and fanD.rect.top == 245:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 641 and fanD.rect.top == 325:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 641 and fanD.rect.top == 445:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 171 and fanD.rect.top == 285:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 171 and fanD.rect.top == 325:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 171 and fanD.rect.top == 405:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 599 and fanD.rect.top == 285:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 599 and fanD.rect.top == 325:
        fanDRanMov = randrange(1, 5)
    elif fanD.rect.left == 599 and fanD.rect.top == 405:
        fanDRanMov = randrange(1, 5)

    if 129 < fanD.rect.left < 385 and 285 < fanD.rect.top < 405:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
    elif 385 < fanD.rect.left < 641 and 285 < fanD.rect.top < 405:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
    elif 171 < fanD.rect.left < 599 and 285 < fanD.rect.top <= 365:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
        if fanD.rect.left != 325:
            if fanDRanMov == 3:
                fanD.rect.top += movimiento
    elif 171 < fanD.rect.left < 599 and 285 <= fanD.rect.top < 325:
        if fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanD.rect.left != 385 and fanD.rect.top != 285:
            if fanDRanMov == 1:
                fanD.rect.top -= movimiento
    elif 171 <= fanD.rect.left < 385 and 285 <= fanD.rect.top < 325:
        if fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanD.rect.left != 171 and fanD.rect.top != 285:
            if fanDRanMov == 1:
                fanD.rect.top -= movimiento
            elif fanDRanMov == 2:
                fanD.rect.left -= movimiento
    elif 171 < fanD.rect.left <= 599 and 325 < fanD.rect.top <= 405:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.left != 599 and fanD.rect.top != 405:
            if fanDRanMov == 3:
                fanD.rect.top += movimiento
            elif fanDRanMov == 4:
                fanD.rect.left += movimiento
    elif 171 <= fanD.rect.left < 599 and 325 < fanD.rect.top <= 405:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanD.rect.left != 171 and fanD.rect.top != 405:
            if fanDRanMov == 3:
                fanD.rect.top += movimiento
            elif fanDRanMov == 2:
                fanD.rect.left -= movimiento
    elif 129 <= fanD.rect.left < 385 and 285 <= fanD.rect.top < 325:
        if fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanD.rect.left != 129 and fanD.rect.top != 285:
            if fanDRanMov == 1:
                fanD.rect.top -= movimiento
            elif fanDRanMov == 2:
                fanD.rect.left -= movimiento
    elif 87 <= fanD.rect.left < 385 and 205 <= fanD.rect.top < 325:
        if fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanD.rect.left != 87 and fanD.rect.top != 205:
            if fanDRanMov == 1:
                fanD.rect.top -= movimiento
            elif fanDRanMov == 2:
                fanD.rect.left -= movimiento
    elif 45 <= fanD.rect.left < 385 and 165 <= fanD.rect.top < 325:
        if fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanD.rect.left != 45 and fanD.rect.top != 165:
            if fanDRanMov == 1:
                fanD.rect.top -= movimiento
            elif fanDRanMov == 2:
                fanD.rect.left -= movimiento
    elif 3 <= fanD.rect.left < 385 and 125 <= fanD.rect.top < 325:
        if fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanD.rect.left != 3 and fanD.rect.top != 125:
            if fanDRanMov == 1:
                fanD.rect.top -= movimiento
            elif fanDRanMov == 2:
                fanD.rect.left -= movimiento
    elif 129 <= fanD.rect.left < 385 and 325 < fanD.rect.top <= 445:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanD.rect.left != 129 and fanD.rect.top != 445:
            if fanDRanMov == 3:
                fanD.rect.top += movimiento
            elif fanDRanMov == 2:
                fanD.rect.left -= movimiento
    elif 87 <= fanD.rect.left < 385 and 325 < fanD.rect.top <= 485:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanD.rect.left != 87 and fanD.rect.top != 485:
            if fanDRanMov == 3:
                fanD.rect.top += movimiento
            elif fanDRanMov == 2:
                fanD.rect.left -= movimiento
    elif 45 <= fanD.rect.left < 385 and 325 < fanD.rect.top <= 525:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanD.rect.left != 45 and fanD.rect.top != 525:
            if fanDRanMov == 3:
                fanD.rect.top += movimiento
            elif fanDRanMov == 2:
                fanD.rect.left -= movimiento
    elif 3 <= fanD.rect.left < 385 and 325 < fanD.rect.top <= 565:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanD.rect.left != 3 and fanD.rect.top != 565:
            if fanDRanMov == 3:
                fanD.rect.top += movimiento
            elif fanDRanMov == 2:
                fanD.rect.left -= movimiento
    elif 385 < fanD.rect.left <= 641 and 325 < fanD.rect.top <= 445:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.left != 641 and fanD.rect.top != 445:
            if fanDRanMov == 3:
                fanD.rect.top += movimiento
            elif fanDRanMov == 4:
                fanD.rect.left += movimiento
    elif 385 < fanD.rect.left <= 683 and 325 < fanD.rect.top <= 485:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.left != 683 and fanD.rect.top != 485:
            if fanDRanMov == 3:
                fanD.rect.top += movimiento
            elif fanDRanMov == 4:
                fanD.rect.left += movimiento
    elif 385 < fanD.rect.left <= 725 and 325 < fanD.rect.top <= 525:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.left != 725 and fanD.rect.top != 525:
            if fanDRanMov == 3:
                fanD.rect.top += movimiento
            elif fanDRanMov == 4:
                fanD.rect.left += movimiento
    elif 385 < fanD.rect.left <= 767 and 325 < fanD.rect.top <= 565:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.left != 767 and fanD.rect.top != 565:
            if fanDRanMov == 3:
                fanD.rect.top += movimiento
            elif fanDRanMov == 4:
                fanD.rect.left += movimiento
    elif 385 < fanD.rect.left <= 599 and 285 <= fanD.rect.top < 325:
        if fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanD.rect.left != 599 and fanD.rect.top != 285:
            if fanDRanMov == 1:
                fanD.rect.top -= movimiento
            elif fanDRanMov == 4:
                fanD.rect.left += movimiento
    elif 385 < fanD.rect.left <= 641 and 245 <= fanD.rect.top < 325:
        if fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanD.rect.left != 641 and fanD.rect.top != 245:
            if fanDRanMov == 1:
                fanD.rect.top -= movimiento
            elif fanDRanMov == 4:
                fanD.rect.left += movimiento
    elif 385 < fanD.rect.left <= 683 and 205 <= fanD.rect.top < 325:
        if fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanD.rect.left != 683 and fanD.rect.top != 205:
            if fanDRanMov == 1:
                fanD.rect.top -= movimiento
            elif fanDRanMov == 4:
                fanD.rect.left += movimiento
    elif 385 < fanD.rect.left <= 725 and 165 <= fanD.rect.top < 325:
        if fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanD.rect.left != 725 and fanD.rect.top != 165:
            if fanDRanMov == 1:
                fanD.rect.top -= movimiento
            elif fanDRanMov == 4:
                fanD.rect.left += movimiento
    elif 385 < fanD.rect.left <= 767 and 125 <= fanD.rect.top < 325:
        if fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanD.rect.left != 767 and fanD.rect.top != 125:
            if fanDRanMov == 1:
                fanD.rect.top -= movimiento
            elif fanDRanMov == 4:
                fanD.rect.left += movimiento
    elif 45 <= fanD.rect.left < 87 and 165 < fanD.rect.top < 525:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanD.rect.left != 45:
            if fanDRanMov == 2:
                fanD.rect.left -= movimiento
    elif 129 <= fanD.rect.left < 171 and 245 < fanD.rect.top < 445:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanD.rect.left != 129:
            if fanDRanMov == 2:
                fanD.rect.left -= movimiento
    elif 683 <= fanD.rect.left < 725 and 205 < fanD.rect.top < 485:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanD.rect.left != 683:
            if fanDRanMov == 2:
                fanD.rect.left -= movimiento
    elif 45 < fanD.rect.left <= 87 and 165 < fanD.rect.top < 525:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.left != 87:
            if fanDRanMov == 4:
                fanD.rect.left += movimiento
    elif 599 < fanD.rect.left <= 641 and 245 < fanD.rect.top < 445:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.left != 641:
            if fanDRanMov == 4:
                fanD.rect.left += movimiento
    elif 683 < fanD.rect.left <= 725 and 165 < fanD.rect.top < 525:
        if fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.left != 725:
            if fanDRanMov == 4:
                fanD.rect.left += movimiento
    elif 3 < fanD.rect.left < 767 and 125 <= fanD.rect.top < 165:
        if fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.top != 125:
            if fanDRanMov == 1:
                fanD.rect.top -= movimiento
    elif 87 < fanD.rect.left < 683 and 205 <= fanD.rect.top < 245:
        if fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.top != 205:
            if fanDRanMov == 1:
                fanD.rect.top -= movimiento
    elif 3 < fanD.rect.left < 767 and 125 <= fanD.rect.top < 165:
        if fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.top != 125:
            if fanDRanMov == 1:
                fanD.rect.top -= movimiento
    elif 129 < fanD.rect.left < 641 and 445 <= fanD.rect.top < 485:
        if fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.top != 445:
            if fanDRanMov == 1:
                fanD.rect.top -= movimiento
    elif 45 < fanD.rect.left < 725 and 525 <= fanD.rect.top < 565:
        if fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanDRanMov == 3:
            fanD.rect.top += movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.top != 525:
            if fanDRanMov == 1:
                fanD.rect.top -= movimiento
    elif 3 < fanD.rect.left < 767 and 525 < fanD.rect.top <= 565:
        if fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.top != 565:
            if fanDRanMov == 3:
                fanD.rect.top += movimiento
    elif 87 < fanD.rect.left < 683 and 445 < fanD.rect.top <= 485:
        if fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.top != 485:
            if fanDRanMov == 3:
                fanD.rect.top += movimiento
    elif 129 < fanD.rect.left < 641 and 205 < fanD.rect.top <= 245:
        if fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.top != 245:
            if fanDRanMov == 3:
                fanD.rect.top += movimiento
    elif 45 < fanD.rect.left < 725 and 125 < fanD.rect.top <= 165:
        if fanDRanMov == 4:
            fanD.rect.left += movimiento
        elif fanDRanMov == 1:
            fanD.rect.top -= movimiento
        elif fanDRanMov == 2:
            fanD.rect.left -= movimiento
        elif fanD.rect.top != 165:
            if fanDRanMov == 3:
                fanD.rect.top += movimiento

    return fanD, fanDRanMov


def checaChoque(listaFan, pacman):
    ModoDeJuego = 2
    xPac, yPac, wPac, hPac = pacman.rect
    for fan in listaFan:
        if ((fan.rect.left < xPac < fan.rect.left + fan.rect.width) or (fan.rect.left < xPac + wPac < fan.rect.left + fan.rect.width)) and ((fan.rect.top < yPac < fan.rect.top + fan.rect.height) or (fan.rect.top < yPac + hPac < fan.rect.top + fan.rect.height)):
            ModoDeJuego = 3
    return ModoDeJuego


def dibujar():

    # Inicializa el motor de pygame
    pygame.init()
    pygame.display.set_caption("'パックマン' by: Paco Murillo")
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución


    #Personaje Pacman inicialización
    imgPacman = pygame.image.load("Pacman2.png")
    pacman = pygame.sprite.Sprite()
    pacman.rect = imgPacman.get_rect()


    # Posición inicial Pacman
    pacman.rect.left = 400 - pacman.rect.width//2
    pacman.rect.top = 562 - pacman.rect.height//2

    # Inicialización de Fantasmas
    fantasmaAImg = pygame.image.load("Fantasma 1.png")
    fantasmaA = pygame.sprite.Sprite()
    fantasmaA.rect = fantasmaAImg.get_rect()
    fantasmaA.rect.left = 343
    fantasmaA.rect.top = 365
    fantasmaA.image = fantasmaAImg
    fanARanMov = 0
    
    fantasmaBImg = pygame.image.load("Fantasma 2.png")
    fantasmaB = pygame.sprite.Sprite()
    fantasmaB.rect = fantasmaBImg.get_rect()
    fantasmaB.rect.left = 427
    fantasmaB.rect.top = 365
    fantasmaB.image = fantasmaBImg
    fanBRanMov = 0
    
    fantasmaCImg = pygame.image.load("Fantasma 3.png")
    fantasmaC = pygame.sprite.Sprite()
    fantasmaC.rect = fantasmaCImg.get_rect()
    fantasmaC.rect.left = 301
    fantasmaC.rect.top = 365
    fantasmaC.image = fantasmaCImg
    fanCRanMov = 0
    
    fantasmaDImg = pygame.image.load("Fantasma 4.png")
    fantasmaD = pygame.sprite.Sprite()
    fantasmaD.rect = fantasmaDImg.get_rect()
    fantasmaD.rect.left = 469
    fantasmaD.rect.top = 365
    fantasmaD.image = fantasmaDImg
    fanDRanMov = 0

    
    # Inicialización de Dots
    listaDots = []
    copiaLista = []
    imgDot = pygame.image.load("Dot.png")
    crearDots(listaDots, imgDot)
    ticksFan = 0

    # Animación
    contadorAni = 0

    # Movimiento
    direccion = 0

    # Puntaje
    Font = pygame.font.Font("8-BIT WONDER.TTF", 30)
    score = 0

    # Modos de Juego
    ModoDeJuego = 1

    Menu = 1
    Juego = 2
    GameOver = 3
    Gano = 4

    # Inicializacion Fondo y Boton
    fondo = pygame.sprite.Sprite()
    fondoImg = pygame.image.load("Fondo_Pacman.jpg")
    fondo.image = fondoImg
    fondo.rect = fondoImg.get_rect()
    fondo.rect.left = 0
    fondo.rect.top = 0

    boton = pygame.sprite.Sprite()
    botonImg = pygame.image.load("Boton_Play.png")
    boton.image = botonImg
    boton.rect = botonImg.get_rect()
    boton.rect.left = ANCHO//2 - boton.rect.width//2
    boton.rect.top = 3*(ALTO//4) - boton.rect.height//2

    # Inicializacion Sonidos
    pygame.mixer.init()
    musicaInicio = pygame.mixer.Sound("pacman_beginning.wav")
    musicaJuego = pygame.mixer.Sound("pacman_chomp.wav")
    efectoMuerte = pygame.mixer.Sound("pacman_death.wav")
    musicaVictoria = pygame.mixer.Sound("pacman_extrapac.wav")
    pygame.mixer.set_num_channels(1)


    while not termina:  # Ciclo principal

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            if ModoDeJuego == Menu:
                if evento.type == pygame.MOUSEBUTTONUP:
                    xM, yM = pygame.mouse.get_pos()
                    if boton.rect.left <= xM <= boton.rect.left + boton.rect.width:
                        if boton.rect.top <= yM <= boton.rect.top + boton.rect.height:
                            ModoDeJuego = Juego


        # Borrar pantalla
        ventana.fill(NEGRO)

        if ModoDeJuego == Menu:
            if pygame.mixer.Sound.get_num_channels(musicaInicio) < 5:
                pygame.mixer.Sound.play(musicaInicio, loops=0)
            ventana.blit(fondo.image, fondo.rect)
            ventana.blit(boton.image, boton.rect)
        elif ModoDeJuego == Juego:
            pygame.mixer.Sound.stop(musicaInicio)
            pygame.mixer.Sound.play(musicaJuego)
            listaFan = []
            listaFan.append(fantasmaA)
            listaFan.append(fantasmaB)
            listaFan.append(fantasmaC)
            listaFan.append(fantasmaD)
            contadorAni, pacman.image = animarPacman(contadorAni)
            pacman, direccion = movimientoPacman(pacman, direccion)
            if ticksFan <= 650:
                fantasmaA, fantasmaB, fantasmaC, fantasmaD, ticksFan = movimientoFantasmas(fantasmaA, fantasmaB, fantasmaC, fantasmaD, ticksFan)
            fantasmaA, fanARanMov = movFanA(fantasmaA, fanARanMov)
            fantasmaB, fanBRanMov = movFanB(fantasmaB, fanBRanMov)
            fantasmaC, fanCRanMov = movFanC(fantasmaC, fanCRanMov)
            fantasmaD, fanDRanMov = movFanD(fantasmaD, fanDRanMov)

            ventana.blit(Font.render("Pacman", False, BLANCO), (5, 10))
            # ventana.blit(Font.render("%03d, %03d" % (pacman.rect.left, pacman.rect.top), False, BLANCO), (5, 10))
            mapa(ventana)
            dibujarDots(ventana, listaDots)
            ventana.blit(fantasmaB.image, fantasmaB.rect)
            ventana.blit(fantasmaC.image, fantasmaC.rect)
            ventana.blit(fantasmaD.image, fantasmaD.rect)
            ventana.blit(fantasmaA.image, fantasmaA.rect)
            ventana.blit(pacman.image, pacman.rect)

            ModoDeJuego = checaChoque(listaFan, pacman)

            scoreTitulo, scoreNum = puntaje(Font, score, fantasmaA)
            score = checaPuntaje(pacman, listaDots, copiaLista, score)

            ventana.blit(scoreTitulo, (3, 60))
            ventana.blit(scoreNum, (163, 60))

            if len(listaDots)== 0:
                ModoDeJuego = Gano
        elif ModoDeJuego == GameOver:
            pygame.mixer.Sound.stop(musicaJuego)
            if pygame.mixer.Sound.get_num_channels(efectoMuerte) < 5:
                pygame.mixer.Sound.play(efectoMuerte, loops=0)
            ventana.blit(fondo.image, fondo.rect)
            ventana.blit(Font.render("Perdiste", False, BLANCO), (ANCHO//2 - 105, 3*(ALTO//4) - 15))
        elif ModoDeJuego == Gano:
            pygame.mixer.Sound.stop(musicaJuego)
            if pygame.mixer.Sound.get_num_channels(musicaVictoria) < 5:
                pygame.mixer.Sound.play(musicaVictoria, loops=0)
            ventana.blit(fondo.image, fondo.rect)
            ventana.blit(Font.render("Ganaste", False, BLANCO), (ANCHO//2 - 100, 3*(ALTO//4) - 15))


        pygame.display.flip()  # Actualiza trazos
        reloj.tick(60)  # 40 fps


    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    dibujar()


main()

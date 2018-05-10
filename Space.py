# Autor: Carlos Martínez

# Librerías
import pygame
import random
import os

# Configuración general del juego (tamaño de pantalla y velocidad)
WIDTH = 800
HEIGHT = 600
FPS = 30

# Paleta de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (235, 47, 6)
BLUE = (0, 168, 255)
ORANGE = (229, 142, 38)

# Declarar la ubicación del folder donde se encuentra el juego para que funciones en cualquier
# sistema operativo
gameFolder = os.path.dirname(__file__)
assetsFolder = os.path.join(gameFolder, "img")
musicFolder = os.path.join(gameFolder, "music")


# Preguntar nombre al usuario para guardar High Score
def preguntarNombre():
    nombre = input(
        "Listo para jugar?\nAntes de comenzar, por favor escribe tu nombre.\nSe utilizará para guardar tu puntuación: ")
    return nombre


# Función para dibujar texto en la ventana del juego
fontName = pygame.font.match_font('arial')


def typeText(surface, text, size, x, y):
    font = pygame.font.Font(fontName, size)
    textSurface = font.render(text, True, WHITE)
    textRect = textSurface.get_rect()
    textRect.midtop = (x, y)
    surface.blit(textSurface, textRect)


def nuevoMeteorito():
    mob = Mob()
    allSprites.add(mob)
    mobs.add(mob)


def dibujarBarraEscudo(ventana, x, y, porcentage):
    if porcentage < 0:
        porcentage = 0
    bLength = 100
    bHeight = 10
    border = pygame.Rect(x, y, bLength, bHeight)
    fillRect = pygame.Rect(x, y, porcentage, bHeight)
    pygame.draw.rect(ventana, BLUE, fillRect)
    pygame.draw.rect(ventana, WHITE, border, 2)
    ventana.blit(shieldImg, (10, 8))


def inicioJuego():
    ventana.blit(bg, bgRect)
    typeText(ventana, "Space Shooter", 72, WIDTH / 2, HEIGHT / 4)
    ventana.blit(btnJugar.image, btnJugar.rect)
    ventana.blit(btnHowToPlay.image, btnHowToPlay.rect)
    ventana.blit(btnHighScore.image, btnHighScore.rect)
    pygame.display.flip()
    menu = True
    while menu:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                menu = False


def highScores():
    ventana.blit(bg, bgRect)
    typeText(ventana, "High Scores", 54, WIDTH / 2, HEIGHT / 5)
    pygame.display.flip()
    gameOver = True
    while gameOver:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                gameOver = False

def gameOver(score):
    ventana.blit(bg, bgRect)
    typeText(ventana, "Game Over", 72, WIDTH / 2, HEIGHT / 4)
    typeText(ventana, "Score: " + str(score), 36, WIDTH / 2, HEIGHT / 2)
    typeText(ventana, "Presiona cualquier tecla para volver a jugar!", 20, WIDTH / 2, HEIGHT - 100)

    while gameOver:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                gameOver = False


def mostrarVidas(ventana, x, y, vidas, img):
    for vida in range(vidas):
        imgRect = img.get_rect()
        imgRect.x = x + (imgRect.width + 5) * vida
        imgRect.y = y
        ventana.blit(img, imgRect)


# Sprites
class Player(pygame.sprite.Sprite):
    # Sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(naveImg, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedX = 0
        self.speed = 15
        self.shield = 100
        self.vidas = 3
        self.display = False
        self.displayTimer = pygame.time.get_ticks()

    def update(self):
        # Mostrar nave
        if self.display and pygame.time.get_ticks() - self.displayTimer > 1000:
            self.display = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
        self.speedX = 0
        keystate = pygame.key.get_pressed()
        # Movimiento del Sprite si se precionan las teclas izquierda o derecha(<-- o -->)
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speedX = -self.speed
        if keystate[pygame.K_RIGHT]:
            self.speedX = self.speed
        self.rect.x += self.speedX
        # Límites del Sprite respecto a los bordes de la pantalla
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        allSprites.add(bullet)
        bullets.add(bullet)
        shootSound.play()

    def ocultar(self):
        self.display = True
        self.displayTimer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imageOriginal = random.choice(meteorImages)
        self.imageOriginal.set_colorkey(BLACK)
        self.image = self.imageOriginal.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 2)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedY = random.randrange(5, 15)
        self.speedX = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.rect.top > HEIGHT + 10 or self.rect.left < -30 or self.rect.right > WIDTH + 30:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-150, -100)
            self.speedY = random.randrange(5, 15)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletImg
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        # Eliminar el sprite si se sale de la pantalla
        if self.rect.bottom < 0:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosionAnimation[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.lastUpdate = pygame.time.get_ticks()
        self.frameCount = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.lastUpdate > self.frameCount:
            self.lastUpdate = now
            self.frame += 1
            if self.frame == len(explosionAnimation[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosionAnimation[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


# Botones
imgBotonJugar = pygame.image.load(os.path.join(assetsFolder, "start.png"))
imgBotonHowToPlay = pygame.image.load(os.path.join(assetsFolder, "howToPlay.png"))
imgBotonHighScore = pygame.image.load(os.path.join(assetsFolder, "highScore.png"))

btnJugar = pygame.sprite.Sprite()  # SPRITE
btnJugar.image = imgBotonJugar
btnJugar.rect = imgBotonJugar.get_rect()
btnJugar.rect.left = WIDTH / 2 - btnJugar.rect.width / 2   # coordenada x
btnJugar.rect.top = HEIGHT / 2 - btnJugar.rect.height / 2  # coordenada y

btnHighScore = pygame.sprite.Sprite()
btnHighScore.image = imgBotonHighScore
btnHighScore.rect = imgBotonHighScore.get_rect()
btnHighScore.rect.left = WIDTH / 2 - btnHighScore.rect.width / 2   # coordenada x
btnHighScore.rect.top = HEIGHT / 2 - btnHighScore.rect.height / 2 + 5# coordenada y

btnHowToPlay = pygame.sprite.Sprite()
btnHowToPlay.image = imgBotonHowToPlay
btnHowToPlay.rect = imgBotonHowToPlay.get_rect()
btnHowToPlay.rect.left = WIDTH / 2 - btnHowToPlay.rect.width / 2   # coordenada x
btnHowToPlay.rect.top = HEIGHT / 2 - btnHowToPlay.rect.height / 2 + 10  # coordenada y

# Iniciar Pygame y crear la ventana del juego
pygame.init()
pygame.mixer.init()
ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

# Cargar gráficos del juego
bg = pygame.image.load(os.path.join(assetsFolder, "corona_rt.png")).convert()
bgRect = bg.get_rect()
naveImg = pygame.image.load(os.path.join(assetsFolder, "playerShip1_red.png")).convert()
naveVidaImg = pygame.image.load(os.path.join(assetsFolder, "playerLife1_red.png")).convert()
naveVidaImg.set_colorkey(BLACK)
meteorImages = []
meteorList = ['meteorBrown_big1.png', 'meteorBrown_big2.png', 'meteorBrown_big3.png', 'meteorBrown_big4.png',
              'meteorBrown_med1.png', 'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',
              'meteorBrown_tiny1.png', 'meteorBrown_tiny2.png']
for img in meteorList:
    meteorImages.append(pygame.image.load(os.path.join(assetsFolder, img)))
bulletImg = pygame.image.load(os.path.join(assetsFolder, "laserBlue16.png")).convert()
# En el siguiente diccionario se van a agregar dos tamaños de explociones para llamarlas individualmente
# según el tamaño que corresponde al Sprite
explosionAnimation = {}
explosionAnimation['lg'] = []
explosionAnimation['sm'] = []
for f in range(9):
    filename = 'regularExplosion0{}.png'.format(f)
    img = pygame.image.load(os.path.join(assetsFolder, filename)).convert()
    img.set_colorkey(BLACK)
    imgLarge = pygame.transform.scale(img, (80, 80))
    explosionAnimation['lg'].append(imgLarge)
    imgSmall = pygame.transform.scale(img, (32, 32))
    explosionAnimation['sm'].append(imgSmall)
shieldImg = pygame.image.load(os.path.join(assetsFolder, "shield.png"))

# Cargar sonidos del juego
shootSound = pygame.mixer.Sound(os.path.join(musicFolder, "laser1.wav"))
explotionSounds = [pygame.mixer.Sound(os.path.join(musicFolder, "explosion1.wav")),
                   pygame.mixer.Sound(os.path.join(musicFolder, "explosion2.wav"))]

naveDestruidaSound = pygame.mixer.Sound(os.path.join(musicFolder, "playerDead.wav"))
# Musica de fondo
pygame.mixer.music.load(os.path.join(musicFolder, "Notathing2.mp3"))
pygame.mixer.music.set_volume(0.4)
# Tocar música de fondo
pygame.mixer.music.play(loops=-1)
# Agrupar Sprites para agregarlos facilmente al juego
allSprites = pygame.sprite.Group()
# Mobs group
mobs = pygame.sprite.Group()
# Bullets Gorup
bullets = pygame.sprite.Group()
player = Player()
allSprites.add(player)
for i in range(8):
    nuevoMeteorito()
# Puntos acumulados del juego
score = 0


def dibujar(score):
    # Loop del Juego
    menu = True
    running = True
    while running:
        if menu:
            inicioJuego()
            menu = False
        # Mantener el loop corriendo a la velocidad requerida
        clock.tick(FPS)
        # Eventos - Procesos
        for event in pygame.event.get():
            # Revisar si se cerró la ventana del juego
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # Actualizar
        allSprites.update()

        # Revisa si una bala se impacta con algún enemigo(mob)
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            score += 100 - hit.radius
            random.choice(explotionSounds).play()
            explosion = Explosion(hit.rect.center, 'lg')
            allSprites.add(explosion)
            nuevoMeteorito()

        # Revisa si algún enemigo(mob) choca con el Sprite Player
        hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
        for hit in hits:
            player.shield -= hit.radius
            random.choice(explotionSounds).play()
            explosion = Explosion(hit.rect.center, 'sm')
            allSprites.add(explosion)
            nuevoMeteorito()
            if player.shield <= 0:
                naveDestruidaSound.play()
                naveDestruida = Explosion(player.rect.center, 'lg')
                allSprites.add(naveDestruida)
                player.ocultar()
                player.vidas -= 1
                player.shield = 100

        # Si se destruye la nave y la explosión termino
        if player.vidas == 0 and not naveDestruida.alive():
            gameOver(score)

        # Renedr / Draw
        ventana.fill(BLACK)
        ventana.blit(bg, bgRect)
        allSprites.draw(ventana)
        dibujarBarraEscudo(ventana, 30, 10, player.shield)
        typeText(ventana, str(player.shield), 14, 150, 8)
        typeText(ventana, str(score), 18, WIDTH / 2, 10)
        mostrarVidas(ventana, WIDTH - 120, 10, player.vidas, naveVidaImg)
        # After drawing flip the new slide
        pygame.display.flip()
    pygame.quit()


def main():
    dibujar(score)


main()

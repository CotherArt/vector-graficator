# coding: utf-8
__author__ = 'CotherArt'

import pygame
import pygame_textinput
from vector import Vector

pygame.init()
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGTH_BLUE =(186, 212, 239)

color_fondo = WHITE
color_linea = BLUE
color_punto = BLACK
color_texto = BLACK
color_graph = RED
color_grid = LIGTH_BLUE

# Variables
done = False
vectors = []
vector_thicknes = 2
WIDTH, HEIGHT = 600, 600
ORIGEN = (int(WIDTH/2), int(HEIGHT/2))
text_font_size = 30

# Crea el TextInput-object
textinput = pygame_textinput.TextInput(font_size=text_font_size)
textinput.set_text_color(color_texto)
textinput.set_cursor_color(color_texto)
text_margen_x = 10
text_margen_y = 25

# Display propertyes
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Vector graficator')
clock = pygame.time.Clock()

def position_conversor(punto):
    # if type(punto) is tuple:
    return (punto[0]+ORIGEN[0], -1*punto[1]+ORIGEN[1])


def add_vector(cords):
    global vectors
    v = Vector(cords)
    vectors.append(v)

def draw_vectores():
    if len(vectors) >= 1:
        for v in vectors:
            # print(v.get_cords())
            end_pos = position_conversor(v.get_cords())
            pygame.draw.line(screen, color_linea, ORIGEN, end_pos, vector_thicknes)
            pygame.draw.circle(screen, color_punto, end_pos, 2)

def draw_ejes():
    # Linea del eje X
    pygame.draw.line(screen, color_graph, (0, HEIGHT/2), (WIDTH,HEIGHT/2), 2)
    # Linea del eje Y
    pygame.draw.line(screen, color_graph, (WIDTH/2, 0), (WIDTH/2,HEIGHT), 2)


# Transforma una string en una tupla y agraga el vector
# ejemplo: '<50, 20>' => (50,20)
def add_vector_text(text):
    text = text.replace('<','')
    text = text.replace('>','')
    spl = text.split(',')
    cordenadas = (int(spl[0]), int(spl[1]))
    
    add_vector(cordenadas)

def draw_cuadricula():
    blockSize = 20 #Set the size of the grid block
    for x in range(10, WIDTH, 10):
        pygame.draw.line(screen, color_grid, (x, 0), (x, HEIGHT), 1)
    for y in range(10, HEIGHT, 10):
        pygame.draw.line(screen, color_grid, (0, y), (WIDTH, y), 1)
    

# add_vector((100,100))
# add_vector((50,150))
# add_vector((-50, -100))

# Main loop
while not done:
    screen.fill(color_fondo)
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
    
# Imprimir la cuadricula
    draw_cuadricula()
    # Imprimir los ejes X y Y
    draw_ejes()
    # Imprimir los vectores en el array
    draw_vectores()

    # Text input events
    if textinput.update(events):
        comando = textinput.get_text()
        textinput.clear_text()

        if comando == 'clear':
            vectors.clear()
        else:
            add_vector_text(comando)
    screen.blit(textinput.get_surface(), (text_margen_x, HEIGHT - text_margen_y))

    pygame.display.update()
    clock.tick(30)
    # pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))




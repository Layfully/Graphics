import pygame
from cube import Cube
from spring import Spring
from texture_loader import TextureLoader
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


class Pygame3DApplication:
    def __init__(self):
        pygame.init()
        self.display = (800, 1000)
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        gluPerspective(45, (self.display[0] / self.display[1]), 0.1, 150.0)
        gluLookAt(0, -10, 30, 0.0, -10.0, 0.0, 0.0, 1.0, 0.0)
        glEnable(GL_DEPTH_TEST)  # Enable depth testing
        glDepthFunc(GL_LESS)
        glTranslate(0, -5, 0)
        self.texture_steel = TextureLoader.load_texture("tex/steel.bmp")
        self.cube = Cube()
        self.spring = Spring(self.texture_steel)

        self.counter = 0
        self.getTicksLastFrame = 0
        self.move = 1.2
        self.v = 0

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    def render_frame(self):
        t = pygame.time.get_ticks()
        deltaTime = (t - self.getTicksLastFrame) / 1000.0
        self.getTicksLastFrame = t

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 0, 1, 0)
        self.counter += 1
        self.cube.draw()
        self.move, self.v = self.spring.draw_spring(0.01, self.move, self.v)

        pygame.display.flip()
        pygame.time.wait(10)

    def run(self):
        while True:
            for event in pygame.event.get():
                self.handle_event(event)
            self.render_frame()


if __name__ == "__main__":
    app = Pygame3DApplication()
    app.run()
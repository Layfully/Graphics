import pygame
from OpenGL.GL import *


class TextureLoader:
    @staticmethod
    def set_texture_parameters():
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    @staticmethod
    def load_texture(filename):
        image = pygame.image.load(filename)
        texture_data = pygame.image.tostring(image, "RGB")
        width, height = image.get_size()
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        TextureLoader.set_texture_parameters()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
        return texture_id

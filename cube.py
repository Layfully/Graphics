from OpenGL.GL import *
from texture_loader import TextureLoader


class Cube:
    def __init__(self):
        self.vertices = [
            (3, 0, 3), (3, 0, -3), (-3, 0, -3), (-3, 0, 3),
            (3, 0.5, 3), (3, 0.5, -3), (-3, 0.5, -3), (-3, 0.5, 3)
        ]

        self.surfaces = (
            (4, 5, 6, 7),
            (0, 1, 5, 4),
            (1, 2, 6, 5),
            (2, 3, 7, 6),
            (3, 0, 4, 7),
            (0, 1, 2, 3)
        )

        self.tex_coords = [
            0.0, 0.0,  1.0, 0.0,  1.0, 1.0,  0.0, 1.0,  # Front face
            1.0, 0.0,  1.0, 1.0,  0.0, 1.0,  0.0, 0.0,  # Back face
            0.0, 1.0,  0.0, 0.0,  1.0, 0.0,  1.0, 1.0,  # Top face
            1.0, 1.0,  0.0, 1.0,  0.0, 0.0,  1.0, 0.0,  # Bottom face
            1.0, 0.0,  1.0, 1.0,  0.0, 1.0,  0.0, 0.0,  # Right face
            0.0, 0.0,  1.0, 0.0,  1.0, 1.0,  0.0, 1.0   # Left face
        ]

        self.texture = TextureLoader.load_texture("tex/wood.bmp")

    def draw(self):
        glPushMatrix()
        glTranslated(0, 0.4, 0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glVertexPointer(3, GL_FLOAT, 0, self.vertices)
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glTexCoordPointer(2, GL_FLOAT, 0, self.tex_coords)
        glDrawElements(GL_QUADS, len(self.surfaces) * 4, GL_UNSIGNED_INT, self.surfaces)
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from physics import Physics
from texture_loader import TextureLoader


class Spring:
    def __init__(self, texture):
        self.texture = texture
        self.wood = TextureLoader.load_texture("tex/wood.bmp")

    def draw_spring_begin(self):
        glPushMatrix()
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTranslated(0.45, 0, -0.25)
        glRotatef(90, 0, 0, 1)
        cylinder = gluNewQuadric()
        gluQuadricTexture(cylinder, True)
        gluCylinder(cylinder, 0.15, 0.15, 0.25, 16, 1)

        sfera = gluNewQuadric()
        gluQuadricTexture(sfera, True)
        gluSphere(sfera, 0.15, 16, 16)

        glRotatef(90, 0, 1, 0)
        cylinder2 = gluNewQuadric()
        gluQuadricTexture(cylinder2, True)
        gluCylinder(cylinder2, 0.15, 0.15, 0.4, 16, 1)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

    def draw_spring_end(self, spring_end):
        glPushMatrix()
        glRotatef(90, 1, 0, 0)
        glTranslated(spring_end[0], spring_end[1], spring_end[2])

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTranslated(-0.15, 0, 0)
        glRotatef(90, 0, 0, 1)
        glTranslated(0.25, 0, 0)
        glRotatef(-90, 0, 1, 0)

        cylinder = gluNewQuadric()
        gluQuadricTexture(cylinder, True)
        gluCylinder(cylinder, 0.15, 0.15, 0.25, 16, 1)

        sfera = gluNewQuadric()
        gluQuadricTexture(sfera, True)
        gluSphere(sfera, 0.15, 16, 16)

        glRotatef(90, 0, 1, 0)
        cylinder2 = gluNewQuadric()
        gluQuadricTexture(cylinder2, True)
        gluCylinder(cylinder2, 0.15, 0.15, 0.4, 16, 1)
        glDisable(GL_TEXTURE_2D)

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.wood)
        glTranslated(0, 0, 2.4)
        sfera = gluNewQuadric()
        gluQuadricTexture(sfera, True)
        gluSphere(sfera, 2, 16, 16)

        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

    def draw_main_spring(self, t, u, precision_t, precision_u, move, scale=1.0):
        tex_cord = [(0.0, 1.0), (1.0, 1.0), (0.0, 0.0), (1.0, 0.0)]
        glPushMatrix()
        glRotatef(90, 1, 0, 0)
        m_t = (t * math.pi) / precision_t
        m_u = (u * math.pi) / precision_u
        vertexes = []

        for p in range(precision_t + 1):
            for v in range(precision_u):
                x_i = (math.cos(m_t * p) * (3 + math.cos(m_u * v))) * scale
                y_i = (math.sin(m_t * p) * (3 + math.cos(m_u * v))) * scale
                z_i = ((0.3 + move) * m_t * p + math.sin(m_u * v)) * scale
                vertexes.append((x_i, y_i, z_i))

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glBegin(GL_TRIANGLES)

        for p in range(precision_t):
            for v in range(precision_u):
                curr_idx = p * precision_u + v
                if v != precision_u - 1:
                    w1 = curr_idx + precision_u
                    w2 = curr_idx + 1
                    glTexCoord2fv(tex_cord[0])
                    glVertex3fv(vertexes[curr_idx])
                    glTexCoord2fv(tex_cord[1])
                    glVertex3fv(vertexes[curr_idx + precision_u])
                    glTexCoord2fv(tex_cord[2])
                    glVertex3fv(vertexes[curr_idx + 1])
                else:
                    w1 = curr_idx + 1
                    w2 = curr_idx - precision_u + 1
                    glTexCoord2fv(tex_cord[0])
                    glVertex3fv(vertexes[curr_idx])
                    glTexCoord2fv(tex_cord[1])
                    glVertex3fv(vertexes[curr_idx + precision_u])
                    glTexCoord2fv(tex_cord[2])
                    glVertex3fv(vertexes[curr_idx - precision_u + 1])
                if v:
                    w1 = curr_idx + precision_u - 1
                    w2 = curr_idx + precision_u
                    glTexCoord2fv(tex_cord[2])
                    glVertex3fv(vertexes[curr_idx])
                    glTexCoord2fv(tex_cord[1])
                    glVertex3fv(vertexes[curr_idx + precision_u - 1])
                    glTexCoord2fv(tex_cord[3])
                    glVertex3fv(vertexes[curr_idx + precision_u])
                else:
                    w1 = curr_idx + (2 * precision_u - 1)
                    w2 = curr_idx + precision_u
                    glTexCoord2fv(tex_cord[2])
                    glVertex3fv(vertexes[curr_idx])
                    glTexCoord2fv(tex_cord[1])
                    glVertex3fv(vertexes[curr_idx + (2 * precision_u - 1)])
                    glTexCoord2fv(tex_cord[3])
                    glVertex3fv(vertexes[curr_idx + precision_u])

        glEnd()
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
        return vertexes[-precision_u], move + 0.3

    def draw_spring(self, deltaTime, move, v):
        self.draw_spring_begin()
        spring_end, pos = self.draw_main_spring(12, 2, 75, 12, move, 0.15)
        self.draw_spring_end(spring_end)
        pos, v = Physics.calculate_movement(pos, v, deltaTime)
        return pos - 0.3, v
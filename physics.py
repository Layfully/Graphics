import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Physics:
    GRAVITY_ACCELERATION = 9.81
    MASS = 10
    REST_LENGTH = 0.8
    SPRING_CONSTANT = 1000

    @staticmethod
    def calculate_force(displacement):
        spring_force = Physics.SPRING_CONSTANT * displacement
        gravity_force = Physics.GRAVITY_ACCELERATION * Physics.MASS
        return spring_force + gravity_force

    @staticmethod
    def calculate_acceleration(force):
        return force / Physics.MASS

    @staticmethod
    def calculate_displacement(pos):
        return Physics.REST_LENGTH - pos

    @staticmethod
    def update_velocity(velocity, acceleration, delta_time):
        return velocity + acceleration * delta_time

    @staticmethod
    def update_position(pos, velocity, delta_time):
        return pos + velocity * delta_time

    @staticmethod
    def calculate_movement(pos, velocity, delta_time):
        displacement = Physics.calculate_displacement(pos)
        force = Physics.calculate_force(displacement)
        acceleration = Physics.calculate_acceleration(force)

        velocity = Physics.update_velocity(velocity, acceleration, delta_time)
        pos = Physics.update_position(pos, velocity, delta_time)

        return pos, velocity
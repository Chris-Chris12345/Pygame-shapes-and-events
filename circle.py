import pygame
pygame.init()

scr = pygame.display.set_mode((600,600))
scr.fill((255,255,255))
blue = (0,0,255)
red = (255,0,0)

pygame.display.update()

class Circle():
    def __init__(self, color, pos, radius, width):
        self.circle_color = color
        self.circle_pos = pos
        self.circle_radius = radius
        self.circle_width = width
        self.circle_surface = scr

    def draw(self):
        self.draw_circle = pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)

    def grow(self, r):
        self.circle_radius = self.circle_radius + r
        self.draw_circle = pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)

circle = Circle(blue, (300,300), 25, 0)

class Rectangle():
    def __init__(self, color, pos, length, width):
        self.rectangle_color = color
        self.rectangle_pos = pos
        self.rectangle_length = length
        self.rectangle_width = width
        self.rectangle_surface = scr

    def area(self):
        return self.rectangle_length * self.rectangle_width

rectangle = Rectangle(red, (300,300), 20, 10)
print(rectangle.area())


while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            scr.fill((255,255,255))
            circle.draw()
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            scr.fill((255,255,255))
            circle.grow(10)
            pygame.display.update()
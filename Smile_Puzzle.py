import sys
import pygame
from pygame.locals import *

# Initialize
pygame.init()

# Display Screen
display_width = 1280
display_height = 720
display = pygame.display.set_mode((display_width, display_height))
display_rect = display.get_rect()

# Essentials
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Display Picture
Image_display = pygame.image.load("Smile_Screen_Back.jpg")

# Center Rectangle
center_rectangle = Rect(0, 0, 498, 498)
center_rectangle.center = display_width // 2, display_height // 2

# rectangle
rect = Rect(0, 0, 300, 50)
rect.center = display_width // 2, display_height // 2 - 50
rect_2 = Rect(0, 0, 300, 50)
rect_2.center = display_width // 2, display_height // 2 + 50

# font
font = pygame.font.SysFont('Open Sans Bold', 30)

# Random Images
images = ["SmileScreen_1.png", "SmileScreen_2.png", "SmileScreen_3.png", "SmileScreen_4.png", "SmileScreen_5.png",
          "SmileScreen_6.png", "SmileScreen_7.png", "SmileScreen_8.png"]

# We can use random.choice

# Pictures of Rectangles
Image_1 = pygame.image.load("SmileScreen_1.png").convert()
rectangle_1 = Image_1.get_rect()
rectangle_1.update(391, 111, 166.6, 166.6)
Image_2 = pygame.image.load("SmileScreen_2.png").convert()
rectangle_2 = Image_2.get_rect()
rectangle_2.update(557, 111, 166.6, 166.6)
Image_3 = pygame.image.load("SmileScreen_3.png").convert()
rectangle_3 = Image_3.get_rect()
rectangle_3.update(723, 111, 166.6, 166.6)
Image_4 = pygame.image.load("SmileScreen_4.png").convert()
rectangle_4 = Image_4.get_rect()
rectangle_4.update(391, 277, 166.6, 166.6)
Image_5 = pygame.image.load("SmileScreen_5.png").convert()
rectangle_5 = Image_5.get_rect()
rectangle_5.update(557, 277, 166.6, 166.6)
Image_6 = pygame.image.load("SmileScreen_6.png").convert()
rectangle_6 = Image_6.get_rect()
rectangle_6.update(723, 277, 166.6, 166.6)
Image_7 = pygame.image.load("SmileScreen_7.png").convert()
rectangle_7 = Image_7.get_rect()
rectangle_7.update(391, 443, 166.6, 166.6)
Image_8 = pygame.image.load("SmileScreen_8.png").convert()
rectangle_8 = Image_8.get_rect()
rectangle_8.update(557, 443, 166.6, 166.6)

# Movement Necessities
current_image = None
LeftButton = 0
rectangle_dragging = False

# Game Title and Icon
pygame.display.set_caption("This is my smile game")
icon = pygame.image.load("smile.png")
pygame.display.set_icon(icon)
font = pygame.font.SysFont("SansitaOne.tff", 25)


def blit():
    display.blit(Image_display, (0, 0))
    display.blit(Image_1, rectangle_1)
    display.blit(Image_2, rectangle_2)
    display.blit(Image_3, rectangle_3)
    display.blit(Image_4, rectangle_4)
    display.blit(Image_5, rectangle_5)
    display.blit(Image_6, rectangle_6)
    display.blit(Image_7, rectangle_7)
    display.blit(Image_8, rectangle_8)


# all rectangle coordinates
rect_top = [rectangle_1.midtop, rectangle_2.midtop, rectangle_3.midtop, rectangle_4.midtop, rectangle_5.midtop,
            rectangle_6.midtop, rectangle_7.midtop, rectangle_8.midtop]
rect_bottom = [rectangle_1.midbottom, rectangle_2.midbottom, rectangle_3.midbottom, rectangle_4.midbottom,
               rectangle_5.midbottom, rectangle_6.midbottom, rectangle_7.midbottom, rectangle_8.midbottom]
rect_right = [rectangle_1.midright, rectangle_2.midright, rectangle_3.midright, rectangle_4.midright,
              rectangle_5.midright, rectangle_6.midright, rectangle_7.midright, rectangle_8.midright]
rect_left = [rectangle_1.midleft, rectangle_2.midleft, rectangle_3.midleft, rectangle_4.midleft, rectangle_5.midleft,
             rectangle_6.midleft, rectangle_7.midleft, rectangle_8.midleft]
print("\n", rect_top, "\n", rect_bottom, "\n", rect_right, "\n", rect_left, "\n")


# working on the slide (Functionality)
def movement():
    if current_image == 1:
        if rectangle_1.midtop != rectangle_2.midbottom and \
                rectangle_1.midtop != rectangle_3.midbottom and \
                rectangle_1.midtop != rectangle_4.midbottom and \
                rectangle_1.midtop != rectangle_5.midbottom and \
                rectangle_1.midtop != rectangle_6.midbottom and \
                rectangle_1.midtop != rectangle_7.midbottom and \
                rectangle_1.midtop != rectangle_8.midbottom and \
                rectangle_1.top != center_rectangle.top:
            rectangle_1.x += 0
            rectangle_1.y -= 166
            rectangle_1.clamp_ip(center_rectangle)
        elif rectangle_1.midbottom != rectangle_2.midtop and \
                rectangle_1.midbottom != rectangle_3.midtop and \
                rectangle_1.midbottom != rectangle_4.midtop and \
                rectangle_1.midbottom != rectangle_5.midtop and \
                rectangle_1.midbottom != rectangle_6.midtop and \
                rectangle_1.midbottom != rectangle_7.midtop and \
                rectangle_1.midbottom != rectangle_8.midtop and \
                rectangle_1.bottom != center_rectangle.bottom:
            rectangle_1.x += 0
            rectangle_1.y += 166
            rectangle_1.clamp_ip(center_rectangle)
        elif rectangle_1.midleft != rectangle_2.midright and \
                rectangle_1.midleft != rectangle_3.midright and \
                rectangle_1.midleft != rectangle_4.midright and \
                rectangle_1.midleft != rectangle_5.midright and \
                rectangle_1.midleft != rectangle_6.midright and \
                rectangle_1.midleft != rectangle_7.midright and \
                rectangle_1.midleft != rectangle_8.midright and \
                rectangle_1.left != center_rectangle.left:
            rectangle_1.x -= 166
            rectangle_1.y += 0
            rectangle_1.clamp_ip(center_rectangle)
        elif rectangle_1.midright != rectangle_2.midleft and \
                rectangle_1.midright != rectangle_3.midleft and \
                rectangle_1.midright != rectangle_4.midleft and \
                rectangle_1.midright != rectangle_5.midleft and \
                rectangle_1.midright != rectangle_6.midleft and \
                rectangle_1.midright != rectangle_7.midleft and \
                rectangle_1.midright != rectangle_8.midleft and \
                rectangle_1.right != center_rectangle.right:
            rectangle_1.x += 166
            rectangle_1.y += 0
            rectangle_1.clamp_ip(center_rectangle)
    elif current_image == 2:
        if rectangle_2.midtop != rectangle_1.midbottom and \
                rectangle_2.midtop != rectangle_3.midbottom and \
                rectangle_2.midtop != rectangle_4.midbottom and \
                rectangle_2.midtop != rectangle_5.midbottom and \
                rectangle_2.midtop != rectangle_6.midbottom and \
                rectangle_2.midtop != rectangle_7.midbottom and \
                rectangle_2.midtop != rectangle_8.midbottom and \
                rectangle_2.top != center_rectangle.top:
            rectangle_2.x += 0
            rectangle_2.y -= 166
            rectangle_2.clamp_ip(center_rectangle)
        elif rectangle_2.midbottom != rectangle_1.midtop and \
                rectangle_2.midbottom != rectangle_3.midtop and \
                rectangle_2.midbottom != rectangle_4.midtop and \
                rectangle_2.midbottom != rectangle_5.midtop and \
                rectangle_2.midbottom != rectangle_6.midtop and \
                rectangle_2.midbottom != rectangle_7.midtop and \
                rectangle_2.midbottom != rectangle_8.midtop and \
                rectangle_2.bottom != center_rectangle.bottom:
            rectangle_2.x += 0
            rectangle_2.y += 166
            rectangle_2.clamp_ip(center_rectangle)
        elif rectangle_2.midleft != rectangle_1.midright and \
                rectangle_2.midleft != rectangle_3.midright and \
                rectangle_2.midleft != rectangle_4.midright and \
                rectangle_2.midleft != rectangle_5.midright and \
                rectangle_2.midleft != rectangle_6.midright and \
                rectangle_2.midleft != rectangle_7.midright and \
                rectangle_2.midleft != rectangle_8.midright and \
                rectangle_2.left != center_rectangle.left:
            rectangle_2.x -= 166
            rectangle_2.y += 0
            rectangle_2.clamp_ip(center_rectangle)
        elif rectangle_2.midright != rectangle_1.midleft and \
                rectangle_2.midright != rectangle_3.midleft and \
                rectangle_2.midright != rectangle_4.midleft and \
                rectangle_2.midright != rectangle_5.midleft and \
                rectangle_2.midright != rectangle_6.midleft and \
                rectangle_2.midright != rectangle_7.midleft and \
                rectangle_2.midright != rectangle_8.midleft and \
                rectangle_2.right != center_rectangle.right:
            rectangle_2.x += 166
            rectangle_2.y += 0
            rectangle_2.clamp_ip(center_rectangle)
    elif current_image == 3:
        if rectangle_3.midtop != rectangle_1.midbottom and \
                rectangle_3.midtop != rectangle_2.midbottom and \
                rectangle_3.midtop != rectangle_4.midbottom and \
                rectangle_3.midtop != rectangle_5.midbottom and \
                rectangle_3.midtop != rectangle_6.midbottom and \
                rectangle_3.midtop != rectangle_7.midbottom and \
                rectangle_3.midtop != rectangle_8.midbottom and \
                rectangle_3.top != center_rectangle.top:
            rectangle_3.x += 0
            rectangle_3.y -= 166
            rectangle_3.clamp_ip(center_rectangle)
        elif rectangle_3.midbottom != rectangle_1.midtop and \
                rectangle_3.midbottom != rectangle_2.midtop and \
                rectangle_3.midbottom != rectangle_4.midtop and \
                rectangle_3.midbottom != rectangle_5.midtop and \
                rectangle_3.midbottom != rectangle_6.midtop and \
                rectangle_3.midbottom != rectangle_7.midtop and \
                rectangle_3.midbottom != rectangle_8.midtop and \
                rectangle_3.bottom != center_rectangle.bottom:
            rectangle_3.x += 0
            rectangle_3.y += 166
            rectangle_3.clamp_ip(center_rectangle)
        elif rectangle_3.midleft != rectangle_1.midright and \
                rectangle_3.midleft != rectangle_2.midright and \
                rectangle_3.midleft != rectangle_4.midright and \
                rectangle_3.midleft != rectangle_5.midright and \
                rectangle_3.midleft != rectangle_6.midright and \
                rectangle_3.midleft != rectangle_7.midright and \
                rectangle_3.midleft != rectangle_8.midright and \
                rectangle_3.left != center_rectangle.left:
            rectangle_3.x -= 166
            rectangle_3.y += 0
            rectangle_3.clamp_ip(center_rectangle)
        elif rectangle_3.midright != rectangle_1.midleft and \
                rectangle_3.midright != rectangle_2.midleft and \
                rectangle_3.midright != rectangle_4.midleft and \
                rectangle_3.midright != rectangle_5.midleft and \
                rectangle_3.midright != rectangle_6.midleft and \
                rectangle_3.midright != rectangle_7.midleft and \
                rectangle_3.midright != rectangle_8.midleft and \
                rectangle_3.right != center_rectangle.right:
            rectangle_3.x += 166
            rectangle_3.y += 0
            rectangle_3.clamp_ip(center_rectangle)
    elif current_image == 4:
        if rectangle_4.midtop != rectangle_1.midbottom and \
                rectangle_4.midtop != rectangle_2.midbottom and \
                rectangle_4.midtop != rectangle_3.midbottom and \
                rectangle_4.midtop != rectangle_5.midbottom and \
                rectangle_4.midtop != rectangle_6.midbottom and \
                rectangle_4.midtop != rectangle_7.midbottom and \
                rectangle_4.midtop != rectangle_8.midbottom and \
                rectangle_4.top != center_rectangle.top:
            rectangle_4.x += 0
            rectangle_4.y -= 166
            rectangle_4.clamp_ip(center_rectangle)
        elif rectangle_4.midbottom != rectangle_1.midtop and \
                rectangle_4.midbottom != rectangle_2.midtop and \
                rectangle_4.midbottom != rectangle_3.midtop and \
                rectangle_4.midbottom != rectangle_5.midtop and \
                rectangle_4.midbottom != rectangle_6.midtop and \
                rectangle_4.midbottom != rectangle_7.midtop and \
                rectangle_4.midbottom != rectangle_8.midtop and \
                rectangle_4.bottom != center_rectangle.bottom:
            rectangle_4.x += 0
            rectangle_4.y += 166
            rectangle_4.clamp_ip(center_rectangle)
        elif rectangle_4.midleft != rectangle_1.midright and \
                rectangle_4.midleft != rectangle_2.midright and \
                rectangle_4.midleft != rectangle_3.midright and \
                rectangle_4.midleft != rectangle_5.midright and \
                rectangle_4.midleft != rectangle_6.midright and \
                rectangle_4.midleft != rectangle_7.midright and \
                rectangle_4.midleft != rectangle_8.midright and \
                rectangle_4.left != center_rectangle.left:
            rectangle_4.x -= 166
            rectangle_4.y += 0
            rectangle_4.clamp_ip(center_rectangle)
        elif rectangle_4.midright != rectangle_1.midleft and \
                rectangle_4.midright != rectangle_2.midleft and \
                rectangle_4.midright != rectangle_3.midleft and \
                rectangle_4.midright != rectangle_5.midleft and \
                rectangle_4.midright != rectangle_6.midleft and \
                rectangle_4.midright != rectangle_7.midleft and \
                rectangle_4.midright != rectangle_8.midleft and \
                rectangle_4.right != center_rectangle.right:
            rectangle_4.x += 166
            rectangle_4.y += 0
            rectangle_4.clamp_ip(center_rectangle)
    elif current_image == 5:
        if rectangle_5.midtop != rectangle_1.midbottom and \
                rectangle_5.midtop != rectangle_2.midbottom and \
                rectangle_5.midtop != rectangle_3.midbottom and \
                rectangle_5.midtop != rectangle_4.midbottom and \
                rectangle_5.midtop != rectangle_6.midbottom and \
                rectangle_5.midtop != rectangle_7.midbottom and \
                rectangle_5.midtop != rectangle_8.midbottom and \
                rectangle_5.top != center_rectangle.top:
            rectangle_5.x += 0
            rectangle_5.y -= 166
            rectangle_5.clamp_ip(center_rectangle)
        elif rectangle_5.midbottom != rectangle_1.midtop and \
                rectangle_5.midbottom != rectangle_2.midtop and \
                rectangle_5.midbottom != rectangle_3.midtop and \
                rectangle_5.midbottom != rectangle_4.midtop and \
                rectangle_5.midbottom != rectangle_6.midtop and \
                rectangle_5.midbottom != rectangle_7.midtop and \
                rectangle_5.midbottom != rectangle_8.midtop and \
                rectangle_5.bottom != center_rectangle.bottom:
            rectangle_5.x += 0
            rectangle_5.y += 166
            rectangle_5.clamp_ip(center_rectangle)
        elif rectangle_5.midleft != rectangle_1.midright and \
                rectangle_5.midleft != rectangle_2.midright and \
                rectangle_5.midleft != rectangle_3.midright and \
                rectangle_5.midleft != rectangle_4.midright and \
                rectangle_5.midleft != rectangle_6.midright and \
                rectangle_5.midleft != rectangle_7.midright and \
                rectangle_5.midleft != rectangle_8.midright and \
                rectangle_5.left != center_rectangle.left:
            rectangle_5.x -= 166
            rectangle_5.y += 0
            rectangle_5.clamp_ip(center_rectangle)
        elif rectangle_5.midright != rectangle_1.midleft and \
                rectangle_5.midright != rectangle_2.midleft and \
                rectangle_5.midright != rectangle_3.midleft and \
                rectangle_5.midright != rectangle_4.midleft and \
                rectangle_5.midright != rectangle_6.midleft and \
                rectangle_5.midright != rectangle_7.midleft and \
                rectangle_5.midright != rectangle_8.midleft and \
                rectangle_5.right != center_rectangle.right:
            rectangle_5.x += 166
            rectangle_5.y += 0
            rectangle_5.clamp_ip(center_rectangle)
    elif current_image == 6:
        if rectangle_6.midtop != rectangle_1.midbottom and \
                rectangle_6.midtop != rectangle_2.midbottom and \
                rectangle_6.midtop != rectangle_3.midbottom and \
                rectangle_6.midtop != rectangle_4.midbottom and \
                rectangle_6.midtop != rectangle_5.midbottom and \
                rectangle_6.midtop != rectangle_7.midbottom and \
                rectangle_6.midtop != rectangle_8.midbottom and \
                rectangle_6.top != center_rectangle.top:
            rectangle_6.x += 0
            rectangle_6.y -= 166
            rectangle_6.clamp_ip(center_rectangle)
        elif rectangle_6.midbottom != rectangle_1.midtop and \
                rectangle_6.midbottom != rectangle_2.midtop and \
                rectangle_6.midbottom != rectangle_3.midtop and \
                rectangle_6.midbottom != rectangle_4.midtop and \
                rectangle_6.midbottom != rectangle_5.midtop and \
                rectangle_6.midbottom != rectangle_7.midtop and \
                rectangle_6.midbottom != rectangle_8.midtop and \
                rectangle_6.bottom != center_rectangle.bottom:
            rectangle_6.x += 0
            rectangle_6.y += 166
            rectangle_6.clamp_ip(center_rectangle)
        elif rectangle_6.midleft != rectangle_1.midright and \
                rectangle_6.midleft != rectangle_2.midright and \
                rectangle_6.midleft != rectangle_3.midright and \
                rectangle_6.midleft != rectangle_4.midright and \
                rectangle_6.midleft != rectangle_5.midright and \
                rectangle_6.midleft != rectangle_7.midright and \
                rectangle_6.midleft != rectangle_8.midright and \
                rectangle_6.left != center_rectangle.left:
            rectangle_6.x -= 166
            rectangle_6.y += 0
            rectangle_6.clamp_ip(center_rectangle)
        elif rectangle_6.midright != rectangle_1.midleft and \
                rectangle_6.midright != rectangle_2.midleft and \
                rectangle_6.midright != rectangle_3.midleft and \
                rectangle_6.midright != rectangle_4.midleft and \
                rectangle_6.midright != rectangle_5.midleft and \
                rectangle_6.midright != rectangle_7.midleft and \
                rectangle_6.midright != rectangle_8.midleft and \
                rectangle_6.right != center_rectangle.right:
            rectangle_6.x += 166
            rectangle_6.y += 0
            rectangle_6.clamp_ip(center_rectangle)
    elif current_image == 7:
        if rectangle_7.midtop != rectangle_1.midbottom and \
                rectangle_7.midtop != rectangle_2.midbottom and \
                rectangle_7.midtop != rectangle_3.midbottom and \
                rectangle_7.midtop != rectangle_4.midbottom and \
                rectangle_7.midtop != rectangle_6.midbottom and \
                rectangle_7.midtop != rectangle_5.midbottom and \
                rectangle_7.midtop != rectangle_8.midbottom and \
                rectangle_7.top != center_rectangle.top:
            rectangle_7.x += 0
            rectangle_7.y -= 166
            rectangle_7.clamp_ip(center_rectangle)
        elif rectangle_7.midbottom != rectangle_1.midtop and \
                rectangle_7.midbottom != rectangle_2.midtop and \
                rectangle_7.midbottom != rectangle_3.midtop and \
                rectangle_7.midbottom != rectangle_4.midtop and \
                rectangle_7.midbottom != rectangle_6.midtop and \
                rectangle_7.midbottom != rectangle_5.midtop and \
                rectangle_7.midbottom != rectangle_8.midtop and \
                rectangle_7.bottom != center_rectangle.bottom:
            rectangle_7.x += 0
            rectangle_7.y += 166
            rectangle_7.clamp_ip(center_rectangle)
        elif rectangle_7.midleft != rectangle_1.midright and \
                rectangle_7.midleft != rectangle_2.midright and \
                rectangle_7.midleft != rectangle_3.midright and \
                rectangle_7.midleft != rectangle_4.midright and \
                rectangle_7.midleft != rectangle_6.midright and \
                rectangle_7.midleft != rectangle_5.midright and \
                rectangle_7.midleft != rectangle_8.midright and \
                rectangle_7.left != center_rectangle.left:
            rectangle_7.x -= 166
            rectangle_7.y += 0
            rectangle_7.clamp_ip(center_rectangle)
        elif rectangle_7.midright != rectangle_1.midleft and \
                rectangle_7.midright != rectangle_2.midleft and \
                rectangle_7.midright != rectangle_3.midleft and \
                rectangle_7.midright != rectangle_4.midleft and \
                rectangle_7.midright != rectangle_6.midleft and \
                rectangle_7.midright != rectangle_5.midleft and \
                rectangle_7.midright != rectangle_8.midleft and \
                rectangle_7.right != center_rectangle.right:
            rectangle_7.x += 166
            rectangle_7.y += 0
            rectangle_7.clamp_ip(center_rectangle)
    elif current_image == 8:
        if rectangle_8.midtop != rectangle_1.midbottom and \
                rectangle_8.midtop != rectangle_2.midbottom and \
                rectangle_8.midtop != rectangle_3.midbottom and \
                rectangle_8.midtop != rectangle_4.midbottom and \
                rectangle_8.midtop != rectangle_5.midbottom and \
                rectangle_8.midtop != rectangle_7.midbottom and \
                rectangle_8.midtop != rectangle_6.midbottom and \
                rectangle_8.top != center_rectangle.top:
            rectangle_8.x += 0
            rectangle_8.y -= 166
            rectangle_8.clamp_ip(center_rectangle)
        elif rectangle_8.midbottom != rectangle_1.midtop and \
                rectangle_8.midbottom != rectangle_2.midtop and \
                rectangle_8.midbottom != rectangle_3.midtop and \
                rectangle_8.midbottom != rectangle_4.midtop and \
                rectangle_8.midbottom != rectangle_5.midtop and \
                rectangle_8.midbottom != rectangle_7.midtop and \
                rectangle_8.midbottom != rectangle_6.midtop and \
                rectangle_8.bottom != center_rectangle.bottom:
            rectangle_8.x += 0
            rectangle_8.y += 166
            rectangle_8.clamp_ip(center_rectangle)
        elif rectangle_8.midleft != rectangle_1.midright and \
                rectangle_8.midleft != rectangle_2.midright and \
                rectangle_8.midleft != rectangle_3.midright and \
                rectangle_8.midleft != rectangle_4.midright and \
                rectangle_8.midleft != rectangle_5.midright and \
                rectangle_8.midleft != rectangle_7.midright and \
                rectangle_8.midleft != rectangle_6.midright and \
                rectangle_8.left != center_rectangle.left:
            rectangle_8.x -= 166
            rectangle_8.y += 0
            rectangle_8.clamp_ip(center_rectangle)
        elif (rectangle_8.midright != rectangle_1.midleft) and \
                (rectangle_8.midright != rectangle_2.midleft) and \
                (rectangle_8.midright != rectangle_3.midleft) and \
                (rectangle_8.midright != rectangle_4.midleft) and \
                (rectangle_8.midright != rectangle_5.midleft) and \
                (rectangle_8.midright != rectangle_7.midleft) and \
                (rectangle_8.midright != rectangle_6.midleft) and \
                (rectangle_8.right != center_rectangle.right):
            rectangle_8.x += 166
            rectangle_8.y += 0
            rectangle_8.clamp_ip(center_rectangle)


# Main Loop of the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Working on movement of rectangle
        elif event.type == MOUSEBUTTONDOWN:
            if rectangle_1.collidepoint(event.pos):
                current_image = 1
            elif rectangle_2.collidepoint(event.pos):
                current_image = 2
            elif rectangle_3.collidepoint(event.pos):
                current_image = 3
            elif rectangle_4.collidepoint(event.pos):
                current_image = 4
            elif rectangle_5.collidepoint(event.pos):
                current_image = 5
            elif rectangle_6.collidepoint(event.pos):
                current_image = 6
            elif rectangle_7.collidepoint(event.pos):
                current_image = 7
            elif rectangle_8.collidepoint(event.pos):
                current_image = 8
            else:
                current_image = None
            movement()  # press whatever the mouse button you want to

    blit()  # Displaying Images
    pygame.display.update()

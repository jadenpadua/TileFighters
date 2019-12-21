
import pygame as pg
from settings import *
# Player class making yellow rectangle sprite
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(DARKGREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
    # Allows sprite to move, setting x and y positions
    def move(self, dx=0, dy=0):
        # Collision Handling
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy
    # Collision Handling, loops through walls and checks if cords are same
    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False
    # Updates sprite's position
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
# Wall object 
class Wall(pg.sprite.Sprite):
    
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(SIENNA)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    


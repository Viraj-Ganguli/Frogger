import pygame

class Log(pygame.sprite.Sprite):
  # constant values
  image = pygame.image.load('resources/log.png')
  starting_position = (300, 150)
  size = (60,30)
  screen_dim = 600, 500
  move_dist = 1

  def __init__(self):
    super().__init__()
    self.image = log.image
    self.rect = pygame.Rect((0, 0), Log.size)
    self.rect.center = Log.starting_position

  def move(self):
    self.rect.centerx += Log.move_dist

    if self.rect.left >= Log.screeen_dim[0]:
      self.rect.centerx = -Log.size[0] / 2

# Pygame introduction

### To starts pygame

`pygame.init()`

### Creation of the window

`screen = pygame.display.set_mode((800, 400))`

### In order to keep the window and update it

```
while True:
    pygame.display.update()
```

### How to close the game

```
for event in pygame.event.get():    # check all input event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()      # from sys
```

### How to give a name to the window

```
pygame.display.set_caption("game")
```

### Control the game speed (framerate)

```
# get the clock
clock = pygame.time.Clock()
# inside the while true loop
clock.tick(60) # the game runs not faster than 60 fps
```

### How to create a surface and display it

```
test_surface = pygame.Surface((width, height))  # create a surface
test_surface.fill('Color')

# inside while true
screen.blit(test_surface, (coordinate x, coordinate y))
```

### Coordinate system

The top-left corner of the window has the coordinate (0,0). The top-left corner of the surface will be placed in the indicated coordinates.

to move to the right, have to increase x;

to move to the bottom, have to _increase_ y;

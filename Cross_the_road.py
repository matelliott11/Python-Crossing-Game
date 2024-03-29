#Game Development 

#Gains access to pygame libary
import pygame

SCREEN_TITLE = "Matt's Crossing Game RPG in Python"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
#Colors in the game
WHITE_COLOR = (255,255,255)
BLACK_COLOR = (0,0,0)
RED_COLOR = (255,0,0)
GREEN_COLOR = (0,255,0)
BLUE_COLOR = (0,0,255)
##set the FPS to render the page
clock = pygame.time.Clock()

class Game:
# Typical rate of 60, equivalent to FPS
    TICK_RATE = 60

# Initializer for the game class to set up the width, height, and title
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
 
        # Create the window of specified size in white to display the game
        self.game_screen = pygame.display.set_mode((width, height))
        # Set the game window color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)
 
    def run_game_loop(self):
         is_game_over = False
         direction = 0
 
         player_character = PlayerCharacter('player.png', 375, 700, 50, 50)
         enemy_0 = NonPlayerCharacter('enemy.png', 20, 600, 50, 50)
   
# Main game loop, used to update all gameplay such as movement, checks, and graphics
# Runs until is_game_over = True
while not is_game_over:
 
         # A loop to get all of the events occuring at any given time
         # Events are most often mouse movement, mouse and button clicks, or exit events
         for event in pygame.event.get():
              # If we have a quite type event (exit out) then exit out of the game loop
                if event.type == pygame.QUIT:
                    is_game_over = True
              # Detect when key is pressed down
                elif event.type == pygame.KEYDOWN:
              # Move up if up key pressed
                    if event.key == pygame.K_UP:
                        direction = 1
              # Move down if down key pressed
                    elif event.key == pygame.K_DOWN:
                        direction = -1
              # Detect when key is released
                elif event.type == pygame.KEYUP:
              # Stop movement when key no longer pressed
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                
                print(event)
 
            # Redraw the screen to be a blank white window
            self.game_screen.fill(WHITE_COLOR)
            # Update the player position
            player_character.move(direction)
            # Draw the player at the new position
            player_character.draw(self.game_screen)
 
            # Move and draw the enemy character
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)
 
            # Update all game graphics
            pygame.display.update()
            # Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)
 
# Generic game object class to be subclassed by other objects in the game
class GameObject:
 
    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        # Scale the image up
        self.image = pygame.transform.scale(object_image, (width, height))
        
        self.x_pos = x
        self.y_pos = y
 
        self.width = width
        self.height = height
 
    # Draw the object by blitting it onto the background (game screen)
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))
 
# Class to represent the character contolled by the player
class PlayerCharacter(GameObject):
 
    # How many tiles the character moves per second
    SPEED = 10
 
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
 
# Move function will move character up if direction > 0 and down if < 0
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
# Make sure the character never goes past the bottom of the screen
        if self.y_pos >= max_height - 20:
            self.y_pos = max_height - 20
 
# Class to represent the enemies moving left to right and right to left
class NonPlayerCharacter(GameObject):
 
    # How many tiles the character moves per second
    SPEED = 10
 
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
 
    # Move function will move character right once it hits the far left of the
    # screen and left once it hits the far right of the screen
    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >=  max_width - 20:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED
 
       
pygame.init()
 
new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()
 
# Load the player image from the file directory
# player_image = pygame.image.load('player.png')
# Scale the image up
# player_image = pygame.transform.scale(player_image, (50, 50))
 
# Quit pygame and the program
pygame.quit()
quit()

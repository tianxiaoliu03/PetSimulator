
import pygame
import sys
from pet import Pet

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("Pet simulator!")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("Virtual Pet")

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the cat image
cat_image_path = "cat.jpg"

# Create the pet
pet_name = "Fluffy"
pet = Pet(pet_name, cat_image_path)

# Load the background image
bg = pygame.image.load("background.jpg")

# Health bar constants
BAR_WIDTH = 100
BAR_HEIGHT = 20

# Define buttons and food rect
buttons = {
    "feed": pygame.Rect(650, 50, 100, 50),
    "play": pygame.Rect(650, 110, 100, 50),
    "sleep": pygame.Rect(650, 170, 100, 50),
    "earn": pygame.Rect(650, 230, 100, 50),
    "status": pygame.Rect(650, 290, 100, 50)
}

food_image = pygame.image.load("food.jpg")
food_image = pygame.transform.scale(food_image, (50, 50))
food_rect = food_image.get_rect(topleft=(600, 400))

# Initial food dragging state
dragging_food = False

# Main loop
run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if food_rect.collidepoint(event.pos):
                    dragging_food = True
                for name, rect in buttons.items():
                    if rect.collidepoint(event.pos):
                        if name == "feed":
                            pet.feed()
                        elif name == "play":
                            pet.play()
                        elif name == "sleep":
                            pet.sleep()
                        elif name == "earn":
                            pet.earn_coins()
                        elif name == "status":
                            pet.check_status()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                dragging_food = False
                if pet.rect.colliderect(food_rect):
                    pet.feed()
        elif event.type == pygame.MOUSEMOTION:
            if dragging_food:
                food_rect.move_ip(event.rel)

    screen.blit(bg, (0, 0))  # Draw the background

    # Draw the pet
    screen.blit(pet.image, pet.rect)

    # Draw the food
    screen.blit(food_image, food_rect)

    # Draw buttons
    for name, rect in buttons.items():
        pygame.draw.rect(screen, GRAY, rect)
        text = my_font.render(name.capitalize(), True, BLACK)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    # Draw health bars
    pygame.draw.rect(screen, RED, (10, 10, BAR_WIDTH, BAR_HEIGHT))  # Hunger bar background
    pygame.draw.rect(screen, GREEN, (10, 10, pet.hunger, BAR_HEIGHT))  # Hunger bar
    pygame.draw.rect(screen, RED, (10, 40, BAR_WIDTH, BAR_HEIGHT))  # Sleepiness bar background
    pygame.draw.rect(screen, GREEN, (10, 40, pet.sleepiness, BAR_HEIGHT))  # Sleepiness bar
    pygame.draw.rect(screen, RED, (10, 70, BAR_WIDTH, BAR_HEIGHT))  # Happiness bar background
    pygame.draw.rect(screen, GREEN, (10, 70, pet.happiness, BAR_HEIGHT))  # Happiness bar

    coins_text = my_font.render(f"Coins: {pet.coins}", True, BLACK)
    screen.blit(coins_text, (10, 100))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()


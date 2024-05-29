
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
YELLOW = (255, 255, 0)

# Initialize Pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("Virtual Pet")

# Add the following at the start of your main.py file
intro_screen = True

# Define the play button for the intro screen
play_button = pygame.Rect(350, 450, 100, 50)

# Define instructions text
instructions = [
    "Welcome to the Pet Simulator!",
    "Take care of your pet by feeding, playing, and letting it sleep.",
    "Earn coins to buy food and water.",
    "Use the buttons to interact with your pet.",
    "Press 'Play' to start the game!"
]

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the cat image
cat_image_path = "cat.png"  # Ensure this is a PNG with transparency

# Create the pet
pet_name = "Fluffy"
pet = Pet(pet_name, cat_image_path)

# Load and scale the background image
bg = pygame.image.load("background.png").convert()
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Health bar constants
BAR_WIDTH = 100
BAR_HEIGHT = 20

# Define buttons and food/water rect
buttons = {
    "feed": pygame.Rect(650, 50, 100, 50),
    "play": pygame.Rect(650, 110, 100, 50),
    "sleep": pygame.Rect(650, 170, 100, 50),
    "earn": pygame.Rect(650, 230, 100, 50),
    "status": pygame.Rect(650, 290, 100, 50)
}

# Load the food image with transparency
food_image = pygame.image.load("food.png").convert_alpha()  # Ensure this is a PNG with transparency
food_image = pygame.transform.scale(food_image, (50, 50))
food_rect = food_image.get_rect(topleft=(10, 540))

# Load the water image with transparency
water_image = pygame.image.load("water.png").convert_alpha()  # Ensure this is a PNG with transparency
water_image = pygame.transform.scale(water_image, (50, 50))
water_rect = water_image.get_rect(topleft=(70, 540))

# Initial dragging state
dragging_food = False
dragging_water = False

# Main loop
run = True
clock = pygame.time.Clock()

show_status = False
status_text = ""


def draw_health_bar(screen, x, y, value, label):
    """Draw a health bar with a dynamic color gradient."""
    # Determine the color based on the value

    color = GREEN

    pygame.draw.rect(screen, RED, (x, y, BAR_WIDTH, BAR_HEIGHT))  # Background
    pygame.draw.rect(screen, color, (x, y, value, BAR_HEIGHT))  # Value bar

    label_text = my_font.render(label, True, BLACK)
    screen.blit(label_text, (x + BAR_WIDTH + 5, y))


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if food_rect.collidepoint(event.pos):
                    dragging_food = True
                elif water_rect.collidepoint(event.pos):
                    dragging_water = True
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
                            status_text = pet.check_status()
                            show_status = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                if dragging_food:
                    dragging_food = False
                    if pet.rect.colliderect(food_rect):
                        pet.feed()
                    food_rect.topleft = (10, 540)
                elif dragging_water:
                    dragging_water = False
                    if pet.rect.colliderect(water_rect):
                        pet.quench_thirst()
                    water_rect.topleft = (70, 540)
        elif event.type == pygame.MOUSEMOTION:
            if dragging_food:
                food_rect.move_ip(event.rel)
            elif dragging_water:
                water_rect.move_ip(event.rel)

    screen.blit(bg, (0, 0))  # Draw the background

    # Draw the pet
    screen.blit(pet.image, pet.rect)

    # Draw the food and water
    screen.blit(food_image, food_rect)
    screen.blit(water_image, water_rect)

    # Draw buttons
    for name, rect in buttons.items():
        pygame.draw.rect(screen, WHITE , rect, border_radius=10)
        text = my_font.render(name.capitalize(), True, BLACK)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    # Draw health bars
    draw_health_bar(screen, 10, 10, pet.hunger, "Hunger")
    draw_health_bar(screen, 10, 40, pet.sleepiness, "Sleepiness")
    draw_health_bar(screen, 10, 70, pet.happiness, "Happiness")
    draw_health_bar(screen, 10, 100, pet.thirstiness, "Thirstiness")

    coins_text = my_font.render(f"Coins: {pet.coins}", True, BLACK)
    screen.blit(coins_text, (10, 130))

    if show_status:
        status_surface = pygame.Surface((200, 100), pygame.SRCALPHA)
        status_surface.fill((255, 255, 255, 200))
        status_lines = status_text.split('\n')
        for i, line in enumerate(status_lines):
            line_text = my_font.render(line, True, BLACK)
            status_surface.blit(line_text, (10, 10 + 20 * i))
        screen.blit(status_surface, (50, 400))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()



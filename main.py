import pygame
import sys
from pet import Pet
from food import Food
from water import Water
from coin import Coin
import random

# Initialize Pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30, bold=True)  # Increased font size and made it bold
title_font = pygame.font.SysFont('Arial', 60, bold=True)  # Increased font size and made it bold
pygame.display.set_caption("Virtual Pet")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Add the following at the start of your main.py file
intro_screen = True



# Define instructions text
instructions = [
    "Welcome to the Pet Simulator!",
    "Take care of your pet by feeding, playing, and letting it sleep.",
    "Earn coins to buy food and water.",
    "Use the buttons to interact with your pet.",
    "Press 'Play' to start the game!"
]

# Set up the screen
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define the play button for the intro screen with adjusted dimensions
play_button_width = 150
play_button_height = 80
play_button_x = 380
play_button_y = 500
play_button = pygame.Rect(play_button_x, play_button_y, play_button_width, play_button_height)

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
    "play": pygame.Rect(650, 90, 100, 50),
    "sleep": pygame.Rect(650, 170, 100, 50),
}

# Load the food image with transparency
food_image = pygame.image.load("food.png").convert_alpha()  # Ensure this is a PNG with transparency
food_image = pygame.transform.scale(food_image, (50, 50))
food_rect = food_image.get_rect(topleft=(10, 540))
initial_food_position = food_rect.topleft

# Load the water image with transparency
water_image = pygame.image.load("water.png").convert_alpha()  # Ensure this is a PNG with transparency
water_image = pygame.transform.scale(water_image, (50, 50))
water_rect = water_image.get_rect(topleft=(70, 540))
initial_water_position = water_rect.topleft

# Create the coin
coin_image_path = "coin-sprite.png"  # Adjust file name/path as needed
coin = Coin(coin_image_path, SCREEN_WIDTH, SCREEN_HEIGHT)
coin_scale_factor = 1.75
coin.image = pygame.transform.scale(coin.image, (coin.image.get_width() * coin_scale_factor, coin.image.get_height() * coin_scale_factor))
coin.rect = coin.image.get_rect(center=coin.rect.center)

# Initial dragging state
dragging_food = False
dragging_water = False

# Main loop
run = True
clock = pygame.time.Clock()

show_status = False
status_text = ""

# Timer for status bar decrease
status_decrease_timer = pygame.time.get_ticks()
status_decrease_interval = 1000  # Decrease every second

def draw_health_bar(screen, x, y, value, label):
    BAR_WIDTH = 100
    BAR_HEIGHT = 20
    MESSAGE_BOX_WIDTH = 250
    MESSAGE_BOX_HEIGHT = 70
    MESSAGE_BOX_SPACING = 10
    MESSAGE_FONT_SIZE = 24

    # Determine color based on value
    if value <= 0:
        value = 0
        color = RED
        message = "Your pet is starving!" if label == "Hunger" else \
                  "Your pet is exhausted!" if label == "Sleepiness" else \
                  "Your pet is unhappy!" if label == "Happiness" else \
                  "Your pet is thirsty!"
        # Render message text
        message_font = pygame.font.SysFont('Arial', MESSAGE_FONT_SIZE, bold=True)  # Making the message bold
        message_text = message_font.render(message, True, BLACK)
        # Calculate message bubble position
        active_bars = [label for label, val in zip(["Hunger", "Sleepiness", "Happiness", "Thirstiness"], [pet.hunger, pet.sleepiness, pet.happiness, pet.thirstiness]) if val <= 0]
        num_active_messages = len(active_bars)
        total_height = MESSAGE_BOX_HEIGHT * num_active_messages + MESSAGE_BOX_SPACING * (num_active_messages - 1)
        message_rect = message_text.get_rect(midtop=(SCREEN_WIDTH // 2, MESSAGE_BOX_HEIGHT // 2))
        # Draw message bubble
        pygame.draw.rect(screen, WHITE, (message_rect.left - 5, message_rect.top - 5, message_rect.width + 10, message_rect.height + 10), border_radius=20)
        pygame.draw.rect(screen, color, (message_rect.left - 5, message_rect.top - 5, message_rect.width + 10, message_rect.height + 10), width=2, border_radius=20)
        # Draw message text
        screen.blit(message_text, message_rect)

    elif value < 30:
        color = RED
    elif value < 70:
        color = YELLOW
    else:
        color = GREEN

    # Draw status bar
    pygame.draw.rect(screen, GRAY, (x, y, BAR_WIDTH, BAR_HEIGHT))  # Background
    pygame.draw.rect(screen, color, (x, y, value, BAR_HEIGHT))  # Value bar

    # Draw status label
    label_text = my_font.render(label, True, BLACK)
    screen.blit(label_text, (x + BAR_WIDTH + 5, y))


# Timer for coin movement
coin_movement_timer = pygame.time.get_ticks()
coin_movement_interval = 3000  # 3 seconds

while run:
    current_time = pygame.time.get_ticks()

    # Check if it's time to move the coin
    if current_time - coin_movement_timer >= coin_movement_interval:
        coin.randomize_position()
        coin_movement_timer = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Check if the mouse click overlaps with the coin's rect
                if coin.rect.collidepoint(event.pos):
                    pet.coins += 5  # Add 5 coins to the pet's total
                    coin.randomize_position()  # Move the coin to a new location
                elif food_rect.collidepoint(event.pos):
                    dragging_food = True
                elif water_rect.collidepoint(event.pos):
                    dragging_water = True
                elif play_button.collidepoint(event.pos) and intro_screen:
                    intro_screen = False  # Transition to the main game screen
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                if dragging_food:
                    dragging_food = False
                    if pet.rect.colliderect(food_rect):
                        pet.feed()
                    food_rect.topleft = initial_food_position  # Reset food position
                if dragging_water:
                    dragging_water = False
                    if pet.rect.colliderect(water_rect):
                        pet.quench_thirst()
                    water_rect.topleft = initial_water_position  # Reset water position

        elif event.type == pygame.MOUSEMOTION:
            if dragging_food:
                food_rect.move_ip(event.rel)
            if dragging_water:
                water_rect.move_ip(event.rel)

    current_time = pygame.time.get_ticks()
    if current_time - status_decrease_timer >= status_decrease_interval:
        pet.hunger = max(pet.hunger - 1, 0)
        pet.sleepiness = max(pet.sleepiness - 1, 0)
        pet.happiness = max(pet.happiness - 1, 0)
        pet.thirstiness = max(pet.thirstiness - 1, 0)
        status_decrease_timer = current_time

    screen.fill(WHITE)  # Fill the screen with white color

    if intro_screen:
        # Display introduction screen
        screen.blit(bg, (0, 0))  # Draw the background

        # Draw title "PET SIMULATOR"
        title_text = title_font.render("PET SIMULATOR", True, BLACK)
        title_text_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        screen.blit(title_text, title_text_rect)

        # Draw instructions
        instructions_font = pygame.font.SysFont('Arial', 35, bold=True)  # Increased font size and made it bold
        for i, instruction in enumerate(instructions):
            instruction_text = instructions_font.render(instruction, True, BLACK)
            instruction_text_rect = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, 150 + i * 40))
            screen.blit(instruction_text, instruction_text_rect)

        # Draw the bigger play button with larger font
        pygame.draw.rect(screen, BLACK, play_button, 3, border_radius=20)  # Draw play button border
        play_text = my_font.render("PLAY", True, BLACK)
        play_text_rect = play_text.get_rect(center=play_button.center)
        screen.blit(play_text, play_text_rect)  # Draw play button text
    else:
        # Display main game screen
        screen.blit(bg, (0, 0))  # Draw the background
        # Draw the pet
        screen.blit(pet.image, pet.rect)

        # Draw the food and water
        screen.blit(food_image, food_rect)
        screen.blit(water_image, water_rect)
        screen.blit(coin.image, coin.rect)

        # Draw buttons
        for name, rect in buttons.items():
            pygame.draw.rect(screen, WHITE, rect, border_radius=10)
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

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

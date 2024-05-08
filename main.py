import pygame
import time

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
green = (0, 255, 0)
red = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Virtual Pet")


# Main program
def main():
    pet_name = input("Enter your pet's name: ")
    pet = Pet(pet_name)

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Feed button
                if 50 <= mouse_pos[0] <= 150 and 50 <= mouse_pos[1] <= 100:
                    pet.feed()

                # Play button
                if 50 <= mouse_pos[0] <= 150 and 120 <= mouse_pos[1] <= 170:
                    pet.play()

                # Sleep button
                if 50 <= mouse_pos[0] <= 150 and 190 <= mouse_pos[1] <= 240:
                    pet.sleep()

                # Earn coins button
                if 200 <= mouse_pos[0] <= 300 and 120 <= mouse_pos[1] <= 170:
                    pet.earn_coins()

                # Check status button
                if 200 <= mouse_pos[0] <= 300 and 190 <= mouse_pos[1] <= 240:
                    pet.check_status()

        # Draw buttons
        pygame.draw.rect(screen, gray, (50, 50, 100, 50))  # Feed button
        pygame.draw.rect(screen, gray, (50, 120, 100, 50))  # Play button
        pygame.draw.rect(screen, gray, (50, 190, 100, 50))  # Sleep button
        pygame.draw.rect(screen, gray, (200, 120, 100, 50))  # Earn coins button
        pygame.draw.rect(screen, gray, (200, 190, 100, 50))  # Check status button

        # Display text on buttons
        font = pygame.font.Font(None, 36)
        text_feed = font.render("Feed", True, black)
        text_play = font.render("Play", True, black)
        text_sleep = font.render("Sleep", True, black)
        text_earn = font.render("Earn Coins", True, black)
        text_status = font.render("Check Status", True, black)
        screen.blit(text_feed, (65, 65))
        screen.blit(text_play, (65, 135))
        screen.blit(text_sleep, (65, 205))
        screen.blit(text_earn, (210, 135))
        screen.blit(text_status, (210, 205))

        # Update the screen
        pygame.display.flip()

        # Decrease bars every iteration
        pet.hunger += 5
        pet.sleepiness += 5

        # Check if pet is hungry or sleepy
        if pet.hunger >= 100:
            print(pet.name + " is hungry! Feed it.")
        if pet.sleepiness >= 100:
            print(pet.name + " is sleepy! Let it sleep.")


    pygame.quit()





import pygame
import time
import pet


# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Virtual Pet")

# Load the cat image
cat_image = pygame.image.load("cat.jpg")  # Assuming "cat.png" is the image file name

# Scale the cat image
cat_image = pygame.transform.scale(cat_image, (100, 100))  # Adjust size as needed


# Pet class
class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.hunger = 50
        self.sleepiness = 50
        self.coins = 0

    def feed(self):
        if self.coins >= 5:
            self.hunger -= 10
            self.coins -= 5
        else:
            print("Not enough coins to buy food.")

    def play(self):
        if self.happiness < 90:
            self.happiness += 10
        else:
            print(self.name + " is already very happy.")

    def sleep(self):
        if self.sleepiness < 90:
            self.sleepiness += 10
        else:
            print(self.name + " is already well-rested.")

    def check_status(self):
        print("Name:", self.name)
        print("Happiness:", self.happiness)
        print("Hunger:", self.hunger)
        print("Sleepiness:", self.sleepiness)
        print("Coins:", self.coins)

    def earn_coins(self):
        self.coins += 10


# Main program
def main():
    pet_name = input("Enter your pet's name: ")
    pet = Pet(pet_name)

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)

        # Blit the cat image onto the screen
        screen.blit(cat_image, (150, 50))

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
        pygame.draw.rect(screen, GRAY, (50, 50, 100, 50))  # Feed button
        pygame.draw.rect(screen, GRAY, (50, 120, 100, 50))  # Play button
        pygame.draw.rect(screen, GRAY, (50, 190, 100, 50))  # Sleep button
        pygame.draw.rect(screen, GRAY, (200, 120, 100, 50))  # Earn coins button
        pygame.draw.rect(screen, GRAY, (200, 190, 100, 50))  # Check status button

        # Display text on buttons
        font = pygame.font.Font(None, 36)
        text_feed = font.render("Feed", True, BLACK)
        text_play = font.render("Play", True, BLACK)
        text_sleep = font.render("Sleep", True, BLACK)
        text_earn = font.render("Earn Coins", True, BLACK)
        text_status = font.render("Check Status", True, BLACK)
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

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

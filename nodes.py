class GRTrajectory:     


    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {       
                    "text": ("STRING", {"multiline": False, "default": "Hello World"}),
                    }
                }

    RETURN_TYPES = ()
    FUNCTION = "print_text"
    OUTPUT_NODE = True
    CATEGORY = "Tutorial Nodes"

    def print_text(self, text):

        print(f"Tutorial Text : {text}")
        
        return {}
        
        
import pygame
import json

# Initialize Pygame
pygame.init()

# Set up display
width, height = 576, 320
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing App")

# Set up drawing variables
drawing = False
userDrawnPixels = []
lines = []

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            userDrawnPixels = []
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                x, y = event.pos
                userDrawnPixels.append([x, y])
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            lines.append(userDrawnPixels)

    # Draw on the screen
    screen.fill((255, 255, 255))
    for line in lines:
        pygame.draw.lines(screen, (169, 169, 169), False, line, 6)

    pygame.display.flip()

# Save the trajectory to a JSON file
with open("trajectory.json", "w") as file:
    json.dump(lines, file)

pygame.quit()

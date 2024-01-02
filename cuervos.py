import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display in fullscreen mode
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("El juego de Nina")

# Load images
bird_image = pygame.image.load("bird.png")
bird2_image = pygame.image.load("bird2.png")

# Load background image
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (width, height))

# Mapping of notes to keyboard keys
note_mapping = {"a": "C", "s": "D", "d": "E", "f": "F", "g": "G", "h": "A", "j": "B"}

# Load sounds for each note
note_sounds = {
    "C": "C.mid",
    "D": "D.mid",
    "E": "E.mid",
    "F": "F.mid",
    "G": "G.mid",
    "A": "A.mid",
    "B": "B.mid",
}


# Function to play sound for a given note
def play_note_sound(note):
    pygame.mixer.music.load(note_sounds[note])
    pygame.mixer.music.play()


# Function to draw a note on the staff
def draw_note(note, x, y):
    image = bird2_image if note in ["C", "E", "G", "B"] else bird_image
    screen.blit(image, (x, y))


# Example melodies
melody1 = ["C", "C", "G", "G", "A", "A", "G"]
melody2 = ["F", "F", "E", "E", "D", "D", "C"]

# Combine melodies into a single list
melody = melody1 + melody2

# Define y-axis positions for each note (manually adjusted)
note_positions = {
    "C": 10,
    "D": 0,
    "E": -10,
    "F": -20,
    "G": -30,
    "A": -40,
    "B": -50,
}

# Index to keep track of the current note in the melodies
current_note_index_melody1 = 0
current_note_index_melody2 = 0

# Horizontal offset for notes
horizontal_offset = 50

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Check if the pressed key corresponds to the current note
            key = pygame.key.name(event.key)
            if key == "q":
                running = False
            elif (
                current_note_index_melody1 < len(melody1)
                and key in note_mapping
                and note_mapping[key] == melody[current_note_index_melody1]
            ):
                # Play the sound for the current note in melody1
                play_note_sound(melody[current_note_index_melody1])
                current_note_index_melody1 += 1
            elif (
                len(melody1) <= current_note_index_melody1 < len(melody)
                and key in note_mapping
                and note_mapping[key] == melody[current_note_index_melody1]
            ):
                # Play the sound for the current note in melody2
                play_note_sound(melody[current_note_index_melody1])
                current_note_index_melody1 += 1

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Draw the remaining notes with an offset for both melodies
    for i, note in enumerate(melody):
        if i < current_note_index_melody1:
            continue
        x_position = i * 100 + horizontal_offset
        y_position = height // 2 - bird_image.get_height() // 2 + note_positions[note]

        # Check if it's melody2 and adjust the x_position
        if i >= len(melody1):
            x_position += 100  # Add a space of 100 pixels between melody 1 and melody 2

        draw_note(note, x_position, y_position)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

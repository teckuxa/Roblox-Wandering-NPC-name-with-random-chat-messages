import pydirectinput
import random
import time
import keyboard

# ==========================
# SETTINGS (adjust these!)
MOVE_DURATION_MIN = 1           # Minimum seconds to hold movement key
MOVE_DURATION_MAX = 3           # Maximum seconds to hold movement key
WAIT_MIN = 1                    # Minimum wait time between actions
WAIT_MAX = 3                    # Maximum wait time between actions
JUMP_WHILE_MOVE_CHANCE = 0.3    # Chance to jump once while moving
JUMP_IN_PLACE_CHANCE = 0.1      # Chance to jump in place instead of moving
CHAT_CHANCE = 0.3              # Chance to send chat message
# ==========================

# Movement keys and chat phrases (all lowercase for safety)
keys = ['w', 'a', 's', 'd']
phrases = [
    "hello!",
    "hi!",
    "get off mah lawn",
    "how’s everyone?",
    "what’s up?",
    "i like tacos.",
    "random phrase here!"
]

print("Starting in 2 seconds...")
time.sleep(2)
print("Press 'F' to stop the script.")

# Helper function to type phrase character by character
def type_phrase(phrase):
    for char in phrase:
        pydirectinput.press(char)
        time.sleep(0.05)  # small delay between characters

while True:
    if keyboard.is_pressed('f'):
        print("Script stopped by user.")
        break

    # Chance to open chat and type a phrase
    if random.random() < CHAT_CHANCE:
        pydirectinput.press('/')          # Open chat
        time.sleep(0.3)                   # Wait for chat to open
        phrase = random.choice(phrases)
        type_phrase(phrase)
        pydirectinput.press('enter')
        time.sleep(random.uniform(1, 2))
        continue  # Skip movement this loop

    # Decide whether to jump in place or move
    if random.random() < JUMP_IN_PLACE_CHANCE:
        # Jump in place
        jumps = random.randint(1, 3)
        for _ in range(jumps):
            pydirectinput.press('space')
            time.sleep(random.uniform(0.2, 0.5))
    else:
        # Move
        key = random.choice(keys)
        duration = random.uniform(MOVE_DURATION_MIN, MOVE_DURATION_MAX)
        pydirectinput.keyDown(key)

        # Chance to jump once while moving
        if random.random() < JUMP_WHILE_MOVE_CHANCE:
            time.sleep(random.uniform(0.2, duration / 2))
            pydirectinput.press('space')

        time.sleep(duration)
        pydirectinput.keyUp(key)

    # Wait before next action
    wait_time = random.uniform(WAIT_MIN, WAIT_MAX)
    time.sleep(wait_time)

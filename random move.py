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
CHAT_CHANCE = 0.1              # Chance to send chat message
# ==========================

# Movement keys and chat phrases
keys = ['w', 'a', 's', 'd']
phrases = [
    "Hello!",
    "Hi!",
    "GET OFF MAH LAWN",
    "How’s everyone?",
    "What’s up?",
    "I like tacos.",
    "Random phrase here!"
]

print("Starting in 2 seconds...")
time.sleep(2)
print("Press 'F' to stop the script.")

while True:
    if keyboard.is_pressed('f'):
        print("Script stopped by user.")
        break

    # Chance to open chat
    if random.random() < CHAT_CHANCE:
        pydirectinput.press('/')          # Open chat
        time.sleep(0.3)                   # Wait for chat to open
        # Handle first letter capitalization
        phrase = random.choice(phrases)
        first_char = phrase[0]
        if first_char.isupper():
            pydirectinput.keyDown('shift')
            pydirectinput.press(first_char.lower())
            pydirectinput.keyUp('shift')
        else:
            pydirectinput.press(first_char)
        time.sleep(0.05)
        pydirectinput.typewrite(phrase[1:])
        pydirectinput.press('enter')
        time.sleep(random.uniform(1, 2))
        continue

    # Decide whether to move or jump in place
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

    # Wait 1-3 seconds before next action
    wait_time = random.uniform(WAIT_MIN, WAIT_MAX)
    time.sleep(wait_time)

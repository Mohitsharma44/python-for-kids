"""
🎮 GOLD COLLECTOR GAME 🎮
========================

This is a simple game where you control a player (blue rectangle or alien sprite)
and try to collect gold coins. Each time you touch a coin, your score increases
and the coin moves to a new location.

WHAT YOU'LL LEARN:
- How games work (drawing, updating, input handling)
- Variables and how to change them
- Functions and why we use them
- Collision detection (when things touch)
- Random numbers and how to use them

HOW TO PLAY:
- Use arrow keys to move the player
- Touch the gold coin to collect it
- Try to get the highest score!

CREATED BY: Mohit Sharma (Mohitsharma44@gmail.com)
FOR: Python for Kids Course
"""

# ========================================
# IMPORT STATEMENTS
# ========================================
# These lines bring in code that other people wrote for us to use
import random  # This lets us create random numbers (like for coin placement)

import pgzrun  # This is the game engine - it handles drawing, input, etc.

# ========================================
# GAME SETTINGS - Change these to unlock features!
# ========================================
# These are like switches that turn features on and off
# Change False to True to enable each feature!

USE_SPRITES = False  # Set to True to use images instead of shapes
USE_RANDOM_MOVEMENT = False  # Set to True to make coin move randomly
USE_BACKGROUND = False  # Set to True to use background image

# ========================================
# GAME VARIABLES
# ========================================
# These are like containers that hold information our game needs

# Game window size (how big the game window will be)
WIDTH, HEIGHT = 800, 600  # 800 pixels wide, 600 pixels tall

# Game objects - these are the things that appear in our game
if USE_SPRITES:
    # Try to use images (sprites) for the player and coin
    try:
        # Actor() creates a game object that can use images
        # The first part ('alien') is the image name, then (100, 300) is the start position
        player = Actor("alien", (100, 300))  # Player starts at (100, 300)
        coin = Actor("coin", (500, 300))  # Coin starts at position (500, 300)
        print("✅ Using sprites (images)!")
    except Exception:
        # If images aren't found, we'll use shapes instead
        print("⚠️  Images not found, using shapes instead")
        USE_SPRITES = False

if not USE_SPRITES:
    # Fallback to simple shapes (rectangles and circles)
    # Rect() creates a rectangle: (position), (size)
    player = Rect((380, 280), (44, 44))  # Player: position (380,280), size 44x44 pixels
    coin = Rect((520, 320), (24, 24))  # Coin: position (520,320), size 24x24 pixels

# Keep track of how many coins the player has collected
score = 0  # Start with 0 points

# ========================================
# GAME FUNCTIONS
# ========================================
# Functions are like recipes - they contain instructions for doing specific tasks


def draw():
    """
    This function runs every frame (about 60 times per second!) to draw everything on screen.
    Think of it like a painter who repaints the entire picture over and over.
    """
    # Clear the screen (erase everything from the last frame)
    screen.clear()

    # Draw the background (the "floor" of our game)
    if USE_BACKGROUND and USE_SPRITES:
        try:
            # Try to use a background image
            screen.blit("bg", (0, 0))  # blit means "draw an image"
        except Exception:
            # If no background image, use a solid color
            screen.fill((20, 24, 34))  # Dark blue background
    else:
        # Use a solid color background
        screen.fill((20, 24, 34))  # Dark blue background (Red=20, Green=24, Blue=34)

    # Draw the game objects (player and coin)
    if USE_SPRITES:
        # If using images, just tell them to draw themselves
        player.draw()  # Draw the player image
        coin.draw()  # Draw the coin image
    else:
        # If using shapes, we need to draw them manually
        # Draw a filled rectangle for the player
        # (90, 150, 255) = Blue color (Red=90, Green=150, Blue=255)
        screen.draw.filled_rect(player, (90, 150, 255))

        # Draw a filled circle for the coin
        # coin.center = the middle point of the coin rectangle
        # 12 = radius (how big the circle is)
        # (250, 210, 80) = Gold color (Red=250, Green=210, Blue=80)
        screen.draw.filled_circle(coin.center, 12, (250, 210, 80))

    # Show the score on screen
    # (10, 10) = position in top-left corner
    # color="white" = white text
    screen.draw.text(f"Score: {score}", (10, 10), color="white")

    # Show which mode we're in (sprites or shapes)
    mode_text = f"Mode: {'Sprites' if USE_SPRITES else 'Shapes'}"
    screen.draw.text(mode_text, (10, 30), color="yellow")


def update():
    """
    This function runs every frame to update the game logic.
    This is where we handle player input, check for collisions, and update game state.
    Think of it as the "brain" of the game.
    """
    # We need to tell Python we want to change the score variable
    global score

    # How fast the player moves (in pixels per frame)
    speed = 5

    # Handle keyboard input for movement
    # keyboard.left means "is the left arrow key being pressed?"
    # If it is, move the player left by subtracting speed from x position
    if keyboard.left:
        player.x = player.x - speed
    if keyboard.right:
        player.x = player.x + speed
    if keyboard.up:
        player.y = player.y - speed
    if keyboard.down:
        player.y = player.y + speed

    # Keep player inside the game window (so they can't go off-screen)
    if USE_SPRITES:
        # For sprites, we use the full window size
        player.x = max(
            0, min(player.x, WIDTH)
        )  # max(0, ...) prevents going off left edge
        player.y = max(
            0, min(player.y, HEIGHT)
        )  # min(..., HEIGHT) prevents going off bottom edge
    else:
        # For rectangles, we need to account for their size
        player.x = max(0, min(player.x, WIDTH - player.w))  # player.w = width of player
        player.y = max(
            0, min(player.y, HEIGHT - player.h)
        )  # player.h = height of player

    # Check if player touched the coin (collision detection)
    # colliderect() returns True if two rectangles overlap
    if player.colliderect(coin):
        score += 1  # Increase score by 1
        move_coin_to_new_position()  # Move coin to a new spot


def move_coin_to_new_position():
    """
    This function moves the coin to a new position when it's collected.
    It's like a helper function - it does one specific job.
    """
    if USE_RANDOM_MOVEMENT:
        # Advanced: Move coin randomly anywhere on screen
        if USE_SPRITES:
            # For sprites, keep them away from the edges
            coin.x = random.randint(40, WIDTH - 40)  # Random X position
            coin.y = random.randint(40, HEIGHT - 40)  # Random Y position
        else:
            # For rectangles, account for their size
            coin.x = random.randint(0, WIDTH - coin.w)  # Random X position
            coin.y = random.randint(0, HEIGHT - coin.h)  # Random Y position
        print("🎯 Coin moved to random position!")
    else:
        # Basic: Move coin only on X-axis (horizontal movement)
        # This formula moves the coin 160 pixels to the right, then wraps around
        # % (modulo) operator gives us the remainder after division
        # This makes the coin "wrap around" to the left side when it goes off the right edge
        coin.x = (coin.x + 160) % (WIDTH - coin.w)
        print("➡️  Coin moved horizontally!")


# ========================================
# INSTRUCTIONS FOR KIDS:
# ========================================
#
# 🎮 STEP 1: Run the game as-is to see how it works
#    - Use arrow keys to move the blue rectangle
#    - Touch the gold circle to collect it
#    - Watch your score increase!
#
# 🎨 STEP 2: Try using images instead of shapes
#    - Find the line: USE_SPRITES = False
#    - Change it to: USE_SPRITES = True
#    - Run the game again. What changed?
#
# 🎲 STEP 3: Make the coin move randomly
#    - Find the line: USE_RANDOM_MOVEMENT = False
#    - Change it to: USE_RANDOM_MOVEMENT = True
#    - Now the coin will appear anywhere when you collect it!
#
# 🔧 STEP 4: Experiment and customize!
#    - Change the speed (try 2, 10, or 20)
#    - Change the colors (RGB values from 0-255)
#    - Change the window size (WIDTH and HEIGHT)
#    - Add your own features!
#
# 💡 TIPS:
#    - Save your work before making changes
#    - If something breaks, you can always change the settings back to False
#    - Try changing one thing at a time
#    - Don't be afraid to experiment!
#
# ========================================

# Start the game! This line tells Pygame Zero to begin running our game
pgzrun.go()

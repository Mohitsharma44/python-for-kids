"""
🚀 STAR DODGER 🚀
==================

A space dodging game! You pilot a spaceship through an asteroid field.
Dodge the falling asteroids to survive. You have 3 lives — lose them all
and it's game over! Press SPACE to try again.

WHAT YOU'LL LEARN:
- Lists — storing many objects in one container (like a backpack!)
- For loops — doing the same thing to every item in a list
- append() — adding new items to a list
- Removing items from a list safely
- Timed events with clock.schedule_interval()
- Functions that return values

HOW TO PLAY:
- Use LEFT and RIGHT arrow keys to move your spaceship
- Use UP and DOWN to move within the lower half of the screen
- Dodge the falling asteroids!
- Collect bonus stars for extra points (if enabled)
- You have 3 lives — try to survive as long as you can!

CREATED BY: Mohit Sharma (Mohitsharma44@gmail.com)
FOR: Python for Kids Course - Week 02
"""

# ========================================
# IMPORT STATEMENTS
# ========================================
# These lines bring in code that other people wrote for us to use
import random  # For creating random numbers (asteroid positions, starfield)

import pgzrun  # The game engine that handles drawing, input, etc.

# ========================================
# GAME SETTINGS - Change these to unlock features!
# ========================================
# These are like switches that turn features on and off.
# Change False to True to enable each feature!

USE_SPRITES = True  # Set to True to use images instead of shapes
USE_BONUS_STARS = False  # Set to True to enable collectible bonus stars (+5 pts each!)
USE_INCREASING_DIFFICULTY = False  # True = asteroids get faster as score goes up
USE_INVINCIBILITY = False  # Set to True to get a brief shield after being hit

ASTEROID_SPEED = 3  # How fast asteroids fall (try 1, 5, or 8!)

# ========================================
# GAME VARIABLES
# ========================================
# These are like containers that hold information our game needs

# Game window size (how big the game window will be)
WIDTH, HEIGHT = 800, 600  # 800 pixels wide, 600 pixels tall

# --- Player Setup ---
# Same pattern as Week 01: try to use images, fall back to shapes if not found
if USE_SPRITES:
    try:
        player = Actor("spaceship", (WIDTH // 2, HEIGHT - 60))
        print("✅ Using spaceship sprite!")
    except Exception:
        print("⚠️  Spaceship image not found, using shapes instead")
        USE_SPRITES = False

if not USE_SPRITES:
    # Create a rectangle for the spaceship: position (center-bottom), size 40x50
    player = Rect((WIDTH // 2 - 20, HEIGHT - 70), (40, 50))

# --- Asteroid List ---
# 🆕 NEW CONCEPT: LISTS!
# In Week 01, you might have made coin1, coin2, coin3...
# But what if you need 50 coins? You'd need 50 variables! 😱
# A LIST lets you store as many items as you want in ONE variable!
# Think of it like a backpack — you can put things in and take things out.
asteroids = []  # Empty list — asteroids will be added by spawn_asteroid()

# --- Bonus Stars List ---
# Same idea! A separate list for collectible bonus stars.
bonus_stars = []  # Empty list — stars will be added by spawn_bonus_star()

# --- Starfield Background ---
# Let's use a list + for loop to create a starry night sky!
# This is a gentle first look at how lists and for loops work together.
# No gameplay pressure here — just pretty background stars ✨
background_stars = []  # Start with an empty list

# 🆕 NEW CONCEPT: FOR LOOPS!
# This loop runs 80 times. Each time, it creates a star and adds it to the list.
# Without a loop, we'd need to write 80 lines of code! 😵
for i in range(80):  # i goes from 0 to 79
    star_x = random.randint(0, WIDTH)  # Random x position
    star_y = random.randint(0, HEIGHT)  # Random y position
    star_size = random.randint(1, 3)  # Random size (1, 2, or 3 pixels)
    # append() adds the star to the END of the list — like putting it in a backpack!
    background_stars.append((star_x, star_y, star_size))

print(f"✨ Created {len(background_stars)} background stars using a list + for loop!")

# --- Game State ---
score = 0  # Points earned by surviving and collecting stars
lives = 3  # How many hits you can take before game over
game_over = False  # Is the game over?
invincible = False  # Is the player currently shielded?
invincible_timer = 0  # Counts frames of invincibility (for the flash effect)


# ========================================
# GAME FUNCTIONS
# ========================================
# Functions are like recipes — they contain instructions for specific tasks


def spawn_asteroid():
    """
    Create a new asteroid at a random position along the top of the screen
    and add it to the asteroids list.

    This is called automatically by clock.schedule_interval() every 1.5 seconds.
    """
    if game_over:
        return  # Don't spawn asteroids if the game is over

    # Pick a random x position along the top
    x = random.randint(30, WIDTH - 30)

    if USE_SPRITES:
        try:
            asteroid = Actor("asteroid", (x, -20))  # Start above the screen
        except Exception:
            # If image not found, use a shape instead
            asteroid = Rect((x - 15, -20), (30, 30))
    else:
        asteroid = Rect((x - 15, -20), (30, 30))  # 30x30 pixel rectangle

    # 🆕 append() adds the asteroid to the END of our list
    # It's like putting a new item in your backpack!
    asteroids.append(asteroid)
    print(f"📦 asteroids.append(asteroid) → list now has {len(asteroids)} item(s)")


def spawn_bonus_star():
    """
    Create a bonus star at a random position along the top.
    Stars are worth +5 points when collected!
    Only works if USE_BONUS_STARS is True.
    """
    if game_over or not USE_BONUS_STARS:
        return

    x = random.randint(30, WIDTH - 30)

    if USE_SPRITES:
        try:
            star = Actor("star", (x, -20))
        except Exception:
            star = Rect((x - 10, -20), (20, 20))
    else:
        star = Rect((x - 10, -20), (20, 20))

    bonus_stars.append(star)
    print(f"📦 bonus_stars.append(star) → list now has {len(bonus_stars)} item(s)")


def get_asteroid_speed():
    """
    Returns how fast asteroids should fall.

    🆕 NEW CONCEPT: FUNCTIONS THAT RETURN VALUES!
    This function gives back a number using the 'return' keyword.
    Other code can use that number, like: speed = get_asteroid_speed()

    If USE_INCREASING_DIFFICULTY is True, asteroids get faster as score goes up!
    """
    if USE_INCREASING_DIFFICULTY:
        # Every 10 points, asteroids get 0.5 pixels/frame faster
        # But never faster than 10 (that would be impossibly fast!)
        extra_speed = (score // 10) * 0.5
        speed = ASTEROID_SPEED + extra_speed
        return min(speed, 10)  # min() keeps it from going above 10
    else:
        return ASTEROID_SPEED  # Just use the fixed speed from settings


def reset_game():
    """
    Reset everything so the player can try again.
    Called when SPACE is pressed on the game over screen.
    """
    # We need 'global' to change these variables from inside a function
    # (We'll learn a cleaner way to do this with classes in a future week!)
    global score, lives, game_over, invincible, invincible_timer

    score = 0
    lives = 3
    game_over = False
    invincible = False
    invincible_timer = 0

    # .clear() removes ALL items from a list — like emptying your backpack!
    print(f"🧹 asteroids.clear() — removing {len(asteroids)} item(s)...")
    asteroids.clear()
    print(f"   → asteroids is now: {asteroids}")  # Prints [] (empty list!)
    print(f"🧹 bonus_stars.clear() — removing {len(bonus_stars)} item(s)...")
    bonus_stars.clear()
    print(f"   → bonus_stars is now: {bonus_stars}")

    # Reset player position to center-bottom
    if hasattr(player, "pos"):
        # Actor (sprite) — set the center position
        player.x = WIDTH // 2
        player.y = HEIGHT - 60
    else:
        # Rect (shape) — set the top-left corner
        player.x = WIDTH // 2 - 20
        player.y = HEIGHT - 70

    print("🔄 Game reset! Good luck!")


def end_invincibility():
    """
    Turn off the player's shield.
    This is called by clock.schedule_unique() after 2 seconds.

    clock.schedule_unique() sets a one-time timer. "unique" means if a timer
    already exists for this function, it REPLACES it instead of adding another.
    This prevents timer stacking if you get hit twice quickly.
    """
    global invincible
    invincible = False
    print("🛡️  Shield expired!")


def draw_player():
    """
    Helper function to draw the player spaceship.
    Used by draw() to handle the invincibility flash effect.
    """
    if hasattr(player, "draw"):
        # Sprites know how to draw themselves!
        player.draw()
    else:
        # Draw a spaceship using simple shapes
        # Main body (blue rectangle)
        screen.draw.filled_rect(player, (50, 150, 255))
        # Cockpit window (lighter blue circle near the top)
        cx = player.x + player.w // 2  # Center x of the player
        cy = player.y + 10  # Near the top
        screen.draw.filled_circle((cx, cy), 6, (150, 220, 255))
        # Engine flames (orange rectangles at the bottom)
        flame_y = player.y + player.h - 6
        screen.draw.filled_rect(Rect((player.x + 4, flame_y), (8, 6)), (255, 150, 50))
        screen.draw.filled_rect(
            Rect((player.x + player.w - 12, flame_y), (8, 6)), (255, 150, 50)
        )


def draw():
    """
    This function runs every frame (about 60 times per second!) to draw
    everything on screen. Like a painter who repaints the entire picture
    over and over, super fast.
    """
    # Clear the screen with dark space color
    screen.fill((10, 10, 30))  # Very dark blue, almost black — like space!

    # --- Draw the starfield background ---
    # 🆕 This for loop goes through EVERY star in our background_stars list.
    # Each star is a tuple: (x, y, size)
    for bg_star in background_stars:
        x, y, size = bg_star  # "Unpack" the tuple into three variables
        screen.draw.filled_circle((x, y), size, (255, 255, 255))  # White dots

    # --- Draw asteroids ---
    # 🆕 Another for loop! This one draws every asteroid in the asteroids list.
    # Whether there are 0 asteroids or 100, this SAME code handles them all!
    for asteroid in asteroids:
        if hasattr(asteroid, "draw"):
            asteroid.draw()  # Sprites draw themselves
        else:
            # Draw a gray circle for each asteroid
            screen.draw.filled_circle(asteroid.center, 15, (160, 160, 160))
            # Darker outline to make it look more like a rock
            screen.draw.circle(asteroid.center, 15, (100, 100, 100))

    # --- Draw bonus stars ---
    if USE_BONUS_STARS:
        for star in bonus_stars:
            if hasattr(star, "draw"):
                star.draw()
            else:
                # Draw a bright yellow circle for each star
                screen.draw.filled_circle(star.center, 10, (255, 255, 50))

    # --- Draw the player ---
    if invincible and invincible_timer % 6 < 3:
        # Flash effect! Every 3 frames, skip drawing the player.
        # This makes the spaceship "blink" so you know the shield is active.
        pass
    else:
        draw_player()

    # --- Draw the HUD (Heads-Up Display) ---
    # Score in top-left
    screen.draw.text(f"Score: {score}", (10, 10), color="white", fontsize=30)

    # Lives counter
    screen.draw.text(f"Lives: {lives}", (10, 40), color="red", fontsize=24)

    # Show asteroid count (watch the list grow and shrink in real time!)
    screen.draw.text(
        f"Asteroids on screen: {len(asteroids)}",
        (10, 70),
        color="gray",
        fontsize=18,
    )

    # Show current speed (useful when increasing difficulty is on)
    if USE_INCREASING_DIFFICULTY:
        speed_text = f"Speed: {get_asteroid_speed():.1f}"
        screen.draw.text(speed_text, (10, 90), color="cyan", fontsize=18)

    # Show mode in top-right
    mode_text = f"Mode: {'Sprites' if USE_SPRITES else 'Shapes'}"
    screen.draw.text(mode_text, (WIDTH - 180, 10), color="yellow", fontsize=18)

    # --- Game Over Screen ---
    if game_over:
        # Draw a dark box in the center
        box = Rect((WIDTH // 2 - 200, HEIGHT // 2 - 90), (400, 200))
        screen.draw.filled_rect(box, (0, 0, 0))
        screen.draw.rect(box, (255, 50, 50))  # Red border

        screen.draw.text(
            "GAME OVER",
            center=(WIDTH // 2, HEIGHT // 2 - 40),
            color="red",
            fontsize=60,
        )
        screen.draw.text(
            f"Final Score: {score}",
            center=(WIDTH // 2, HEIGHT // 2 + 10),
            color="white",
            fontsize=36,
        )
        screen.draw.text(
            "Press SPACE to play again!",
            center=(WIDTH // 2, HEIGHT // 2 + 50),
            color="yellow",
            fontsize=24,
        )


def update():
    """
    Update game logic every frame. This is the "brain" of the game.
    Handles movement, collisions, and all the game rules.
    """
    # We need 'global' to change these variables from inside a function.
    # That's 4 global variables — we'll learn a cleaner way (classes) in a future week!
    global score, lives, game_over, invincible, invincible_timer

    # If the game is over, don't update anything
    if game_over:
        return

    # --- Player Movement ---
    speed = 5  # How fast the player moves (pixels per frame)

    if keyboard.left:
        player.x -= speed  # Shorthand for player.x = player.x - speed
    if keyboard.right:
        player.x += speed
    if keyboard.up:
        player.y -= speed
    if keyboard.down:
        player.y += speed

    # Keep player inside the game window
    # The player can only move in the BOTTOM HALF of the screen.
    # This prevents the "hide at the top" strategy! 😄
    min_y = HEIGHT // 2  # The highest the player can go (middle of screen)

    if hasattr(player, "pos"):
        # Actor (sprite) — pos is the center point
        player.x = max(20, min(player.x, WIDTH - 20))
        player.y = max(min_y, min(player.y, HEIGHT - 25))
    else:
        # Rect (shape) — x,y is the top-left corner, so account for size
        player.x = max(0, min(player.x, WIDTH - player.w))
        player.y = max(min_y, min(player.y, HEIGHT - player.h))

    # --- Update invincibility timer ---
    if invincible:
        invincible_timer += 1

    # --- Move Asteroids ---
    # 🆕 This for loop moves EVERY asteroid in the list down the screen.
    # Whether there are 2 or 200 asteroids, this SAME code handles them all!
    current_speed = get_asteroid_speed()  # Get speed (might increase with score)

    for asteroid in asteroids:
        asteroid.y += current_speed  # Move each asteroid down

    # --- Move Bonus Stars ---
    if USE_BONUS_STARS:
        for star in bonus_stars:
            star.y += 2  # Stars fall slower than asteroids

    # --- Remove off-screen objects and check collisions ---
    # ⚠️  IMPORTANT: We can't remove items from a list WHILE we're looping through it!
    # That would be like pulling cards from a deck while someone is counting them —
    # it messes up the count!
    # Instead, we make a SEPARATE list of things to remove, then remove them AFTER.
    asteroids_to_remove = []  # Asteroids we want to take out of the list
    dodged_count = 0  # Count how many asteroids we dodged this frame

    for asteroid in asteroids:
        # Check if asteroid has fallen off the bottom of the screen
        if asteroid.y > HEIGHT + 30:
            asteroids_to_remove.append(asteroid)
            score += 1  # +1 point for each asteroid you dodge!
            dodged_count += 1
            continue  # Skip to the next asteroid (no need to check collision)

        # Check collision with player
        if player.colliderect(asteroid):
            if not invincible:
                lives -= 1
                asteroids_to_remove.append(asteroid)
                print(f"💥 Hit! Lives remaining: {lives}")

                if lives <= 0:
                    game_over = True
                    print(f"💀 Game Over! Final score: {score}")
                elif USE_INVINCIBILITY:
                    # Turn on the shield!
                    invincible = True
                    invincible_timer = 0
                    # clock.schedule_unique() sets a one-time timer.
                    # "unique" means it replaces any existing timer for this function
                    # (prevents stacking if you get hit twice quickly)
                    clock.schedule_unique(end_invincibility, 2.0)
                    print("🛡️  Shield activated for 2 seconds!")

    # NOW remove the asteroids (after we're done looping through the list)
    for asteroid in asteroids_to_remove:
        asteroids.remove(asteroid)

    # Show what happened to the list this frame
    if dodged_count > 0:
        print(
            f"✅ Dodged {dodged_count} asteroid(s)! +{dodged_count} pts (score: {score})"
        )
    if asteroids_to_remove:
        print(
            f"🗑️  asteroids.remove() × {len(asteroids_to_remove)}"
            f" → list now has {len(asteroids)} item(s)"
        )

    # --- Bonus Star Collisions ---
    if USE_BONUS_STARS:
        stars_to_remove = []  # Same "to_remove" pattern as asteroids!

        for star in bonus_stars:
            # Check if star fell off the bottom
            if star.y > HEIGHT + 20:
                stars_to_remove.append(star)
                continue

            # Check if player collected the star
            if player.colliderect(star):
                score += 5  # Bonus stars are worth 5 points!
                stars_to_remove.append(star)
                print(f"⭐ Bonus star collected! +5 points! Score: {score}")

        for star in stars_to_remove:
            bonus_stars.remove(star)

        if stars_to_remove:
            print(
                f"🗑️  bonus_stars.remove() × {len(stars_to_remove)}"
                f" → list now has {len(bonus_stars)} item(s)"
            )


def on_key_down(key):
    """
    This function is called ONCE when a key is pressed down.
    (Different from keyboard.left in update() which checks if a key IS held down.)

    pgzero automatically calls this function for us — just like draw() and update().
    """
    if key == keys.SPACE and game_over:
        reset_game()


# ========================================
# TIMERS - Automatically spawn new objects
# ========================================
# 🆕 clock.schedule_interval() calls a function over and over at a set time interval.
# This spawns a new asteroid every 1.5 seconds — try changing 1.5 to see what happens!
clock.schedule_interval(spawn_asteroid, 1.5)

# Spawn bonus stars less frequently (every 4 seconds)
if USE_BONUS_STARS:
    clock.schedule_interval(spawn_bonus_star, 4.0)

print("🚀 Star Dodger loaded! Use arrow keys to dodge asteroids!")
print(f"📋 Settings: Sprites={USE_SPRITES}, Bonus Stars={USE_BONUS_STARS}")
print(f"📋 Difficulty={USE_INCREASING_DIFFICULTY}, Invincibility={USE_INVINCIBILITY}")
print(f"📋 Asteroid Speed={ASTEROID_SPEED}")

# ========================================
# INSTRUCTIONS FOR KIDS:
# ========================================
#
# 🚀 STEP 1: Run the game and try to survive!
#    - Use arrow keys to dodge the falling asteroids
#    - Watch your lives in the top-left corner
#    - When you lose all 3 lives, press SPACE to restart
#
# ⚡ STEP 2: Tweak the settings
#    - Change ASTEROID_SPEED to 1 (easy) or 6 (hard)
#    - Change lives = 3 to lives = 5 for more chances
#    - Set USE_SPRITES = True to use images
#
# 📦 STEP 3: Understand LISTS (the big new concept!)
#    - Find: asteroids = []  — this creates an empty list
#    - Find: asteroids.append(asteroid) — this adds to the list
#    - Find: for asteroid in asteroids: — this loops through the list
#    - Watch the console — it shows how many asteroids are on screen!
#
# 🌟 STEP 4: Enable bonus features
#    - Set USE_BONUS_STARS = True for collectible stars
#    - Set USE_INCREASING_DIFFICULTY = True for a real challenge
#    - Set USE_INVINCIBILITY = True for a shield after getting hit
#    - Try enabling ALL features at once!
#
# 💡 TIPS:
#    - Save your work before making changes
#    - If something breaks, change settings back to False
#    - Try changing one thing at a time
#    - Don't be afraid to experiment - that's how you learn!
#
# ========================================

# Start the game! This line tells Pygame Zero to begin running our game
pgzrun.go()

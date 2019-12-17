# Import the "arcade" library
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """Draw the ground"""
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)


def draw_sun(x, y):
    """Draw the sun"""
    arcade.draw_circle_filled(400 + x, 500 + y, 90, arcade.color.YELLOW)


def draw_triangle(x, y):
    """Draw triangle"""
    # Draw a point at x, y for reference
    arcade.draw_triangle_filled(310 + x, 200 + y, 490 + x, 200 + y, 400 + x, 300 + y, arcade.color.BRONZE_YELLOW)


def on_draw(delta_time):
    """Draw Everything"""
    arcade.start_render()

    draw_sun(0, on_draw.circle1_y)
    draw_grass()
    draw_triangle(on_draw.triangle1_x, 0)
    draw_triangle(on_draw.triangle2_x, 50)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.triangle1_x -= 1
    on_draw.triangle2_x += 1
    on_draw.circle1_y -= 1


# Create a value that our on_draw.snow_person1_x will start at.
on_draw.triangle1_x = 0
on_draw.triangle2_x = 0
on_draw.circle1_y = 0


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
    arcade.set_background_color(arcade.color.AZURE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()

# Call the main function to get the program started.
main()

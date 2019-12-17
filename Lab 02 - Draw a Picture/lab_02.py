# Import the "arcade" library
import arcade
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_grass():
    """Draw the ground"""
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
    arcade.set_background_color(arcade.color.AZURE)
    arcade.start_render()

def draw_grass()

    # Draw Sun
    arcade.draw_circle_filled(400, 500, 90, arcade.color.YELLOW)

    # Draw triangle
    arcade.draw_triangle_filled(310, 200, 490, 200, 400, 300, arcade.color.BRONZE_YELLOW)

    # --- Finish drawing ---
    arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
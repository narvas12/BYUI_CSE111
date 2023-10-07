# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import (
    start_drawing, draw_oval, draw_rectangle, draw_polygon, draw_text, finish_drawing
)

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Outdoor Scene", scene_width, scene_height)

    # Call your drawing functions here.
    draw_sky(canvas)
    draw_ground(canvas)
    draw_pine_tree(canvas, 100, 300)
    draw_pine_tree(canvas, 300, 300)
    draw_grass(canvas)
    draw_house(canvas, 500, 200)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your drawing functions.

def draw_sky(canvas):
    # Draw a blue sky
    draw_rectangle(canvas, 0, 0, 800, 250, fill="sky blue")

def draw_ground(canvas):
    # Draw the ground
    draw_rectangle(canvas, 0, 250, 800, 500, fill="brown")

def draw_pine_tree(canvas, x, y):
    # Draw a pine tree
    draw_polygon(canvas, x, y, x - 20, y - 100, x + 20, y - 100, fill="dark green")
    draw_rectangle(canvas, x - 5, y - 100, x + 5, y - 70, fill="tan4")

def draw_grass(canvas):
    # Draw grass
    for x in range(0, 800, 20):
        draw_polygon(canvas, x, 250, x + 10, 270, x + 20, 250, fill="green")

def draw_house(canvas, x, y):
    # Draw a simple house
    draw_rectangle(canvas, x, y, x + 100, y + 100, fill="brown")
    draw_polygon(canvas, x, y, x + 100, y, x + 50, y - 50, fill="black")

# Call the main function to start the program.
main()

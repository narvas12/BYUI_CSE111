# This program exceeds the requirements for the "Intermediate" grading category by
# incorporating a variety of repetitive objects in the scene. All objects are drawn with functions defined once, but
# when repeated, are called with different arguments to alter the size and/or locations.
# Outdoor Scene Drawing Program
# This program creates a semi-realistic outdoor scene using the Draw 2-D library.
# It includes the sky, ground, trees, birds, flowers, insects, clouds, a house,
# and pickets in a fence. 



# Import the functions from the Draw 2-D library
from draw2d import finish_drawing, start_drawing, draw_rectangle, draw_oval

def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Outdoor Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Call the functions to draw trees, birds, flowers, insects, and clouds.
    draw_trees(canvas)
    draw_birds(canvas)
    draw_insects(canvas)
    draw_clouds(canvas) 
    draw_catapilers(canvas)
    draw_sun_shine(canvas)
     # Draw clouds
    draw_house(canvas, 400, canvas.winfo_height() // 2 + 210)
    draw_flowers(canvas)

    # Call the finish_drawing function
    # in the draw2d.py library.

    # Draw pickets in a fence
    draw_fence(canvas, 200, canvas.winfo_height() // 2 - 180)
    draw_fence(canvas, 300, canvas.winfo_height() // 2 - 180)
    draw_fence(canvas, 500, canvas.winfo_height() // 2 - 180)
    draw_fence(canvas, 600, canvas.winfo_height() // 2 - 180)
    finish_drawing(canvas)


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky."""
    draw_rectangle(canvas, 0, 0, scene_width, scene_height, width=0, fill="tan4")


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground."""
    draw_rectangle(canvas, 0, scene_height // 2 - 210, scene_width, scene_height, width=0, fill="sky blue")


def draw_trees(canvas):
    # Draw a few pine trees
    draw_pine_tree(canvas, 150, canvas.winfo_height() // 2 + 210)
    draw_pine_tree(canvas, 350, canvas.winfo_height() // 2 + 210)
    draw_pine_tree(canvas, 600, canvas.winfo_height() // 2 + 210)
    # Add more trees as needed

# Function to draw a single pine tree
def draw_pine_tree(canvas, x, y):
    # Draw the tree trunk
    canvas.create_rectangle(x - 10, y, x + 10, y - 60, fill="brown", outline="black")

    # Draw the larger pine tree leaves (crown)
    canvas.create_polygon(
        x, y - 200,
        x + 50, y - 50,
        x - 50, y - 50,
        outline="black", fill="dark green"
    )



# Implement bird drawing logic 
def draw_birds(canvas):
    # Draw a few birds
    draw_bird(canvas, 200, 100)
    draw_bird(canvas, 400, 150)
    draw_bird(canvas, 600, 80)
    # Add more birds as needed

# Function to draw a single bird
def draw_bird(canvas, x, y):
    # Draw a bird as a simple triangle
    canvas.create_polygon(x, y, x - 10, y - 5, x + 10, y + 5, fill="black")

# Implement flower drawing logic here
def draw_flowers(canvas):
    # Draw a few flowers
    draw_flower(canvas, 200, canvas.winfo_height() // 2 + 210)
    draw_flower(canvas, 250, canvas.winfo_height() // 2 + 210)
    draw_flower(canvas, 300, canvas.winfo_height() // 2 + 210)
    draw_flower(canvas, 350, canvas.winfo_height() // 2 + 210)
    draw_flower(canvas, 400, canvas.winfo_height() // 2 + 210)
    draw_flower(canvas, 500, canvas.winfo_height() // 2 + 210)
    draw_flower(canvas, 550, canvas.winfo_height() // 2 + 210)
    draw_flower(canvas, 600, canvas.winfo_height() // 2 + 210)
    draw_flower(canvas, 650, canvas.winfo_height() // 2 + 210)
    draw_flower(canvas, 700, canvas.winfo_height() // 2 + 210)
    # Add more flowers as needed

# Function to draw a single flower
def draw_flower(canvas, x, y):
    # Draw the flower stem
    canvas.create_line(x, y, x, y - 40, fill="green", width=2)

    # Draw the flower petals
    canvas.create_oval(x - 10, y - 45, x + 10, y - 25, fill="red")
    canvas.create_oval(x - 10, y - 25, x + 10, y - 45, fill="red")
    # canvas.create_oval(x - 20, y - 35, x, y - 35, fill="red")


# Implement insect drawing logic here
def draw_insects(canvas):
    # Draw a few insects
    draw_insect(canvas, 280, canvas.winfo_height() // 2 + 210)
    draw_insect(canvas, 530, canvas.winfo_height() // 2 + 210)
    draw_insect(canvas, 540, canvas.winfo_height() // 2 + 210)
    draw_insect(canvas, 550, canvas.winfo_height() // 2 + 210)
    draw_insect(canvas, 560, canvas.winfo_height() // 2 + 210)
    draw_insect(canvas, 570, canvas.winfo_height() // 2 + 210)
    # Add more insects as needed

# Function to draw a single insect
def draw_insect(canvas, x, y):
    # Draw an insect as a simple oval
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
# =================

def draw_catapilers(canvas):
    # Draw a few insects
    draw_catapiler(canvas, 280, canvas.winfo_height() // 2 + 120)
    draw_catapiler(canvas, 530, canvas.winfo_height() // 2 + 110)
    # draw_catapiler(canvas, 240, canvas.winfo_height() // 2 + 140)
    draw_catapiler(canvas, 760, canvas.winfo_height() // 2 + 115)
    # Add more insects as needed

# Function to draw a single insect
def draw_catapiler(canvas, x, y):
    # Draw an insect as a simple oval
    canvas.create_oval(x - 5, y - 5, x + 2, y + 5, fill="black")
    canvas.create_oval(x - 5, y - 5, x + 2, y + 5, fill="black")
    canvas.create_oval(x - 5, y - 5, x + 15, y + 5, fill="black")

# ===================
def draw_clouds(canvas):
    # Draw a few clouds
    draw_cloud(canvas, 250, 450, size=100)
    draw_cloud(canvas, 520, 420, size=50)
    draw_cloud(canvas, 720, 400, size=50)
    draw_cloud(canvas, 690, 420, size=50)
    draw_cloud(canvas, 400, 450, size=90)
   

# Function to draw a single cloud
def draw_cloud(canvas, x, y, size=50):
    # Draw a cloud as an egg shape
    draw_oval(canvas, x - size, y - size // 2, x + size, y + size // 2, fill="white", outline="white")


def draw_sun_shine(canvas):
    draw_sun(canvas, 20, 480, size=40)
    

# Function to draw a sun
def draw_sun(canvas, x, y, size=90):
    # Draw a sun
    draw_oval(canvas, x - size, y - size , x + size, y + size , fill="yellow")


def draw_house(canvas, x, y):
    # Draw the base of the house
    canvas.create_rectangle(x - 50, y, x + 50, y - 80, fill="light blue", outline="black")

    # Draw the roof of the house (a triangle)
    canvas.create_polygon(x - 60, y - 80, x + 60, y - 80, x, y - 120, fill="black", outline="black")


# Function to draw pickets in a fence
def draw_fence(canvas, x, y):
    picket_width = 10
    picket_height = 30
    num_pickets = 5
    spacing = 10

    for i in range(num_pickets):
        draw_rectangle(canvas, x + i * (picket_width + spacing), y,
                       x + (i + 1) * (picket_width + spacing), y - picket_height, fill="white", outline="black")

# Call the main function so that
# this program will start executing.
main()





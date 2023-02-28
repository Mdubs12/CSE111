# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
   


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):

    draw_rectangle(canvas, 0, scene_height / 3,  scene_width, scene_height, width=0, fill='sky blue')

    draw_cloud(canvas, scene_width, scene_height)

def draw_ground(canvas, scene_width, scene_height):

    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width = 0, fill = 'tan4')

def draw_cloud(canvas, scene_width, scene_height):
    
    min_diam =20
    max_diam = 90

    for i in range(100):

        x = random.randint(0, scene_width)
        y = random.randint(scene_height / 2, scene_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x+diameter, y + diameter, width = 0, fill='snow1')


# Call the main function so that
# this program will start executing.
main()
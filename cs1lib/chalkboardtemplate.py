# chalkboard.py
# Allows the user to drag the mouse to draw, using different types of chalk/pens, on a blackboard or whiteboard.

from cs1lib import *

def main():
    old_x = mouse_x()           # initialize old_x, old_y
    old_y = mouse_y()
    canvas.set_size(16, 16)

    # set the default chalk/pen color (white for blackboard, black for whiteboard)
	# set the default chalk/pen width (2 is recommended, but you can play around with different widths)
    # set the board color (black for blackboard, white for whiteboard)
    width = 2

    set_stroke_color(0, 0, 0, alpha = 1.0) #black
    set_stroke_width(width)
    set_clear_color(1, 1, 1, alpha = 1.0)
    

    clear()                     # show the background
    enable_smoothing()          # it looks a little better this way

    while not window_closed():    
        if mouse_down():
            draw_line(old_x, old_y, mouse_x(), mouse_y())
    
		#Now you can customize your board to do things on command based on different keys
		#Try to create different chalk colors, erasers, whatever you want!

        elif is_key_pressed("r"):			#EXAMPLE
            set_stroke_color(1, 0, 0, alpha = 1.0)
        elif is_key_pressed("g"):			#EXAMPLE
            set_stroke_color(0, 1, 0, alpha = 1.0)
        elif is_key_pressed("b"):			#EXAMPLE
            set_stroke_color(0, 0, 1, alpha = 1.0)
        elif is_key_pressed("B"):
            set_stroke_color(1, 1, 1, alpha = 1.0)
            
        elif is_key_pressed("e"):
            clear()
            set_stroke_color(0, 0, 0, alpha = 1.0)

        elif is_key_pressed("+"):
            width = width + 1
            set_stroke_width(width)
        elif is_key_pressed("-"):
            width = width - 1
            set_stroke_width(width)
                    
                    


    
        # Remember where the mouse is now for the next time we draw.
        # If the button is not pressed, then when it is first pressed,
        # it'll probably be here, so it's OK to draw a line from here
        # to where the mouse is when the button is first pressed.
        old_x = mouse_x()
        old_y = mouse_y()
        
        request_redraw()    # show what we've done
        sleep(.02)          # and wait 1/50 second

start_graphics(main)

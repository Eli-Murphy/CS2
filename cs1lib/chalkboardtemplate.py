# chalkboard.py
# Allows the user to drag the mouse to draw, using different types of chalk/pens, on a blackboard or whiteboard.

from cs1lib import *	

def main():
    old_x = mouse_x()           # initialize old_x, old_y
    old_y = mouse_y()
    
    # set the default chalk/pen color (white for blackboard, black for whiteboard)
	# set the default chalk/pen width (2 is recommended, but you can play around with different widths)
    # set the board color (black for blackboard, white for whiteboard)

    clear()                     # show the background
    enable_smoothing()          # it looks a little better this way

    while not window_closed():    
        if # draw only if the mouse button is pressed
            draw_line(old_x, old_y, mouse_x(), mouse_y())
    
		#Now you can customize your board to do things on command based on different keys
		#Try to create different chalk colors, erasers, whatever you want!

        if is_key_pressed("r"):			#EXAMPLE
            # draw in red

	    elif is_key_pressed("E"):
            # erase the board
            # draw in original chalk/pen color
    
        # Remember where the mouse is now for the next time we draw.
        # If the button is not pressed, then when it is first pressed,
        # it'll probably be here, so it's OK to draw a line from here
        # to where the mouse is when the button is first pressed.
        old_x = mouse_x()
        old_y = mouse_y()
        
        request_redraw()    # show what we've done
        sleep(.02)          # and wait 1/50 second

start_graphics(main)

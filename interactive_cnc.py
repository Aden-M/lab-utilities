
"""
Allows the user to easily manually drive the CNC around the volume.
"""

# Imports
from lab.cnc import CNC
import colorama as colors

# Constant
VELOCITY = 150

# Function definitions

def get_step(axis):
    """
    Gets a step size (in mm) from the user
    """
    step = None
    while step is None:
        try:
            step = float(input('Move in {} direction (mm): '.format(axis)))
        except ValueError as err:
                print(err)
    return step

def interactive_cnc_session(cnc):
    """
    Loops throug the x, y, and z axes getting movement steps from the user.
    Prints the final position when finished.
    """
    axes = ['x', 'y', 'z']
    for i, axis in enumerate(axes):
        print("On {} axis.".format(axis))
        print("Enter 0 for step to move onto next axis")
        while True:
            step = get_step(axis)
            if step == 0:
                break
            try:
                point=[0, 0, 0]
                point[i]=step
                cnc.dmove(*tuple(point), VELOCITY)
            except ValueError as err:
                print(err)
    print('Final position:', cnc.get_pos())
    cnc.move_to(0, 0, 50)
    cnc.move_to(0, 0, 0)

# Run the script
if __name__ == '__main__':
    cnc = CNC()
    cnc.issue_warning()
    cnc.home()
    cnc.dmove(0, 0, 50)
    interactive_cnc_session(cnc)

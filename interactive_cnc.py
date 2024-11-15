
"""
Allows the user to easily manually drive the CNC around the volume.
"""

''' Modified by Aden Mann'''
'''
    ___       __              __  ___                
   /   | ____/ /__  ____     /  |/  /___ _____  ____ 
  / /| |/ __  / _ \/ __ \   / /|_/ / __ `/ __ \/ __ \
 / ___ / /_/ /  __/ / / /  / /  / / /_/ / / / / / / /
/_/  |_\__,_/\___/_/ /_/  /_/  /_/\__,_/_/ /_/_/ /_/
'''
# Imports
#from lab.cnc import CNC
import colorama as colors
print("Disclaimer!")
print("This program has been modified by Aden Mann and is otherwise the property of the Texas A&M Physics Department.")
print("Raise any issues found with the functionality of this program at https://github.com/adenmanntamu")
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

def aden_get_step(axis):
    """
    Gets a step size (in mm) from the user
    """
    step = None
    while True:
        try:
            step = input('Move in {} direction (mm): '.format(axis))
            if step == '-':
                break
            # if step == '--':
            #     break
            else:
                step = float(step)
                break
        except ValueError as err:
                print(err)
    print(step)
    return step

def interactive_cnc_session(cnc):
    """
    Loops through the x, y, and z axes getting movement steps from the user.
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
                #cnc.dmove(*tuple(point), VELOCITY)
            except ValueError as err:
                print(err)
    #print('Final position:', cnc.get_pos())
    #cnc.move_to(0, 0, 50)
    #cnc.move_to(0, 0, 0)

def aden_interactive_cnc_session(cnc):
    """
    Loops through the x, y, and z axes getting movement steps from the user.
    Prints the final position when finished.
    Modified by Aden Mann for customized axis order.
    https://github.com/AdenMannTamu
    """
    direction_dict = {'x':'x','y':'y','z':'z'}  # Valid Input Dictionary
    while True:
        first_axis = input("Input first axis for movement: ")  
        second_axis = input("Input second axis for movement: ")
        third_axis = input("Input third axis for movement: ")
        if all(key in direction_dict for key in (first_axis,second_axis,third_axis)) and (len(set([first_axis,second_axis,third_axis])) == 3):  ## Covers poor input choices which might cause problems.
            print(f'Valid Input: {first_axis,second_axis,third_axis}')
            break
        elif not all(key in direction_dict for key in (first_axis,second_axis,third_axis)):  # Check for non xyz input
            print(f'Input Error: One of the inputs: {first_axis,second_axis,third_axis} was not in {direction_dict}')
        else:
            print(f"Input Error: Two or more inputs matched: {first_axis,second_axis,third_axis}")  # Matching inputs
    axes = [first_axis,second_axis,third_axis]
    axis_dict = {'x':0,'y':1,'z':2}
    for axis in axes:
        print("On {} axis.".format(axis))
        print("Enter 0 for step to move onto next axis")
        while True:
            step = get_step(axis)
            if step == 0:
                break
            try:
                point=[0, 0, 0]
                point[axis_dict[axis]]=step
                #print(axis_dict[axis],step,point)
                cnc.dmove(*tuple(point), VELOCITY)
            except ValueError as err:
                print(err)
    print('Final position:', cnc.get_pos())
    cnc.move_to(0, 0, 50)
    cnc.move_to(0, 0, 0)

def aden_interactive_cnc_session_roided(cnc):
    """
    Loops through the x, y, and z axes getting movement steps from the user.
    Allows for customized axis options.
    Prints the final position when finished.
    Modified by Aden Mann for customized axis order.
    https://github.com/AdenMannTamu
    """
    direction_dict = {'x':'x','y':'y','z':'z'}  # Valid Input Dictionary
    while True:
        first_axis = input("Input first axis for movement: ")  
        second_axis = input("Input second axis for movement: ")
        third_axis = input("Input third axis for movement: ")
        if all(key in direction_dict for key in (first_axis,second_axis,third_axis)) and (len(set([first_axis,second_axis,third_axis])) == 3):  ## Covers poor input choices which might cause problems.
            print(f'Valid Input: {first_axis,second_axis,third_axis}')
            break
        elif not all(key in direction_dict for key in (first_axis,second_axis,third_axis)):  # Check for non xyz input
            print(f'Input Error: One of the inputs: {first_axis,second_axis,third_axis} was not in {direction_dict}')
        else:
            print(f"Input Error: Two or more inputs matched: {first_axis,second_axis,third_axis}")  # Matching inputs
    axes = [first_axis,second_axis,third_axis]
    axis_dict = {'x':0,'y':1,'z':2}
    previous_axes = []
    i = 0
    while i < len(axes):
        axis = axes[i]
        print("On {} axis.".format(axis))
        print("Enter 0 for step to move onto next axis")
        print("Enter - for step to move onto previous axis")
        # print("Enter -- for step to move onto first axis")
        while True:
            step = aden_get_step(axis)
            print(step, previous_axes)
            if step == 0:
                if axis not in previous_axes:
                    previous_axes += axis
                i += 1  # Move to next axis
                break
            elif step == '-' and i > 0:
                i -= 1  # Move back to previous axis
                break
            # elif step == '--' and i > 1:
            #     i -= 2  # Move back two axes
            #     break
            else:
                try:
                    point = [0, 0, 0]
                    point[axis_dict[axis]] = step
                    #print(axis_dict[axis], step, point)
                    cnc.dmove(*tuple(point), VELOCITY)
                    # previous_axes += axis
                except ValueError as err:
                    print(err)
        # Ensure index stays within bounds
        if i < 0:
            i = 0
        elif i >= len(axes):
            print("All axes have been processed.")
            break
    print('Final position:', cnc.get_pos())
    cnc.move_to(0, 0, 50)
    cnc.move_to(0, 0, 0)

def choose_session(cnc):
    ''' Allows user to choose session type'''
    sessions = [1,2,3]
    print('Please choose from the following CNC sessions')
    print('1: Default interactive cnc (TAMU)')
    print('2: Custom Direction order interactive cnc (ADEN)')
    print('3: Custom Direction order and cyclable axes (ADEN)')
    while True:
        choice = input("Input CNC session choice: ")
        if choice in sessions:
            break
        else:
            print(f"Input Error: {choice} is not a valid choice")
    if choice == 1:
        interactive_cnc_session(cnc)
    elif choice == 2:
        aden_interactive_cnc_session(cnc)
    elif choice == 3:
        aden_interactive_cnc_session_roided(cnc)    

#interactive_cnc_session(cnc)
# Run the script
if __name__ == '__main__':
    cnc = CNC()
    cnc.issue_warning()
    cnc.home()
    cnc.dmove(0, 0, 50)
    choose_session(cnc)

import matplotlib.pyplot as mpl
from visualization import plot_cube
import os

def user_cube(cube, colors, label_state):
    while True:
        plot_cube(cube, colors, label_state)

        def custom_cube(cube):
            face = input("Please enter the centre pieces as they appear in the cube diagram.\nEnter the face (U, D, F, B, L, R) followed by 'R' for row/'C' for column number, then the orientation of colors\n(Example: UR1WWW, DC2RGB)\nEnter '0' if your custom cube is complete\nEnter: ").upper()
            count = 0
            if face[0] == '0' and len(face) == 1:
                return cube, False
            elif face[0] == 'Q' and len(face) == 1:
                os._exit(0)
            else:
                if len(face) == 6:
                    if face[0] in ['U', 'D', 'R', 'L', 'F', 'B']:
                        if face[1] in ['R', 'C']:
                            for i in range(3,6):
                                if face[i] in ['W', 'G', 'R', 'B', 'Y', 'O']:
                                    count+=1
                                if count == 3:
                                    if face[1] == 'R':
                                        row_index = int(face[2])-1
                                        for i in range(3):
                                            cube[face[0]][row_index, i] = face[i+3]
                                    elif face[1] == 'C':
                                        column_index = int(face[2])-1
                                        for i in range(3):
                                            cube[face[0]][i, column_index] = face[i+3]
                                    return cube, True
                            else:
                                print("Please enter valid input.")
                        else:
                            print("Please enter valid input.")
                    else:
                        print("Please enter valid input.")
                else:
                    print("Please enter valid input.")
            return cube, True

        
        cube, finished = custom_cube(cube)
        if finished is not True:
            break
    return cube
 
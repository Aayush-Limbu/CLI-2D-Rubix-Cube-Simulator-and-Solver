from cube import Cube
from rotation import rotate_cube_clockwise, rotate_cube_anticlockwise
from visualization import plot_cube
from custom_cube import user_cube
from solve import cube_solve


def userinterface():
    cube_instance = Cube()
    
    while True:
        plot_cube(cube_instance.cube, cube_instance.colors, 0)
        user_input = input("Enter a move (U, D, R, L, F, B, U\', D\', R\', L\', F\', B\') or 'Q' at any time to quit\nEnter '0' to enter your own cube\nEnter 'S' to solve the cube\nEnter: ").upper()
        if user_input == 'Q':
            break
        elif user_input == '0':
            user_cube(cube_instance.cube, cube_instance.colors, 1)
        elif user_input in ['U', 'D', 'R', 'L', 'F', 'B']:
            rotate_cube_clockwise(cube_instance.cube, user_input)
        elif user_input in ["U\'", "D\'", "R\'", "L\'", "F\'", "B\'"]:
            rotate_cube_anticlockwise(cube_instance.cube, user_input)
        elif user_input == 'S':
            print(cube_solve(cube_instance.cube))
            
    
        else:
            print("Invalid input. Please type a valid move.")

if __name__ == "__main__":
    userinterface()

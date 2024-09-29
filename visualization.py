import matplotlib.pyplot as mpl

def plot_cube(cube, colors, label_state):
    fig, ax = mpl.subplots()
    mpl.axis('off')

    def draw_face(face, position):
        x, y = position
        for i in range(3):
            for j in range(3):
                color = colors[cube[face][i, j]]
                rect = mpl.Rectangle((x + j, y - i), 1, 1, edgecolor='black', facecolor=color)
                ax.add_patch(rect)
                if label_state == 1:
                    label = f"{face}{i * 3 + j + 1}"
                    ax.text(x + j + 0.5, y - i + 0.5, label, ha='center', va='center', fontsize=8, color='black')

    draw_face('U', (3, 9))
    draw_face('L', (0, 6))
    draw_face('F', (3, 6))
    draw_face('R', (6, 6))
    draw_face('B', (9, 6))
    draw_face('D', (3, 3))

    mpl.xlim(0, 12)
    mpl.ylim(0, 12)
    mpl.gca().set_aspect('equal', adjustable='box')
    mpl.show()

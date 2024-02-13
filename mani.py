import numpy as np

def rot_90(A, times):
    rotated_A = np.zeros((A.shape[0], A.shape[0]), dtype=object)
    transposed_A = np.transpose(A)  # np.flipud(np.fliplr(A))

    times = times % 4

    if times == 0:
        return A
    if times == 1:
        for i in range(A.shape[0]):
            rotated_A[i] = transposed_A[-1-i]
        return rotated_A
    if times == 2:
        return transposed_A
    if times == 3:
        for i in range(A.shape[0]):
            rotated_A[i] = A[-1-i]
        return np.transpose(rotated_A)


class CuboRubik:
    def __init__(self):
        self.front = np.array([['green ' for _ in range(3)] for _ in range(3)])
        self.back = np.array([['yellow ' for _ in range(3)] for _ in range(3)])
        self.up = np.array([['white ' for _ in range(3)] for _ in range(3)])
        self.down = np.array([['blue  ' for _ in range(3)] for _ in range(3)])
        self.right = np.array([['red   ' for _ in range(3)] for _ in range(3)])
        self.left = np.array([['orange' for _ in range(3)] for _ in range(3)])
    #def __init__(self):
    #    self.front = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    #    self.back = np.array([[9, 10, 11], [12, 13, 14], [15, 16, 17]])
    #    self.up = np.array([[18, 19, 20], [21, 22, 23], [24, 25, 26]])
    #    self.down = np.array([[27, 28, 29], [30, 31, 32], [33, 34, 35]])
    #    self.right = np.array([[36, 37, 38], [39, 40, 41], [42, 43, 44]])
    #    self.left = np.array([[45, 46, 47], [48, 49, 50], [51, 52, 53]])

    def F(self, times=-1):
        self.front = rot_90(self.front, times)

        left_column = self.left[:, 2].copy()
        right_column = self.right[:, 0].copy()
        up_row = self.up[2, :].copy()
        down_row = self.down[0, :].copy()

        self.left[:, 2] = down_row
        self.right[:, 0] = up_row
        self.up[2, :] = np.flipud(left_column)
        self.down[0, :] = np.flipud(right_column)

    def execute_moves(self, moves):
        move_mapping = {
            'F': self.F,
            "F'": self.Fp,
            'vacavoladora': self.vacavoladora
            # poner las demás rotaciones
        }

        for move in moves:
            move_function = move_mapping.get(move)
            if move_function:
                move_function()
            else:
                print(f"Error: No se encontró la función asociada a la cadena '{move}'")

    def print_cube(self):
            # Imprimir el diseño del cubo
            #print('   U')
            #print('L  F  R  B')
            #print('   D')

            # Imprimir las caras del cubo
            print('\nCara U:')
            print(self.up)
            print('\nCara L:')
            print(self.left)
            #print('\nCara F:')
            #print(self.front)
            print('\nCara R:')
            print(self.right)
            #print('\nCara B:')
            #print(self.back)
            print('\nCara D:')
            print(self.down)


# Crear un cubo de Rubik
cubo = CuboRubik()
# Imprimir el diseño del cubo
cubo.print_cube()
cubo.F()
print('\n')
cubo.print_cube()

import numpy as np

#He definido esta func para estudiar un poco las simetrías en las rotaciones, pero numpy tiene la suya: np.rot90()
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
    #def __init__(self):
    #    self.left = np.array([[_ for _ in range(3)] for _ in range(3)])
    #    self.front = np.array([[_ for _ in range(3)] for _ in range(3)])
    #    self.right = np.array([[_ for _ in range(3)] for _ in range(3)])
    #    self.back = np.array([[_ for _ in range(3)] for _ in range(3)])
    #    self.up = np.array([[_ for _ in range(3)] for _ in range(3)])
    #    self.down = np.array([[_ for _ in range(3)] for _ in range(3)])
    def F(self, times=-1):
        #Rotación cara ppal
        self.front = rot_90(self.front, times)

        #Definición elementos adyacentes
        left_column = self.left[:, 2].copy()
        right_column = self.right[:, 0].copy()
        up_row = self.up[2, :].copy()
        down_row = self.down[0, :].copy()

        #Modificación elementos adyacentes
        self.left[:, 2] = down_row
        self.right[:, 0] = up_row
        self.up[2, :] = np.flipud(left_column)
        self.down[0, :]  = np.flipud(right_column)
    def Fp(self, times=1):
        self.front = rot_90(self.front, times)

        left_column = self.left[:, 2].copy()
        right_column = self.right[:, 0].copy()
        up_row = self.up[2, :].copy()
        down_row = self.down[0, :].copy()

        self.left[:, 2]  = np.flipud(up_row)
        self.right[:, 0] = np.flipud(down_row)
        self.up[2, :]    = right_column
        self.down[0, :]  = left_column

    def B(self, times=-1):
        self.back = rot_90(self.back, times)

        left_column = self.right[:, 2].copy()
        right_column = self.left[:, 2].copy()
        up_row = np.flipud(self.up[0, :].copy())
        down_row = np.flipud(self.down[2, :].copy())

        self.right[:, 2] = np.flipud(down_row)
        self.left[:, 2] = np.flipud(up_row)
        self.up[0, :] = left_column
        self.down[2, :] = right_column

    def Bp(self, times=1):
        self.back = rot_90(self.back, times)

        left_column = self.right[:, 2].copy()
        right_column = self.left[:, 2].copy()
        up_row = np.flipud(self.up[0, :].copy())
        down_row = np.flipud(self.down[2, :].copy())

        self.left[:, 2] = up_row
        self.right[:, 2] = down_row
        self.up[0, :] = np.flipud(right_column)
        self.down[2, :] = np.flipud(left_column)

    def L(self, times=-1):
        self.left = rot_90(self.left, times)

        left_column = self.back[:, 2].copy()
        right_column = self.front[:, 0].copy()
        up_row = self.up[:, 0].copy()
        down_row = np.flipud(self.down[:, 0].copy())

        self.back[:, 2] = np.flipud(down_row)
        self.front[:, 0] = up_row
        self.up[:, 0] = np.flipud(left_column)
        self.down[:, 0] = right_column

    def Lp(self, times=1):
        self.left = rot_90(self.left, times)

        left_column = self.back[:, 2].copy()
        right_column = self.front[:, 0].copy()
        up_row = self.up[:, 0].copy()
        down_row = np.flipud(self.down[:, 0].copy())

        self.back[:, 2] = np.flipud(up_row)
        self.front[:, 0] = down_row
        self.up[:, 0] = right_column
        self.down[:, 0] = np.flipud(left_column)

    def R(self, times=-1):
        self.right = rot_90(self.right, times)

        left_column = self.front[:, 2].copy()
        right_column = self.back[:, 0].copy()
        up_row = np.flipud(self.up[:, 2].copy())
        down_row = self.down[:, 2].copy()

        self.front[:, 2] = down_row
        self.back[:, 0] = np.flipud(up_row)
        self.up[:, 2] = left_column
        self.down[:, 2] = np.flipud(right_column)

    def Rp(self, times=1):
        self.right = rot_90(self.right, times)

        left_column = self.front[:, 2].copy()
        right_column = self.back[:, 0].copy()
        up_row = np.flipud(self.up[:, 2].copy())
        down_row = self.down[:, 2].copy()

        self.front[:, 2] = up_row
        self.back[:, 0] = np.flipud(down_row)
        self.up[:, 2] = np.flipud(right_column)
        self.down[:, 2] = left_column

    def U(self, times=-1):
        self.up = rot_90(self.up, times)

        left_column = self.left[0, :].copy()
        right_column = np.flipud(self.right[0, :].copy())
        up_row = np.flipud(self.back[0, :].copy())
        down_row = self.front[0, :].copy()

        self.left[0, :] = down_row
        self.right[:, 0] = up_row
        self.back[0, :] = left_column
        self.front[0, :] = right_column

    def Up(self, times=1):
        self.front = rot_90(self.front, times)

        left_column = self.left[0, :].copy()
        right_column = np.flipud(self.right[0, :].copy())
        up_row = np.flipud(self.back[0, :].copy())
        down_row = self.front[0, :].copy()

        self.left[0, :] = up_row
        self.right[:, 0] = down_row
        self.back[0, :] = right_column
        self.front[0, :] = left_column

    def D(self, times=-1):
        self.down = rot_90(self.down, times)

        left_column = np.flipud(self.left[2, :].copy())
        right_column = self.right[2, :].copy()
        up_row = self.front[2, :].copy()
        down_row = np.flipud(self.down[2, :].copy())

        self.left[2, :] = down_row
        self.right[2, :] = up_row
        self.front[2, :] = left_column
        self.down[2, :] = right_column

    def Dp(self, times=1):
        self.down = rot_90(self.down, times)

        left_column = np.flipud(self.left[2, :].copy())
        right_column = self.right[2, :].copy()
        up_row = self.front[2, :].copy()
        down_row = np.flipud(self.down[2, :].copy())

        self.left[:, 2] = up_row
        self.right[:, 0] = down_row
        self.up[2, :] = right_column
        self.down[0, :] = left_column

    """
    Importante: Kociemba dará una lista de la forma
    kociemba_str = "R' D2 R' U2 R F2 D B2 U' R F' U R2 D L2 D' B2 R2 B2 U' B2"
    
    Para que podamos trabajar con ella:
    kociemba_lst = kociemba_str.split()
    """
    def execute_moves(self, moves):
        #Diccionario para identificar la salida de Kociemba con las rotaciones
        move_mapping = {
            'F': self.F,
            "F'": self.Fp,
            "F2": lambda: [self.F() for _ in range(2)],

            'B': self.B,
            "B'": self.Bp,
            "B2": lambda: [self.B() for _ in range(2)],

            'L': self.L,
            "L'": self.Lp,
            "L2": lambda: [self.L() for _ in range(2)],

            'R': self.R,
            "R'": self.Rp,
            "R2": lambda: [self.R() for _ in range(2)],

            'U': self.U,
            "U'": self.Up,
            "U2": lambda: [self.U() for _ in range(2)],

            'D': self.D,
            "D'": self.Dp,
            "D2": lambda: [self.D() for _ in range(2)]
        }

        #Ejecución de rotaciones en orden de array
        for move in moves:
            move_function = move_mapping.get(move)
            if move_function:
                move_function()
            else:
                print(f"Error: No se encontró '{move}'")

    """
    Esta función guarra pinta el cubo como viene siendo habitual:
       U
    L  F  R  B
       D
    """
    def print_state(self):
        for i in range(3):
            print("\t\t\t\t\t\t|", end=" ")
            for j in range(3):
                print(f"{self.up[i][j]}", end=" ")
            print("|")
        print("-------------------------------------------------------------------------------------------------------------")
        for i in range(3):
            print("|", end=" ")
            for j in range(3):
                print(f"{self.left[i][j]}", end=" ")
            print("|", end=" ")
            for j in range(3):
                print(f"{self.front[i][j]}", end=" ")
            print("|", end=" ")
            for j in range(3):
                print(f"{self.right[i][j]}", end=" ")
            print("|", end=" ")
            for j in range(3):
                print(f"{self.back[i][j]}", end=" ")
            print("|")
        print("-------------------------------------------------------------------------------------------------------------")
        for i in range(3):
            print("\t\t\t\t\t\t|", end=" ")
            for j in range(3):
                print(f"{self.down[i][j]}", end=" ")
            print("|")

# Testeo
cubo = CuboRubik()
#Prueba de exmoves
#kociemba_array = ["F", "F'", "F2"]
#cubo.execute_moves(kociemba_array)

# Imprimir el diseño del cubo
cubo.print_state()
cubo.Fp()
print('\n')
cubo.print_state()
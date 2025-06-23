import cv2
import numpy as np
import kociemba as Cube
import colorama
import textwrap
import serial
import time
import random

ser = serial.Serial("COM5", 115200, timeout=1)
time.sleep(2)

# Variables globales
dragging = False
selected_point = None
width, height = 200, 200  # Tamaño de la imagen transformada
p = 0

# Esquinas iniciales del cuadrado (ajústalas según la imagen)
points = np.float32([[227, 245], [324, 321], [336, 440], [244, 362], [331, 193], [429, 243], [419, 353]])


def draw_points(img, points):
    """Dibuja los puntos y líneas del cuadrado en la imagen."""
    for i, point in enumerate(points):
        cv2.circle(img, tuple(point), 5, (0, 0, 255), -1)  # Puntos rojos
        cv2.line(img, tuple(points[0]), tuple(points[1]), (0, 255, 0), 2)  # Líneas verdes
        cv2.line(img, tuple(points[1]), tuple(points[2]), (0, 255, 0), 2)
        cv2.line(img, tuple(points[2]), tuple(points[3]), (0, 255, 0), 2)
        cv2.line(img, tuple(points[3]), tuple(points[0]), (0, 255, 0), 2)
        cv2.line(img, tuple(points[0]), tuple(points[4]), (0, 255, 0), 2)
        cv2.line(img, tuple(points[5]), tuple(points[1]), (0, 255, 0), 2)
        cv2.line(img, tuple(points[4]), tuple(points[5]), (0, 255, 0), 2)
        cv2.line(img, tuple(points[2]), tuple(points[6]), (0, 255, 0), 2)
        cv2.line(img, tuple(points[5]), tuple(points[6]), (0, 255, 0), 2)

def apply_perspective_transform(img, points):
    """Aplica la transformación de perspectiva y devuelve la imagen corregida."""
    pts1Left = np.float32(points[0:4])
    pts2Left = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    matrixLeft = cv2.getPerspectiveTransform(pts1Left, pts2Left)
    imgOutputLeft = cv2.warpPerspective(img, matrixLeft, (width, height))
    pts1Right = np.float32([points[4], points[5], points[1], points[0]])
    pts2Right = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    matrixRight = cv2.getPerspectiveTransform(pts1Right, pts2Right)
    imgOutputRight = cv2.warpPerspective(img, matrixRight, (width, height))
    pts1Up = np.float32([points[1], points[5], points[6], points[2]])
    pts2Up = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    matrixUp = cv2.getPerspectiveTransform(pts1Up, pts2Up)
    imgOutputUp = cv2.warpPerspective(img, matrixUp, (width, height))

    return imgOutputLeft, imgOutputRight, imgOutputUp

def mouse_callback(event, x, y, flags, param):
    """Maneja los eventos del ratón para arrastrar los puntos."""
    global dragging, selected_point, points

    if event == cv2.EVENT_LBUTTONDOWN:
        for i, point in enumerate(points):
            if np.linalg.norm(np.array(point) - np.array([x, y])) < 10:  # Si el clic está cerca de un punto
                dragging = True
                selected_point = i
                break

    elif event == cv2.EVENT_MOUSEMOVE:
        if dragging and selected_point is not None:
            points[selected_point] = [x, y]

    elif event == cv2.EVENT_LBUTTONUP:
        dragging = False
        selected_point = None


GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
RED = colorama.Fore.RED
MAGENTA = colorama.Fore.MAGENTA
colorama.init()

state = {
    'up': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', ],
    'right': ['white', 'white', 'white', 'white', 'red', 'white', 'white', 'white', 'white', ],
    'front': ['white', 'white', 'white', 'white', 'green', 'white', 'white', 'white', 'white', ],
    'down': ['white', 'white', 'white', 'white', 'yellow', 'white', 'white', 'white', 'white', ],
    'left': ['white', 'white', 'white', 'white', 'orange', 'white', 'white', 'white', 'white', ],
    'back': ['white', 'white', 'white', 'white', 'blue', 'white', 'white', 'white', 'white', ]
}

solved_state = {
    'up': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', ],
    'right': ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', ],
    'front': ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', ],
    'down': ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', ],
    'left': ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', ],
    'back': ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', ]
}


sign_conv = {
    'green': 'F',
    'white': 'U',
    'blue': 'B',
    'red': 'R',
    'orange': 'L',
    'yellow': 'D'
}

color = {
    'red': (0, 0, 255),
    'orange': (0, 165, 255),
    'blue': (255, 0, 0),
    'green': (0, 255, 0),
    'white': (255, 255, 255),
    'yellow': (0, 255, 255)
}

stickers = {
    'caraF': [
        [20, 520], [86, 520], [152, 520],
        [20, 584], [86, 584], [152, 584],
        [20, 648], [86, 648], [152, 648]
    ],
    'caraU': [
        [220, 520], [286, 520], [352, 520],
        [220, 584], [286, 584], [352, 584],
        [220, 648], [286, 648], [352, 648]
    ],
    'caraR': [
        [420, 520], [486, 520], [552, 520],
        [420, 584], [486, 584], [552, 584],
        [420, 648], [486, 648], [552, 648]
    ],
    'currentF': [
        [35, 358], [80, 358], [125, 358],
        [35, 403], [80, 403], [125, 403],
        [35, 448], [80, 448], [125, 448]
    ],
    'currentU': [
        [235, 358], [280, 358], [325, 358],
        [235, 403], [280, 403], [325, 403],
        [235, 448], [280, 448], [325, 448]
    ],
    'currentR': [
        [435, 358], [480, 358], [525, 358],
        [435, 403], [480, 403], [525, 403],
        [435, 448], [480, 448], [525, 448]
    ],
    'preview': [
        [20, 130], [54, 130], [88, 130],
        [20, 164], [54, 164], [88, 164],
        [20, 198], [54, 198], [88, 198]
    ],
    'left': [
        [50, 280], [94, 280], [138, 280],
        [50, 324], [94, 324], [138, 324],
        [50, 368], [94, 368], [138, 368]
    ],
    'front': [
        [188, 280], [232, 280], [276, 280],
        [188, 324], [232, 324], [276, 324],
        [188, 368], [232, 368], [276, 368]
    ],
    'right': [
        [326, 280], [370, 280], [414, 280],
        [326, 324], [370, 324], [414, 324],
        [326, 368], [370, 368], [414, 368]
    ],
    'up': [
        [188, 128], [232, 128], [276, 128],
        [188, 172], [232, 172], [276, 172],
        [188, 216], [232, 216], [276, 216]
    ],
    'down': [
        [188, 434], [232, 434], [276, 434],
        [188, 478], [232, 478], [276, 478],
        [188, 522], [232, 522], [276, 522]
    ],
    'back': [
        [464, 280], [508, 280], [552, 280],
        [464, 324], [508, 324], [552, 324],
        [464, 368], [508, 368], [552, 368]
    ],
}

font = cv2.FONT_HERSHEY_SIMPLEX
textPoints = {
    'up': [['U', 242, 202], ['W', (255, 255, 255), 260, 208]],
    'right': [['R', 380, 354], ['R', (0, 0, 255), 398, 360]],
    'front': [['F', 242, 354], ['G', (0, 255, 0), 260, 360]],
    'down': [['D', 242, 508], ['Y', (0, 255, 255), 260, 514]],
    'left': [['L', 104, 354], ['O', (0, 165, 255), 122, 360]],
    'back': [['B', 518, 354], ['B', (255, 0, 0), 536, 360]],
}

check_state = []
solution = []
solved = False

cap = cv2.VideoCapture(1)
cap.set(3, 1000)
time.sleep(2)


# Rotaciones horario
def rotate(side):
    main = state[side]
    front = state['front']
    left = state['left']
    right = state['right']
    up = state['up']
    down = state['down']
    back = state['back']

    if side == 'front':
        left[2], left[5], left[8], up[6], up[7], up[8], right[0], right[3], right[6], down[0], down[1], down[2] = \
            down[0], down[1], down[2], left[8], left[5], left[2], up[6], up[7], up[8], right[6], right[3], right[0]
    elif side == 'up':
        left[0], left[1], left[2], back[0], back[1], back[2], right[0], right[1], right[2], front[0], front[1], front[
            2] = front[0], front[1], front[2], left[0], left[1], left[2], back[0], back[1], back[2], right[0], \
                 right[1], right[2]
    elif side == 'down':
        left[6], left[7], left[8], back[6], back[7], back[8], right[6], right[7], right[8], front[6], front[7], front[
            8] = back[6], back[7], back[8], right[6], right[7], right[8], front[6], front[7], front[8], left[6], left[
            7], left[8]
    elif side == 'back':
        left[0], left[3], left[6], up[0], up[1], up[2], right[2], right[5], right[8], down[6], down[7], down[8] = \
            up[2], up[1], up[0], right[2],  right[5], right[8], down[8], down[7], down[6], left[0], left[3], left[6]
    elif side == 'left':
        front[0], front[3], front[6], down[0], down[3], down[6], back[2], back[5], back[8], up[0], up[3], up[6] = \
            up[0], up[3], up[6], front[0], front[3], front[6], down[6], down[3], down[0], back[8], back[5], back[2]
    elif side == 'right':
        front[2], front[5], front[8], down[2], down[5], down[8], back[0], back[3], back[6], up[2], up[5], up[8] = \
            down[2], down[5], down[8], back[6], back[3], back[0], up[8], up[5], up[2], front[2], front[5], front[8]

    main[0], main[1], main[2], main[3], main[4], main[5], main[6], main[7], main[8] = main[6], main[3], main[0], main[
        7], main[4], main[1], main[8], main[5], main[2]


# rotaciones antihorario
def revrotate(side):
    main = state[side]
    front = state['front']
    left = state['left']
    right = state['right']
    up = state['up']
    down = state['down']
    back = state['back']

    if side == 'front':
        left[2], left[5], left[8], up[6], up[7], up[8], right[0], right[3], right[6], down[0], down[1], down[2] = \
            up[8], up[7], up[6], right[0], right[3], right[6], down[2], down[1], down[0], left[2], left[5], left[8]
    elif side == 'up':
        left[0], left[1], left[2], back[0], back[1], back[2], right[0], right[1], right[2], front[0], front[1], front[
            2] = back[0], back[1], back[2], right[0], right[1], right[2], front[0], front[1], front[2], left[0], left[
            1], left[2]
    elif side == 'down':
        left[6], left[7], left[8], back[6], back[7], back[8], right[6], right[7], right[8], front[6], front[7], front[
            8] = front[6], front[7], front[8], left[6], left[7], left[8], back[6], back[7], back[8], right[6], \
                 right[7], right[8]
    elif side == 'back':
        left[0], left[3], left[6], up[0], up[1], up[2], right[2], right[5], right[8], down[6], down[7], down[8] = \
            down[6], down[7], down[8], left[6], left[3], left[0], up[0], up[1], up[2], right[8], right[5], right[2]
    elif side == 'left':
        front[0], front[3], front[6], down[0], down[3], down[6], back[2], back[5], back[8], up[0], up[3], up[6] = \
            down[0], down[3], down[6], back[8], back[5], back[2], up[6], up[3], up[0], front[0], front[3], front[6]
    elif side == 'right':
        front[2], front[5], front[8], down[2], down[5], down[8], back[0], back[3], back[6], up[2], up[5], up[8] = \
            up[2], up[5], up[8], front[2], front[5], front[8], down[8], down[5], down[2], back[6], back[3], back[0]

    main[0], main[1], main[2], main[3], main[4], main[5], main[6], main[7], main[8] = main[2], main[5], main[8], main[
        1], main[4], main[7], main[0], main[3], main[6]


# devuelve los movimientos solucion. No cambia el estado del cubo
def solve(state):
    raw = ''
    for i in state:
        for j in state[i]:
            raw += sign_conv[j]
    # print(Cube.solve(raw), ' ')
    sol = Cube.solve(raw) + " "
    sol_array = sol.split()
    sol_doblegiro = giro_doble(sol)
    #print(sol)
    print(sol_doblegiro)
    text_lines.append(sol_doblegiro)
    sol_doblegiro_cronometer = "start " + sol_doblegiro + "stop "
    ser.write(sol_doblegiro_cronometer.encode('ascii'))
    return Cube.solve(raw)


#Funcion que genera una secuencia aleatoria de movimientos
def mix(moves=20):
    movimientos = ["U", "U'", "U2", "F", "F'", "F2", "R", "R'", "R2", "B", "B'", "B2", "L", "L'", "L2", "D", "D'", "D2"]

    secuencia_aleatoria = [random.choice(movimientos)]

    for _ in range(moves - 1):
        siguiente_movimiento = random.choice(movimientos)
        while siguiente_movimiento[0] == secuencia_aleatoria[-1][0]:
            siguiente_movimiento = random.choice(movimientos)

        secuencia_aleatoria.append(siguiente_movimiento)

    return " ".join(secuencia_aleatoria)


def color_detect(h, s, v):
    # print(h,s,v)
    if h <= 6 and s >= 30:
        return 'red'
    elif h >= 170 and s >= 30:
        return 'red'
    elif h <= 27 and h >= 7 and s >= 30:
        return 'orange'
    elif h <= 48 and h >= 28 and s >= 30:
        return 'yellow'
    elif h >= 51 and h <= 70 and s >= 50:
        return 'green'
    elif h >= 75 and h <= 150 and s >= 80:
        return 'blue'

    return 'white'




def draw_stickers(frame, stickers, name, size):
    for x, y in stickers[name]:
        cv2.rectangle(frame, (x, y), (x + size, y + size), (255, 255, 255), 2)


def draw_preview_stickers(frame, stickers):
    stick = ['front', 'back', 'left', 'right', 'up', 'down']
    for name in stick:
        for x, y in stickers[name]:
            cv2.rectangle(frame, (x, y), (x + 40, y + 40), (255, 255, 255), 2)


def texton_preview_stickers(frame, stickers):
    stick = ['front', 'back', 'left', 'right', 'up', 'down']
    for name in stick:
        for x, y in stickers[name]:
            sym, x1, y1 = textPoints[name][0][0], textPoints[name][0][1], textPoints[name][0][2]
            cv2.putText(preview, sym, (x1, y1), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
            sym, col, x1, y1 = textPoints[name][1][0], textPoints[name][1][1], textPoints[name][1][2], \
                               textPoints[name][1][3]
            cv2.putText(preview, sym, (x1, y1), font, 0.5, col, 1, cv2.LINE_AA)


def fill_stickers(frame, stickers, sides):
    for side, colors in sides.items():
        num = 0
        for x, y in stickers[side]:
            cv2.rectangle(frame, (x, y), (x + 40, y + 40), color[colors[num]], -1)
            num += 1


# Recibe una secuencia de movimientos y ejecuta las rotaciones en el estado del cubo
def process(operation):
    replace = {
        "F": [rotate, 'front'],
        "F2": [rotate, 'front', 'front'],
        "F'": [revrotate, 'front'],
        "U": [rotate, 'up'],
        "U2": [rotate, 'up', 'up'],
        "U'": [revrotate, 'up'],
        "L": [rotate, 'left'],
        "L2": [rotate, 'left', 'left'],
        "L'": [revrotate, 'left'],
        "R": [rotate, 'right'],
        "R2": [rotate, 'right', 'right'],
        "R'": [revrotate, 'right'],
        "D": [rotate, 'down'],
        "D2": [rotate, 'down', 'down'],
        "D'": [revrotate, 'down'],
        "B": [rotate, 'back'],
        "B2": [rotate, 'back', 'back'],
        "B'": [revrotate, 'back']
    }
    a = 0

    for i in operation:
         for j in range(len(replace[i]) - 1):
             replace[i][0](replace[i][j + 1])


def split_text_lines(text, max_width):
    # Divide el texto en líneas más cortas con un ancho máximo
    wrapped_text = textwrap.fill(text, width=max_width)
    lines = wrapped_text.split('\n')
    return lines


button_x1, button_y1, button_width1, button_height1 = 1000, 150, 150, 70
button_x2, button_y2, button_width2, button_height2 = 1180, 150, 150, 70
button_x3, button_y3, button_width3, button_height3 = 1270, 600, 80, 30
button_x4, button_y4, button_width4, button_height4 = 1000, 50, 150, 70


def draw_button_solve(img, text):
        cv2.rectangle(img, (button_x1, button_y1), (button_x1 + button_width1, button_y1 + button_height1), (30, 200, 30), -1)
        cv2.putText(img, text, (button_x1 + 32, button_y1 + 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)


def draw_button_mix(img, text):
        cv2.rectangle(img, (button_x2, button_y2), (button_x2 + button_width2, button_y2 + button_height2), (20, 225, 225), -1)
        cv2.putText(img, text, (button_x2 + 47, button_y2 + 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)


def draw_button_quit(img, text):
    cv2.rectangle(img, (button_x3, button_y3), (button_x3 + button_width3, button_y3 + button_height3), (0, 0, 250), -1)
    cv2.putText(img, text, (button_x3 + 18, button_y3 + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2,
                cv2.LINE_AA)


def draw_button_scan(img, text):
        cv2.rectangle(img, (button_x4, button_y4), (button_x4 + button_width4, button_y4 + button_height4), (215, 89, 35),
                      -1)
        cv2.putText(img, text, (button_x4 + 32, button_y4 + 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,
                    cv2.LINE_AA)


def is_mouse_inside_button_solve(x, y):
    return button_x1 <= x <= button_x1 + button_width1 and button_y1 <= y <= button_y1 + button_height1


def is_mouse_inside_button_mix(x, y):
    return button_x2 <= x <= button_x2 + button_width2 and button_y2 <= y <= button_y2 + button_height2


def is_mouse_inside_button_quit(x, y):
    return button_x2 <= x <= button_x3 + button_width3 and button_y3 <= y <= button_y3 + button_height3


def is_mouse_inside_button_scan(x, y):
    return button_x4 <= x <= button_x4 + button_width4 and button_y4 <= y <= button_y4 + button_height4


def on_mouse_event(event, x, y, flags, param):
    global text_lines, dragging, selected_point, points, p

    if event == cv2.EVENT_LBUTTONDOWN:
        for i, point in enumerate(points):
            if np.linalg.norm(np.array(point) - np.array([x, y])) < 10:  # Si el clic está cerca de un punto
                dragging = True
                selected_point = i
                break

    elif event == cv2.EVENT_MOUSEMOVE:
        if dragging and selected_point is not None:
            points[selected_point] = [x, y]

    elif event == cv2.EVENT_LBUTTONUP:
        dragging = False
        selected_point = None
    if event == cv2.EVENT_LBUTTONDOWN:
        if is_mouse_inside_button_solve(x, y):
            if len(set(check_state)) == 6:
                try:
                    solved = solve(state)
                    if solved:
                        operation = solved.split(' ')
                        process(operation)
                        # text_lines.append(solved)
                except:
                    print("Error in side detection. Please try again.")
                    text_lines.append("Error in side detection")
            else:
                print("All sides are not scanned. Check other windows to find which side needs to be scanned.")
                print("Left to scan:", 6 - len(set(check_state)))
                text_lines.append("All sides are not scanned")
        elif is_mouse_inside_button_mix(x, y):
            secuencia_mezcla = mix()
            print(secuencia_mezcla + ' ')
            text_lines.append(secuencia_mezcla)
            operation = secuencia_mezcla.split(' ')
            process(operation)
            secuencia_mezcla_ser = '0 ' + secuencia_mezcla + ' '
            ser.write(secuencia_mezcla_ser.encode('ascii'))
        elif is_mouse_inside_button_scan(x, y):
            p = 1
        elif is_mouse_inside_button_quit(x, y):
            cv2.destroyAllWindows()
            ser.close()
            quit()

        if event == cv2.EVENT_LBUTTONDOWN:
            for i, point in enumerate(points):
                if np.linalg.norm(np.array(point) - np.array([x, y])) < 10:  # Si el clic está cerca de un punto
                    dragging = True
                    selected_point = i
                    break

        elif event == cv2.EVENT_MOUSEMOVE:
            if dragging and selected_point is not None:
                points[selected_point] = [x, y]

        elif event == cv2.EVENT_LBUTTONUP:
            dragging = False
            selected_point = None


def giro_doble(total_str):
    total_lst = total_str.split()
    direction_lst = list(map(lambda x: x[0], total_str.split()))
    opuestos = {
        "F": "B",
        "B": "F",
        "U": "D",
        "D": "U",
        "L": "R",
        "R": "L"
    }
    result_str = ""
    i = 0
    while i < len(total_lst):
        result_str += total_lst[i]
        if i <= len(total_lst) - 2 and direction_lst[i] == opuestos.get(direction_lst[i+1]):
            result_str += total_lst[i+1]
            i += 1
        result_str += " "
        i += 1
    return result_str


def nothing(x):
    pass

if __name__ == '__main__':

    preview = np.full((700, 830, 3), (50, 50, 50), np.uint8)
    text_lines = []



    while True:
        hsvF = []
        hsvU = []
        hsvR = []
        current_stateF = []
        current_stateU = []
        current_stateR = []
        # cap.set(3, 1000)
        ret, img = cap.read()
        resized_img = cv2.resize(img, [600, 500])
        img_copy = img.copy()
        img_copy_resized = cv2.resize(img_copy, [600, 500])
        draw_points(img_copy_resized, points.astype(int))
        transformed_img = apply_perspective_transform(resized_img, points)  # Aplicar la transformación en tiempo real
        # Mostrar ambas imágenes
        imgStack1 = np.hstack([transformed_img[0], transformed_img[1], transformed_img[2]])
        imgStack = np.vstack([img_copy_resized, imgStack1])
        frame = cv2.cvtColor(imgStack, cv2.COLOR_BGR2HSV)
        mask = np.zeros(frame.shape, dtype=np.uint8)

        draw_stickers(imgStack, stickers, 'caraF', 30)
        draw_stickers(imgStack, stickers, 'caraR', 30)
        draw_stickers(imgStack, stickers, 'caraU', 30)
        draw_stickers(imgStack, stickers, 'currentF', 40)
        draw_stickers(imgStack, stickers, 'currentU', 40)
        draw_stickers(imgStack, stickers, 'currentR', 40)
        draw_preview_stickers(preview, stickers)
        fill_stickers(preview, stickers, state)
        texton_preview_stickers(preview, stickers)



        for i in range(9):
            hsvF.append(frame[stickers['caraF'][i][1] + 10][stickers['caraF'][i][0] + 10])
            hsvU.append(frame[stickers['caraU'][i][1] + 10][stickers['caraU'][i][0] + 10])
            hsvR.append(frame[stickers['caraR'][i][1] + 10][stickers['caraR'][i][0] + 10])
        a = 0

        for x, y in stickers['currentF']:
            color_nameF = color_detect(hsvF[a][0], hsvF[a][1], hsvF[a][2])
            cv2.rectangle(imgStack, (x, y), (x + 40, y + 40), color[color_nameF], -1)
            a += 1
            current_stateF.append(color_nameF)
        a = 0

        for x, y in stickers['currentU']:
            color_nameU = color_detect(hsvU[a][0], hsvU[a][1], hsvU[a][2])
            cv2.rectangle(imgStack, (x, y), (x + 40, y + 40), color[color_nameU], -1)
            a += 1
            current_stateU.append(color_nameU)
        a = 0

        for x, y in stickers['currentR']:
            color_nameR = color_detect(hsvR[a][0], hsvR[a][1], hsvR[a][2])
            cv2.rectangle(imgStack, (x, y), (x + 40, y + 40), color[color_nameR], -1)
            a += 1
            current_stateR.append(color_nameR)
        a = 0

        combined_img = np.hstack((imgStack, preview))
        draw_button_solve(combined_img, 'Solve')
        draw_button_mix(combined_img, 'Mix')
        draw_button_quit(combined_img, "Quit")
        draw_button_scan(combined_img, "Scan")

        #Para  mostrar los mivimientos en pantalla:
        max_lines = 1  # Número máximo de líneas a mostrar
        for i, line in enumerate(text_lines[-max_lines:]):  # Mostrar las últimas líneas
            y_position = 480 + i * 35
            words = line.split(' ')  # Dividir la línea en palabras
            current_line = ''
            for word in words:
                if cv2.getTextSize(current_line + word, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 1)[0][0] > 800 - 400:
                    # Si agregar la palabra supera el ancho disponible, inicia una nueva línea
                    cv2.putText(combined_img, current_line, (970, y_position), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                                (255, 255, 255), 1, cv2.LINE_AA)
                    current_line = word + ' '
                    y_position += 35
                else:
                    current_line += word + ' '

            # Agrega la última línea (o la única línea si no se produjo ningún salto)
            cv2.putText(combined_img, current_line, (970, y_position), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255),
                        1, cv2.LINE_AA)

        cv2.namedWindow('Rubik\'s cube solver', cv2.WINDOW_NORMAL)  # Ventana ajustable
        #cv2.setWindowProperty('Rubik\'s cube solver', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('Rubik\'s cube solver', combined_img)
        cv2.setMouseCallback('Rubik\'s cube solver', on_mouse_event)

        #Instrucciones con el teclado
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
        elif k == ord('p'):
            p = 1
        elif p == 1:
            state['front'] = current_stateF
            state['up'] = current_stateU
            state['right'] = current_stateR
            state['front'][4] = 'green'
            state['up'][4] = 'white'
            state['right'][4] = 'red'
            state['back'][4] = 'blue'
            state['left'][4] = 'orange'
            state['down'][4] = 'yellow'
            check_state = ['f', 'b', 'r', 'l', 'u', 'd']

            print('R2L2 ')
            ser.write('R2L2 '.encode('ascii'))
            time.sleep(0.5)
            p = 2
        elif p == 2:
            state['back'][0], state['back'][3], state['back'][6] = current_stateF[8], current_stateF[5], current_stateF[2]
            state['back'][5], state['back'][8] = current_stateF[3], current_stateF[0]
            state['down'][3], state['down'][6] = current_stateU[3], current_stateU[6]
            state['down'][2], state['down'][5], state['down'][8] = current_stateU[2], current_stateU[5], current_stateU[8]
            state['right'][8] = current_stateR[0]
            print('R2L2 ')
            ser.write('R2L2 '.encode('ascii'))
            time.sleep(0.5)
            print('F2B2 ')
            ser.write('F2B2 '.encode('ascii'))
            time.sleep(0.5)
            p = 3
        elif p == 3:
            state['left'][3], state['left'][6] = current_stateR[5], current_stateR[2]
            state['left'][2], state['left'][5], state['left'][8] = current_stateR[6], current_stateR[3], current_stateR[0]
            state['down'][0], state['down'][1] = current_stateU[8], current_stateU[7]
            state['down'][7] = current_stateU[1]
            state['front'][6] = current_stateF[2]
            print('F2B2 ')
            ser.write('F2B2 '.encode('ascii'))
            time.sleep(0.5)
            print('U2D2 ')
            ser.write('U2D2 '.encode('ascii'))
            time.sleep(0.5)
            p = 4
        elif p == 4:
            state['back'][1], state['back'][2] = current_stateF[1], current_stateF[2]
            state['back'][7] = current_stateF[7]
            state['left'][0], state['left'][1] = current_stateR[0], current_stateR[1]
            state['left'][7] = current_stateR[7]
            state['up'][0] = current_stateU[8]
            print('U2D2 ')
            ser.write('U2D2 '.encode('ascii'))
            p = 0
        elif k == ord('u'):
            state['up'] = current_stateU
            check_state.append('u')
        elif k == ord('r'):
            check_state.append('r')
            state['right'] = current_stateR
        elif k == ord('l'):
            check_state.append('l')
            state['left'] = current_stateF
        elif k == ord('d'):
            check_state.append('d')
            state['down'] = current_stateF
        elif k == ord('f'):
            check_state.append('f')
            state['front'] = current_stateF
        elif k == ord('b'):
            check_state.append('b')
            state['back'] = current_stateF
        elif k == ord('s'):
            state = solved_state
            check_state = ['f', 'b', 'r', 'l', 'u', 'd']
        elif k == ord('m') : #Al pulsar 'm' se crea una secuencia, se imprime y se cambia el estado del cubo con process()
            secuencia_mezcla = mix()
            text_lines.append(secuencia_mezcla)
            operation = secuencia_mezcla.split(' ')
            process(operation)
            secuencia_mezcla_ser = '0 ' + secuencia_mezcla + ' '
            print(secuencia_mezcla_ser)
            ser.write(secuencia_mezcla_ser.encode('ascii'))
        elif k == ord('\r'): #Al pulsar enter resuelve el cubo, se imprime y se cambia el estado del cubo
            if len(set(check_state)) == 6:
                try:
                    solved = solve(state)
                    if solved:
                        operation = solved.split(' ')
                        process(operation)
                        # text_lines.append(solved)
                except:
                    print(
                        "error in side detection ,you may do not follow sequence or some color not detected well.Try again")
                    text_lines.append("Error in side detection")
            else:
                print("all side are not scanned check other window for finding which left to be scanned?")
                print("left to scan:", 6 - len(set(check_state)))
                text_lines.append("All sides are not scanned")
    cv2.destroyAllWindows()
    ser.close()

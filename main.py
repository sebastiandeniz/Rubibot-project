import cv2
import numpy as np
import kociemba as Cube
import colorama
import textwrap
import serial
import time
import random

ser = serial.Serial("COM7", 9600, timeout=1)
time.sleep(2)

GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
RED = colorama.Fore.RED
MAGENTA = colorama.Fore.MAGENTA
colorama.init()

state = {
    'up': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', ],
    'right': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', ],
    'front': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', ],
    'down': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', ],
    'left': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', ],
    'back': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', ]
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
    'main': [
        [100, 350], [200, 350], [300, 350],
        [100, 450], [200, 450], [300, 450],
        [100, 550], [200, 550], [300, 550]
    ],
    'current': [
        [115, 110], [183, 110], [251, 110],
        [115, 180], [183, 180], [251, 180],
        [115, 250], [183, 250], [251, 250]
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

cap = cv2.VideoCapture(0)


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
    print(giro_doble(sol))
    ser.write(sol_doblegiro.encode('ascii'))
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
    if h > 170 and s > 100:
        return 'red'
    elif h < 16 and h > 5 and s > 70:
        return 'orange'
    elif h <= 38 and h > 17 and s > 5:
        return 'yellow'
    elif h >= 50 and h <= 85 and s > 36:
        return 'green'
    elif h > 80 and h <= 140 and s > 60:
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


button_x1, button_y1, button_width1, button_height1 = 800, 150, 150, 70
button_x2, button_y2, button_width2, button_height2 = 1000, 150, 150, 70
button_x3, button_y3, button_width3, button_height3 = 1070, 600, 80, 30


def draw_button_solve(img, text):
        cv2.rectangle(img, (button_x1, button_y1), (button_x1 + button_width1, button_y1 + button_height1), (0, 250, 0), -1)
        cv2.putText(img, text, (button_x1 + 32, button_y1 + 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)


def draw_button_mix(img, text):
        cv2.rectangle(img, (button_x2, button_y2), (button_x2 + button_width2, button_y2 + button_height2), (20, 225, 225), -1)
        cv2.putText(img, text, (button_x2 + 47, button_y2 + 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)


def draw_button_quit(img, text):
    cv2.rectangle(img, (button_x3, button_y3), (button_x3 + button_width3, button_y3 + button_height3), (0, 0, 250), -1)
    cv2.putText(img, text, (button_x3 + 18, button_y3 + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2,
                cv2.LINE_AA)


def is_mouse_inside_button_solve(x, y):
    return button_x1 <= x <= button_x1 + button_width1 and button_y1 <= y <= button_y1 + button_height1


def is_mouse_inside_button_mix(x, y):
    return button_x2 <= x <= button_x2 + button_width2 and button_y2 <= y <= button_y2 + button_height2


def is_mouse_inside_button_quit(x, y):
    return button_x2 <= x <= button_x3 + button_width3 and button_y3 <= y <= button_y3 + button_height3


def on_mouse_event(event, x, y, flags, param):
    global text_lines
    if event == cv2.EVENT_LBUTTONDOWN:
        if is_mouse_inside_button_solve(x, y):
            if len(set(check_state)) == 6:
                try:
                    solved = solve(state)
                    if solved:
                        operation = solved.split(' ')
                        process(operation)
                        text_lines.append(solved)
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
            secuencia_mezcla_ser = secuencia_mezcla + ' '
            ser.write(secuencia_mezcla_ser.encode('ascii'))
        elif is_mouse_inside_button_quit(x, y):
            cv2.destroyAllWindows()
            ser.close()
            quit()


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


if __name__ == '__main__':

    preview = np.zeros((700, 830, 3), np.uint8)
    text_lines = []

    while True:
        hsv = []
        current_state = []
        ret, img = cap.read()
        cropped_img = img[0:480, 98:382]
        resized_img = cv2.resize(cropped_img, (415, 700))
        frame = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)
        mask = np.zeros(frame.shape, dtype=np.uint8)

        draw_stickers(resized_img, stickers, 'main', 30)
        draw_stickers(resized_img, stickers, 'current', 60)
        draw_preview_stickers(preview, stickers)
        fill_stickers(preview, stickers, state)
        texton_preview_stickers(preview, stickers)

        for i in range(9):
            hsv.append(frame[stickers['main'][i][1] + 10][stickers['main'][i][0] + 10])

        a = 0
        for x, y in stickers['current']:
            color_name = color_detect(hsv[a][0], hsv[a][1], hsv[a][2])
            cv2.rectangle(resized_img, (x, y), (x + 60, y + 60), color[color_name], -1)
            a += 1
            current_state.append(color_name)

        combined_img = np.hstack((resized_img, preview))
        draw_button_solve(combined_img, 'Solve')
        draw_button_mix(combined_img, 'Mix')
        draw_button_quit(combined_img, "Quit")

        #Para  mostrar los mivimientos en pantalla:
        max_lines = 1  # Número máximo de líneas a mostrar
        for i, line in enumerate(text_lines[-max_lines:]):  # Mostrar las últimas líneas
            y_position = 480 + i * 35
            words = line.split(' ')  # Dividir la línea en palabras
            current_line = ''
            for word in words:
                if cv2.getTextSize(current_line + word, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 1)[0][0] > 800 - 400:
                    # Si agregar la palabra supera el ancho disponible, inicia una nueva línea
                    cv2.putText(combined_img, current_line, (770, y_position), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                                (255, 255, 255), 1, cv2.LINE_AA)
                    current_line = word + ' '
                    y_position += 35
                else:
                    current_line += word + ' '

            # Agrega la última línea (o la única línea si no se produjo ningún salto)
            cv2.putText(combined_img, current_line, (770, y_position), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255),
                        1, cv2.LINE_AA)

        cv2.namedWindow('Rubik\'s cube solver', cv2.WINDOW_NORMAL)  # Ventana ajustable
        cv2.setWindowProperty('Rubik\'s cube solver', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('Rubik\'s cube solver', combined_img)
        cv2.setMouseCallback('Rubik\'s cube solver', on_mouse_event)

        #Instrucciones con el teclado
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
        elif k == ord('u'):
            state['up'] = current_state
            check_state.append('u')
        elif k == ord('r'):
            check_state.append('r')
            state['right'] = current_state
        elif k == ord('l'):
            check_state.append('l')
            state['left'] = current_state
        elif k == ord('d'):
            check_state.append('d')
            state['down'] = current_state
        elif k == ord('f'):
            check_state.append('f')
            state['front'] = current_state
        elif k == ord('b'):
            check_state.append('b')
            state['back'] = current_state
        elif k == ord('s'):
            state = solved_state
            check_state = ['f', 'b', 'r', 'l', 'u', 'd']
        elif k == ord('m') : #Al pulsar 'm' se crea una secuencia, se imprime y se cambia el estado del cubo con process()
            secuencia_mezcla = mix()
            text_lines.append(secuencia_mezcla)
            operation = secuencia_mezcla.split(' ')
            process(operation)
            secuencia_mezcla_ser = secuencia_mezcla + ' '
            ser.write(secuencia_mezcla_ser.encode('ascii'))
        elif k == ord('\r'): #Al pusar enter resuelve el cubo, se imprime y se cambia el estado del cubo
            if len(set(check_state)) == 6:
                try:
                    solved = solve(state)
                    if solved:
                        operation = solved.split(' ')
                        process(operation)
                        text_lines.append(solved)
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

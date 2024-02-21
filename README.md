# Rubikaso
polla culo

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

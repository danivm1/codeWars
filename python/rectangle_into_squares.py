# https://www.codewars.com/kata/55466989aeecab5aac00003e/

def sq_in_rect(lng, wdth):
    if lng == wdth: return None

    rect = [lng, wdth]
    lst = []

    while rect[0] and rect[1]:
        if rect[0] < rect[1]:
            rect[1] -= rect[0]
            lst.append(rect[0])
        else:
            rect[0] -= rect[1]
            lst.append(rect[1])

    return lst

print(sq_in_rect(9, 5))
import math
# import numpy as np
# from numpy import matrix
import PySimpleGUI as sg


def degreeToRaydians(x):
    return (x*math.pi)/180


TimesOk = 0
angleList = [0, 0]
DisplayText = 'enter starting angle'
layout = [
    [sg.Text('enter starting angle', size=(40, 1), key='-Directions-')],
    [sg.Input(key='-Input-')],
    [sg.Button('Ok'), sg.Button('Quit'), sg.Button('Reset')],
    [sg.Text(size=(40, 1), key='-output1-')],
    [sg.Text(size=(40, 1), key='-output2-')]]
window = sg.Window("Calculate", layout)
while True:
    event, values = window.read()
    if event == 'Ok':
        angleList[TimesOk] = values['-Input-']
        TimesOk += 1
        DisplayText = 'enter angle that transformation should result in'
        window['-Directions-'].update(DisplayText)
        window['-Input-'].update('')
        for i in range(int(TimesOk-1)):
            TimesOk = 0
            DisplayText = 'enter starting angle'
            window['-Directions-'].update(DisplayText)
            startRaydian = degreeToRaydians(int(angleList[0]))
            finalRaydian = degreeToRaydians(int(angleList[1]))
            # convert raydians to vectors by taking their sines and cosines
            startVector = [math.cos(startRaydian), math.sin(startRaydian)]
            finalVector = [math.cos(finalRaydian), math.sin(finalRaydian)]
            # start vector * matrix x = final vector. solve for matrix
            # find the scalars that when multiplied by the basis vectors, distort them in a
            # way that would turn startVector into finalVector
            ScalarX = finalVector[0]/startVector[0]
            ScalarY = finalVector[1]/startVector[1]
            # now assemble the matrix. scalarX goes in the top left slot, and scalarY goes
            # in the Bottom right. the other two slots are 0's, as they make up the
            # matrix's null space
            topLine = '[ ' + str(ScalarX) + ', 0 ]'
            bottomLine = '[ 0, ' + str(ScalarY) + ' ]'
            # format and print the matrix
            window['-output1-'].update(topLine)
            window['-output2-'].update(bottomLine)
    if event == 'Reset':
        TimesOk = 0
        angleList = [0, 0]
        DisplayText = 'enter starting angle'
        window['-Directions-'].update(DisplayText)
        window['-Input-'].update('')
        window['-output1-'].update('')
        window['-output2-'].update('')
    if event == 'Quit' or event == sg.WIN_CLOSED:
        break
window.close()

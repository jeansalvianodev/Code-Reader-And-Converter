import cv2
import qrcode
from barcode import Code128
from barcode import EAN13
from barcode.writer import ImageWriter
import PySimpleGUI as sg
from pyzbar.pyzbar import decode
import os
from pathlib import Path


class Codes:

    def __init__(self, code):
        self.__code = code       

    def get_code(self):
        image = cv2.imread(self.__code)
        barcodes = decode(image)
        # Cycle detected barcodes
        for barcode in barcodes:
            # The location of the bounding box from which the barcode is extracted
            # Draw the bounding box of the barcode in the image
            (x, y, w, h) = barcode.rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            crop_img = image[y:y+h, x:x+w]
            cv2.imwrite('RCI.png', crop_img)
        # The barcode data is a byte object, so if we want to print it on the output image
        # To draw it, you need to convert it into a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        # Draw the barcode data and barcode type on the image
        text = f"{barcodeData} ({barcodeType})"
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
        0.5, (0, 0, 255), 2)

        code_type = None

        if barcodeType == 'QRCODE':
            code_type = 'Barcode'
        else:
            code_type = 'QR Code'
        
        all_datas = {'code_types': code_type, 'code_data': barcodeData, 'org_codetype': barcodeType}

        return all_datas
    
    def convert_code(self):
        code = self.get_code()
        if code['code_types'] == 'Barcode':
            if len(code['code_data']) <= 13: 
                my_code = EAN13(code['code_data'], writer=ImageWriter())
            else:
                my_code = Code128(code['code_data'], writer=ImageWriter())
            my_code.save("Barcode")
        else:
            img = qrcode.make(code['code_data'])
            img.save(f'QRCode.png')


def create_layout():
    sg.theme('Reddit')

    def get_infos():
        layout = [
            [sg.Image(r'logo.png')],
            [sg.Text('Choose the image with the code: ')],
            [sg.Text('Before opening, rename your image (remove any type of accent) to avoid errors.')],
            [sg.Input(key='-INPUT-'),
            sg.FileBrowse(button_text="Open")],
            [sg.Button('Next')],
        ]

        return sg.Window('Code Reader', layout, finalize=True)
    
    def show_options():
        right_click_menu = ['', ['Copy']]
        code_datas = read_code.get_code()
        layout = [
            [sg.Image('RCI.png', size=(300, 300))],
            [sg.InputText(code_datas['code_data'], use_readonly_for_disable=True, disabled=True, key='-IN-', size=(50), right_click_menu=right_click_menu)],
            [sg.Text(f'Do you want to convert the code to {code_datas["code_types"]}?\nConversion to bar code with more than 13 digits will be of type Code128, if less, they will have type EAN13.')],
            [sg.Checkbox('Convert', key='confirm')],
            [sg.Button('Continue'), sg.Button('Back')]
        ]

        return sg.Window('Code Reader', layout, finalize=True)

    window1, window2 = get_infos(), None
    MLINE_KEY = '-IN-'

    while True:
        window, event, values = sg.read_all_windows()
        if window == window1 and event == sg.WINDOW_CLOSED:
            break
        elif window == window2 and event == sg.WINDOW_CLOSED:
            break
        if window == window1 and event == 'Next':
            code_image = values['-INPUT-']
            read_code = Codes(code_image)
            if Path(code_image).is_file():
                try:
                    window2 = show_options()
                    os.remove('RCI.png')
                except:
                    sg.popup_error('Image error!', 'Invalid filename or no code found in the image!')
                    continue
                window1.hide()
        if window == window2:
            mline:sg.Multiline = window2[MLINE_KEY]
            if event == 'Copy':
                try:
                    text = mline.Widget.selection_get()
                    window.TKroot.clipboard_clear()
                    window.TKroot.clipboard_append(text)
                except:
                    print('Nothing selected!')
        if window == window2 and event == 'Continue':
            if values['confirm']:
                try:
                    read_code.convert_code()
                except:
                    sg.popup_error('Erro', 'Error converting code, check and try again.')
                    os.remove('RCI.png')
                    continue
                os.remove('RCI.png')
                sg.popup_annoying('Concluded!', 'Your code has been converted successfully! Check the Code Reader folder')
                continue
        if window == window2 and event == 'Back':
            window2.hide()
            window1 = get_infos()       
                

create_layout()

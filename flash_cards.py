from tkinter import *
from fpdf import FPDF
from pandas import read_csv
from numpy import copy, flip
import math
import configparser

# VARIABLES
config = configparser.ConfigParser()
config.read('config.ini')

input_name = config['general']['input_name']
output_name = config['general']['output_name']
csv_separator = config['general']['csv_separator']
borders = config['general']['flash_borders']
if borders == 'False':
    borders = False
elif borders == 'True':
    borders = True
else:
    borders = True
    print('flash_borders set to True (flash_borders value in config was not valid)')

font_file = config['font']['font_file']
font_size = int(config['font']['font_size'])
uppercase = config['font']['uppercase']

# 3 flashcard in row variables
width_3 = 70
# size_8 = 37.12  # is implemented in 4 row flash
size_7 = 42.42
size_6 = 49.5

# 4 flashcard in row variables
width_4 = 52.5
size_8 = 37.12
size_9 = 33
size_10 = 29.7

# borders = True
width = width_3
height = size_6


# READ DATA
data = read_csv(f'{input_name}.csv', header=None, sep=csv_separator)

words_lang_1 = data.iloc[:, 0].to_numpy()
words_lang_2 = data.iloc[:, 1].to_numpy()


def backend():
    ncards = rows * columns
    pages = math.ceil(data.shape[0] / ncards)
    print('Number of pages: ', pages * 2)

    resized_words_lang_1 = copy(words_lang_1)
    resized_words_lang_1.resize((pages, rows, columns))

    resized_words_lang_2 = copy(words_lang_2)
    resized_words_lang_2.resize((pages, rows, columns))

    resized_words_lang_2 = flip(resized_words_lang_2, axis=2)

    #$$$

    pdf = FPDF()
    pdf.add_font('MyFont', '', f'{font_file}.ttf', uni=True)
    flash_font = pdf.set_font('MyFont', '', font_size)


    for page in range(pages):

      # language 1 add page

      pdf.add_page()
        # left: float, top: float, right: float = 0
      pdf.set_auto_page_break(False, margin=0.0)
      flash_font
      pdf.set_margins(0, 0, 0)
      for row in range(rows):
        for col in range(columns):
          if resized_words_lang_1[page, row, col] == 0:
            pdf.cell(width, height, '', 0, 0, 'C')
          else:
            pdf.cell(width, height, str(resized_words_lang_1[page, row, col]), borders, 0, 'C')
        pdf.ln()

      # language 2 add page

      pdf.add_page()
      pdf.set_margins(0, 0, 0)  # left: float, top: float, right: float = 0
      pdf.set_auto_page_break(False, margin=0.0)
      flash_font

      for row in range(rows):
        for col in range(columns):
          if resized_words_lang_2[page, row, col] == 0:
            pdf.cell(width, height, '', 0, 0, 'C')
          else:
            pdf.cell(width, height, str(resized_words_lang_2[page, row, col]), borders, 0, 'C')
        pdf.ln()

    pdf.output(f'{output_name}.pdf', 'F')

# INIT APP WINDOW
root = Tk()
root.title('Flash card generator')
dis_width = 650
dis_height = 600
margin = 25
app = Canvas(root, width=dis_width, height=dis_height, bg='gray')
app.pack()

font1 = Label(root, text='Choose Size of the FlashCards', bg='gray', font=('helvetica', 15, 'bold'))
app.create_window(dis_width / 2, 20, window=font1, anchor='n')


# BUTTONS FUNCTIONS
def f_flash1():
    global width, height, columns, rows
    width = width_4
    height = size_10
    columns = 4
    rows = 10
    change_all_buttons(1)


def f_flash2():
    global width, height, columns, rows
    width = width_4
    height = size_9
    columns = 4
    rows = 9
    change_all_buttons(2)


def f_flash3():
    global width, height, columns, rows
    width = width_4
    height = size_8
    columns = 4
    rows = 8
    change_all_buttons(3)


def f_flash4():
    global width, height, columns, rows
    width = width_3
    height = size_8
    columns = 3
    rows = 8
    change_all_buttons(4)


def f_flash5():
    global width, height, columns, rows
    width = width_3
    height = size_7
    columns = 3
    rows = 7
    change_all_buttons(5)


def f_flash6():
    global width, height, columns, rows
    width = width_3
    height = size_6
    columns = 3
    rows = 6
    change_all_buttons(6)


def change_all_buttons(active):
    buttons = [flash1, flash2, flash3, flash4, flash5, flash6]
    for i in range(6):
        if active - 1 == i:
            buttons[i]['bg'] = '#a7e8bf'
            buttons[i]['state'] = DISABLED
        else:
            buttons[i]['bg'] = '#bababa'
            buttons[i]['state'] = NORMAL
    generate['bg'] = '#bababa'
    generate['text'] = 'Generate cards'
    generate['state'] = NORMAL


flash1 = Button(root, text=f'40 flash cards\n{width_4} x {size_10}', bg='#bababa', height=4, width=35, command=f_flash1)
app.create_window(margin, 420, window=flash1, anchor='nw')

flash2 = Button(root, text=f'36 flash cards\n{width_4} x {size_9}', bg='#bababa', height=5, width=35, command=f_flash2)
app.create_window(margin, 265, window=flash2, anchor='nw')

flash3 = Button(root, text=f'32 flash cards\n{width_4} x {size_8}', bg='#bababa', height=6, width=35, command=f_flash3)
app.create_window(margin, 90, window=flash3, anchor='nw')

flash4 = Button(root, text=f'24 flash cards\n{width_3} x {size_8}', bg='#bababa', height=6, width=42, command=f_flash4)
app.create_window(dis_width - margin, 420, window=flash4, anchor='ne')

flash5 = Button(root, text=f'21 flash cards\n{width_3} x {size_7}', bg='#bababa', height=8, width=42, command=f_flash5)
app.create_window(dis_width - margin, 265, window=flash5, anchor='ne')

flash6 = Button(root, text=f'18 flash cards\n{width_3} x {size_6}', bg='#bababa', height=10, width=42, command=f_flash6)
app.create_window(dis_width - margin, 90, window=flash6, anchor='ne')


# GENERATE BUTTON
def PDF_generate():
    generate['bg'] = '#a7e8bf'
    generate['text'] = 'Flash Cards generated !'
    generate['state'] = DISABLED
    backend()


generate = Button(root, text='Generate cards', bg='#bababa', state=DISABLED, height=1, width=30, command=PDF_generate)
app.create_window(350, 590, window=generate, anchor='s')

# MAIN LOOP
root.mainloop()
# FlashCards
FlashCard generator for learning a foreign language.
This app generates FlashCards for learning vocabulary in a foreign language. It generates a PDF file in A4 format in which words in language_1 are put on even pages, and words in language_2 are placed on the odd pages. **This PDF must be double-sided printed!** To correct work this app needs two extra files: spreadsheet in .csv format (with comma separator), font file in .ttf format. The font file is responsible for font on flashcards (thanks to this you can use a font with Chinese or Greek letters to learn those languages).

**To propper work this app needs:**
- **flash_card.py** or **flash_card.exe** file
- **data.csv** file with vocabulary (with 2 columns i.e. in 1'st column Polish words, in 2'nd column English words)(**name of this file can be changed in config**)
- **font.ttf** file with a font which you want on your flashcards
- **config.ini** file with configuration 

Notes: 
- Example font.ttf and data.csv are included in the project
- flash_card.exe is in archive (.rar) with the same name

Config.ini description:
```bat
[general]
input_type      type: csv
input_name      name of file without extension
output_name     name of file without extension because file has allways PDF extension
csv_separator   separator in csv file: , or ;
flash_borders   Boolean value: True, False

[font]
font_file       font file name without extension (.ttf)
font_size       flashcard font_size
uppercase       uppercase words on flashcards, boolean value: True, False (NOT IMPLEMENTED YET)
```

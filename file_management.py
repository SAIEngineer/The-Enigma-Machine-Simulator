from string import ascii_uppercase
from exceptions import (
    NoAsciiDetected,
    WrongFileName,
    WrongNumberOfLines,
    UndefinedFileName,
    FileNotFound,
    NoTextToProcess,
    InvalidRotorQuantity
)
import json

'''IS THIS OPTIMAl???'''
def check_if_ascii(letter):  # checks if input is in ascii uppercases
    '''
    Input must be UPPERCASE alphabet character
    '''
    if letter in ascii_uppercase:
        return True
    else:
        return False

'''
.txt file operations
'''

def read_txt_file(input_file):
    '''
    This function receives path to .txt file that later returns as string
    '''
    try:
        with open(input_file, "r") as file:  # open file
            lines = file.readlines()  # file's lines
            # if any line from file is an empty line, release
            if any(len(line.strip()) == 0 for line in lines):
                raise NoTextToProcess('No text was inserted')
            else:
                if int(len(lines)) == 1:  # if there is only one line in file
                    data = []
                    for line in lines:
                        for letter in line:
                            if check_if_ascii(letter):
                                data.append(letter)
                            else:
                                raise NoAsciiDetected('No ascii characters were inserted')
                    text = ''.join(data)
                    return text # return text
                else:
                    raise WrongNumberOfLines('Files does not contain one line. Format it or choose a different one')
    except FileNotFoundError:
        raise FileNotFound('File was not found')

def save_txt_file(text):
    '''
    This function receives text that is later appended to the created .txt file
    > User chooses name of the file, and program adds .txt extension to it
    > Allowed characters used to name a file are numbers and letters from range a-z
    > If there is already a .txt file  with that name, program will overwrite this file
    '''

    '''
    User enters name of the file that will be created.
    Later that name is checked for unallowable characters
    '''
    name_of_the_file = input('\nGive your file a name. Extension will be added automatically : ')
    if name_of_the_file:  # if name was inserted
        # Create file
        create_file_txt(name_of_the_file, text)
        '''
        Proper message is displayed
        '''
        print(f'\nFile {name_of_the_file}.txt was created in the main directory')

    else:
        raise UndefinedFileName('No name was inserted')


def create_file_txt(name_of_the_file, text):
    for letter in name_of_the_file:  # iterate through every letter
        # letter is checked for characters from ascii alphabet
        # letter is inserted to function as formatted for uppercase character to fit condition in this function
        if check_if_ascii(letter.upper()) or letter.isdigit():  # if letter mets assumpions continue
            continue
        else:
            raise WrongFileName('File name assumpions were not met')
    # If no exception has been raised continue
    '''
    File is created
    '''
    with open(f"{name_of_the_file}.txt", "w") as file:
        file.write(text)


'''
.json file operations
'''

def save_json_file(settings):
    '''
    This function saves all the initial settings of the enigma
    machine to the json file
    '''

    name_of_the_file = input('\nGive your file a name. Extension will be added automatically : ')
    if name_of_the_file:  # if name was inserted

        # Create file
        create_file_json(name_of_the_file, settings)
        '''
        Proper message is displayed
        '''
        print(f'\n{name_of_the_file}.json was created in the main directory')
    else:
        raise UndefinedFileName('No name was inserted')

def create_file_json(name_of_the_file, settings):
    for letter in name_of_the_file:  # iterate through every letter
        # letter is checked for characters from ascii alphabet
        # letter is inserted to function as formatted for uppercase character to fit condition in this function
        if check_if_ascii(letter.upper()) or letter.isdigit():  # if letter mets assumpions continue
            continue
        else:
            raise WrongFileName('File name assumpions were not met')
    # If no exception has been raised continue
    '''
    File is created
    '''
    with open(f'{name_of_the_file}.json', 'w') as filehandle:
        json.dump(settings, filehandle)

def read_json_file(path):
    '''
    This function receives path to .json file that later returns settings.
    Program assumes that this file contains data in way defined in program
    '''
    try:
        with open(path, "r") as filehandle:  # open file
            data = json.load(filehandle)
            list_of_rotors = data['rotors']
            steckenbrett = data['steckenbrett']
            reflector = data['reflector']
            return list_of_rotors, steckenbrett, reflector
    except FileNotFoundError:
        raise FileNotFound('File was not found')

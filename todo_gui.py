'''
GUI version of Todo list app
'''

import argparse
from pathlib import Path
import sys

import FreeSimpleGUI as sg

import logging_setting as lg
import todo2


def main():
    lg.logger_app.info(f'Version: {sg.__version__}')
    
    label = sg.Text('Todo Entry')
    input_box = sg.InputText(tooltip='Enter a Todo')
    button_add = sg.Button('Add')
    main_win = sg.Window('Todo List App',[[label], [input_box, button_add]])

    main_win.read()
    lg.logger_app.debug('Exiting...')
    main_win.close()



if __name__ == '__main__':
    parser = argparse.ArgumentParser('Todo App')
    lg.parse_logging_argument(parser)

    args = parser.parse_args()
    # Get the program name without the ".py" extension
    program_name = Path(sys.argv[0]).stem
    # Setup logger
    lg.setup_logger(program_name, args.loglevel)
    main()
# Objects for program
import os
from argparse import Namespace
from dataclasses import dataclass

@dataclass
class Test:
    input:  str
    output: str
    def __init__(self, input_content, output_content):
        self.input  = input_content
        self.output = output_content

@dataclass
class Prog:
    file_path: str
    test_path: str

    def __init__(self, prog_args: Namespace):
        self.file_path      = os.path.abspath(
            os.path.normpath(prog_args.file[0])
        )
        self.test_path     = os.path.abspath(
            os.path.normpath(prog_args.test_file[0])
        )
    def get_test(self):
        with open(self.test_path, 'r', encoding='utf-8') as test_file:
            test_content    = test_file.read()
            test_content    = test_content.splitlines()
        input_index_start   = test_content.index('Entradas')
        input_index_end     = test_content.index('Salida')
        output_index_start  = input_index_end
        output_index_end    = output_index_start + test_content[output_index_start + 2:].index('```')
        input_content       = test_content[input_index_start  + 2 : input_index_end - 1]
        output_content      = test_content[output_index_start + 2 : output_index_end + 2]

        return Test(input_content, output_content)

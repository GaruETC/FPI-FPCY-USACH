# Objects for program
import os
from argparse import Namespace
from dataclasses import dataclass

@dataclass
class Test:
    input:  str
    output: str

@dataclass
class Prog:
    file_path: str
    test_path: str
    test_content: list[Test] | None
    def __init__(self, prog_args: Namespace):
        self.file_path      = os.path.abspath(
            os.path.normpath(prog_args.file[0])
        )
        self.test_path     = os.path.abspath(
            os.path.normpath(prog_args.test_file[0])
        )

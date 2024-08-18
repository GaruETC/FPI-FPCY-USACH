from utils import cli
import os, sys, subprocess

args = cli.get_args()

prog_dir_path       = os.path.abspath(
    os.path.normpath(args.dir[0])
)
prog_file_path      = os.path.join(
    prog_dir_path, os.path.normpath(args.file[0])
)
prog_test_path      = os.path.join(
        prog_dir_path, os.path.normpath(args.test_file[0])
)

# Test getter
prog_test_content = []
with open(prog_test_path, 'r') as prog_test_file:
    prog_test_content = prog_test_file.read()
    prog_test_content = prog_test_content.splitlines()

prog_tests          = []
prog_test_input     = []
prog_test_output    = []
prog_test_data      = []

if prog_test_content[0] != '###ENTRADA###':
    print('[!] Archivo de Test invalido, comprueba que existan casos de Entrada y Salida')
    sys.exit(1)

for line in prog_test_content[1:]:
    if line == '###ENTRADA###':
        prog_test_output    =  prog_test_data
        prog_test_data      = [] 
        prog_tests.append([prog_test_input, prog_test_output])
    elif line == '###SALIDA###':
        prog_test_input     = prog_test_data
        prog_test_data      = [] 
    else:
        prog_test_data.append(line)

# Runner
for test in prog_tests:
    prog_command = [sys.executable, prog_file_path]
    prog_test_time = 5
    prog_process = subprocess.Popen(
        prog_command,
        stdin   = subprocess.PIPE,
        stdout  = subprocess.PIPE,
        stderr  = subprocess.PIPE,
        text    = True,
        cwd     = os.path.dirname(prog_file_path)
    )
    prog_stdout, prog_stderr = prog_process.communicate(input='\n'.join(test[0]), timeout=prog_test_time)
    prog_exit_code= prog_process.returncode
    if prog_stderr:
        print('Error: ', prog_stderr)
    elif prog_stdout[:-1] == '\n'.join(test[1]):
        print("Test Correcto")
    else:
        print("Test Incorrecto")
        print(prog_stdout)
        print('\n'.join(test[1]))
    print('-'*30)

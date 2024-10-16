from utils import cli
import os, sys, subprocess

prog_info = cli.get_args()

# Getter
test = prog_info.get_test()

# Runner
prog_command = [sys.executable, prog_info.script_file.path]
prog_test_time = 5
prog_process = subprocess.Popen(
    prog_command,
    stdin   = subprocess.PIPE,
    stdout  = subprocess.PIPE,
    stderr  = subprocess.PIPE,
    text    = True,
    cwd     = os.path.dirname(prog_info.script_file.path)
)
prog_input  = '\n'.join(test.input)
prog_output  = '\n'.join(test.output)
prog_stdout, prog_stderr = prog_process.communicate(input=prog_input, timeout=prog_test_time)
prog_exit_code= prog_process.returncode


print(f'{prog_info.script_file.name} - {prog_info.test_file.name}')
if prog_stderr:
    print('Error: ', prog_stderr)
elif prog_stdout[:-1] == prog_output:
    print("[✓] Test Correcto")
else:
    print("[X] Test Incorrecto")
    print(f'- Entrada del Programa: \n"""\n{prog_input}\n"""')
    print(f'- Salida del Programa:\n"""\n{prog_stdout}"""')
    print(f'- Salida Esperada \n"""\n{prog_output}\n"""')
    print("\n\n")

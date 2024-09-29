# Instance for manage cli interface

import argparse

def get_args():
    parser = argparse.ArgumentParser(
        prog='revisador',
        description='Verificar la funcionalidad de un programa de python a partir de un archivo de tests con parametros de entrada y salida definidos',
        epilog='https://github.com/Cristobal-Quezada-N/FPI-FPCY-USACH'
    )
    parser.add_argument(
        '-f',
        '--file',
        metavar='FILE.py',
        required=True,
        type = str,
        nargs= 1,
        help = 'ruta del archivo al cual se le realizan tests funcionales'
    )
    parser.add_argument(
        '-t',
        '--tests-file',
        metavar='FILE.md',
        required=True,
        type = str,
        nargs= 1,
        help = 'ruta del archivo con los parametros de entrada y salida esperados'
    )

    args = parser.parse_args()
    return args

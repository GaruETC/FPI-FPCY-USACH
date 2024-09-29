import argparse

def get_args():
    parser = argparse.ArgumentParser(
        prog='Test_Funcionales',
        description='Ejecutar tests sobre un programa de python a partir de un archivo .txt con los parametros deseados.',
        epilog='https://github.com/Cristobal-Quezada-N/FPI-FPCY-USACH'
    )
    parser.add_argument(
        '-d',
        '--dir',
        metavar='DIR-PROYECT',
        required=True,
        type = str,
        nargs= 1,
        help = 'ruta del directorio del proyecto.'
    )
    parser.add_argument(
        '-f',
        '--file',
        metavar='FILE.py',
        required=True,
        type = str,
        nargs= 1,
        help = 'ruta relativa del archivo dentro de DIR-PROYECT al cual se le realizan tests funcionales.'
    )
    parser.add_argument(
        '-t',
        '--test-file',
        metavar='FILE.txt',
        required=True,
        type = str,
        nargs= 1,
        help = 'ruta relativa del archivo dentro de DIR-PROYECT con los resultados de entrada y salida esperados.'
    )

    args = parser.parse_args()
    return args

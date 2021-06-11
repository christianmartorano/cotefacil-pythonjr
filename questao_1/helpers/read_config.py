# -*- coding: utf-8 -*-
import os


def capture_params(file):
    params = {}
    for line in file.readlines():
        arg = line.split('=')[-1].rstrip()
        if arg == '':
            return None
        params[line.split('=')[0]] = arg

    print(f'>>>Parâmetros atualizados {params}')
    file.close()

    return params


def read():
    file_path = '{0}{1}config{1}config.ini'.format(os.getcwd(), os.sep)

    try:
        file = open(file_path, 'r')
        params = capture_params(file)
        if None in params:
            raise ValueError('>>>Parâmetro não pode estar em branco')
    except IOError:
        print(f">>>Arquivo => {file_path} não encontrado!")
        return False, None
    except ValueError:
        return False, None

    return True, params

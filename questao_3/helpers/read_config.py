import os


def capture_params(file):
    params = {}
    for line in file.readlines():
        params[line.split('=>')[0]] = line.split('=>')[-1].rstrip()
    print(f">>> Parâmetros atualizados {params}")

    return params


def read():
    file_path = '{0}{1}config{1}config.ini'.format(os.getcwd(), os.sep)

    try:
        file = open(file_path, 'r')
        params = capture_params(file)
    except IOError:
        print(f">>> Arquivo => {file_path} não encontrado!")
        return False, None
    finally:
        file.close()

    return True, params

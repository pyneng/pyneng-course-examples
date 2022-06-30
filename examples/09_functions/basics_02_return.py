from pprint import pprint



def clean_cfg(cfg_filename):
    """
    Функция читает файл с конфигурацией cfg_filename, удаляет из него строки с !
    и возвращает список строк
    """
    result = []
    with open(cfg_filename) as f:
        for line in f:
            if not line.startswith("!"):
                result.append(line.strip())
    return result


file1 = "configs/cfg1.txt"
line_list = clean_cfg(file1)
pprint(line_list)

file2 = "configs/cfg2.txt"
line_list2 = clean_cfg(file2)
pprint(line_list2)

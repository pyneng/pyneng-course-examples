# -*- coding: utf-8 -*-
"""
Задание 20.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt
и данных из файла data_files/for.yml.

"""
import os
from jinja2 import Environment, FileSystemLoader
import yaml


def get_env(templ_dir, **env_kwargs):
    env = Environment(
        loader=FileSystemLoader(templ_dir), **env_kwargs
    )
    return env

def get_standard_env(templ_dir):
    env = get_env(templ_dir, trim_blocks=True, lstrip_blocks=True)
    return env


def render_template(env, templ_file, data_dict):
    templ = env.get_template(templ_file)
    return templ.render(data_dict)


if __name__ == "__main__":
    data_file = "data_files/for.yml"
    template_file = "for.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)

    env = get_standard_env("templates")
    print(render_template(env, template_file, data1))
    print(render_template(env, template_file, data2))
    print(render_template(env, template_file, data3))

# -*- coding: utf-8 -*-
from pprint import pprint
import sys
import os

from jinja2 import Environment, FileSystemLoader
import yaml


# $ python basics_03_syntax.py templates/for.txt data_files/for.yml
template_dir, template_file = os.path.split(sys.argv[1])

vars_file = sys.argv[2]

env = Environment(
    loader=FileSystemLoader(template_dir),
    trim_blocks=True,
    lstrip_blocks=True,
)
template = env.get_template(template_file)

with open(vars_file) as f:
    vars_dict = yaml.safe_load(f)

print(template.render(vars_dict))

from jinja2 import Environment, FileSystemLoader, StrictUndefined

env = Environment(
    loader=FileSystemLoader("templates"),
    undefined=StrictUndefined,
    trim_blocks=True,
    lstrip_blocks=True
)
cfg_templ = env.get_template("whitespace.txt")

print(cfg_templ.render(vlans=[1, 2, 3]))

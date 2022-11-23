from jinja2 import Environment, FileSystemLoader, StrictUndefined

env = Environment(
    loader=FileSystemLoader("templates"),
    undefined=StrictUndefined,
)
cfg_templ = env.get_template("short_cfg_template.txt")

data = {
    "name": "R1",
    "id": 100,
    "ip": "10.1.1.1",
    "process_id": 244,
}
print(cfg_templ.render(name="R1", id=55, ip="10.1.1.1"))
# print(cfg_templ.render(data))

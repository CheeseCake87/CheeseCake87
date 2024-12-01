from jinja2 import Environment, FileSystemBytecodeCache, DictLoader

e = Environment(
    bytecode_cache=FileSystemBytecodeCache(),
    loader=DictLoader({'test': 'Test\n'}),
    keep_trailing_newline=True
)

template = e.get_template("test")
print(repr(template.render()))
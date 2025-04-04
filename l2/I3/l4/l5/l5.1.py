import keyword
name = input("Введите Имя: ")
is_valid = (
    name not in keyword.kwlist and
    not name[0].isdigit() and
    all(c.islower() or c.isdigit() or c == '_' for c in name) and
    not name.startswith('_') and
    not name.endswith('_') and
    '__' not in name
)
if name == "_":
    is_valid = True
print(is_valid)

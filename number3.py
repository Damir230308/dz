def thesaurus(*names):
    result = {}
    for name in names:
        key = name[0].capitalize()
        if key not in result:
            result[key] = []
        result[key].append(name)
    return result

print(thesaurus("Иван", "Мария", "Петр", "Илья"))

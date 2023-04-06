from chardet import detect

def encoding_convert():
    """Конвертация"""
    with open('test.txt', 'rb') as f_obj:
        content_bytes = f_obj.read()
    detected = detect(content_bytes)
    print(detected)
    encoding = detected['encoding']
    content_text = content_bytes.decode(encoding)
    with open('test.txt', 'w', encoding='utf-8') as f_obj:
        f_obj.write(content_text)

encoding_convert()
with open('test.txt', encoding='utf-8') as file:
    CONTENT = file.read()
print(CONTENT)

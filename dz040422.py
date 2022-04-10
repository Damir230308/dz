# task 1
import os
if os.path.isdir('my_project'):
    print('Папка уже существует и другие не будут созданы :(')
    print('Удалите директорию my_project и всё станет нормально :)')
    exit(1)

if not os.path.isdir('my_project'):
    os.mkdir('my_project')
    os.chdir('my_project')
    os.mkdir('settings')
    os.mkdir('main_app')
    os.mkdir('admin_app')
    os.mkdir('auth_app')

os.chdir('settings')
open('__init__.py', 'w')
open('dev.py', 'w')
open('prod.py', 'w')
os.chdir('..')

os.chdir('main_app')
open('__init__.py', 'w')
open('models.py', 'w')
open('views.py', 'w')
if not os.path.isdir('templates'):
    os.mkdir('templates')
    os.chdir('templates')
    if not os.path.isdir('main_app'):
        os.mkdir('main_app')
        os.chdir('main_app')
        open('base.html', 'w')
        open('index.html', 'w')
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')

os.chdir('auth_app')
open('__init__.py', 'w')
open('models.py', 'w')
open('views.py', 'w')
if not os.path.isdir('templates'):
    os.mkdir('templates')
    os.chdir('templates')
    if not os.path.isdir('auth_app'):
        os.mkdir('auth_app')
        os.chdir('auth_app')
        open('base.html', 'w')
        open('index.html', 'w')

# task 3


import shutil
my_dir = 'task3'  # save folder
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folder = r'my_project'  # search folder
files = []


for r, d, f in os.walk(folder):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))
for path in files:
    folder_new = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder_new):
        os.mkdir(folder_new)
    save_path = os.path.join(folder_new, os.path.basename(path))
    shutil.copy(path, save_path)

# task 4

files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)
max_size = max(files)

i = 1
out_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = 0

for file in files:
    out_dict[10 ** len(str(file))] += 1


print(out_dict)

import os

with open('assets/html/template.html', 'r') as file:
    template = file.readlines()
    for i in range(len(template)):
        if template[i].find('<div id="main">') != -1:
            break

for filename in os.listdir('assets/content'):
    with open(os.path.join('assets/content', filename), 'r') as file:
        contents = file.readlines()
    with open(filename, 'w+') as file:
        file.writelines(template[:i + 1])
        file.writelines(contents)
        file.writelines(template[i + 1:])
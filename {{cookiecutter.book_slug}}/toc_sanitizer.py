#!/usr/bin/env python3

from glob import glob

for file in glob('{{ cookiecutter.book_name }}/_build/html/*.html'):
    new_content = ''
    with open(file, 'r') as fr:
        for line in fr.readlines():
            if line.startswith('<div class="toc">'):
                old_values = line.split('#')
                new_line = old_values[0] + '#' + '#'.join([c[0].lower() + c[1:] for c in old_values[1:]])
                new_content += new_line
            else:
                new_content += line
        
    with open(file, 'w') as fw:
        fw.write(new_content)

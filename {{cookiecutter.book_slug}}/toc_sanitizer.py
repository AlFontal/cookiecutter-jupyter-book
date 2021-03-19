#!/usr/bin/env python3

from glob import glob

for file in glob('{{cookiecutter.book_slug}}/_build/html/*.html'):
    new_content = ''
    with open(file, 'r') as fr:
        ggplot_counter = 0
        for line in fr.readlines():
            if line.startswith('<div class="toc">'):
                old_values = line.split('#')
                new_line = old_values[0] + '#'
                links = [c.split('"') for c in old_values[1:]]
                new_links = []
                for l in links:
                    new_link = l[0].lower() + '"' + '"'.join(l[1:])
                    new_links.append(new_link)
                new_line += '#'.join(new_links)
                new_content += new_line
            # Very hacky way to remove ggplot output cells
            # TODO: handle this with a proper html parser like beautifulsoup
            elif 'ggplot: (' in line:
                ggplot_counter = 1
            elif ggplot_counter == 1:
                ggplot_counter += 1
            elif ggplot_counter == 2:
                ggplot_counter = 0
            elif line.startswith('<h1>Table of Contents<span class="tocSkip"></span></h1>'):
                pass
            else:
                new_content += line

    with open(file, 'w') as fw:
        fw.write(new_content)

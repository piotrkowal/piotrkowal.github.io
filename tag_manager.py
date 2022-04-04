#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import sys

def is_tags_line(file_content):
    tags_index_line = ['tags' in line for line in file_content]    
    
    return any(tags_index_line)

def get_end_header_line_index(file_content):
    tags_index_line = ['---' in line for line in file_content]
    end_index = tags_index_line.index(True, 1)

    print(end_index)
    return end_index

post_dir = '_posts/'
draft_dir = '_drafts/'
tag_dir = 'tag/'
books_dir = post_dir+'books/'

books_filenames = glob.glob(books_dir+'*md')
books_filenames = books_filenames+ glob.glob(draft_dir+'*md')

tag_constant = 'tags: książki'

for filename in books_filenames:    
    file_content = ''
    with open(filename, 'r') as f:
        file_content = f.read()

    file_lines = file_content.split('\n')
    
    tags_index_line = ['tags' in line for line in file_lines]    
    if not is_tags_line(file_content):
        index = get_end_header_line_index(file_content.split('\n'))
        for line in range(len(file_lines)):            
            if line == index:   
                file_lines.insert(index, tag_constant)
                print(file_lines[line])  
                print(file_lines[line+1])  
    print(file_lines)
    with open(filename, 'w') as f:
        f.writelines(line +'\n' for line in file_lines)

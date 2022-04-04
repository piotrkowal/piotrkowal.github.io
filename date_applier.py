#!/usr/bin/env python

'''
tag_generator.py
Copyright 2017 Long Qian
Contact: lqian8@jhu.edu
This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

import glob
import os
import sys
import subprocess

def is_file_postlike(file_path):
    original_name = os.path.basename(filename)
    return original_name.startswith('20')

def roll_back_post_filename(file_path):
    original_name = os.path.basename(filename)
    filename_without_date_list = original_name.split('-')[3:]
    filename_without_date = '-'.join(filename_without_date_list)
    path = os.path.dirname(filename)
    destination_filename =  path+ '/' + filename_without_date
    os.rename(file_path, destination_filename)
    print(destination_filename)

post_dir = '_posts/'
draft_dir = '_drafts/'
tag_dir = 'tag/'
books_dir = post_dir+'books/'

books_filenames = glob.glob(books_dir+'*md')
books_filenames = books_filenames+ glob.glob(draft_dir+'*md')

for filename in books_filenames:
    book_date_read = ''
    if len(sys.argv) > 1:
        roll_back_post_filename(filename) if sys.argv[1] == 'revert' else 0

    if is_file_postlike(filename):
        print('Post is already named with a date at start!')
        continue
    
    with open(filename, 'r') as f:
        file_content = f.read()
        file_lines = file_content.split('\n')
        has_date_read_index = ['date_read' in line for line in file_lines]    
        date_read_index = has_date_read_index.index(True)
        book_date_read_raw = file_lines[date_read_index].split('date_read:')[-1]
        book_date_read = book_date_read_raw.strip().replace('/','-')
    
    original_name = os.path.basename(filename)
    path = os.path.dirname(filename)
    destination_filename =  path+ '/' + book_date_read + '-' + original_name
    print("renamed: {}" .format(destination_filename))
    
    if sys.argv[1] == 'mv':
        process = subprocess.Popen(["git", 'mv', filename, destination_filename], stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print(output)
    # os.rename(filename, destination_filename)
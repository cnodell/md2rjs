#!/usr/bin/env python

import sys
import configparser
import os
import shutil

# Read config file

home_dir = os.path.expanduser("~")
conf_path = os.path.join(home_dir, ".config/md2rjs/md2rjs.conf")

config = configparser.ConfigParser(delimiters=('='))
config.read(conf_path)

if len(sys.argv) == 2:
    o_file_full = os.path.abspath(sys.argv[1])
    o_file_dir = os.path.dirname(o_file_full)
    o_file_name = os.path.basename(os.path.normpath(o_file_full))
    o_file_name_bare = os.path.splitext(o_file_name)[0]

    d_file_dir = os.path.join(o_file_dir + '/' + o_file_name_bare +
                              '_presentation' + '/')

    html_file_full = os.path.join(d_file_dir, o_file_name_bare + ".html")

    shutil.copytree(os.path.normpath(config['DEFAULT']['revealjs_path']),
                    os.path.join(d_file_dir, "reveal.js"))
    
    md_file = open(o_file_full, 'r')
    md_content = md_file.read()
    md_file.close()

    f = open(html_file_full, 'w')
    f.write(config['DEFAULT']['html_top'] + '\n\n' +
            md_content + '\n\n' +
            config['DEFAULT']['html_bottom'])
    f.close()
else:
    print("Usage: md2rjs <FILE>")

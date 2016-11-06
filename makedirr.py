#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--dirr", type=str, dest='dirr',
                    help="Name of the dirr")

parser.add_argument("-w", type=str, dest='wd',
                    help="Name of the dirr")

args = parser.parse_args()
directory = args.dirr
wd = args.wd

os.chdir(wd)

if not os.path.exists(directory):
    os.makedirs(directory)

    os.chdir(directory)

    index = open('index.php', 'w+')

    index.write("""<?php $title=' CHANGE ME '; include(__DIR__ . '/../template/header.php'); ?>
    <div id='flash'>
        <p id='text' class='red'>Hi this text should be replaced when page and DOM is loaded.</p>
    </div>
<?php $path=__DIR__; include(__DIR__ . '/../template/footer.php'); ?>
    """)

    main = open('main.js', 'w+')

    main.write("""$(document).ready(function(){});""")

    style = open('style.less', 'w+')

    style.write("""@import "../template/base";""")


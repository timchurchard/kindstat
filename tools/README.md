# tools

## Overview

Run `0_copy.py /path/to/Kindle` to copy reading data from your kindle.  Then `1_decode.py path_to_output` to see the data that has been collected.  If you are happy please `tar czfv testdata.tgz path_to_output` to create an archive and attach this to an issue on github or email it to 'tc at omg.lol'.


## 0_copy.py - Create a copy of non-books from Kindle ereader

This script copies the kindle extra files and fmcache to a new directory

usage: ./0_copy.py /path/to/Kindle /optional/output/path


## 1_decode.py - Check the copy of non-books

This script reads the directory produced by 0_copy.py and prints a human readable report

usage: ./1_decode.py /path/to/data

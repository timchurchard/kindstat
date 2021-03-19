#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import os
import shutil
import sys


KRDS_FILETYPES = ('azw3f', 'azw3r', 'yjf', 'yjr', 'mbs', 'mbp1', 'pdt', 'pds', 'tas', 'tal')


def process_dir(start_dir, out_dir):
    for dir_name, subdir_list, file_list in os.walk(start_dir):
        for fname in file_list:
            for ftype in KRDS_FILETYPES:
                if fname.endswith(f'.{ftype}'):
                    fpath = os.path.join(dir_name, fname)
                    outpath = os.path.join(out_dir, fname)
                    if not os.path.exists(outpath):
                        print(f'copying {fpath} -> {outpath}')
                        shutil.copy(fpath, outpath)

        for sdir in subdir_list:
            process_dir(os.path.join(dir_name, sdir), out_dir)


def get_dirs():
    if len(sys.argv) < 2:
        print('usage: ./0_copy.py /path/to/Kindle /optional/output/path')
        sys.exit(1)
    mount_dir = sys.argv[1]
    if not os.path.isdir(mount_dir):
        print(f'{mount_dir} not a directory?')
        sys.exit(1)
    fmcache = os.path.join(mount_dir, 'system/fmcache/fmcache.db')
    if not os.path.isfile(fmcache):
        print(f'{fmcache} file not found')
        sys.exit(1)

    out_dir = os.getenv('USER') + '_' + datetime.now().strftime('%Y%m%d_%H%M')
    if len(sys.argv) > 2:
        if not os.path.exists(sys.argv[2]):
            os.mkdir(sys.argv[2])
            out_dir = sys.argv[2]
        else:
            print(f'directory {sys.argv[2]} exists. will not overwrite.')
            sys.exit(1)

    # Copy the fmcache.db rather than building the path again
    outpath = os.path.join(out_dir, 'fmcache.db')
    print(f'copying {fmcache} -> {outpath}')
    shutil.copy(fmcache, outpath)

    return mount_dir, out_dir


if __name__ == '__main__':
    mount_dir, out_dir = get_dirs()
    process_dir(mount_dir, out_dir)
    print('Success')

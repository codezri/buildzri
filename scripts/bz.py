#!/bin/env python3

import os
import platform
import json
import glob

C = {}

BZ_CONFIG_FILE = 'buildzri.config.json'
BZ_OS = platform.system().lower()
BZ_ISLINUX = BZ_OS == 'linux'
BZ_ISDARWIN = BZ_OS == 'darwin'
BZ_ISWIN = BZ_OS == 'windows'

def get_arch():
    arch = platform.machine()
    if arch == 'x86_64':
        arch = 'x64'
    return arch

def get_os_shortname():
    osnames = {'linux': 'linux', 'windows': 'win', 'darwin': 'mac'}
    return osnames[BZ_OS]

def get_compiler():
    compilers = {'linux': 'g++', 'windows': 'cl', 'darwin': 'c++'}
    return compilers[BZ_OS] + ' '

def get_std():
    if 'std' not in C:
        return ''

    std_prefix = '--std'
    if BZ_ISWIN:
        std_prefix = '/std:'
    return '%s=%s ' % (std_prefix, C['std'])

def get_source_files():
    file_defs = ['*', BZ_OS]
    files = ''

    for file_def in file_defs:
        if file_def not in C['source']:
            continue
        for entry in C['source'][file_def]:
            glob_files = glob.glob(entry)
            if len(glob_files) > 0:
                files += ' '.join(glob_files) + ' '

    return files

def get_includes():
    if 'include' not in C:
        return ''

    inc_defs = ['*', BZ_OS]
    incs = ''
    inc_prefix = '-I'
    if BZ_ISWIN:
        inc_prefix = '/I'

    for inc_def in inc_defs:
        if inc_def not in C['include']:
            continue
        for entry in C['include'][inc_def]:
            incs += '%s %s ' % (inc_prefix, entry)

    return incs

def get_definitions():
    if 'definitions' not in C:
        return ''

    defs = ''
    def_prefix = '-D'
    if BZ_ISWIN:
        def_prefix = '/D'

    for entry in C['definitions']:
        defs += '%s%s ' % (def_prefix, entry)

    return defs

def get_target():
    if 'output' not in C:
        return ''

    out_prefix = '-o '
    if BZ_ISWIN:
        out_prefix = '/OUT:'
    out_file = C['output']

    out_file = out_file\
        .replace('${BZ_OS}', get_os_shortname()) \
        .replace('${BZ_ARCH}', get_arch())

    out_path = os.path.dirname(out_file)

    if out_path != '' and not os.path.isdir(out_path):
        os.makedirs(out_path, exist_ok = True)

    return '%s%s ' % (out_prefix, out_file)

def build_compiler_cmd():
    cmd = get_compiler()
    cmd += get_std()
    cmd += get_source_files()
    cmd += get_definitions()
    cmd += get_includes()
    cmd += get_target()
    return cmd

def compile(cmd):
    print('Compiling %s...' % C['name'])
    print('Running cmd: %s' % cmd)
    os.system(cmd)

def print_ascii_art():
    print('''
  ____        _ _     _ ______     _
 |  _ \      (_) |   | |___  /    (_)
 | |_) |_   _ _| | __| |  / / _ __ _
 |  _ <| | | | | |/ _` | / / | '__| |
 | |_) | |_| | | | (_| |/ /__| |  | |
 |____/ \__,_|_|_|\__,_/_____|_|  |_|

 BuildZri - A minimal build automation tool for C++

    ''')

if __name__ == '__main__':
    with open(BZ_CONFIG_FILE) as configFile:
        print_ascii_art()
        C = json.loads(configFile.read())
        cmd = build_compiler_cmd()
        compile(cmd)

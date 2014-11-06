#!/usr/bin/env python

""" Tutorial taken from http://eli.thegreenplace.net/2011/07/03/parsing-c-in-python-with-clang/
    scripts need to be able to find the clang.cindex which resides in
    '${llvm-repository-root}\tools\clang\bindings\python\clang' (you need to checkout llvm and clang
    add '${llvm-repository-root}\llvm\tools\clang\bindings\python\' to PYTHONPATH environment variable
    the binding must find the libclang library on Windows set the PATH environment variable to find
    libclang.dll on on Linux set the LD_LIBRARY_PATH environment library to find libclang.so
    the library should be found in '${llvm-build-directory}\bin\' or one of its subdirectories

    if there is a problem with the calling convention then change cdll.LoadLibrary to windll.LoadLibrary in cindex.py

    in some builds the DLL is called clang.dll in others it's libclang.dll

    if a error message like: 'clang.cindex.LibclangError: [Error 193] %1 ist keine zulaessige Win32-Anwendung. To
    provide a path to libclang use Config.set_library_path() or Config.set_library_file().'
    is shown then the word size (32bit/64bit) of the Python interpreter is not the same as of the [lib]clang.dll.
 """


import sys
import os


print sys.maxint

path_to_this_file = os.path.realpath(__file__)
path_to_this_directory = os.path.split(path_to_this_file)[0]
sys.path.append(path_to_this_directory + "/clang/")

import clang.cindex
LIB_FILE = "C:/Program Files (x86)/clang3.2/bin/clang.dll"
assert(os.path.isfile(LIB_FILE))
#clang.cindex.Config.set_library_file(LIB_FILE)


import findTyperefs

findTyperefs.main(['room.cpp', 'Person'])


import findFunctions

findFunctions.main(['room.cpp'])

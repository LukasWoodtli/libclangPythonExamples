#!/usr/bin/env python

""" Tutorial taken from http://eli.thegreenplace.net/2011/07/03/parsing-c-in-python-with-clang/
    scripts need to be able to find the clang.cindex which resides in 
    '${llvm-repository-root}\tools\clang\bindings\python\clang' (you need to checkout llvm and clang
    add '${llvm-repository-root}\llvm\tools\clang\bindings\python\' to PYTHONPATH environment variable
    the binding must find the libclang library on Windows set the PATH environment variable to find
    libclang.dll on on Linux set the LD_LIBRARY_PATH environment library to find libclang.so
    the library should be found in '${llvm-build-directory}\bin\' or one of its subdirectories
 """


import sys
import os

path_to_this_file = os.path.realpath(__file__)
path_to_this_directory = os.path.split(path_to_this_file)[0]
sys.path.append(path_to_this_directory + "/clang/")
import findTyperefs


findTyperefs.main(['room.cpp', 'Person'])


import findFunctions

findFunctions.main(['room.cpp'])

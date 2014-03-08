#!/usr/bin/env python3 

from sys import path
path.append('./../')
from yson import load, load_from_text

f = open('example.yson')
print(load(f))

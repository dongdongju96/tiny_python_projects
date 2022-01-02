#! C:\Users\user\anaconda3\envs\tiny_python_projects\python.exe
# Purpose: Say Hello

import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('name', help='Name to greet')
args =parser.parse_args()
print('Hello, ' + args.name + '!')
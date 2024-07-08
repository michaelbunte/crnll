'''
Copyright 2024

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the “Software”), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of 
the Software, and to permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER 
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import argparse
import subprocess
import os
import getch
import re


parser = argparse.ArgumentParser(
                    prog='Cornell Notes',
                    description='Description')

parser.add_argument("-f", "--file", required=True)
parser.add_argument("-q", "--questions")
args = parser.parse_args()

SPAS = {
    "shell": True,
    "capture_output": True,
    "text": True
}

notes_filename = args.file
questions_filename = args.questions if args.questions != None else "q_" + notes_filename

def peek_line(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line


def print_answer(num):
    with open(notes_filename, "r") as h:
        while True:
            input = h.readline()
            if len(re.findall("^\\d+", input)) == 1 and re.findall("^\\d+", input)[0] == str(num):
                print(input, end="")
                break
            if input == "":
                return

        while True:
            input = h.readline()
            if len(re.findall("^#+ ", input)) == 1:
                break
            if len(re.findall("^\\d+", input)) == 1:
                break
            print(input, end="")
            if input == "":
                return

def seek_forwards(f, seek_stack):
    f.seek(seek_stack[-1])
    os.system("clear")
    print()
    print(f.readline(), end="")
    print()

    while True:
        pos = f.tell()

        subprocess.run("touch eco.txt", **SPAS)
        g = open("eco.txt", "w")
        eco = f.readline()
        g.write(eco)
        g.close()
        if(int(subprocess.run("cat eco.txt | grep -E '^\d+\-?\d*\.' | wc -c | tr -d ' '", **SPAS).stdout) != 0):
            f.seek(pos)
            print(os.get_terminal_size()[0] * "=" + "\n")
            seek_stack.append(f.tell())
            break
        if eco == "":
            print(os.get_terminal_size()[0] * "=" + "\n")

            # check if EOF
            r = open(questions_filename, "r")
            r.seek(seek_stack[-1])
            linelen = len(r.readline())
            r.close()
            
            if linelen == 0:
                break
            seek_stack.append(f.tell())
            f.seek(pos)
            break
        print(eco, end="")
    subprocess.run("rm eco.txt", **SPAS)

    

def seek_backwards(f, seek_stack):
    len(seek_stack) > 1 and seek_stack.pop()
    len(seek_stack) > 1 and seek_stack.pop()
    seek_forwards(f, seek_stack)

def is_eof(f):
    pos = f.tell()
    a = f.readline()
    res = len(a) == 0
    f.seek(pos)
    return res

def find_answer(f, seek_stack):
    if len(seek_stack) <= 1:
        return
    
    l = open(questions_filename, "r")

    l.seek(seek_stack[-2])
    line = peek_line(l)
    l.close()

    if len(re.findall("^\\d+\\.", line)) == 1:
        print_answer(int(re.findall("^\\d+", line)[0]))
    elif len(re.findall("^\\d+\\-\\d+", line)) == 1:
        nums = list(map(lambda x: int(x), (re.findall("^\\d+\\-\\d+", line)[0]).split("-")))
        for i in range(nums[0], nums[1] + 1):
            print_answer(i)
    


with open(questions_filename, "r") as f:
    os.system("clear")
    print("You are reviewing: " + notes_filename)
    print()
    print("To navigate:")
    print("\t> or f \t\t- next card")
    print("\t< \t\t- prev card")
    print("\tm or space \t- show answer")
    print("\tq\t\t- quit")

    seek_stack = [f.tell()]

    is_showing_answer = False
    while True:
        f.seek(seek_stack[-1])
        char = getch.getch()
        if char == "." or char == "f":
            seek_forwards(f, seek_stack)
            is_showing_answer = False
        elif char == ",":
            seek_backwards(f, seek_stack)
            is_showing_answer = False
        elif (char == "m" or char == " ") and not is_showing_answer:
            find_answer(f, seek_stack)
            is_showing_answer = True
        elif (char == "q"):
            break
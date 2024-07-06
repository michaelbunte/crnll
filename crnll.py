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


def print_answer(num):
    with open(notes_filename, "r") as h:
        while True:
            input = h.readline()
            if len(re.findall("^\\d+", input)) == 1 and re.findall("^\\d+", input)[0] == str(num):
                print(input, end="")
                break
    if h.eof
        while True:
            input = h.readline()
            if len(re.findall("^#+ ", input)) == 1:
                break
            if len(re.findall("^\\d+", input)) == 1:
                break
            print(input, end="")

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
            print(os.get_terminal_size()[0] * "=")
            seek_stack.append(f.tell())
            break
        print(eco, end="")

    

def seek_backwards(f, seek_stack):
    len(seek_stack) > 1 and seek_stack.pop()
    len(seek_stack) > 1 and seek_stack.pop()
    print(len(seek_stack))

    seek_forwards(f, seek_stack)

with open(questions_filename, "r") as f:
    seek_stack = [f.tell()]

    while True:
        f.seek(seek_stack[-1])
        char = getch.getch()
        if char == "l":
            seek_forwards(f, seek_stack)
        if char == "j":
            seek_backwards(f, seek_stack)




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
            break
        print(eco, end="")

    

def seek_backwards(f, seek_stack):
    len(seek_stack) > 1 and seek_stack.pop()
    len(seek_stack) > 1 and seek_stack.pop()
    seek_forwards(f, seek_stack)

def find_answer(f, seek_stack):
    if len(seek_stack) <= 1:
        return
    l = open(questions_filename, "r")
    l.seek(seek_stack[-2])
    line = peek_line(l)
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
    print("\t. - next card")
    print("\tm - prev card")
    print("\t, - show answer")

    seek_stack = [f.tell()]

    while True:
        f.seek(seek_stack[-1])
        char = getch.getch()
        if char == ".":
            seek_forwards(f, seek_stack)
        elif char == "m":
            seek_backwards(f, seek_stack)
        elif char == ",":
            find_answer(f, seek_stack)
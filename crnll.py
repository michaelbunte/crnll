import argparse
import subprocess
import os


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

with open(questions_filename, "r") as f:
    while True:
        input("")
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
                break
            

            print(eco, end="")


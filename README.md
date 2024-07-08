# CRNLL
## About
`crnll` is a python script that allows users to view [Cornell-Style](https://lsc.cornell.edu/how-to-study/taking-notes/cornell-note-taking-system/)  notes as flashcards. 

This script is [kludged](https://en.wikipedia.org/wiki/Kludge) - if in the future I'd like to add additional features, I'll probably need to rewrite the codebase from scratch and take a more elegant approach to file seeking. 

## Installation
`crnll` only works on Unix-Like systems as it relies on command line utilities such as `grep`.

1. You'll need to have Python installed on your machine.
2. You'll also need to run `pip install getch` or `pip3 install getch`

## Running
To take notes that `crnll` understands, write your notes in a separate file from your questions. Questions and their corresponding notes should be numbered (see the syntax section).

Assuming your notes are held in a file `notes.py`, we can can run 

`python3 crnll.py -u notes.md`

Here, `crnll.py` assumes that your answers document comes in the form `q_notes.md`.

If your notes document does not come in this form, we can also run `crnll` with

`python3 crnll.py -u notes.md -q questionsfile.md`

## Syntax Expectations
### Notes Example:
```
1. This is a question

2. This is another question.
4. I skipped question three. That is okay.
5. This is a multiline question. 
That's okay.
6. This
* is another

* multiline question

## This is a header. This won't be included in the above question
7. One more question
```

### Questions example:

```
1. This is a question
4. I skipped questions 2 and 3. That's okay.
Multiline questions are okay as well.

5-7. Range questions are okay.
```

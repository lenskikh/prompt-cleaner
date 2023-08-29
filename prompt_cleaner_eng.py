import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
import re

root = ttk.Window("Prompt Cleaner")
tokens = {}
text3 = []

def cleaner():
    text = text_area.get("1.0", 'end')

    #clean
    if "(" or ")" in text:
        text =  re.sub(r'[()]', '', text)
    if ":" in text:
        text = re.sub(r':\d+\.\d+', '', text)
    if ":" in text:
        text = re.sub(r':\d+', '', text)
    if ":" in text:
        text = re.sub(r':\s*\d+\.\d+', '', text)
    if "BREAK" in text:
        text = text.replace("BREAK", "")
        
    text2 = text.split(",")
    text3 = []

    #remove whitespaces
    for word in text2:
        word = word.strip()
        word = word.lower()
        text3.append(word)

    #create unique 
    for token in text3:
        if "<lora" in token:
            pass
        else:
            tokens[token] = ""

    #clear text area
    text_area.delete('1.0', 'end')

    #insert text in text area
    for token in tokens:
        text_area.insert("end",token + ", ")

def clean_text_area():
    text_area.delete('1.0', 'end')
    tokens.clear()
    text3.clear()

def sorted_tokens():
    sorted_dict = dict(sorted(tokens.items()))
    text_area.delete('1.0', 'end')
    for token in sorted_dict:
        if token == "":
            pass
        else:
            text_area.insert("end",token + ", ")

def copy():
    root.clipboard_clear()
    root.clipboard_append(text_area.get("1.0", 'end'))

def paste():
    clean_text_area()
    paste_text = root.clipboard_get()
    text_area.insert("end", paste_text)

text_area = ScrolledText(root, height = 10, autohide=True)
text_area.pack(side=LEFT, fill=X, expand=YES, padx=5, pady=0)

#------ Buttons ---------
b3 = ttk.Button(root, text="Clear the text area", bootstyle="primary-outline", command = clean_text_area)
b3.pack(side=BOTTOM, fill=X, expand=NO, padx=5, pady=2)

copy_btn = ttk.Button(root, text="Copy", bootstyle="primary-outline", command = copy)
copy_btn.pack(side=BOTTOM, fill=X, expand=NO, padx=5, pady=2)

b2 = ttk.Button(root, text="The Sorting", bootstyle="primary-outline", command = sorted_tokens)
b2.pack(side=BOTTOM, fill=X, expand=NO, padx=5, pady=2)

b4 = ttk.Button(root, text="Delete Duplicates", bootstyle="primary-outline", command = cleaner)
b4.pack(side=BOTTOM, fill=X, expand=NO, padx=5, pady=2)

paste_btn = ttk.Button(root, text="Paste", bootstyle="primary-outline", command = paste)
paste_btn.pack(side=BOTTOM, fill=X, expand=NO, padx=5, pady=2)

root.mainloop()

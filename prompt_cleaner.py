import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
import re
import json

prefix = "eng-"

def load_lang(filename):
    with open(filename, encoding="UTF-8") as f:
        content = f.read()

    interface = json.loads(content)
    return interface

def switch_languages(prefix):
    b5.config(text=interface[prefix+"clean"])
    b4.config(text=interface[prefix+"copy"])
    b3.config(text=interface[prefix+"sorting"])
    b2.config(text=interface[prefix+"duplicates"])
    b1.config(text=interface[prefix+"paste"])

interface = load_lang("langs.json")

root = ttk.Window(interface[prefix+"title"])
text3 = []
tokens = {}
op2 = ttk.BooleanVar()


def cleaner():
    
    text = text_area.get("1.0", 'end')
    info = op2.get()

    #delete ()
    if "(" or ")" in text:
        text =  re.sub(r'[()]', '', text)
    #delete any weight like 1.3 and etc.
    if ":" in text:
        text = re.sub(r':\d+\.\d+', '', text)
    # weight 1 without digit after
    if ":" in text:
        text = re.sub(r':\d+', '', text)
    # with space symbol token: 1.3
    if ":" in text:
        text = re.sub(r':\s*\d+\.\d+', '', text)
    if ". " in text:
        text = re.sub(r'\. ', ', ', text)
    if ".," in text:
        text = re.sub(r'\.\,', ', ', text)     
    if ",." in text:
        text = re.sub(r'\,\.', ', ', text)            
    if ":" in text: 
        text = text.replace(":", "")
    if "+" in text: 
        text = text.replace("+", ",")
    if "!" in text: 
        text = text.replace("!", "")   
    if "?" in text: 
        text = text.replace("?", "")     
    if '"' in text: 
        text = text.replace('"', "")                            
    #if used regional prompter
    if "BREAK" in text:
        text = text.replace("BREAK", "")

    reconstruction(text) 


def reconstruction(text):

    tokens.clear()
    text2 = text.split(",")
    text3 = []

    #remove whitespaces
    for word in text2:
        word = word.strip()
        word = word.lower()
        text3.append(word)

    #create unique 
    for token in text3:
        #remove lora in prompt
        if "<lora" in token:
            pass
        else:
            #create unique
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
    cleaner()
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

#------ Translate buttons ---------

frame_top = ttk.Frame(root)
frame_top.pack(fill="both", expand=True, padx=5)

russian = ttk.Button(frame_top, text=interface["rus"], bootstyle="primary-outline", command = lambda: switch_languages("rus-"))
russian.pack(side=LEFT, expand=NO, padx=2, pady=2)

english = ttk.Button(frame_top, text=interface["eng"], bootstyle="primary-outline", command = lambda: switch_languages("eng-"))
english.pack(side=LEFT, expand=NO, padx=2, pady=2)

spanish = ttk.Button(frame_top, text=interface["spanish"], bootstyle="primary-outline", command = lambda: switch_languages("spanish-"))
spanish.pack(side=LEFT, expand=NO, padx=2, pady=2)

chinese = ttk.Button(frame_top, text=interface["chinese"], bootstyle="primary-outline", command = lambda: switch_languages("chinese-"))
chinese.pack(side=LEFT, expand=NO, padx=2, pady=2)

japanese = ttk.Button(frame_top, text=interface["japanese"], bootstyle="primary-outline", command = lambda: switch_languages("japanese-"))
japanese.pack(side=LEFT, expand=NO, padx=2, pady=2)

korean = ttk.Button(frame_top, text=interface["korean"], bootstyle="primary-outline", command = lambda: switch_languages("korean-"))
korean.pack(side=LEFT, expand=NO, padx=2, pady=2)

hebrew = ttk.Button(frame_top, text=interface["hebrew"], bootstyle="primary-outline", command = lambda: switch_languages("hebrew-"))
hebrew.pack(side=LEFT, expand=NO, padx=2, pady=2)

arabic = ttk.Button(frame_top, text=interface["arabic"], bootstyle="primary-outline", command = lambda: switch_languages("arabic-"))
arabic.pack(side=LEFT, expand=NO, padx=2, pady=2)


# Text arae
text_area = ScrolledText(root, wrap=WORD, height = 10, autohide=True)
text_area.pack(side=LEFT, fill=X, expand=YES, padx=5, pady=0)


#------ Buttons ---------

#clean text
b5 = ttk.Button(root, text=interface[prefix+"clean"], bootstyle="primary-outline", command = clean_text_area)
b5.pack(side=BOTTOM, fill=X, expand=NO, padx=5, pady=2)

#copy button
b4 = ttk.Button(root, text=interface[prefix+"copy"], bootstyle="primary-outline", command = copy)
b4.pack(side=BOTTOM, fill=X, expand=NO, padx=5, pady=2)

#sorted button
b3 = ttk.Button(root, text=interface[prefix+"sorting"], bootstyle="primary-outline", command = sorted_tokens)
b3.pack(side=BOTTOM, fill=X, expand=NO, padx=5, pady=2)

#clean button
b2 = ttk.Button(root, text=interface[prefix+"duplicates"], bootstyle="primary-outline", command = cleaner)
b2.pack(side=BOTTOM, fill=X, expand=NO, padx=5, pady=2)

#paste button
b1 = ttk.Button(root, text=interface[prefix+"paste"], bootstyle="primary-outline", command = paste)
b1.pack(side=BOTTOM, fill=X, expand=NO, padx=5, pady=2)

#op1 = ttk.Checkbutton(root, text='Scrolling', variable=op2)
#op1.pack(fill=X, pady=5)

root.mainloop()

from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))

entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNumber>>', lambda e: print('Odd Number'))

print(entry.event_info('<<OddNumber>>'))

entry.event_add('<<EvenNumber>>', '2', '4', '6', '8')
entry.bind('<<EvenNumber>>', lambda e: print('Even Number'))

entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')

# If you want to delete a virtual event
# entry.event_delete('<<OddNumber>>')

root.mainloop()

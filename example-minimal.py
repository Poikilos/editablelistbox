#!/usr/bin/env python3
'''
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
edited Aug 1, 2020 at 14:02
answered May 26, 2017 at 15:04
by David Duran
on <https://stackoverflow.com/a/44204790/4541104>

Requires:
- listboxeditable module (formerly ListboxEditable from same URL)

Changes by Poikilos:
## [unreleased] - 2022-08-04
### Changed

'''
from tkinter import *
# from tkinter.ttk import *
# ^ breaks `bg=` unless `from editablelistbox import *` cancels it out
from tkinter import ttk
# from editablelistbox import *
from editablelistbox import (
    ACTIVE_TAB_COLOR,
    INACTIVE_TAB_COLOR,
    LABEL_FONT,
    LABEL_SIZE,
    EditableListbox,
)

# ACTIVE_TAB_COLOR = "#CCCCCC"
# INACTIVE_TAB_COLOR = "#EBEBEB"
# LABEL_FONT = 'Calibri'
# LABEL_SIZE = 13

# Main window
root = Tk()

# *** Design *****
column_frame = Frame(root, bg=ACTIVE_TAB_COLOR)
name_label_frame = Frame(column_frame, bg='blue')
name_label = Label(name_label_frame, text="Header", bg='blue',
                   fg='white', font=(LABEL_FONT, LABEL_SIZE, 'bold'),
                   pady=2, padx=2, width=10)
listbox_name_frame = Frame(column_frame, bg='blue')
items = ['test1', 'test2', 'test3']
name_listbox = EditableListbox(listbox_name_frame, items)

# *** Packing ****
column_frame.pack(side=LEFT, fill=Y)
name_label_frame.pack(side=TOP, fill=X)
name_label.pack(side=LEFT, fill=X)
listbox_name_frame.pack(side=TOP, fill=X)
name_listbox.placeLabels()

root.mainloop()

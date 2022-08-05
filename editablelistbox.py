# Authors: see readme

from tkinter import *
from tkinter import ttk
# from tkinter.ttk import *  # automatically override tk where available
# ^ `from tkinter.ttk import *`  breaks the bg param
#   in the Frame constructor in the caller somehow.

ACTIVE_TAB_COLOR = "#CCCCCC"  # Color of the active tab
INACTIVE_TAB_COLOR = "#EBEBEB"  # Color of the no active tab

LABEL_FONT = 'Calibri'
LABEL_SIZE = 13


class EditableListbox(object):
    """
    This emulates listbox, but you can also edit a field.
    """
    # Constructor
    def __init__(self, frameMaster, items):
        '''
        Sequential arguments:
        frameMaster -- set master (tk.Tk() or any frame under it)
        items -- provide a list of strings.
        '''
        # *** Assign the first variables ***
        # The frame that contains the EditableListbox
        self.frameMaster = frameMaster
        # List of the initial items
        self.items = items
        # Number of initial rows at the moment
        self.numberRows = len(self.items)

        # *** Create the necessary labels ***
        index = 1
        for row in self.items:
            # Get the name of the label
            labelName = 'label' + str(index)
            # Create the variable
            thisLabel = Label(self.frameMaster, text=self.items[index-1],
                              bg=ACTIVE_TAB_COLOR, fg='black',
                              font=(LABEL_FONT, LABEL_SIZE), pady=2, padx=2,
                              width=10)
            setattr(self, labelName, thisLabel)

            # ** Bind actions
            # 1 left click - Change background
            getattr(self, labelName).bind('<Button-1>', lambda event,
                                          a=labelName: self.changeBackground(a))
            # Double click - Convert to entry
            getattr(self, labelName).bind(
                '<Double-1>',
                lambda event, a=index: self.changeToEntry(a)
            )
            # Move up and down
            getattr(self, labelName).bind("<Up>", lambda event,
                                          a=index: self.up(a))
            getattr(self, labelName).bind("<Down>", lambda event,
                                          a=index: self.down(a))

            # Increase the iterator
            index = index + 1

    def placeLabels(self):
        '''
        Go row by row placing each label.
        '''
        index = 1
        for row in self.items:
            labelName = 'label'+str(index)
            # Place the label
            getattr(self, labelName).grid(row=index-1, column=0)
            index += 1

    def changeBackground(self, labelNameSelected):
        '''
        This runs on single-click.
        '''
        # Ensure that all the remaining labels are deselected
        index = 1
        for row in self.items:
            # Get the name of the label
            labelName = 'label'+str(index)
            # Place the variable
            getattr(self, labelName).configure(bg=ACTIVE_TAB_COLOR)

            # Increase the iterator
            index = index + 1

        # Change the background of the corresponding label
        getattr(self, labelNameSelected).configure(bg=INACTIVE_TAB_COLOR)
        # Set the focus for future bindings (moves)
        getattr(self, labelNameSelected).focus_set()

    def up(self, index):
        '''
        This runs when the up button is pressed.
        '''
        if index == 1:  # Go to the last
            # Get the name of the label
            labelName = 'label' + str(self.numberRows)
        else:  # Normal
            # Get the name of the label
            labelName = 'label' + str(index-1)

        # Call the select
        self.changeBackground(labelName)

    def down(self, index):
        '''
        This runs when the down button is pressed.
        '''
        if index == self.numberRows:  # Go to the last
            # Get the name of the label
            labelName = 'label1'
        else:  # Normal
            # Get the name of the label
            labelName = 'label' + str(index+1)

        # Call the select
        self.changeBackground(labelName)

    def changeToEntry(self, index):
        '''
        This runs on double-click.
        '''
        # Variable of the current entry
        self.entryVar = StringVar()
        # Create the entry
        # entryName='entry'+str(index) # Name
        self.entryActive = ttk.Entry(self.frameMaster,
                                     font=(LABEL_FONT, LABEL_SIZE),
                                     textvariable=self.entryVar, width=10)
        # Place it on the correct grid position
        self.entryActive.grid(row=index-1, column=0)
        # Focus to the entry
        self.entryActive.focus_set()

        # Bind the action of focusOut
        self.entryActive.bind("<FocusOut>",
                              lambda event, a=index: self.saveEntryValue(a))

    def saveEntryValue(self, index):
        '''
        This runs when focus is lost.
        '''
        # Find the label to recover
        labelName = 'label'+str(index)
        # Remove the entry from the screen
        self.entryActive.grid_forget()
        # Place it again
        getattr(self, labelName).grid(row=index-1, column=0)
        # Change the name to the value of the entry
        getattr(self, labelName).configure(text=self.entryVar.get())

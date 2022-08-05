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
    This emulates listbox, but you can also edit a field. When an item
    (Label) is double-clicked, it transforms into an Entry. When it
    loses focus, its value is stored back to the label.
    """

    def __init__(self, parent, items):
        '''
        Sequential arguments:
        parent -- set master (tk.Tk() or any frame under it)
        items -- Provide a list of names. They must not contain spaces
            since they are used as member variable names (with "label"
            prepended).
        '''
        self.parent = parent
        # self.names = [self.rowToName(i) for i in range(len(items))]
        # self.items = items
        self.names = []
        self.rowCount = len(items)
        self.activeEntry = None
        self.activeRow = None

        for index in range(len(items)):
            row = index + 1
            value = items[index]
            labelName = self.rowToName(row)  # self.names[index]
            thisLabel = Label(self.parent, text=value,
                              bg=ACTIVE_TAB_COLOR, fg='black',
                              font=(LABEL_FONT, LABEL_SIZE), pady=2, padx=2,
                              width=10)
            setattr(self, labelName, thisLabel)
            self.names.append(labelName)

            # ** Bind actions
            # 1 left click - Change background
            getattr(self, labelName).bind(
                '<Button-1>',
                lambda event,a=labelName: self._onClick(a))
            # Double click - Convert to entry
            getattr(self, labelName).bind(
                '<Double-1>',
                lambda event,a=row: self._onDoubleClick(a)
            )
            # Move up and down
            getattr(self, labelName).bind("<Up>", lambda event,
                                          a=row: self._onUp(a))
            getattr(self, labelName).bind("<Down>", lambda event,
                                          a=row: self._onDown(a))

    def rowToName(self, row):
        return "label" + str(row)

    def gridAll(self):
        '''
        Place each row's Label on the parent grid.
        '''
        for index in range(len(self.names)):
            row = index + 1
            labelName = self.names[index]
            getattr(self, labelName).grid(row=row-1, column=0)
            # getattr(self, labelName).configure(text="")

    def _onClick(self, labelNameSelected):
        '''
        On single-click, change the background.
        '''
        # row = self.labelNameToRow(labelNameSelected)
        # self._stopEntry(row)
        self._select(labelNameSelected)
        # self._startEntry(row)

    def labelNameToRow(self, labelName):
        for index in range(len(self.names)):
            row = index + 1
            if self.rowToName(row) == labelName:
                return row
        return None

    def _select(self, labelNameSelected):
        # Ensure that all the remaining labels are deselected
        for index in range(len(self.names)):
            labelName = self.names[index]
            # Place the variable
            getattr(self, labelName).configure(bg=ACTIVE_TAB_COLOR)

        # Change the background of the corresponding label
        getattr(self, labelNameSelected).configure(bg=INACTIVE_TAB_COLOR)
        # Set the focus for future bindings (moves)
        getattr(self, labelNameSelected).focus_set()

    def _onUp(self, row):
        '''
        This runs when the up button is pressed.
        '''
        if row == 1:
            # Wrap around to the end.
            labelName = 'label' + str(self.rowCount)
        else:  # Normal
            labelName = 'label' + str(row-1)  # go to the previous one

        self._onClick(labelName)

    def _onDown(self, row):
        '''
        This runs when the down button is pressed.
        '''
        if row == self.rowCount:
            # Wrap around to the start.
            labelName = self.nameToIndex(1)
        else:
            labelName = self.nameToIndex(row+1)  # go to the next one

        self._select(labelName)

    def _onDoubleClick(self, row):
        # pass
        self._startEntry(row)

    def _startEntry(self, row):
        '''
        Change the Label to an entry.
        '''
        if row is None:
            raise ValueError("row is None.")

        self.entryVar = StringVar()

        labelName = self.rowToName(row)
        self.entryVar.set(getattr(self, labelName).cget("text"))

        # entryName='entry'+str(row)
        self.activeRow = row
        self.activeEntry = ttk.Entry(self.parent,
                                     font=(LABEL_FONT, LABEL_SIZE),
                                     textvariable=self.entryVar, width=10)
        self.activeEntry.grid(row=row-1, column=0)
        self.activeEntry.focus_set()

        self.activeEntry.bind("<FocusOut>",
                              lambda event, a=row: self._onLostFocus(a))

        self.activeEntry.bind("<Return>",
                              lambda event, a=row: self._onEnterPressed(a))

    def _onLostFocus(self, row):
        self._stopEntry(row)

    def _onEnterPressed(self, row):
        self._stopEntry(row)

    def _stopEntry(self, row):
        '''
        When focus is lost, replace the entry with the recovered label
        with the new value.

        Sequential arguments:
        row -- This is ignored now. The new and more reliable
            self.activeRow is now used.
        '''
        if self.activeEntry is None:
            return False
        labelName = self.rowToName(row)
        self.activeEntry.grid_forget()  # Remove the entry.
        getattr(self, labelName).grid(row=self.activeRow-1, column=0)
        # Store the entry value in the label:
        getattr(self, labelName).configure(text=self.entryVar.get())
        # self.activeEntry = None
        # self.activeRow = None
        # self.entryVar = None
        return True

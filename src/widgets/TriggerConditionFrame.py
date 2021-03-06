""" AggregatedTriggerFrame.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
"""

from functools import partial
from tkinter import ttk


class TriggerConditionFrame(object):
    """This class extends ttk.Frame to create a custom GUI widget"""

    def __init__(self, master, trigger, populating=False):
        self.condition = None
        if not populating:
            self.condition = trigger.add_tc()
        self.master = master
        self.trigger = trigger

        self.frame = ttk.Frame(master.inner)
        self.frame.pack(expand=True, fill="x")
        self.frame.grid_columnconfigure(0, weight=1)

        label = ttk.Label(self.frame, text=str("trigger" + "\t\t"))
        label.grid(row=0, column=0, sticky="ew", padx=(5, 0))

        self.master.tc_frame_list.append(self)

        edit_button = ttk.Button(self.frame, text="edit", width=3, command=partial(self.master.edit_trigger_condition, self))
        edit_button.grid(row=0, column=1)

        delete_button = ttk.Button(self.frame, text="X", width=0, command=partial(self.master.delete_trigger_condition, self))
        delete_button.grid(row=0, column=2)
    #end init


    def cleanup(self):
        """Remove this widget from the gui"""
        self.master.delete_trigger_condition(self)
    #end _cleanup
# end class TriggerConditionFrame

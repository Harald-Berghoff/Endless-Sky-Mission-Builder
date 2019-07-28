""" GUI.py
# Copyright (c) 2019 by Andrew Sneed
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

This handles the GUI for ESMB
"""

from ttkthemes import ThemedTk

from menuactions import *
from guiutils import *
from ScrollingCenterFrame import ScrollingCenterFrame
from AggregatedTriggerFrame import AggregatedTriggerFrame


class GUI(object):

    def __init__(self, debug_mode):
        print("Building GUI...")
        self.debugging = debug_mode

        self.missionList = []
        self.missionNameToObjectDict = {}
        self.missionNames = []

        if self.debugging:
            self.missionList             = [Mission("Debugging", default=True)]
            self.missionNameToObjectDict = {self.missionList[0].missionName: self.missionList[0]}
            self.missionNames.append(self.missionList[0].missionName)
        #end if

        # Build the application window
        self.gui = ThemedTk(theme="plastik")
        self.gui.title("ESMissionBuilder")
        self.gui.configure(bg="orange")

        # enable window resizing
        self.gui.columnconfigure(0, weight=1)
        self.gui.rowconfigure(0, weight=1)

        self.disabledEntryStyle = ttk.Style()
        self.disabledEntryStyle.configure('D.TEntry', background='#D3D3D3')
        self.disabledComboboxStyle = ttk.Style()
        self.disabledComboboxStyle.configure('D.TCombobox', background='#D3D3D3')

        self.ofWidth = None
        self.cfWidth = None
        self.mfWidth = None

        # Declare the frames
        self.optionFrame  = None
        self.centerFrame  = None
        self.missionFrame = None

        # declare optionFrame components
        self.missionComboBox = None
        self.activeMission   = None

        # declare centerFrame components
        self.displayNameComponent   = None
        self.descriptionComponent   = None
        self.blockedComponent       = None
        self.deadlineComponent      = None
        self.cargoComponent         = None
        self.passengersComponent    = None
        self.illegalComponent       = None
        self.stealthComponent       = None
        self.invisibleComponent     = None
        self.priorityLevelComponent = None
        self.whereShownComponent    = None
        self.repeatComponent        = None
        self.clearanceComponent     = None
        self.infiltratingComponent  = None
        self.waypointComponent      = None
        self.stopoverComponent      = None
        self.sourceComponent        = None
        self.destinationComponent   = None

        # Triggers
        self.triggersFrame = None
        self.activeTrigger = None

        # declare missionFrame components
        self.missionTextBox = None

        # Build the different parts of the main window
        #self.buildMenu(self.gui)
        self.build_main_view(self.gui)

        self.activeMission = None
        if self.debugging:
            self.activeMission = self.missionList[0]
        # Run the program
        self.gui.mainloop()
    #end init

    # This may be used later, after shortcuts are introduced
    '''
    def buildMenu(self, window):
        #TODO: IMPLEMENT THIS
        # creating a menu instance
        menu = Menu()
        window.config(menu=menu)

        # create the file object
        file = Menu(menu)
        edit = Menu(menu)

        # adds a command to the menu option, names it, and set the command to run
        file.add_command(label="New", command=lambda: newFile(self))
        file.add_command(label="Open", command=lambda: open_file(self))
        file.add_command(label="Save", command=lambda: save_file(self))
        file.add_command(label="Exit", command=exit)

        # added "File" to our menu
        menu.add_cascade(label="File", menu=file)

        # adds a command to the menu option, names it, and set the command to run
        edit.add_command(label="Undo", command=lambda: undoAction(self))

        # added "Edit" to our menu
        menu.add_cascade(label="Edit", menu=edit)
    #end buildMenu
    '''

    def build_main_view(self, window):
        option_frame  = ttk.Frame(window)
        center_frame  = ScrollingCenterFrame(self, window)
        mission_frame = ttk.Frame(window)

        self.optionFrame  = option_frame
        self.centerFrame  = center_frame
        self.missionFrame = mission_frame

        # set up each of the frames
        self.build_option_frame()
        self.build_center_frame()
        self.build_mission_frame()
    #end build_main_view


    ### BUILDING FRAMES ###


    def build_option_frame(self):
        print("Building optionFrame...", end="\t\t")
        self.optionFrame.grid(row=0, column=0, sticky="ns")

        of_title = ttk.Label(self.optionFrame, text="Mission")
        of_title.pack()

        # declare the combobox here, fill with missionNames
        self.missionComboBox = ttk.Combobox(self.optionFrame, state="readonly", values=self.missionNames)
        self.missionComboBox.bind("<<ComboboxSelected>>", self.mission_selected)
        self.missionComboBox.pack()

        if self.debugging:
            self.missionComboBox.current(0)

        # add function buttons
        new_mission_button = ttk.Button(self.optionFrame, text="New Mission", command=lambda: new_mission(self))
        new_mission_button.pack(fill='x')

        save_mission_file_button = ttk.Button(self.optionFrame, text="Save Mission File", command=lambda: save_file(self))
        save_mission_file_button.pack(fill='x')

        open_mission_file_button = ttk.Button(self.optionFrame, text="Open Mission File", command=lambda: open_file(self))
        open_mission_file_button.pack(fill='x')

        compile_mission_file_button = ttk.Button(self.optionFrame, text="Compile Mission", command=lambda: compile_mission(self))
        compile_mission_file_button.pack(fill='x')

        help_button = ttk.Button(self.optionFrame, text="Help", command=help_user)
        help_button.pack(fill='x')

        #TODO: Add functions to change missionName and delete mission. Also, update button grouping to reflect

        print("Done.")
    #end build_option_frame


    def build_center_frame(self):
        print("Building centerFrame...", end="\t\t")

        self.centerFrame.grid(row=0, column=1, sticky="ns")

        cf = self.centerFrame.inner

        # Display name
        self.displayNameComponent = build_component_frame(cf, "Mission Display Name", 1, 0, ["<text>"])
        self.displayNameComponent.grid(row=0, column=0, sticky="ew")

        # Description
        self.descriptionComponent = build_component_frame(cf, "Description", 1, 0, ["<description>"])
        self.descriptionComponent.grid(row=1, column=0, sticky="ew")

        # isBlocked
        self.blockedComponent = build_component_frame(cf, "Blocked", 1, 0, ["<message>"])
        self.blockedComponent.grid(row=2, column=0, sticky="ew")

        # Deadline
        self.deadlineComponent = build_component_frame(cf, "Deadline", 0, 2, ["[<days#>]", "[<multiplier#>]"])
        self.deadlineComponent.grid(row=3, column=0, sticky="ew")

        # Cargo
        self.cargoComponent = build_component_frame(cf, "Cargo", 2, 2, ["(random | <name>)", "<number#>", "[<number#>]", "[<probability#>]"])
        self.cargoComponent.grid(row=4, column=0, sticky="ew")

        # Passengers
        self.passengersComponent = build_component_frame(cf, "Passengers", 1, 2, ["<number#>", "[<number#>]", "[<probability#>]"])
        self.passengersComponent.grid(row=5, column=0, sticky="ew")

        # Illegal
        self.illegalComponent = build_component_frame(cf, "Illegal", 1, 1, ["<fine#>", "[<message>]"])
        self.illegalComponent.grid(row=6, column=0, sticky="ew")

        # Stealth
        self.stealthComponent = build_component_frame(cf, "Stealth", 0, 0, [])
        self.stealthComponent.grid(row=7, column=0, sticky="ew")

        # Invisible
        self.invisibleComponent = build_component_frame(cf, "Invisible", 0, 0, [])
        self.invisibleComponent.grid(row=8, column=0, sticky="ew")

        # priorityLevel
        self.priorityLevelComponent = build_combo_component_frame(cf, "Priority Level", ["Priority", "Minor"])
        self.priorityLevelComponent.grid(row=9, column=0, sticky="ew")

        # whereShown
        self.whereShownComponent = build_combo_component_frame(cf, "Where Shown", ["Job", "Landing", "Assisting", "Boarding"])
        self.whereShownComponent.grid(row=10, column=0, sticky="ew")

        # Repeat
        self.repeatComponent = build_component_frame(cf, "Repeat", 0, 1, ["[<times#>]"])
        self.repeatComponent.grid(row=11, column=0, sticky="ew")

        # Clearance
        self.clearanceComponent = build_component_frame(cf, "Clearance", 0, 1, ["[<message>]"])
        self.clearanceComponent.grid(row=12, column=0, sticky="ew")

        # Infiltrating
        self.infiltratingComponent = build_component_frame(cf, "Infiltrating", 0, 0, [])
        self.infiltratingComponent.grid(row=13, column=0, sticky="ew")

        # Waypoint
        self.waypointComponent = build_component_frame(cf, "Waypoint", 1, 0, ["[<system>]"])
        self.waypointComponent.grid(row=14, column=0, sticky="ew")

        # Stopover
        self.stopoverComponent = build_component_frame(cf, "Stopover", 1, 0, ["[<planet>]"])
        self.stopoverComponent.grid(row=15, column=0, sticky="ew")

        # Source
        self.sourceComponent = build_component_frame(cf, "Source", 1, 0, ["[<planet>]"])
        self.sourceComponent.grid(row=16, column=0, sticky="ew")

        # Destination
        self.destinationComponent = build_component_frame(cf, "Destination", 1, 0, ["[<planet>]"])
        self.destinationComponent.grid(row=17, column=0, sticky="ew")

        # triggers
        self.triggersFrame = AggregatedTriggerFrame(self, cf)
        self.triggersFrame.grid(row=18, column=0, sticky="ew")

        # add a blank label to pad the bottom of the frame
        bl1 = ttk.Label(cf, textvariable=" ")
        bl1.grid(row=19, column=0, sticky="ew")

        print("Done.")
    #end build_center_frame


    def build_mission_frame(self):
        print("Building missionFrame...", end="\t")

        #Display a default mission template on launch
        self.missionFrame.grid(row=0, column=2, sticky="nsew")
        mf_title = ttk.Label(self.missionFrame, text="Mission Text")
        mf_title.pack()

        # Populate the Text with a mission template
        self.missionTextBox = Text(self.missionFrame, wrap=WORD, height=50, width=100)
        self.missionTextBox.pack(expand=1, fill='both')
        welcome_message = "\n"
        welcome_message += "\t\t\tWelcome to Endless Sky Mission Builder!\n"
        welcome_message += "\n\t - Click \"New Mission\" to get started\n"
        welcome_message += "\n\t - Click \"Save Mission File\" to save all the missions to a text file\n"
        welcome_message += "\n\t - Click \"Open Mission File\" to open a mission file for editing\n"
        welcome_message += "\n\t - Click \"Compile Mission\" to save save the current mission\n"
        welcome_message += "\n\t - Click \"Help\" to be directed to the Mission Creation wiki\n"
        self.missionTextBox.insert(END, welcome_message)
        self.missionTextBox.config(state=DISABLED)

        print("Done.")
    #end build_mission_frame


    ### UPDATING FRAMES ###


    def update_option_frame(self):
        print("\nUpdating optionFrame...")

        ### Start updating combobox
        ml = self.missionList
        self.missionNames = []
        print("\tNew mission options:", end=" ")
        for m in ml:
            self.missionNames.append(m.missionName)
        print(self.missionNames)

        # update options in the combobox
        self.missionComboBox['values'] = self.missionNames
        self.missionComboBox.current(0)
        ### Finish updating combobox

        # update the other two frames to reflect the current mission
        self.update_center_frame()
        self.update_mission_frame()

        print("Done.")
    #end update_option_frame


    def update_center_frame(self):
        print("\nUpdating centerFrame...")

        components = self.activeMission.components

        # missionDisplayName
        self.displayNameComponent.reset()
        if components.missionDisplayName is not None:
            self.displayNameComponent.set(0, 0, components.missionDisplayName)

        # description
        self.descriptionComponent.reset()
        if components.description is not None:
            description = components.description
            self.descriptionComponent.set(0, 0, description)
        #end if

        # blocked
        self.blockedComponent.reset()
        if components.blocked is not None:
            self.blockedComponent.set(0, 0, components.blocked)

        # deadline
        self.deadlineComponent.reset()
        if components.deadline.isDeadline is True:
            self.deadlineComponent.set(0, None, "isDeadlineCheckbutton")
            if components.deadline.deadline[0] is not None:
                self.deadlineComponent.set(1, 0, components.deadline.deadline[0])
                if components.deadline.deadline[1] is not None:
                    self.deadlineComponent.set(2, 1, components.deadline.deadline[1])
            #end if
        #end if

        # cargo
        self.cargoComponent.reset()
        if components.cargo.isCargo is True:
            self.cargoComponent.set(0, 0, components.cargo.cargo[0])
            self.cargoComponent.set(0, 1, components.cargo.cargo[1])
            if components.cargo.cargo[2] is not None:
                self.cargoComponent.set(1, 2, components.cargo.cargo[2])
                if components.cargo.cargo[2] is not None:
                    self.cargoComponent.set(2, 3, components.cargo.cargo[3])
            #end if
        #end if

        # passengers
        self.passengersComponent.reset()
        if components.passengers.isPassengers is True:
            self.passengersComponent.set(0, 0, components.passengers.passengers[0])
            if components.passengers.passengers[1] is not None:
                self.passengersComponent.set(1, 1, components.passengers.passengers[1])
                if components.passengers.passengers[2] is not None:
                    self.passengersComponent.set(2, 2, components.passengers.passengers[2])
            #end if
        #end if

        # illegal
        self.illegalComponent.reset()
        if components.illegal.isIllegal is True:
            self.illegalComponent.set(0, 0, components.illegal.illegal[0])
            if components.illegal.illegal[1] is not None:
                self.illegalComponent.set(1, 1, components.illegal.illegal[1])
            # end if
        # end if

        # stealth
        self.stealthComponent.reset()
        if components.isStealth is True:
            self.stealthComponent.set(0, None, "stealthCheckbutton")

        # invisible
        self.invisibleComponent.reset()
        if components.isInvisible is True:
            self.invisibleComponent.set(0, None, "isInvisibleCheckbutton")

        # priorityLevel
        self.priorityLevelComponent.reset()
        if components.priorityLevel is not None:
            self.priorityLevelComponent.set(components.priorityLevel)

        # whereShown
        self.whereShownComponent.reset()
        if components.whereShown is not None:
            self.whereShownComponent.set(components.whereShown)

        # repeat
        self.repeatComponent.reset()
        if components.isRepeat is True:
            self.repeatComponent.set(0, None, "isRepeatCheckbutton")
            if components.repeat is not None:
                self.repeatComponent.set(1, 0, components.repeat)
        #end if

        # clearance
        self.clearanceComponent.reset()
        if components.clearance.isClearance is True:
            self.clearanceComponent.set(0, None, "isClearanceCheckbutton")
            if components.clearance.clearance is not None:
                self.clearanceComponent.set(1, 0, components.clearance.clearance)
        #end if

        # infiltrating
        self.infiltratingComponent.reset()
        if components.isInfiltrating is True:
            self.infiltratingComponent.set(0, None, "isInfiltratingCheckbutton")

        # waypoint
        self.waypointComponent.reset()
        if components.waypoint is not None:
            self.waypointComponent.set(0, 0, components.waypoint)


        # stopover
        self.stopoverComponent.reset()
        if components.stopover.isStopover is True:
            self.stopoverComponent.set(0, 0, components.stopover.stopover)

        # source
        self.sourceComponent.reset()
        if components.source.isSource is True:
            self.sourceComponent.set(0, 0, components.source.source)

        # destination
        self.destinationComponent.reset()
        if components.destination.isDestination is True:
            self.destinationComponent.set(0, 0, components.destination.destination)

        # Clear out the AggregatedTriggerFrame
        self.triggersFrame.grid_forget()
        self.triggersFrame = AggregatedTriggerFrame(self, self.centerFrame.inner)
        self.triggersFrame.grid(row=18, column=0, sticky="ew")

        # Triggers
        if components.triggerList:
            print("\tTriggers found")
            for trigger in components.triggerList:
                self.triggersFrame.populate_trigger(trigger)

    print("Done.")
    #end update_center_frame


    def update_mission_frame(self):
        print("\nUpdating missionFrame...", end="\t")

        self.missionTextBox.forget()
        self.missionTextBox = Text(self.missionFrame, height=50, width=100, wrap=WORD)
        self.missionTextBox.pack()
        self.missionTextBox.insert(END, self.activeMission.print_mission_lines_to_text())
        self.missionTextBox.config(state=DISABLED)

        print("Done.")
    #end update_mission_frame


    ### MISC METHODS ###


    def mission_selected(self, event=None):
        selected_mission_name = self.missionComboBox.get()
        print('\nOpening mission "%s"' % selected_mission_name)
        self.activeMission = self.missionNameToObjectDict.get(selected_mission_name)
        self.update_center_frame()
        self.update_mission_frame()
    #end mission_selected

#end class GUI

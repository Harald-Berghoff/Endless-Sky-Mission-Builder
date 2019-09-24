""" MissionParser.py
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

import logging


class MissionParser(object):
    def __init__(self, mission):
        self.mission = mission
        self.components = mission.components
        self.lines = []
        self.tokens = []
    #end init


    def run(self):
        logging.debug("\tParsing mission...")
        self._add_line("mission \"%s\"" % self.mission.missionName)

        # mission display name
        if self._has_mission_display_name():
            self._parse_mission_display_name()

        # description
        if self._has_description():
            self._parse_description()

        # isBlocked
        if self._has_blocked():
            self._parse_blocked()

        # deadline
        if self._has_deadline():
            self._parse_deadline()

        # cargo
        if self._has_cargo():
            self._parse_cargo()

        # passengers
        if self._has_passengers():
            self._parse_passengers()

        # illegal
        if self._has_illegal():
            self._parse_illegal()

        # stealth
        if self._has_stealth():
            self._parse_stealth()

        # isInvisible
        if self._has_invisible():
            self._parse_invisible()

        # priorityLevel
        if self._has_priority_level():
            self._parse_priority_level()

        # whereShown
        if self._has_where_shown():
            self._parse_where_shown()

        # repeat
        if self._has_repeat():
            self._parse_repeat()

        # clearance
        if self._has_clearance():
            self._parse_clearance()

        # isInfiltrating
        if self._has_infiltrating():
            self._parse_infiltrating()

        # waypoint
        if self._has_waypoint():
            self._parse_waypoint()

        # stopover
        if self._has_stopover():
            self._parse_stopover()

        # source
        if self._has_source():
            self._parse_source()

        # destination
        if self._has_destination():
            self._parse_destination()

        # Trigger(s)
        if self._has_triggers():
            self._parse_triggers()

        return self.lines
    #end run


    def _add_line(self, line):
        self.lines.append(line + "\n")
    #end add_line


    ### methods to check if components are active
    def _has_mission_display_name(self):
        if self.components.missionDisplayName is None:
            return False
        return True
    #def _has_mission_display_name


    def _has_description(self):
        if self.components.description is None:
            return False
        return True
    #end _has_description


    def _has_blocked(self):
        if self.components.blocked is None:
            return False
        return True
    #end _has_blocked


    def _has_deadline(self):
        if self.components.deadline.isActive is False:
            return False
        return True
    #def _has_deadline


    def _has_cargo(self):
        if self.components.cargo.isActive is False:
            return False
        return True
    #end _has_cargo


    def _has_passengers(self):
        if self.components.passenger.isActive is False:
            return False
        return True
    #end _has_passengers


    def _has_illegal(self):
        if self.components.illegal.isIllegal is False:
            return False
        return True
    #end _has_illegal


    def _has_stealth(self):
        if self.components.isStealth is False:
            return False
        return True
    #end _has_stealth


    def _has_invisible(self):
        if self.components.isInvisible is False:
            return False
        return True
    #end _hes_invisible


    def _has_priority_level(self):
        if self.components.priorityLevel is None:
            return False
        return True
    #end _has_priority_level


    def _has_where_shown(self):
        if self.components.whereShown is None:
            return False
        return True
    #end _has_where_shown


    def _has_repeat(self):
        if self.components.repeat.isActive is False:
            return False
        return True
    #end _has_repeat


    def _has_clearance(self):
        if self.components.clearance.isActive is False:
            return False
        return True
    #end _has_clearance


    def _has_infiltrating(self):
        if self.components.isInfiltrating is False:
            return False
        return True
    #end _has_infiltrating


    def _has_waypoint(self):
        if self.components.waypoint is None:
            return False
        return True
    #end _has_waypoint


    def _has_stopover(self):
        if self.components.stopover.isActive is False:
            return False
        return True
    # end _has_stopover


    def _has_source(self):
        if self.components.source.isActive is False:
            return False
        return True
    #end _has_source


    def _has_destination(self):
        if self.components.destination.isActive is False:
            return False
        return True
    #end _has_destination


    def _has_triggers(self):
        if not self.components.triggerList:
            return False
        return True
    #end _has_triggers


    ### methods to parse the data from each component in the model
    def _parse_mission_display_name(self):
        logging.debug("\t\tParsing mission display name...")
    #end _parse_mission_display_name


    def _parse_description(self):
        logging.debug("\t\tParsing ...")
    #end _parse_description


    def _parse_blocked(self):
        logging.debug("\t\tParsing ...")
    #end _parse_blocked


    def _parse_deadline(self):
        logging.debug("\t\tParsing ...")
    #end _parse_deadline


    def _parse_cargo(self):
        logging.debug("\t\tParsing ...")
    #end _parse_cargo


    def _parse_passengers(self):
        logging.debug("\t\tParsing ...")
    #end _parse_passengers


    def _parse_illegal(self):
        logging.debug("\t\tParsing ...")
    #end _parse_illegal


    def _parse_stealth(self):
        logging.debug("\t\tParsing ...")
    #end _parse_stealth


    def _parse_invisible(self):
        logging.debug("\t\tParsing ...")
    #end _parse_invisible


    def _parse_priority_level(self):
        logging.debug("\t\tParsing ...")
    #end _parse_priority_level


    def _parse_where_shown(self):
        logging.debug("\t\tParsing ...")
    #end _parse_where_shown


    def _parse_repeat(self):
        logging.debug("\t\tParsing ...")
    #end _parse_repeat


    def _parse_clearance(self):
        logging.debug("\t\tParsing ...")
    #end _parse_clearance


    def _parse_infiltrating(self):
        logging.debug("\t\tParsing ...")
    #end _parse_infiltrating


    def _parse_waypoint(self):
        logging.debug("\t\tParsing ...")
    #end _parse_waypoint


    def _parse_stopover(self):
        logging.debug("\t\tParsing ...")
    #end _parse_stopover


    def _parse_source(self):
        logging.debug("\t\tParsing ...")
    #end _parse_source


    def _parse_destination(self):
        logging.debug("\t\tParsing ...")
    #end _parse_destination


    def _parse_triggers(self):
        logging.debug("\t\tParsing ...")
    #end _parse_triggers

#end class MissionParser

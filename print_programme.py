from lib import get_itineraries, Itinerary
from typing import List
import data

import io

MAX_WIDTH = 24
#######################
# THERMOPRINTER
CODEPAGE = "cp437"
PORT = "/dev/usb/lp0"
ADD_NEWLINE = False
#######################
# TEXT EDITOR
# CODEPAGE = "utf-8"
# PORT = "/tmp/test"
# ADD_NEWLINE = True
#######################


def _print_out_ln(line_wo_newline, printer):
    add_newline = len(line_wo_newline) > 24 or ADD_NEWLINE
    printer.write((line_wo_newline.ljust(MAX_WIDTH, " ") + ("\r\n" if add_newline else "")).encode(CODEPAGE))


def print_out(itinerary_list: List[Itinerary]):
    with io.open(PORT, 'wb') as printer:
        for itinerary in itinerary_list:
            _print_out_ln("▒" * MAX_WIDTH, printer)
            for line in str(itinerary).replace("€", "EUR").split("\n"):
                _print_out_ln(line, printer)
            _print_out_ln("▒" * MAX_WIDTH, printer)
            _print_out_ln(" " * MAX_WIDTH, printer)


if __name__ == '__main__':
    print_out(get_itineraries(data.tuscany))

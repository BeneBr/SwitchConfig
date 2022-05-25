import csv
from typing import List
from switch import Switch

def ReadSwitchFiles(switch_file)->List[Switch]:
    switch_list = []
    with open(switch_file) as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        next(csv_reader, None)
        for switch_line in csv_reader:
            switch = Switch(switch_line[0], switch_line[1])
            switch_list.append(switch)
    return switch_list

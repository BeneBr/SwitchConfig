import csv
from typing import List, Dict

def ReadSwitchFiles(switch_file)->List[dict]:
    switch_list = []
    with open(switch_file) as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')

        for switch_line in csv_reader:
            switch: Dict["str", "str"] = {
                "switch_name": switch_line[0],
                "switch_ip": switch_line[1]
            }
            switch_list.append(switch)
    return switch_list
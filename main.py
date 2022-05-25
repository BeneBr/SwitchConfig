from read_switchs_file import ReadSwitchFiles
from switch_config import ConnectSwitch

if __name__ == '__main__':
    switch_list = ReadSwitchFiles("switch_list.csv")
    ConnectSwitch(switch=switch_list[0], username="gustavoberned",password="741852Stic@",)


import paramiko
from switch import Switch


def ConnectSwitch(switch: Switch, username: str, password: str):
    command = "show interface status"
    paramiko_ssh_client = paramiko.SSHClient()
    paramiko_ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    paramiko_ssh_client.connect(hostname=switch.switch_ip,port=switch.port, username=username, password=password, look_for_keys=False, allow_agent=False)
    stdin, stdout, stderr = paramiko_ssh_client.exec_command(command=command)
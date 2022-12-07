from netmiko.cisco.cisco_ios import CiscoIosSSH


class MyNetmiko(CiscoIosSSH):
    def send_command(self, command, **kwargs):
        output = super().send_command(command, **kwargs)
        if "%" in output:
            raise ValueError(f"ошибка в команде {command} на {self.host}")
        return output

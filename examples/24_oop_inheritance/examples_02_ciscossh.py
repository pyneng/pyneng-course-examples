from pprint import pprint
import re
import time
from collections.abc import Iterable

import paramiko
from examples_01_basessh import BaseSSH


class CiscoSSH(BaseSSH):
    def __init__(
        self,
        host,
        username,
        password,
        enable_password,
        max_read=60000,
        pause=0.5,
    ):
        # BaseSSH.__init__(self, host, username, password)
        super().__init__(host, username, password)

        self._ssh.send("enable\n")
        self._ssh.send(f"{enable_password}\n")
        time.sleep(self.pause)
        self._ssh.send("terminal length 0\n")
        time.sleep(self.pause)
        self._ssh.recv(self.max_read)
        self.prompt = self._get_prompt()

    def _get_prompt(self):
        self._send_line("sh run | i hostname")
        output = self._read_until_regex("#")
        match = re.search(r"\S+#", output)
        if match:
            return match.group()
        else:
            return "#"

    def _regex_until_prompt(self):
        output = self._read_until_regex(self.prompt)
        return output

    def send_command(self, command):
        self._send_line(command)
        output = self._read_until_prompt()
        return output

    def send_config_commands(self, commands):
        if type(commands) == str:
            commands = ["conf t", commands, "end"]
        elif isinstance(commands, Iterable):
            commands = ["conf t", *commands, "end"]
        else:
            raise TypeError(
                "Метод send_config_commands может работать только со строкой или iterable"
            )
        for cmd in commands:
            self._send_line(cmd)
            time.sleep(self.pause)
        output = self._read_until_prompt()
        return output


if __name__ == "__main__":
    with CiscoSSH("192.168.100.1", "cisco", "cisco", "cisco") as r1:
        print(r1.send_command("sh clock"))
        pprint(r1.prompt)
        pprint(r1.send_config_commands("logging 10.1.1.1"))


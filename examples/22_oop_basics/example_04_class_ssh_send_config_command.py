import paramiko
import time
from pprint import pprint
import re


class CiscoSSH:
    def __init__(
        self,
        host,
        username,
        password,
        enable_pass,
        pause=0.2,
        max_read=100000,
        read_timeout=2,
    ):
        self.pause = pause
        self.max_read = max_read
        self.read_timeout = read_timeout

        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.connect(
            hostname=host,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False,
        )
        self.ssh = client.invoke_shell()
        self.ssh.send("enable\n")
        time.sleep(pause)
        self.ssh.send(f"{enable_pass}\n")
        time.sleep(pause)
        self.ssh.send("terminal length 0\n")
        time.sleep(pause)
        self.ssh.recv(max_read)

        self.prompt = self.get_prompt()

    def get_prompt(self):
        self.ssh.send("sh run | i hostname\n")
        time.sleep(self.pause)
        output = self._read_until("#")
        match = re.search(r"\S+#", output)
        if match:
            return match.group()
        else:
            return "#"

    def _read_until_prompt(self):
        output = self._read_until(self.prompt)
        return output

    def _read_until(self, regex):
        self.ssh.settimeout(self.read_timeout)
        output = ""
        while True:
            time.sleep(0.2)
            try:
                part = self.ssh.recv(self.max_read).decode("utf-8")
                output += part
            except OSError:
                break
            match = re.search(regex, output)
            if match:
                break
        return output

    def send_show(self, show_command):
        self.ssh.send(f"{show_command}\n")
        output = self._read_until_prompt()
        return output

    def send_config_commands(self, commands):
        if type(commands) == str:
            commands = ["conf t", commands, "end"]
        else:
            commands = ["conf t", *commands, "end"]
        output = ""
        for cmd in commands:
            self.ssh.send(f"{cmd}\n")
            time.sleep(self.pause)
        output += self._read_until_prompt()
        return output

    def get_config(self):
        return self.send_show("sh run")

    def close(self):
        self.ssh.close()


if __name__ == "__main__":
    r1 = CiscoSSH("192.168.100.1", "cisco", "cisco", "cisco")
    out = r1.send_show("sh ip int br")
    pprint(out, width=120)
    # r1.close()

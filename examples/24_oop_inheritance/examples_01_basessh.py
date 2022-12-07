import time
from pprint import pprint
import re

import paramiko


class BaseSSH:
    def __init__(
        self,
        host,
        username,
        password,
        max_read=60000,
        pause=0.5,
        read_timeout=5,
    ):
        self.host = host
        self.username = username
        self.password = password
        self.max_read = max_read
        self.pause = pause
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
        self._ssh = client.invoke_shell()
        self._ssh.settimeout(2)
        time.sleep(self.pause)
        self._ssh.recv(self.max_read)

    def _send_line(self, command):
        self._ssh.send(f"{command}\n")

    def _read_until_regex(self, regex):
        output = ""
        self._ssh.settimeout(self.read_timeout)
        while True:
            try:
                time.sleep(self.pause)
                part = self._ssh.recv(self.max_read).decode("utf-8")
                output += part
                match = re.search(regex, output)
                if match:
                    break
            except OSError:
                break
        return output.replace("\r\n", "\n")

    def close(self):
        self._ssh.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


if __name__ == "__main__":
    with BaseSSH("192.168.100.1", "cisco", "cisco") as r1:
        r1._ssh.send("sh clock\n")
        print(r1._read_until_regex("#"))

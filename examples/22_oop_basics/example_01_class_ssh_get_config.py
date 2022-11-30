import paramiko
import time
from pprint import pprint


class CiscoSSH:
    def __init__(self, host, username, password, enable_pass, pause=0.5, max_read=100000):
        self.pause = pause
        self.max_read = max_read

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

    def send_show(self, show_command):
        self.ssh.send(f"{show_command}\n")
        time.sleep(self.pause)
        output = self.ssh.recv(self.max_read).decode("utf-8")
        return output

    def get_config(self):
        return self.send_show("sh run")

    def close(self):
        self.ssh.close()


if __name__ == "__main__":
    r1 = CiscoSSH("192.168.100.1", "cisco", "cisco", "cisco")
    out = r1.send_show("sh clock")
    pprint(out, width=120)
    r1.close()

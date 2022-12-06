import telnetlib
import time


class BaseTelnet:
    def __init__(self, ip, username, password, prompt, short_sleep=1, long_sleep=5):
        print("__init__")
        self.ip = ip
        self.username = username
        self.prompt = prompt
        self.short_sleep = short_sleep
        self.long_sleep = long_sleep

        self._telnet = telnetlib.Telnet(ip)
        self._telnet.read_until(b"Username:")
        self._write_line(username)
        self._telnet.read_until(b"Password:")
        self._write_line(password)
        time.sleep(self.short_sleep)
        self._telnet.read_very_eager()

    def _write_line(self, line):
        self._telnet.write(line.encode("utf-8") + b"\n")

    def _read_until_prompt(self):
        output = self._telnet.read_until(self.prompt.encode("utf-8"))
        return output.decode("utf-8").replace("\r\n", "\n")

    def send_command(self, command):
        self._write_line(command)
        output = self._read_until_prompt()
        return output

    def send_config(self, commands):
        if type(commands) == str:
            commands = [commands]
        output = ""
        for cmd in commands:
            self._write_line(cmd)
            time.sleep(self.short_sleep)
            output += self._telnet.read_very_eager().decode("utf-8")
        return output.replace("\r\n", "\n")

    def close(self):
        self._telnet.close()

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__")
        self.close()


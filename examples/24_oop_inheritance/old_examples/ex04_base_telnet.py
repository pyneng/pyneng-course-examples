import telnetlib
import time


class BaseTelnet:
    def __init__(self, ip, username, password, prompt, encoding="utf-8"):
        print("__init__")
        self.ip = ip
        self.prompt = prompt
        self.encoding = encoding

        self._telnet = telnetlib.Telnet(ip)
        self._telnet.read_until(b"Username:")
        self._write_line(username)
        self._telnet.read_until(b"Password:")
        self._write_line(password)
        time.sleep(0.5)
        self._telnet.read_very_eager()

    def _write_line(self, line):
        self._telnet.write(f"{line}\n".encode(self.encoding))

    def _read_until_prompt(self):
        output = self._telnet.read_until(self.prompt.encode(self.encoding))
        output = output.decode(self.encoding)
        return output.replace("\r\n", "\n")

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        print("__exit__")
        self.close()

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
            output += self._read_until_prompt()
        return output

    def close(self):
        self._telnet.close()


if __name__ == "__main__":
    with BaseTelnet(
        ip="192.168.100.1", username="cisco",
        password="cisco", prompt=">"
    ) as r1:
        print(r1.send_command("sh clock"))

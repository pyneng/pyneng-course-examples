from ex04_base_telnet import BaseTelnet


class NetworkCommandError(Exception):
    pass


class CiscoTelnet(BaseTelnet):
    def __init__(self, ip, username, password, enable, prompt="#", **kwargs):
        super().__init__(ip, username, password, prompt, **kwargs)

        self._write_line("enable")
        self._telnet.read_until(b"Password:")
        self._write_line(enable)
        self._read_until_prompt()
        self._write_line("terminal length 0")
        self._read_until_prompt()

    def send_config(self, commands):
        self._write_line("conf t")
        output = self._read_until_prompt()
        output += super().send_config(commands)
        self._write_line("end")
        output += self._read_until_prompt()
        if "%" in output:
            raise NetworkCommandError("При выполнии команды...")
        return output


if __name__ == "__main__":
    with CiscoTelnet(
        ip="192.168.100.1", username="cisco",
        password="cisco", enable="cisco"
    ) as r1:
        print(r1.send_command("sh clock"))
        print(r1.send_config("loggng 10.1.1.1"))


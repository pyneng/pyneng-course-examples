from base_telnet_class import BaseTelnet


class CiscoTelnet(BaseTelnet):
    def __init__(
        self,
        ip,
        username,
        password,
        enable_password,
        prompt="#",
        short_sleep=1,
        long_sleep=5,
    ):
        super().__init__(
            ip, username, password, prompt, short_sleep, long_sleep
        )
        # BaseTelnet.__init__(self, ...)
        self._telnet.write(b"enable\n")
        self._telnet.read_until(b"Password")
        self._write_line(enable_password)
        self._read_until_prompt()
        self._write_line("terminal length 0")
        self._read_until_prompt()

    def send_config(self, commands):
        self._write_line("conf t")
        output = self._read_until_prompt()
        output += super().send_config(commands)
        self._write_line("end")
        output += self._read_until_prompt()
        return output

    def get_config(self, command="sh run"):
        return self.send_command(command)


if __name__ == "__main__":
    with CiscoTelnet("192.168.100.1", "cisco", "cisco", "cisco", prompt="#") as r1:
        print(r1.send_config("logging 10.1.1.1"))
        print(r1.get_config())

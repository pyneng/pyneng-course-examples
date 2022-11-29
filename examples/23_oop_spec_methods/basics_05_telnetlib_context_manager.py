import telnetlib
import time


class CiscoTelnet:
    def __init__(self, ip, username, password, enable_password):
        self.ip = ip
        self._telnet = telnetlib.Telnet(ip)
        self._telnet.read_until(b"Username:")
        self._telnet.write(username.encode("utf-8") + b"\n")
        self._telnet.read_until(b"Password:")
        self._telnet.write(password.encode("utf-8") + b"\n")
        self._telnet.write(b"enable\n")
        self._telnet.read_until(b"Password:")
        self._telnet.write(enable_password.encode("utf-8") + b"\n")
        time.sleep(0.5)
        self._telnet.write(b"terminal length 0\n")
        time.sleep(0.5)
        self._telnet.read_very_eager()

    def send_show(self, command):
        """
        Отправка одной команды show
        """
        self._telnet.write(f"{command}\n".encode("utf-8"))
        output = self._telnet.read_until(b"#").decode("utf-8")
        return output.replace("\r\n", "\n")

    def close(self):
        self._telnet.close()


if __name__ == "__main__":

    r1 = CiscoTelnet(
        ip="192.168.100.1", username="cisco", password="cisco", enable_password="cisco"
    )
    print(r1.send_show("sh clock"))
    r1.close()

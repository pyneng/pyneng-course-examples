from pprint import pprint
import telnetlib


def configure_cisco(host, username, password, enable_pass, commands):
    try:
        with telnetlib.Telnet(host, timeout=5) as t:
            t.read_until(b'Username:')
            t.write(f"{username}\n".encode("utf-8"))
            t.read_until(b'Password')
            t.write(f"{password}\n".encode("utf-8"))
            index, _, _ = t.expect([b">", b"#", b"Login invalid"], timeout=5)
            if index == 0:
                t.write(b"enable\n")
                t.read_until(b'Password')
                t.write(f"{enable_pass}\n".encode("utf-8"))
                index, _, _ = t.expect([b"#", b"Password"], timeout=5)
                if index in (1, -1):
                    raise ConnectionError(f"Enable authentication failed on device {host}")
            elif index == 1:
                # print(">>> enable")
                pass
            else:
                raise ConnectionError(f"Authentication failed on device {host}")

            if type(commands) == str:
                commands = ["conf t", commands, "end"]
            else:
                commands = ["conf t", *commands, "end"]
            output = b""
            for cmd in commands:
                t.write(f"{cmd}\n".encode("utf-8"))
                output += t.read_until(b'#', timeout=5)
            output = output.decode("utf-8").replace("\r\n", "\n")
            return output
    except OSError as error:
        print(error)


if __name__ == "__main__":
    out = configure_cisco("192.168.100.1", "cisco", "cisco", "cisco", ["int lo42", "desc TEST"])
    pprint(out, width=120)

from pprint import pprint
import telnetlib


def get_cisco_show_output(host, username, password, enable_pass, command):
    #try:
        with telnetlib.Telnet(host, timeout=5) as t:
            t.read_until(b"Username:")
            t.write(f"{username}\n".encode("utf-8"))
            t.read_until(b"Password")
            t.write(f"{password}\n".encode("utf-8"))
            passwd_out = t.read_until(b">", timeout=3)
            pprint(passwd_out)
            if "login invalid" in passwd_out.decode("utf-8").lower():
                return

            t.write(b"enable\n")
            t.read_until(b"Password")
            t.write(f"{enable_pass}\n".encode("utf-8"))
            enable_output = t.read_until(b"#", timeout=3)
            print(f"{enable_output=}")
            if "Password" in enable_output.decode("utf-8"):
                return
            t.write(b"terminal length 0\n")
            boutput = t.read_until(b"#", timeout=5)

            t.write(f"{command}\n".encode("utf-8"))
            boutput = t.read_until(b"#", timeout=5)
            output = boutput.decode("utf-8").replace("\r\n", "\n")
            return output
    #except OSError as error:
    #    print(f"Error {error}")


if __name__ == "__main__":
    out = get_cisco_show_output(
        "192.168.100.1", "cisco", "cisco", "cisco123", "sh ip int br"
    )
    pprint(out, width=120)

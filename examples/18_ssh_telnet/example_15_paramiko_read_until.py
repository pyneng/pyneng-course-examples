import paramiko
import time
from pprint import pprint
import re


def cisco_send_show_command(
    host, username, password, enable_pass, command, max_read=60000,
    pause=0.5, prompt="#", read_timeout=5
):
    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=host,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False,
        )
        ssh = client.invoke_shell()
        ssh.settimeout(2)
        ssh.send("enable\n")
        ssh.send(f"{enable_pass}\n")
        time.sleep(pause)
        ssh.send(f"terminal length 0\n")
        time.sleep(pause)
        ssh.recv(max_read)

        ssh.send(f"{command}\n")
        ssh.settimeout(read_timeout)
        output = ""
        while True:
            time.sleep(0.2)
            try:
                part = ssh.recv(100).decode("utf-8")
                pprint(part)
            except OSError:
                break
            print("=" * 40)
            output += part
            if prompt in output:
                break

        return output.replace("\r\n", "\n")


if __name__ == "__main__":
    out = cisco_send_show_command(
        "192.168.100.1", "cisco", "cisco", "cisco", "ping 8.8.8.8 repeat 5",
        prompt="#", read_timeout=10
    )
    pprint(out, width=120)


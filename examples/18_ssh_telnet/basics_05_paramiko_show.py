import paramiko
import time
from pprint import pprint


def cisco_get_show_output(
    host, username, password, enable_pass, command, max_read=100000, pause=0.5
):
    with paramiko.SSHClient() as client:
        client.load_system_host_keys()
        # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=host,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False,
        )
        with client.invoke_shell() as ssh:
            ssh.settimeout(5)
            ssh.send("enable\n")
            ssh.send(f"{enable_pass}\n")
            time.sleep(pause)
            ssh.send("terminal length 0\n")
            time.sleep(pause)
            ssh.recv(max_read)

            ssh.send(f"{command}\n")
            time.sleep(pause * 2)
            output = ssh.recv(max_read)
            return output.decode("utf-8").replace("\r\n", "\n")


if __name__ == "__main__":
    out = cisco_get_show_output(
        "192.168.100.1", "cisco", "cisco", "cisco", "sh run"
    )
    pprint(out, width=120)


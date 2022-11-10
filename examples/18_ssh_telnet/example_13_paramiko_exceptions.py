import time
from pprint import pprint
import paramiko
from paramiko.ssh_exception import SSHException, AuthenticationException


def cisco_send_show_command(
    host, username, password, enable_pass, command, max_read=60000,
    pause=0.5
):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(
            hostname=host,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False,
            timeout=5,
        )
    except (OSError, SSHException) as error:
        print(error)
    else:
        with client.invoke_shell() as ssh:
            try:
                ssh.settimeout(5)
                ssh.send("enable\n")
                time.sleep(pause)
                ssh.recv(max_read)
                ssh.send(f"{enable_pass}\n")
                enable_out = ssh.recv(max_read).decode("utf-8")
                time.sleep(pause)
                if "Password" in enable_out:
                    raise AuthenticationException("Authentication error")
                ssh.send(f"terminal length 0\n")
                time.sleep(pause)
                ssh.recv(max_read)

                ssh.send(f"{command}")
                time.sleep(pause)
                output = ssh.recv(max_read)
                return output.decode("utf-8")
            except OSError as error:
                print(error)


if __name__ == "__main__":
    out = cisco_send_show_command(
        "192.168.100.1", "cisco", "cisco", "cisco", "sh ip int br"
    )
    pprint(out, width=120)


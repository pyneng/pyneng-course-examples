paramiko_set = {
    "AuthenticationException",
    "BERException",
    "BadHostKeyException",
    "ConfigParseError",
    "CouldNotCanonicalize",
    "EOFError",
    "Exception",
    "IOError",
    "ImportError",
    "IncompatiblePeer",
    "InvalidHostKey",
    "KeyError",
    "NeedRekeyException",
    "NoValidConnectionsError",
    "PasswordRequiredException",
    "PipeTimeout",
    "ProxyCommandFailure",
    "SFTPError",
    "SSHException",
    "TypeError",
    "ValueError",
    "WindowsError",
    "gssapi.GSSException",
    "socket.error",
    "socket.timeout",
}

netmiko_set = {
    "AttributeError",
    "ConfigInvalidException",
    "ConnectionException",
    "IOError",
    "ImportError",
    "ModuleNotFoundError",
    "NetmikoAuthenticationException",
    "NetmikoTimeoutException",
    "NotImplementedError",
    "ReadException",
    "ReadTimeout",
    "ValueError",
    "WriteException",
}

netmiko_set_standard = {
    "AttributeError",
    "IOError",
    "ImportError",
    "ModuleNotFoundError",
    "NotImplementedError",
    "ValueError",
}

paramiko_set_standard = {
    "EOFError",
    "Exception",
    "IOError",
    "ImportError",
    "KeyError",
    "TypeError",
    "ValueError",
}

NetmikoBaseException --- ConfigInvalidException
|                 |
-- ReadException  -- ConnectionException
   |
   --- ReadTimeout


  paramiko.ssh_exception.SSHException
   |                             |
   --- NetmikoTimeoutException   -- paramiko.ssh_exception.AuthenticationException
                                        |
                                        -- netmiko.exceptions.NetmikoAuthenticationException


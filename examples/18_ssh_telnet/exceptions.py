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
    "ValueError",
}


## NETMIKO EXCEPTIONS

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


## PARAMIKO EXCEPTIONS
e='NoValidConnectionsError'
[<class 'paramiko.ssh_exception.NoValidConnectionsError'>,
 <class 'OSError'>,

e='SSHException'
[<class 'paramiko.ssh_exception.SSHException'>,

e='IncompatiblePeer'
[<class 'paramiko.ssh_exception.IncompatiblePeer'>,
 <class 'paramiko.ssh_exception.SSHException'>,
e='ConfigParseError'
[<class 'paramiko.ssh_exception.ConfigParseError'>,
 <class 'paramiko.ssh_exception.SSHException'>,
e='PasswordRequiredException'
[<class 'paramiko.ssh_exception.PasswordRequiredException'>,
 <class 'paramiko.ssh_exception.AuthenticationException'>,
 <class 'paramiko.ssh_exception.SSHException'>,
e='CouldNotCanonicalize'
[<class 'paramiko.ssh_exception.CouldNotCanonicalize'>,
 <class 'paramiko.ssh_exception.SSHException'>,
e='ProxyCommandFailure'
[<class 'paramiko.ssh_exception.ProxyCommandFailure'>,
 <class 'paramiko.ssh_exception.SSHException'>,
e='BadHostKeyException'
[<class 'paramiko.ssh_exception.BadHostKeyException'>,
 <class 'paramiko.ssh_exception.SSHException'>,
e='AuthenticationException'
[<class 'paramiko.ssh_exception.AuthenticationException'>,
 <class 'paramiko.ssh_exception.SSHException'>,

paramiko_set_standard = {
    "EOFError",
    "IOError",
    "KeyError",
    "TypeError",
    "ValueError",
}

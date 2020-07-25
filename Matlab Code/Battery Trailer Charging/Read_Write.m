n = modbus('tcpip', '169.235.18.210', 502)
%write(n,'holdingregs',11,0)
%read(n,'holdingregs',11,1)
read(n,'inputregs', 1,1)
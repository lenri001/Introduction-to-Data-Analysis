m = modbus('tcpip', '169.235.18.210', 502)
while (1)
    HB = read(m,'holdingregs', 1,1);
    fprintf('HB: %d\n',HB);
    HB = HB+1; 
    pause(1)
    write(m,'holdingregs',1,HB)
    if HB == 65535
        HB = 0;
        write(m,'holdingregs',1,HB)        
    end
    
end
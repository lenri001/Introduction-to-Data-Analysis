clear all;
close all;
clc
go=true
while go %infinite loop for running this algorithm as long as it is needed
 v=voltage % should I read the voltage from a file or table? I need clarification
while v > 278
    write(obj,'holdingregs',4105,30)% writing 30 to the curtailment set point register
    write(obj,'holdingregs',4100,85)% writing 85 to the 'go now' register
end
end
    

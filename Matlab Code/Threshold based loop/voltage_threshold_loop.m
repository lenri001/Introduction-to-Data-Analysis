clear all;
close all;
clc
go=true
while go %infinite loop for running this algorithm as long as it is needed

    v = [100; 200; 270; 300];%testing for a series of test voltage data as I don't have the voltage measurement in hand 
    for i = 1:length(v)
    %%
    if v(i) > 278
        write(obj,'holdingregs',4105,30)% writing 30 to the curtailment set point register
        write(obj,'holdingregs',4100,85)% writing 85 to the 'go now' register
    end
end
    

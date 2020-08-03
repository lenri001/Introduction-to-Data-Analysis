%TCPIPCONN Code for communicating with an instrument.
%
%   This is the machine generated representation of an instrument control
%   session. The instrument control session comprises all the steps you are
%   likely to take when communicating with your instrument. These steps are:
%   
%       1. Create an instrument object
%       2. Connect to the instrument
%       3. Configure properties
%       4. Write and read data
%       5. Disconnect from the instrument
% 
%   To run the instrument control session, type the name of the file,
%   tcpipconn, at the MATLAB command prompt.
% 
%   The file, TCPIPCONN.M must be on your MATLAB PATH. For additional information 
%   on setting your MATLAB PATH, type 'help addpath' at the MATLAB command 
%   prompt.
% 
%   Example:
%       tcpipconn;
% 
%   See also SERIAL, GPIB, TCPIP, UDP, VISA.
% 
 
%   Creation time: 06-Oct-2014 12:35:11

% Find a tcpip object.
obj1 = instrfind('Type', 'tcpip', 'RemoteHost', '138.23.236.57', 'RemotePort', 8888, 'Tag', '');

% Create the tcpip object if it does not exist
% otherwise use the object that was found.
if isempty(obj1)
    obj1 = tcpip('138.23.236.57', 8888);
else
    fclose(obj1);
    obj1 = obj1(1)
end

% Connect to instrument object, obj1.
fopen(obj1);

% Communicating with instrument object, obj1.
fprintf(obj1, 'P\n');

% Disconnect all objects.
fclose(obj1);

% Clean up all objects.
delete(obj1);


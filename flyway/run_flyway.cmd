@REM Run this file from a Windows Command Prompt or Powershell window.
ECHO OFF
set FLYWAY_HOME=U:\Users\Dale\Development\Flyway\flyway-9.4.0

@REM This command will allow paramters to be passed such as info or migrate
%FLYWAY_HOME%/flyway.cmd -configFiles="./conf/flyway.conf" %1 %2 %3 %4
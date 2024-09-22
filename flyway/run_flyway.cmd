@REM Run this file from a Windows Command Prompt or Powershell window.
@REM Not for the main branch it should be ran from the project root
@REM otherwise you might get a coffee.db in the root and the src directory.
ECHO OFF
set FLYWAY_HOME=U:\Users\Dale\Development\Flyway\flyway-10.7.1

@REM This command will allow paramters to be passed such as info or migrate
%FLYWAY_HOME%/flyway.cmd -configFiles="./conf/flyway.toml" %1 %2 %3 %4
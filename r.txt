@echo off
Title Clock
@mode con cols=30  lines=7
color 03
: main
cls 
echo.
echo time: %time%
echo.
echo date:%date%
echo.
ping -n 2 0.0.0.0>nul
goto main
my name is ritik.
i belong to kasganj.
ratnesh ji is a good boy.
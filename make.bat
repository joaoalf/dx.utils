@echo off
del dist
c:\python26\python.exe setup.py bdist_wininst
cd dist

rem zip *.* ..\dxcommd.zip
rem copy *.* c:\dxcommd\
rem cd ..


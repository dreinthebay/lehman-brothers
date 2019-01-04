echo off
echo hello world
cd ..
pip install virtualenv
mkdir env
cd env
virtualenv test_environment
cd ..
echo The current directory is %CD%
dir
%CD%\env\test_environment\scripts\activate.bat
pip install -r requirements.txt

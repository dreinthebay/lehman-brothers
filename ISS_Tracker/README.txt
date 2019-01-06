This program collects location data of the International Space station and then plots it's movement on a map of the world.

To get started, clone this repository on your machine. Python is a requirement for this project (python.org for installation). Scripts will only run on windows command line.

Go to the /ISS_Tracker/bin folder and run the setup_vm.bat file to install all requirements and python packages. Most machines will allow you to double click on the program to run it.
You can run from cmd line by navigating to the directory and typing "setup_vm.bat" and pressing enter. 

Once the VM is created, run the runner.bat file to create a sample map. 

Users can run their own projects by running the file ISS_Tracker/ISS_Tracker/ISS_Tracker_executable.py with arguments
The arguments for this file are
1. the number of lat/long coordinates to collect (each collection takes 5 seconds)
2. the name of the csv file to store the data
3. the name of the map the program will create

To make a map of 30 data points, type the following into cmd line (suffixes on the file names are optional)
>python ISS_Tracker_executable.py 30 test_csv.csv test_map.html

For a more interactive run, select the ISS_Tracker/ISS_Tracker/ISS_Tracker_runner.py file. You can learn about the program in more depth.
>python ISS_Tracker_runner.py

For any errors or questions, contact Denny Lehman at dendenlehman@gmail.com
Have a great day,
Denny
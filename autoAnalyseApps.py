import os
import getpass
import subprocess

 
current_file_path = os.getcwd()
current_user = getpass.getuser()

apps_dir_path = str(current_file_path) + '/Apps/Medicalapps'

app_list = []

for path in os.listdir(apps_dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(apps_dir_path, path)):
        app_list.append(path)
#print(app_list)

# Construct commands for running Flowdroid on each file.

command_dict = {}
for app in app_list:
    command = ["java", "-jar", "soot-infoflow-cmd-jar-with-dependencies.jar", "-a"]
    command.append("Apps/Medicalapps/"+ app) 
    command.append("-p")
    command.append("/Users/"+current_user+"/Library/Android/sdk/platforms")
    command.append("-s")
    command.append("SourcesAndSinks.txt")
    command_dict[app] = command

#print(command_dict)


path = "Analysis"

if not os.path.exists(path):
    os.makedirs(path)

COUNT = 0
for app, command in command_dict.items():
    file = "Analysis/"+app+".txt"
    print(file, COUNT)
    COUNT+=1
    if not os.path.isfile(file):  
        with open(file, "w") as f:
            p = subprocess.Popen(command, stderr=f)
            p.communicate()
        f.close()


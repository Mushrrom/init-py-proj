import inspect
import os.path
import os
import sys
filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))


current_directory = os.getcwd()
if len(sys.argv) == 2:
    print(f"creating project with name: {sys.argv[1]}")
    project_name = sys.argv[1]
else:
    project_name = input("Enter project name: ")

project_path = current_directory + "/" + project_name

if os.path.exists(project_path):
    print("project already exists")
    sys.exit(1)

os.mkdir(project_path)

with open(f"{path}/.pylintrc", "r") as f:
    pylintsettings = f.read()

with open(f"{project_path}/.pylintrc", "w") as f:
    f.write(pylintsettings)

with open(f"{path}/pyrightconfig.json", "r") as f:
    pyrightconfig = f.read()

with open(f"{project_path}/pyrightconfig.json", "w") as f:
    f.write(pyrightconfig)

with open(f"{project_path}/.gitignore", "w") as f:
    f.write(".pylintrc\n.pyrightconfig.json")

with open(f"{project_path}/requirements.txt", "w") as f:
    f.write("")

with open(f"{project_path}/main.py", "w") as f:
    f.write("")

print("created project :)")

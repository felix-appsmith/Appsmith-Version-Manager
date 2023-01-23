import os
import subprocess
import datetime
import shutil
service_name = "appsmith"

now = datetime.datetime.now()

backup_dir = f"backup_{service_name}_{now.strftime('%Y%m%d%H%M%S')}"
os.makedirs(backup_dir)

subprocess.run(["docker", "system", "prune", "-f"])

subprocess.run(["docker-compose", "down"])

shutil.copytree("./stacks", f"{backup_dir}/stacks")
shutil.copy2("./docker-compose.yml", backup_dir)
shutil.copy2("./rollback.py", backup_dir)

# Specifies the previous version of the image that you want to use for rollback
print('The versions are written only the numbers example: 1.9.4')
current_version = "v" + input('Write the current version of asppmith: ')
previous_version = "v" + input('Enter the version number you want to return to: ')   

with open("docker-compose.yml", "r") as file:
    compose_file = file.read()

# Replaces the current version of the image with the previous version in the file
compose_file = compose_file.replace(current_version, previous_version)

with open("docker-compose.yml", "w") as file:
    file.write(compose_file)

subprocess.run(["docker-compose", "up", "-d"])

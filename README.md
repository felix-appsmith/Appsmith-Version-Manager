# Appsmith Version Manager (AVM)

AVM or Appsmith version manager is a small program created in python that allows us to control the versions of Appsmith, this means we can go from a new version to an old one or from an old version to a new version in a simple way, the program before making the change of version makes a backup copy of the information that Appsmith has so that you do not lose any of your applications in case of a failure.


Note: before starting, you must add this in the docker compose line that has the Appsmith image.

Normal:
`image:index.docker.io/appsmith/appsmith-ce`

As it should be:
`image: index.docker.io/appsmith/appsmith-ce:v1.9.4`


## Table of Contents

1. [Appsmith Version Manager (AVM)](#appsmith-version-manager-avm)
   - Introduction.
   - Features.
2. [Prerequisites](#prerequisites)
   - Python download and installation.
3. [How to use the program](#how-to-use-the-program)
   - Clone the repository.
   - Give permissions to the script.
   - Run the script.
   - Enter the current version of Appsmith.
   - Enter the version you want to go to from Appsmith.
   - Wait for Appsmith to wake up again.

## Prerequisites to use it

1 Python, download it in this [link](https://www.python.org/downloads/)

## How to use the program

To use this program is very simple.

1. Clone this repository to the same folder where you have your docker-compose.yml you can use this command:

   `git clone https://github.com/felix-appsmith/Appsmith-Version-Manager.git`

2. Give permissions to the script to be executed attached the commands:

   Linux: `chmod +x instalador.sh`
   Windows: `attrib +x instalador.sh`

3. Run the script called start with this command `./start` or `python3 -u rollback.py`

4. Enter the current version of Appsmith example: `1.9.4`

5. Enter the version you want to go to from Appsmith example: `1.9.1`

Done that's all now wait a few minutes for Appsmith to wake up again.

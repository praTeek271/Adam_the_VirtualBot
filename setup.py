import os
import subprocess

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def create_virtual_environment(directory):
    subprocess.run(["python", "-m", "venv", directory])
    print("Virtual environment created.")

def activate_virtual_environment(directory):
    if os.name == "nt":
        activate_script = os.path.join(directory, "Scripts", "activate")
    else:
        activate_script = os.path.join(directory, "bin", "activate")
    subprocess.run(activate_script, shell=True)
    print("Virtual environment activated.")

def install_dependencies(requirements_file):
    subprocess.run(["pip", "install", "-r", requirements_file])
    print("Dependencies installed.")

def setup_adam_bot():
    project_directory = "adam_bot"
    virtualenv_directory = "env"
    requirements_file = "requirements.txt"

    create_directory(project_directory)
    create_virtual_environment(virtualenv_directory)
    activate_virtual_environment(virtualenv_directory)
    install_dependencies(requirements_file)

    # Additional setup tasks can be added here

    print("Adam bot setup completed.")

if __name__ == "__main__":
    setup_adam_bot()

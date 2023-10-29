# Python 101 - Reference Page

This page contains information for getting started with python.

## Create Virtual Environment


* Open the Command Palette (**Ctrl+Shift+P**), start typing the **Python: Create Environment** command to search, and then select the command.
* The command presents a list of environment types, Venv or Conda. For this example, select  **Venv** .
* After selecting the interpreter, a notification will show the progress of the environment creation and the environment folder (`/.venv`) will appear in your workspace.
* Ensure your new environment is selected by using the **Python: Select Interpreter** command from the  **Command Palette** .

Online Reference - [Get Started Tutorial for Python in Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial#_create-a-virtual-environment)

## Import Packages

```python
# macOS
python3 -m pip install numpy

# Windows (may require elevation)
py -m pip install numpy

# Linux (Debian)
apt-get install python3-tk
python3 -m pip install numpy
```

Online Reference - [Get Started Tutorial for Python in Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial#_install-and-use-packages)

# Python TKinter tutorial

## Installation on ubuntu

* Install the package **tk-dev** using `sudo apt-get install -y tk-dev`.
* `env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.7.0` to install python 3.7.0. **PYTHON_CONFIGURE_OPTS="--enable-shared"** env needs to be set for pyinstaller to work.
* **tkinter** and **tkmessagebox** ship with python by default.
* `python -m tkinter` should open a window. This verifies tkinter installation

**NOTE**: If you already have a python version installed using pyenv before installing the **tk-dev** package, then you have to uninstall and install the python version again after installing **tk-dev** for tkinter to work.

```bash
# without tk-dev below command raises the following error
# ModuleNotFoundError: No module named '_tkinter'
python -m tkinter

# install tk-dev
sudo apt-get install -y tk-dev

# uninstall the python version using pyenv
python --version
pyenv uninstall 3.7.0

# install the version again
pyenv install 3.7.0

# verify the installation
python --version
```

## Using this repo

* Clone this repo
* `pipenv --python 3.7.0 install --dev` to install all the dependent packages.

## Creating distributable using pyinstaller

* Distributable will be available in the **hello_world/dist** folder

```Bash
# On Windows and Ubuntu
cd hello_world
pyinstaller --onefile --windowed hello_world.py

# Mac
pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' hello_world.py
```

## Learning it using online IDE

* [REPL.it](https://repl.it/languages/python3) supports tkinter development, debugging and running it online. Its very useful for adhoc learning.

## Documentation

* [Python3 tkinter](https://docs.python.org/3/library/tk.html)

---

## References

* [Pyinstaller](https://www.pyinstaller.org/)
* [Pyenv with pyinstaller](https://pyinstaller.readthedocs.io/en/stable/development/venv.html)
* [TKinter part manager app](https://github.com/bradtraversy/part_manager)

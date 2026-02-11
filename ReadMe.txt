Its a calculator. No need to explain much. :)

## Build (Windows)
pip install -U pyinstaller
py -m PyInstaller --onefile --windowed --distpath . --add-data "Icon_Calculator_16x16.ico;." --icon=Icon_Calculator_16x16.ico c_00_main.py -n Taschenrechner

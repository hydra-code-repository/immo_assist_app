import streamlit.web.cli as stcli
import sys
import os

if __name__ == '__main__':
    # Obtain the directory where is the executable
    if getattr(sys, 'frozen', False):
        # If executing with executable PyInstaller
        application_path = sys._MEIPASS
    else:
        # If executing with script Python
        application_path = os.path.dirname(os.path.abspath(__file__))

    # Path to the main file (CHANGE THE FILES NAME)
    main_script = os.path.join(application_path, 'src', 'main.py')

    sys.argv = [
        "streamlit",
        "run",
        main_script,
        "--server.port=8502", # Port chosen
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())
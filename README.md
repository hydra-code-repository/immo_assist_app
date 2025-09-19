# 🔐 Immobilizer Assistant

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-latest-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Build](https://img.shields.io/github/actions/workflow/status/your-username/immo_assist_app/test.yml?branch=main)

A Streamlit application for internal company use that provides vehicle anti-theft system verification and key learning procedures.

## Overview
This project is an extension of [vehicle_security_system_data_cleaning](https://github.com/hydra-code-repository/vehicle_security_system_data_cleaning) where the initial data cleaning and preparation was performed. The cleaned datasets are now used in this application to serve vehicle security information and procedures.

## Features
- Intuitive interface with dropdown menus for vehicle selection
- Vehicle anti-theft system verification
- PDF key learning procedures for:
  - Ford vehicles
  - Lincoln vehicles
  - Mercury vehicles
  - GM brand vehicles (Chevrolet, GMC, Buick, etc.)
  - Mazda vehicles
- Data caching for optimal performance
- Standalone executable for systems without Python

## Technical Details

### Data Structure
- Individual CSV files for each manufacturer
- Optimized data filtering and management
- Local PDF document storage organized by manufacturer

### Tech Stack
- Python 3.12
- Streamlit
- Pandas
- PyInstaller (for executable creation)

## Installation

### Method 1: Using Executable
1. Download the latest release
2. Run `ImmobilizerAssistant.exe`
3. No additional installation required

### Method 2: Development Setup
1. Clone the repository
2. Install dependencies:
```cmd
pip install -r requirements.txt
```
3. Run the application:
```cmd
streamlit run src/main.py
```

## Project Structure
```
Immo_Assist_App/
├── src/
│   └── main.py
├── data/
│   ├── df_ford.csv
│   ├── df_gm.csv
│   ├── df_mazda.csv
│   └── ...
└── docs/
    ├── Ford/
    ├── GM/
    ├── Mazda/
    └── ...
```

## Data Source
The application uses cleaned and structured data from the [vehicle security system data cleaning project](https://github.com/hydra-code-repository/vehicle_security_system_data_cleaning), which processed the original dataset into manufacturer-specific CSV files.

## Build Instructions
To create the standalone executable:
```cmd
pyinstaller --onefile --name ImmobilizerAssistant src/main.py
```

## CI/CD
GitHub Actions workflow is configured to:
- Run automated tests
- Verify code functionality
- Ensure data integrity

## License
MIT

---
**Note**: This application is for internal company use only and provides quick access to vehicle anti-theft system information and key learning procedures. 

## Contact
For questions or suggestions, contact [Weverson Barbieri](https://github.com/weversonbarbieri).

# 🔐 Immobilizer Assistant

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-latest-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Build](https://img.shields.io/github/actions/workflow/status/your-username/immo_assist_app/test.yml?branch=main)

A Streamlit application for internal company use that provides vehicle anti-theft system verification and key learning procedures with standalone executable support.

## Overview
This project is an extension of [vehicle_security_system_data_cleaning](https://github.com/hydra-code-repository/vehicle_security_system_data_cleaning) where the initial data cleaning and preparation was performed. The cleaned datasets are now used in this application to serve vehicle security information and procedures. The application has been enhanced with PyInstaller to create a standalone executable for deployment on machines without Python dependencies.

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
- Standalone executable for systems without Python or dependencies
- Complete distribution package with all required files

## 🎥 Application Demonstration

See the application in action in the video below:

[![Immobilizer Assistant Demo](https://img.shields.io/badge/🎬-View%20Demo-blue?style=for-the-badge)](https://vimeo.com/1121684000?share=copy)

*The video demonstrates:*
- Main application interface
- Manufacturer, year, and model selection
- Anti-theft system verification
- PDF procedure downloads
- Standalone executable functionality

## Technical Details

### Data Structure
- Individual CSV files for each manufacturer
- Excel database with comprehensive vehicle information
- Optimized data filtering and management
- Local PDF document storage organized by manufacturer

### Tech Stack
- Python 3.12
- Streamlit (Web Framework)
- Pandas (Data Processing)
- PyInstaller (Executable Creation)
- GitHub Actions (CI/CD Pipeline)

## Installation & Usage

### Method 1: Standalone Executable (Recommended for End Users)
1. Download the complete distribution package (`ImmobilizerAssistant_v1.0.zip`)
2. Extract all files maintaining the folder structure:
```
ImmobilizerAssistant/
├── run_immo_assist_app.exe
├── data/
│   └── (CSV and Excel files)
└── docs/
    └── (PDF procedures by manufacturer)
```
3. Run `run_immo_assist_app.exe`
4. Application will start on `http://localhost:8502`
5. No Python installation required

### Method 2: Development Setup
1. Clone the repository
```bash
git clone https://github.com/your-username/immo_assist_app.git
```
2. Create and activate virtual environment:
```cmd
python -m venv venv
venv\Scripts\activate
```
3. Install dependencies:
```cmd
pip install -r requirements.txt
```
4. Run the application:
```cmd
streamlit run src/main.py
```

## Project Structure
```
Immo_Assist_App/
├── src/
│   └── main.py                    # Main Streamlit application
├── data/
│   ├── year_make_model_df.xlsx    # Main database
│   ├── df_ford.csv               # Ford-specific data
│   ├── df_gm.csv                 # GM-specific data
│   ├── df_mazda.csv              # Mazda-specific data
│   └── ...                       # Other manufacturer data
├── docs/
│   ├── Ford/                     # Ford procedure PDFs
│   ├── GM/                       # GM procedure PDFs
│   ├── Mazda/                    # Mazda procedure PDFs
│   └── ...                       # Other manufacturer PDFs
├── build/                        # PyInstaller build files
├── dist/
│   └── run_immo_assist_app.exe   # Standalone executable (118MB)
├── .github/workflows/
│   └── test.yml                  # CI/CD pipeline
├── run_immo_assist_app.py        # Entry point for executable
├── run_immo_assist_app.spec      # PyInstaller configuration
└── requirements.txt              # Python dependencies
```

## Data Source
The application uses cleaned and structured data from the [vehicle security system data cleaning project](https://github.com/hydra-code-repository/vehicle_security_system_data_cleaning), which processed the original dataset into manufacturer-specific CSV files and organized PDF procedures.

## Build Instructions

### Creating the Executable
1. Ensure all dependencies are installed:
```cmd
pip install pyinstaller
```

2. Clean previous builds:
```cmd
rmdir /s /q build dist
```

3. Build the executable:
```cmd
pyinstaller run_immo_assist_app.spec --log-level INFO
```

4. Create distribution package:
```cmd
mkdir ImmobilizerAssistant
copy dist\run_immo_assist_app.exe ImmobilizerAssistant\
xcopy /E /I data ImmobilizerAssistant\data
xcopy /E /I docs ImmobilizerAssistant\docs
```

### Distribution Package
The final executable includes:
- Complete Streamlit framework
- All Python dependencies
- Application data files
- PDF procedure documents
- **Size**: ~118MB standalone file

## System Requirements
- **For Executable**: Windows 10+ (no additional requirements)
- **For Development**: Python 3.12+, pip, virtual environment

## Author
Developed by [Weverson Barbieri de Oliveira](https://github.com/weversonbarbieri)
E-mail: weverson.b@mintt.com 

## License
MIT

---
**Note**: This application is for internal company use only and provides quick access to vehicle anti-theft system information and key learning procedures. The standalone executable ensures deployment flexibility across different system configurations without requiring Python installation.

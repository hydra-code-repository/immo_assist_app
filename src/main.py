import streamlit as st
import pandas as pd
import os
import re
import sys
                       

# Configure Streamlit page settings
def setup_page_config():
    st.set_page_config(
        page_title='Immobilizer Assistant',
        page_icon=':closed_lock_with_key:',
        layout='centered',
        initial_sidebar_state='expanded'
    )

# Set and Show the headers using HTML.
st.write("<div align='center'><h2><i>Immobilizer Assistant</i></h2></div>", unsafe_allow_html=True)
st.write("<div align='left'><h2 style='font-size: 20px;'><i>Please, select Make, Year and Model desired:</i></h2></div>", unsafe_allow_html=True)

# Security Procedures Configuration Dictionary 
# Each procedure is mapped to a specific PDF file in the manufacturer folder
SECURITY_PROCEDURES = {
    # Ford Motor Company Brands
    # These brands share common PATS (Passive Anti-Theft System) procedures
    'Ford': {
        'PATS Type A': {'pats_a.pdf'},   
        'PATS Type B': {'pats_a.pdf'},   
        'PATS Type C': {'pats_a.pdf'},
        'PATS Type D': {'pats_d.pdf'},
        'PATS Type E': {'pats_e.pdf'},
        'Parameter Reset Required': {'parameter_reset.pdf'},
        'PATS Type B (Stand Alone PATS Module)': {'parameter_reset.pdf'},
        'PATS Type C (Powertrain Control Module)': {'pats_a.pdf'},
        'PATS Type E (Powertrain Control Module)': {'pats_e.pdf'},
        'PATS Type G (Instrument Cluster)': {'parameter_reset.pdf'},
    },

    # Mazda - Former Ford partner (1979-2015)
    # Uses unique immobilizer system (M-Series) with different procedures
    # Each M-type corresponds to a specific immobilizer generation
    'Mazda': {
        'M-A': {'mazda_ma.pdf'},
        'M-B': {'mazda_mb.pdf'},
        'M-C': {'mazda_mc.pdf'},
        'M-D': {'mazda_md.pdf'},
        'M-E': {'mazda_me.pdf'},
        'M-F': {'mazda_mf.pdf'},
        'M-G': {'mazda_mg.pdf'},
        'M-H': {'mazda_mh.pdf'},
    },

    # GM Division Brands
    # All GM brands share common anti-theft systems:
    # - PASSLOCK: First generation vehicle anti-theft system
    # - PK2: Second generation PASSKEY system
    # - PK3: Latest PASSKEY system with rolling code technology
    'GM': {   # Luxury division, still active
        'PL1': {'gm_passlock.pdf'},
        'PL2': {'gm_passlock.pdf'},
        'PL3': {'gm_passlock.pdf'},
        'PK2': {'gm_passkey_2.pdf'},
        'PK3': {'gm_passkey_3.pdf'}
    }
}

# List with manufaturers with the key relearns avaialable for download 
makes_procedures_list = ['Ford', 'Lincoln', 'Mazda', 'Mercury', 
                         'Chevrolet', 'Pontiac', 'Cadillac', 
                         'Buick', 'Oldsmobile', 'GMC', 'Saturn', 'Hummer'
                         ]

# Function to obtain the correct path from the data
def get_data_path(filename):
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(application_path, filename)

# This function creates the path to the main xlsx file from this project
# Uses os library methods to ensure the file path works in both local and GitHub CI/CD environments
def create_file_path(file_relative_path, dir):
    # Get base path depending on if running as exe or script
    if getattr(sys, 'frozen', False):
        # if running as exe (PyInstaller bundle)
        base_path = sys._MEIPASS
    else:
        # If running as script
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Construct full directory path
    dir_path = os.path.join(base_path, dir)

    # Iterate under dir data to have all files
    for filename in os.listdir(dir_path):
        # Condition to confirm which file is == year_make_model_df.xlsx
        if filename.endswith(file_relative_path):
            # Join the dir + filename to create the path to year_make_model_df.xlsx file  
            file_full_path = os.path.join(dir, filename)
    # Return the full file path
    return file_full_path

# Function to create the pdf file path based on the security system and make given
def create_dir_path(manufaturer_name, security_name):
    # Create a simple string from the security procedures dict based on the make and string found in the security row
    relative_procedure_path = list(SECURITY_PROCEDURES[manufaturer_name][security_name])[0]
    # Unite the docs file name along with the make name to create the directory path
    dir_path = 'docs/' + manufaturer_name
    # Call the function to create the relative pdf file path
    full_pdf_path = create_file_path(relative_procedure_path, dir_path)
    # Return the full relative pdf path
    return full_pdf_path

# Cache the function to avoid reloading the data multiple times
@st.cache_data
def create_doc_file_path(vehicle_info_selected):
    """
    Create file path for PDF document based on vehicle information

    Args:
        vehicle_info_selected: DataFrame row containing vehicle make and security system information

    Returns:
        str: Full path to the PDF file if found
        None: If no matching PDF file is found
    """
    try:
        # First find the make name which requires key relearn.
        for section, string in vehicle_info_selected.items():
            # Condition to select if make is under the list
            if string in makes_procedures_list:
                # Stores the make name in a var
                make_name = string
                break 

        # Condition when Mazda is the make
        if make_name == 'Mazda':
            # Loop to iterate under vehicle selected info       
            for col, data in vehicle_info_selected.items():
                # Condition when Security is the column and when the Mazda security code is under security section
                if col == 'Security' and data in ['M-A', 'M-B', 'M-C', 'M-D', 'M-E', 'M-F', 'M-G', 'M-H']:
                    # Call the function to create the pdf file path based on the security system and 'Mazda' file
                    return create_dir_path('Mazda', data)
                # Condition when Security is the column and when the Mazda security code IS NOT under security section
                elif col == 'Security' and data not in ['M-A', 'M-B', 'M-C', 'M-D', 'M-E', 'M-F', 'M-G', 'M-H']:
                    # Remove all whitespaces
                    data_stripped = data.strip()
                    # Call the function to create the pdf file path when it is from Ford anti-theft system
                    return create_dir_path('Ford', data_stripped)
                        
        # Condition when Ford, Mercury or Lincoln is the make
        elif make_name in ['Ford', 'Lincoln', 'Mercury']:
            # Loop to iterate under vehicle selected info
            for col, data in vehicle_info_selected.items():
                # Condition when the parameter reset is required,
                # there is just one procedure
                if col == 'ParameterReset' and data == 'Parameter Reset Required':
                    # Remove whitespaces from relearn procedure names 
                    security_name_stripped = data.strip()
                    # Call the function to create the pdf file path based on the security system and 'Ford' file
                    return create_dir_path('Ford', security_name_stripped)
            # Pats type column is before the parameter reset column, 
            # that's why needs to iterate under the vehicle info again 
            for colu, information in vehicle_info_selected.items():
                if colu == 'PATS Type':
                    # Remove whitespaces from relearn procedure names 
                    security_name_stripped = information.strip()
                    # Call the function to create the pdf file path based on the security system and 'Ford' file
                    return create_dir_path('Ford', security_name_stripped)      
    
        # Condition when Ford, Mercury or Lincoln is the make
        elif make_name in ['Chevrolet', 'Pontiac', 'Cadillac', 'Buick', 'Oldsmobile', 'GMC', 'Saturn', 'Hummer']:
            # Loop to iterate under vehicle selected info
            for col, data in vehicle_info_selected.items():
                # Condition when the security is one of the columns
                if col == 'Security':
                    # Remove whitespaces from relearn procedure names
                    security_name_stripped = data.strip()
                    # Call the function to create the pdf file path based on the security system and 'GM' file
                    return create_dir_path('GM', security_name_stripped)
        
    # Return None if no path found
    except Exception as e:
        # Log error silently without displaying to user
        # st.write(f"Error creating download button: {str(e)}") # For debugging
        pass # Silent failure
    

# Read excel by calling to function to create the path first
df = pd.read_excel(create_file_path('year_make_model_df.xlsx', 'data'))

# Function to get an array with sorted manufacturers
def get_manufacturer_list(df: pd.DataFrame) -> list:
    # Method to get unique values
    makes_list = df['Make'].unique()
    # Return sorted values
    return sorted(makes_list)

# Function to get an array with sorted manufacturers
def get_year_list(df: pd.DataFrame) -> list:
    # Method to get unique values
    years = df['Year'].unique()
    # Return sorted values
    return sorted(years)

# Call the function to get the manufacturers list and show under a select box
selected_make = st.sidebar.selectbox('Make: ', (get_manufacturer_list(df)))

# Function to create the df name based on the selected make
def create_df_name(make):
    # When not one of these makes, no special string treatment needed,
    # need just lower the make name and add strings to match the df make
    if make not in ['Rolls-Royce', 'Land Rover']:
        # Add 'df_' string and the extension file .csv to the make lowered
        file_path = f'df_{selected_make.lower()}.csv'
    else:
        # Replace hyphens and spaces with underscores
        table_renamed = re.sub(r'[-\s]', '_', selected_make)
        # Add the strings 'df_' and '.csv' to the file path to match the files names on the data directory
        file_path = f'df_{table_renamed.lower()}.csv'
    # Return a string to match the df name
    return file_path

# Function to filter the Dataframe by selected year
def filter_by_year(df:pd.DataFrame, year: str) -> pd.DataFrame:
    # Return the df based on year selected
    return df[df['Year'] == year]

# Function to get sorted list of models for selected year
def get_model_list(df_selected: pd.DataFrame) -> pd.DataFrame:
    # Create an array with unique models
    models = df_selected['Model'].unique()
    # Return the array with sorted values
    return sorted(models)

# Function to extract vehicle details from final selection
def get_vehicle_info(df:pd.DataFrame) -> dict:
    # Select the vehicle info considering the index position 0
    data_final_df = df.iloc[0]
    # Return a dictionary with the vehicle info selected
    return dict(data_final_df)

# Function to display formatted vehicle information
def display_vehicle_info(vehicle_info: dict):
    # Loop to iterate under vehicle information
    for col, data in vehicle_info.items():
        # Dataframes from GM brands are coming with a unknown column.
        # This condition deletes the column 'Unnamed: 0'
        if col is not ['Unnamed: 0']:
            # Print the column with color red and data under each column 
            st.write(f'''**:red[{col}:]** {data}''')

# Call the function rename the make selected
df_name = create_df_name(selected_make)

# Call the function to get the df from Data dir
make_selected = pd.read_csv(create_file_path(df_name, 'data'))

# Call the function to get the years list and show under a select box
selected_year = st.sidebar.selectbox('Year: ', (get_year_list(make_selected)))

# Filter DataFrame by selected year and create model dropdown
df_filtered_after_year_selected = filter_by_year(make_selected, selected_year)

# Call the function to get a model list and show under a selectbox
selected_model = st.sidebar.selectbox('Model: ', (get_model_list(df_filtered_after_year_selected)))


# ---------------------------------------------------------- #
# Call the function to get df_make based on the year selected to obtain the final dataframe
final_df = df_filtered_after_year_selected[df_filtered_after_year_selected['Model'] == selected_model]

# Call the function vehicle information based on the year, make and model selected
dict_final_df = get_vehicle_info(final_df)

# Call the function to display the vehicle information.
display_vehicle_info(dict_final_df)

# Error hadling when the file path is not valid
try:
    # Call the function to create the pdf file path
    file_name = create_doc_file_path(dict_final_df)

    # Condition to show download button if file exists
    if file_name:
        # Show message above the download button
        st.write("**:blue[Click on the button to download the Key Relearn Procedure]**")
        # Open the pdf file based on the file name generated
        with open(file_name , 'rb') as pdf_file:
            # Read the pdf file 
            pdf_bytes = pdf_file.read()
            # Method to create a button to download the key relearn procedure
            st.download_button(
                # Label de button
                label='Key Relearn Procedure',
                # Store the pdf file bytes under a var
                data=pdf_bytes,
                # File name when downloaded locally
                file_name=file_name,
                # Type of the data, in this case pdf format
                mime="application/pdf",
                key= f'pdf-{file_name}'  # Unique key per file
        )
except Exception as e:
    # Log error silently without displaying to user
    # st.write(f"Error creating download button: {str(e)}")  # For debugging
    pass  # Silent failure

    
# streamlit run "C:\Language_Projects\Language_Projects\Python\Flagship_1\Immo_Assist_App\src\main.py"
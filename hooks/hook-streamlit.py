from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Collect files of data from streamlit
datas = collect_data_files('streamlit')

# Collect submodules from Streamlit
hiddenimports = collect_submodules('streamlit')

# add especific imports that can be requested
hiddenimports += [
    'streamlit.we.cli',
    'streamlit.web.server.server',
    'streamlit.runtime.scriptrunner.script_runner',
    'streamlit.runtime.state.session_state',
    'streamlit.components.v1.components',
    'streamlit.elements.form',
    'streamlit.elements.widgets',
    'streamlit.runtime.caching',
    'streamlit.runtime.legacy_caching',
    'importlib.metadata',
    'importlib_metadata'
]

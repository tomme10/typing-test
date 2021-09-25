from cx_Freeze import setup, Executable

setup(name='typeTest', 
      version='0.1', 
      description='',
      #options = {'build_exe': {'includes': additional_mods}},
      executables = [Executable('main.py')]
    )
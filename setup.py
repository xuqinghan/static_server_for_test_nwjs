'''
python setup.py build
python setup.py bdist_msi


ImportError: No module named 'blinker'

pip uninstall blinker
pip install --use-pep517 blinker



'''

import sys
from cx_Freeze import setup, Executable
import os
import shutil

import sys
#base = 'WIN32GUI' if sys.platform == "win32" else None
#控制台
base = None

# if not os.path.exists(os.path.join(sys.base_prefix,"DLLs")) and hasattr(sys,"real_prefix"):
#     shutil.copytree(os.path.join(sys.real_prefix,"DLLs"), os.path.join(sys.base_prefix,"DLLs"))
# 'eventlet', 'dns', , 'threading', 'time', 'queue' 'engineio', 'socketio', 'flask_socketio', 
# Dependencies are automatically detected, but it might need fine tuning.
options = {'includes': [], #子模块XX.xxx
            'include_files': ['static', 'README.md'],
            "packages": ['jinja2.ext'], # 'fcntl'手工创建
            "excludes": ['PIL', 'PyQt5', 'matplotlib', 'scipy', 'numba', 'Cython', 'GDAL', 'tkinter', 'pytz', 'numpy', 'zmq', 'tornado', 'greenlet', 'IPython', 'jupyter_client', 'notebook', 'nose', 'OpenSSL', 'distutils', 'test', 'win32com',
             'pydoc_data', 'unittest',
            'cryptography', 'pkg_resources', #flask依赖，但这个项目不依赖
             ],
            "build_exe": '../build/static_server_nw',
            #"build_exe": 'D:/dev/ne/seim-frontend-mobile/client/backend',
            }

# GUI applications require a different base on Windows (the default is for a
# console application).


setup(  name = "静态web服务器测试nw",
        version = "0.1",
        description = "静态web服务器测试nw",
        options = {"build_exe": options},
        executables = [Executable("app.py", base=base)])
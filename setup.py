import matplotlib
import FileDialog
import sys
from distutils.core import setup
import py2exe

sys.setrecursionlimit(10000)
setup(windows=['BiometricSystem.py'],
      options={ 
                'py2exe': { 
                "includes" : ["PIL","datetime","matplotlib.backends.backend_tkagg","cv2","numpy","scipy.special._ufuncs_cxx","scipy.linalg.*","scipy.sparse.csgraph._validation"],

                'excludes': ['_gtkagg', '_tkagg', '_agg2', '_cairo','_cocoaagg', 
                              "matplotlib.numerix.fft","sip", "PyQt4._qt",
                              "matplotlib.backends.backend_qt4agg",
                              "matplotlib.numerix.linear_algebra", 
                              "matplotlib.numerix.random_array",
                             '_fltkagg', '_gtk','_gtkcairo' ],

                'dll_excludes': ['libgdk-win32-2.0-0.dll',
                                 'libgobject-2.0-0.dll' ,
                                 'MSVCP90.dll',"MSVFW32.dll",
                 "AVIFIL32.dll",
                 "AVICAP32.dll",
                 "ADVAPI32.dll",
                 "CRYPT32.dll",
                 "WLDAP32.dll"]
              }

                },

      data_files=matplotlib.get_py2exe_datafiles(),) 
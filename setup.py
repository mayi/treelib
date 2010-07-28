# setup.py

from distutils.core import setup
import py2exe

setup(windows=[{"script" : "main.pyw", "icon_resources": [(1, "treeleaf.ico")]}], options={"py2exe" : {"includes" : ["sip"], "bundle_files": 1}})

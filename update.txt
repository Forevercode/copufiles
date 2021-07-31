from work.working import Working
import os

path=r"C:\Users\user\PycharmProjects\work\venv\Lib\site-packages\work"
session2=r"C:\Users\user\OneDrive\桌面\python\python_script\session1\work"

job=Working(session2)

job.copy_scripts(py_dir=path,keyword="work")



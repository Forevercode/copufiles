import os
import sys
from workset.baseclass import BaseGet
from workset.writeclass import WriteMethod
from workset.holdingpath import NewDir, NewFile
from workset.value import Keyword,Filetype
from workset.error import Nofile_working

from workset.usefultool import Tool1, DirectoryWalk

import re


# -*- coding: utf-8 -*-

class Working:
    def __init__(self, file_system_path=None):
        if type(file_system_path) != str:
            raise ValueError(f"Paramater:{file_system_path} can be string only")

        self.file_system_path = file_system_path

        # getter and setter

    @property
    def file_system_path(self):
        return self._file_system_path

    @file_system_path.setter
    def file_system_path(self, file_system_path):
        if type(file_system_path) != str:
            raise ValueError(f"Paramater:{file_system_path} can be string only")
        self._file_system_path = file_system_path

    def copy_all_scripts(self, directory,filetype="txt",binaryfiletype="png"):

        result = DirectoryWalk.walk_directory(directory)
        for each_fir in result:
            self.copy_scripts(each_fir,filetype=filetype,binaryfiletype=binaryfiletype)


    def copy_scripts(self, py_dir, keyword=Keyword.pycharm,filetype="txt",binaryfiletype="png"):
        try:
            # get the python files under (py_dir)
            files = BaseGet._get_files(py_dir)
            if files == None:
                raise Nofile_working

            # create new dir in file_system_path
            path_sample = files[0][0]

            new_dir = NewDir._with_original_path(path_sample=path_sample, file_system_path=self.file_system_path,
                                                 keyword=keyword)

            if os.path.exists(new_dir) == False:
                os.makedirs(new_dir)

            # loop throught all file and copy all
            for file in files:
                # use try to hlod binary file
                try:
                    # make new file path
                    new_script = NewFile.newfile(dir=new_dir, filename=file[1],filetype=filetype)
                    # write
                    WriteMethod._write_script(copied=file[0], copy_to=new_script)
                    print(f"以複製:\n{file[0]}")


                except UnicodeDecodeError:
                    os.remove(new_script)
                    new_script = NewFile.newfile(dir=new_dir, filename=file[1],filetype=binaryfiletype)

                    WriteMethod._write_binary(copied=file[0], copy_to=new_script)
                    print(f"以複製<binary file>:\n{file[0]}")
        except Nofile_working:
            print(f"No file under directory: {py_dir}.__working")

    def copy_script(self, py_path, keyword=Keyword.pycharm,filetype="txt",binaryfiletype="png"):

        try:

            # create new dir in os_dir(new_os_dir=od_dir+ last_componet_of_path)

            new_dir = NewDir._with_original_path(file_system_path=self.file_system_path, path_sample=py_path,
                                                 keyword=keyword)

            if os.path.exists(new_dir) == False:
                os.makedirs(new_dir)

            # use another try to hold binary file
            try:
                # make new file path
                filename = py_path.split("\\")[len(py_path.split("\\"))]
                new_script = NewFile.newfile(dir=new_dir, filename=filename,filetype=filetype)
                # write
                WriteMethod._write_script(copied=py_path, copy_to=new_script)


            except UnicodeDecodeError:
                os.remove(new_script)

                new_script = NewFile.newfile_png(dir=new_dir, filename=filename,filetype=binaryfiletype)
                WriteMethod._write_binary(copied=py_path, copy_to=new_script)
                print(f"以複製<binary file>:\n{py_path}")

        except Exception:
            print(f"\n<<No such  path:{py_path}>>__working\n")







    def simply_copy_scripts(self, py_dir,filetype="txt",binaryfiletype="png"):
        try:
            files = BaseGet._get_files(root=py_dir)
            if files == None:
                raise Nofile_working

            for file in files:
                try:
                    new_script = NewFile.newfile(dir=self.file_system_path, filename=file[1],filetype=filetype)
                    WriteMethod._write_script(copied=file[0], copy_to=new_script)

                    print(f"以複製:\n{file[0]}")

                except UnicodeDecodeError:
                    os.remove(new_script)
                    new_script = NewFile.newfile(dir=self.file_system_path, filename=file[1],filetype=binaryfiletype)
                    WriteMethod._write_binary(copied=file[0], copy_to=new_script)

                    print(f"以複製<<binary file>>:\n{file[0]}")
        except Nofile_working:
            print(f"No file under directory {py_dir}.__working\n")


    def simply_copy_script(self, py_path,filetype="txt",binaryfiletype="png"):
        # use  try to hold binary file
        try:
            # make new file path
            filename = py_path.split("\\")[len(py_path.split("\\"))]
            new_script = NewFile.newfile(dir=py_path, filename=filename,filetype=filetype)
            # write
            WriteMethod._write_script(copied=py_path, copy_to=new_script)

            print(f"以複製:\n{py_path}")

        except UnicodeDecodeError:
            os.remove(new_script)

            new_script = NewFile.newfile(dir=py_path, filename=filename,filetype=binaryfiletype)
            WriteMethod._write_binary(copied=py_path, copy_to=new_script)

            print(f"以複製<binary file>:\n{py_path}")

    #  def copy_all_script_(self):

    # take  full path only
    def clear_flie(self, file_full_path):
        try:
            with open(file_full_path, "w") as item:
                print(item.write(""))
        except FileNotFoundError:
            print(f"ERROR  The file:{file_full_path} doesn't exists")

    # take  full path only
    def clear_mutiple_files(self, paths):

        for path in paths:
            try:
                with open(path, "w") as item:
                    print(item.write(""))

            except FileNotFoundError:
                print(f"The file{path} doesn't exists")

    def files(self, root):
        return Tool1.files(root)

    def dirs(self, root):
        return Tool1.dirs(root)


if __name__ == "__main__":
    job = Working(r"/work")
    job.simply_copy_scripts(py_dir=r"C:\Users\user\PycharmProjects\work\work")

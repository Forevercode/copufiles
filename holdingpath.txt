import os
from workset.value import Keyword
from workset.error import FiletypeError


class NewDir:
    def _with_original_path(path_sample, file_system_path, keyword):
        index = path_sample.split("\\").index(keyword) + 1
        componet_of_path = "\\".join(path_sample.split("\\")[index:len(path_sample.split("\\")) - 1])

        return os.path.join(file_system_path, componet_of_path)


class NewFile:
    def newfile(dir, filename,filetype):
        if len(filename.split(".")) > 3:
            raise FiletypeError(f"Too many dot included in filename <<{filename}>>")

        if len(filename.split(".")) == 1:
            filename = f"{filename}.{filetype}"
            return os.path.join(dir,filename)

        elif len(filename.split(".")) == 2:
            filename_firstcomponent = filename.split(".")[0]
            filename = f"{filename_firstcomponent}.{filetype}"
            return os.path.join(dir, filename)
        elif len(filename.split(".")) == 3:
            filename_firstcomponent = filename.split(".")[0]
            filename = f"{filename_firstcomponent}.{filetype}"
            return os.path.join(dir, filename)


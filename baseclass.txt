import os
import sys


class BaseGet:

    def _get_files(root):
        try:

            result = []

            # record cwd for now
            cwd = os.getcwd()
            # change current working derectory
            os.chdir(root)

            files_dirs = os.listdir()

            for file in files_dirs:
                if os.path.isfile(file):
                    result.append((os.path.join(root, file), file))  # (full path,item)

            # check if there is any file in this path
            if len(result) != 0:
                return result

            os.chdir(cwd)
            raise Exception

        except FileNotFoundError:
            print(f"FileNotFoundError:No such directory({root})")
        except Exception:
            print(f"No file under directory {root}")

    def _get_dirs(root):
        try:
            result = []
            # record cwd for now
            cwd = os.getcwd()
            # change current working derectory
            os.chdir(root)

            files_dirs = os.listdir()
            for dir in files_dirs:
                if os.path.isdir(dir):
                    result.append((os.path.join(root, dir), dir))  # (full path,item)

            # make sure at least one dir under the root
            if len(result) == 0:
                raise Exception(f"No dirs in path:{root}")

            os.chdir(cwd)
            return result

        except FileNotFoundError:
            print(f"FileNotFoundError:No such directory({root})")
        except Exception:
            print(f"No direcctory under directory {root}")


if __name__ == "__main__":
    oop_path = r'C:\Users\pands\PycharmProjects\oop\work'
    a = BaseWorking()
    s = a.files(oop_path)

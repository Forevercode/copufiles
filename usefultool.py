from workset.baseclass import BaseGet


class Tool1(BaseGet):
    def files(root):
        try:
            files = BaseGet._get_files(root=root)
            return (file[0] for file in files)
        except Exception:
            print(f"Error : No file in path:{root}")

    def dirs(root):
        try:
            result = BaseGet._get_dirs(root=root)
            dirs = [dir[0] for dir in result]
            return dirs
        except Exception:
            pass


class DirectoryWalk(Tool1):

    def walk_directory(directory):
        all_dir_path = []

        t1 = (Tool1.dirs(directory))
        if t1 != None:

            for i in t1:
                all_dir_path.append(i)
                t2 = Tool1.dirs(i)

                if t2 != None:

                    for i in t2:
                        all_dir_path.append(i)
                        t3 = Tool1.dirs(i)

                        if t3 != None:

                            for i in t3:
                                all_dir_path.append(i)
                                t4 = Tool1.dirs(i)

                                if t4 != None:

                                    for i in t4:
                                        all_dir_path.append(i)
                                        t5 = Tool1.dirs(i)

                                        if t5 != None:
                                            for i in t5:
                                                all_dir_path.append(i)
                                                t6 = Tool1.dirs(i)

                                                if t6 != None:
                                                    for i in t6:
                                                        all_dir_path.append(i)
                                                        t7 = Tool1.dirs(i)

                                                        if t7 != None:
                                                            for i in t7:
                                                                all_dir_path.append(i)
                                                                t8 = Tool1.dirs(i)

                                                                if t8 != None:
                                                                    for i in t8:
                                                                        all_dir_path.append(i)
            print(all_dir_path)
            return all_dir_path


if __name__ == "__main__":
    a = DirectoryWalk()
    print(a.walk_directory(r"C:\Users\user\PycharmProjects"))
from working import Working

job=Working(r"C:\Users\pands\OneDrive\桌面\file_managent")

more_dir=job.dirs(r"C:\Users\pands\PycharmProjects\work")[2]
job.simply_copy_scripts(r"C:\Users\pands\PycharmProjects\work",filetype="py")
job.simply_copy_scripts(more_dir,filetype="py")

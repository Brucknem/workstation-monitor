import os
from notebook import notebookapp

cwd = os.getcwd()
runfiles_dir = cwd.split("run.runfiles")[0]
bark_root = os.path.join(runfiles_dir, "run.runfiles/workspace_monitor/python")

os.chdir(bark_root)

notebookapp.main()
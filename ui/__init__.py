import sys, os

curr_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

#Add all paths pointing to icons here
sys.path.insert(0, curr_dir + "/ui/py_ui/")

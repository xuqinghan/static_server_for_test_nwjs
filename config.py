import yaml
import sys
import os
from pathlib import Path

#学员答案索引表 保存日期，学员开始答卷时间，学员结束答卷时间
columns_answer =  ['datetime_beg', 'datetime_end', 'name_student', 'name_exercise', 'score']


if getattr(sys, 'frozen', False):
    # The application is frozen
    basedir = os.path.dirname(sys.executable)
    ENV = 'prod'
else:
    # The application is not frozen
    # Change this bit to match where you store your data files:
    basedir = os.path.abspath(os.path.dirname(__file__))
    ENV = 'dev'

#-----读取yml-------


#-------flask------------------
PATH_STATIC = str(Path(basedir, 'static/package.nw'))

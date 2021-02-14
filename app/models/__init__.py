import os
import glob
from models.daily_reports import DailyReports

__all__ = [
    os.path.split(os.path.splitext(item)[0])[1].replace(
        "_", " ").title().replace(" ", "")
    for item in glob.glob('/usr/src/app/models/{}'.format('[a-zA-Z0-9]*.py'))
]

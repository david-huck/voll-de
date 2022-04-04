from glob import glob
import pandas as pd
import sys
from pathlib import Path

# getting the path to the parent directory 
parent_dir = Path(__file__).parent.resolve()
# print("globbing:", f"{parent_dir}*.csv")
csvs = glob(f"{parent_dir}\*.csv")

for csv in csvs:
    try:
        name = Path(csv).name.split(".")[0]
        csv_file = parent_dir.joinpath(csv)
        # print("attempting to load Dataframe for:",csv_file.as_posix())

        # setting the name of the csv file as attribute to the module
        # e.g. Aut.ImportTS
        setattr(sys.modules[__name__],name, pd.read_csv(csv_file))
    except Exception as e:
        print("Error:",e, "occured for", csv)

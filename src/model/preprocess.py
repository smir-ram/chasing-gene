import numpy as np

def phenotype_farmMgt(filename: str,
                      columns: list,
                      preprocess: torch,
                      batch_no:int):
    print (filename.format(batch_no = batch_no))
    return np.array([1,])

def weather_daily(filename: str,
                      columns: list,
                      preprocess: torch,
                      batch_no:int):
    print (filename.format(batch_no = batch_no))
    return np.array([2,])

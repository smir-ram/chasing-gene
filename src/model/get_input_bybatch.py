from  batch_parameters import source, target
import preprocess

def get(batch_no: int):
    # source
    for parm_group in source.keys():
        # import parquet
        if 'phen' in parm_group:
            action = getattr(preprocess, parm_group)
            vec = action(**source[parm_group], batch_no=batch_no) # tensor

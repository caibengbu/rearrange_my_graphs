from .detect_format import parse_and_grab
from .gen_latex import groupby

def rearrange(rule,col_axis,row_axis,table_name,unit_size,root_dir='.',col_sort=None,row_sort=None):
    fn2labels = parse_and_grab(rule,root_dir=root_dir)
    groupby(root_dir,fn2labels,col_axis,row_axis,table_name,col_sort=col_sort,row_sort=row_sort,unit_size=unit_size)
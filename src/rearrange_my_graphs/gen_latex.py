import pandas as pd
import os

def gen_full_path(root_dir,sub_df,col_axis,row_axis,col_sort,row_sort,cap,unit_size=0.3):
    sub_df = sub_df.fn.apply(lambda x: r'\addheight{\includegraphics[width='+str(unit_size)+r'\textwidth]{'+os.path.join(root_dir,x)+r'}}')
    if col_sort is None and row_sort is None:
        pass
    else:
        col_sort_keys = {str(col_val):i for i, col_val in enumerate(col_sort)}
        row_sort_keys = {str(row_val):i for i, row_val in enumerate(row_sort)}
        sub_df = sub_df[sub_df.index.get_level_values(col_axis).isin(col_sort_keys) & sub_df.index.get_level_values(row_axis).isin(row_sort_keys)]
        if sub_df.shape[0] == 0:
            raise ValueError("The elements in sort args doesn't match what is described in rule")
        sub_df = sub_df.sort_index(level=0,key=lambda x: [col_sort_keys.get(i) for i in x],sort_remaining=False)
        sub_df = sub_df.sort_index(level=1,key=lambda x: [row_sort_keys.get(i) for i in x],sort_remaining=False)
    sub_df = sub_df.reset_index(drop=False)
    pivoted_df = sub_df.groupby(by=[col_axis,row_axis], sort=False).fn.sum().unstack(row_axis)
    with pd.option_context("max_colwidth", 9999):
        tex_content = pivoted_df.to_latex(escape=False,caption=cap)
    return tex_content


def groupby(root_dir,fn2labels,col_axis,row_axis,table_name,col_sort=None,row_sort=None,unit_size=0.3):
    df = pd.DataFrame.from_dict(fn2labels,orient='index')
    all_keys = df.columns
    assert col_axis in all_keys and row_axis in all_keys
    left_keys = list(set(all_keys) - set([col_axis,row_axis]))
    assert len(left_keys) > 0
    df.reset_index(drop=False,inplace=True)
    df.rename(columns={'index':'fn'},inplace=True)
    df.set_index([col_axis,row_axis],inplace=True)
    all_tables = top()
    for keys,sub_df in df.groupby(left_keys):
        if len(left_keys) == 1:
            cap = str(left_keys)+":"+str(keys)
        else:
            cap = " ".join([str(key_name)+":"+str(key) for key_name,key in zip(left_keys,keys)])
        tex_content = gen_full_path(root_dir,sub_df,col_axis,row_axis,col_sort,row_sort,cap,unit_size=unit_size)
        all_tables += tex_content
    all_tables += bottom()
    with open(table_name,'w') as f:
        f.write(all_tables)
    return all_tables

def top():
    result = r"\documentclass[12pt,a4paper]{article}" + \
    r"\usepackage[active,tightpage,floats]{preview}" + \
    r"\usepackage{graphicx}" + \
    r"\usepackage{booktabs}\usepackage{diagbox}" + \
    r"\newcommand*{\addheight}[2][.5ex]{" + \
    r"\raisebox{0pt}[\dimexpr\height+(#1)\relax]{#2}}" + \
    r"\begin{document}" + \
    r"\noindent"
    return result

def bottom():
    return r"\end{document}"

# Rearrange My Graphs
Have you ever produced a bunch of (more precisely, a cartesian product of) plots/graphs/figures/pictures, wanted to consolidate them together and compare them side by side in a LaTeX output? It is always such a labor to type all the filenames manually! This package will save your precious time on these manual work.

## How to use this package
1. **Naming of the graphs**: Put all your graphs in a directory (for example `my_path/`) and name them in a regular fashion. For example, I have 4 scatter plots between variable group A B and variable group C D. They are saved as: `scatter_plot_between_A_and_C.png`, `scatter_plot_between_A_and_D.png`, `scatter_plot_between_B_and_C.png`, `scatter_plot_between_B_and_D.png`. 
2. **Write the filename pattern**: Write your filenames in a wildcard style but replace the asterisks with a pair of brackets and field namd in the middle. Following our old example, the pattern would be written as `scatter_plot_between_{x}_and_{y}.png`.
3. **Run our Python program**: Run ```python -c `import rearrange_my_graphs; rearrange_my_graphs.rearrange(rule='scatter_plot_between_{x}_and_{y}.png',col_axis='x',row_axis='y',table_name='output.tex',unit_size=0.3,root_dir='my_path/')```
4. **Run LaTeX**: Run LaTeX on the output tex file specified in `table_name`.

## Compulsory Arguments
- `rule`: the filename pattern of your graphs
- `col_axis`: the graph parameter that you want to use as the column of the table
- `row_axis`: the graph parameter that you want to use as the row of the table
- `table_name': the output tex file
- `unit_size`: the size of the graph is specified as `unit_size` times \textwidth of LaTeX.

## Optional Arguments
- `root_dir`: the directory in which your graphs in saved
- `col_sort`: a list of all possible values of `col_axis` can take. The perk of specifying this is that (1) we can sort col_axis however we want (in our example, set `col_sort` to `["B","A"]` will make row `B` above `A`); (2) we can filter our values we don't want (in our example, set `col_sort` to `["A"]` will remove row `B`)
- `row_sort`: a list of all possible values of `row_axis` can take. Similar to `col_sort`.



---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
---

# test page for nbprune.py

+++

## cell metadata

+++ {"tags": ["prune-cell"]}

this cell contains a `prune-cell` tag in its metadata and **should not show up**

+++

## line-oriented

```{code-cell} ipython3
# kept as-is
students_see_this = []
```

```{code-cell} ipython3
# prune-cell
# remove just one cell
students_wont_see_this = {}
```

```{code-cell} ipython3
# preserved again
# prune-line except for this one line that should not show up
visible_stuff = True
```

```{code-cell} ipython3
# prune-begin
going_hyperspace = True
```

```{code-cell} ipython3
still_unvisible = 1
```

```{code-cell} ipython3
# stealth still in action
```

```{code-cell} ipython3
## prune-end
still_hidden = True
```

```{code-cell} ipython3
visible_again = True
```

```{code-cell} ipython3
regular_output = True
```

```{code-cell} ipython3
# preserved again
# prune-line except for this one line that should not show up
visible_stuff = True
## prune-begin-next
```

```{code-cell} ipython3
going_hyperspace = True
```

```{code-cell} ipython3
still_unvisible = 1
```

```{code-cell} ipython3
# stealth still in action
```

```{code-cell} ipython3
still_hidden = True
```

```{code-cell} ipython3
# prune-end-previous
visible_again = True
```

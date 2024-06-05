---
jupytext:
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

+++

## cell-oriented

```{code-cell} ipython3
# kept as-is
students_see_this = []
```

```{code-cell} ipython3
# preserved again
visible_stuff = True
```

```{code-cell} ipython3
visible_again = True
```

```{code-cell} ipython3
regular_output = True
```

```{code-cell} ipython3
# preserved again
visible_stuff = True
```

```{code-cell} ipython3
visible_again = True
```

## line-oriented

```{code-cell} ipython3
# version étudiant : à vous de compléter le code

class Node:
    """
    a node has a reference to a unique Station object
    and also logically a set of neighbours,
    each tagged with a line among the 14 metro lines
    finally it has an optional 'label' attribute that we will use when
    drawing the graph on a map
    """
    def __init__(self, station: "Station"):
        ...


    def iter_neighbours(self):
        "iterates (neighbour, line) over neighbours"
        ...
```

```{code-cell} ipython3
# this cell shows up
```

```{code-cell} ipython3
# check that we can use prune-line as an end-of-line thing

this_shows_up = True

this_shows_up = True
this_shows_up = True


this_shows_up = True
this_shows_up = True
```

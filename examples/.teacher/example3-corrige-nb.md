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

+++ {"tags": ["prune-cell"]}

this cell contains a `prune-cell` tag in its metadata and **should not show up**

+++

## cell-oriented

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
    # a single line to hide to hide # prune-line
    def __init__(self, station: "Station"):
        ...
        # prune-line-begin
        self.station = station
        # use a dictionary to attach a value to each link (here the line number)
        self.line_by_neighbour = dict() # type: Dict[Node -> str]
        self.label = None
        # prune-line-end

    # prune-line-begin
    def __repr__(self):
        return str(f"[Node {self.station.name}]")

    def add_edge(self, neighbour: "Node", line):
        self.line_by_neighbour[neighbour] = line

    def nb_edges(self):
        return len(self.line_by_neighbour)
    # prune-line-end

    def iter_neighbours(self):
        "iterates (neighbour, line) over neighbours"
        ...
        # prune-line-begin
        for neighbour, line in self.line_by_neighbour.items():
            yield neighbour, line
```

```{code-cell} ipython3
# this cell shows up
```

```{code-cell} ipython3
# check that we can use prune-line as an end-of-line thing

this_shows_up = True
this_does_not = False    # prune-line

this_shows_up = True
this_does_not = False    # prune-line-begin
this_does_not = False
this_does_not = False
this_does_not = False    # prune-line-end
this_shows_up = True


this_shows_up = True
# prune-line-begin at the beginnning of a line
this_does_not = False    
this_does_not = False
this_does_not = False
this_does_not = False    
# prune-line-end at the beginnning of a line
this_shows_up = True
```

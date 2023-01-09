# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     formats: py:percent
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version, -language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode, -language_info.file_extension, -language_info.mimetype,
#       -toc
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
# ---

# %% [markdown]
# # test page for nbprune.py

# %% [markdown]
# ## cell metadata

# %% [markdown] tags=["prune-cell"]
# this cell contains a `prune-cell` tag in its metadata and **should not show up**

# %% [markdown]
# ## cell-oriented

# %%
# kept as-is
students_see_this = []

# %%
# prune-cell
# remove just one cell
students_wont_see_this = {}

# %%
# preserved again
# prune-line except for this one line that should not show up
visible_stuff = True

# %%
# prune-begin
going_hyperspace = True

# %%
still_unvisible = 1

# %%
# stealth still in action

# %%
## prune-end
still_hidden = True

# %%
visible_again = True

# %%
regular_output = True

# %%
# preserved again
# prune-line except for this one line that should not show up
visible_stuff = True
## prune-begin-next

# %%
going_hyperspace = True

# %%
still_unvisible = 1

# %%
# stealth still in action

# %%
still_hidden = True

# %%
# prune-end-previous
visible_again = True


# %% [markdown]
# ## line-oriented

# %%
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
        # ...
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
        # xxx ...
        self.line_by_neighbour[neighbour] = line

    def nb_edges(self):
        # xxx ...
        return len(self.line_by_neighbour)
        # prune-line-end

    def iter_neighbours(self):
        "iterates (neighbour, line) over neighbours"
        # ...
        # prune-line-begin
        for neighbour, line in self.line_by_neighbour.items():
            yield neighbour, line


# %%
# this cell shows up

# %%
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

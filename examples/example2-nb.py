# ---
# jupyter:
#   jupytext:
#     formats: py:percent
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

# %% [markdown]
# ## cell-oriented

# %%
# kept as-is
students_see_this = []

# %%
# preserved again
visible_stuff = True

# %%
visible_again = True

# %%
regular_output = True

# %%
# preserved again
visible_stuff = True

# %%
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
    def __init__(self, station: "Station"):
        ...


    def iter_neighbours(self):
        "iterates (neighbour, line) over neighbours"
        ...

# %%
# this cell shows up

# %%
# check that we can use prune-line as an end-of-line thing

this_shows_up = True

this_shows_up = True
this_shows_up = True


this_shows_up = True
this_shows_up = True

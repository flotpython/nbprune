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
# ## line-oriented

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

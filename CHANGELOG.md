# 0.5.3 2025 Oct 03

* fix hard-wired version in `version.py`  
  was broken since the move to pyproject.toml

# 0.5.2 2025 Oct 03

* more robust way to spot jupytext config file
  work around https://github.com/mwouts/jupytext/issues/1440

# 0.5.1 2025 Oct 01

* loosen naming conventions - no longer need to put inputs in .teacher  
  they still need to contain `-corrige` though
* protect against a missing jupytext config
* more helpful help for --force

# 0.5.0 2025 Sep 22

* support for `prune-remove-input` and `prune-remove-output` tags
  to propagate `remove-input` or `remove-output` on the output cell

# 0.4.0 2024 Jun 5

* uses jupytext config file to read and write

# 0.3.2 2024 Jun 3

* update README to mention `prune-line-begin` and `prune-line-end`

# 0.3.1 2023 Jan 9

* an input that does not comply with naming conventions
  is no longer deemed a problem

# 0.3.0 2023 Jan 9

* add prune-line-begin and prune-line-end logic
  to skip just parts of a cell; useful for partial classes

# 0.2.2 2022 Dec 16

* tweak the renaming rule to allow a path to start with .teacher
* the -j option helps triage notebooks and plain files

# 0.2.1 2022 Dec 16

* renaming still hardwired, but simpler, essentially
  (.*)/.teacher/(.*)-corrige(.*) is rewritten into \1/\2\3
* -lv and -Lv show both inputs and ouputs

# 0.2.0 2022 Dec 15

* drop the builtin renaming rule that deals with howto files
  and btw will soon add a way to customize the renaming rules

# 0.1.0 2022 Jun 10

* added the -l -L and -d options
  as helpers to make sure results are under git
  and/inspect the results for differences from the inputs

# 0.0.5 2022 Jun 8

* messing with the scheme again, only 3 rules now
  about -corrige -howto and .teacher/

# 0.0.4 2022 Jun 8

* more complete and consistent naming scheme based on
  * -solution -corrige
  * .solutions/ and .corriges/
  * .solution/ and .corrige/

# 0.0.3 2022 Jun 7

* can also store inputs in a .solutions/ subfolder

# 0.0.2 2022 Jun 7

* with a -o option to choose an output file

# 0.0.1 2022 Jun 7

* basic functionality
* hard-wired filenaming policy, that simply consists of removing
  any `-corrige` or `-solution` from the input filename

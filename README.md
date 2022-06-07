# nbprune

typical use case is, a teacher writes a notebook, with solution(s) to a problem that students must solve

so this means 2 versions, one for the teacher(s) with the solutions, and one for the students

this tool defines annotations that the teacher can use to define the parts that will be automatically removed by the tool

## keywords

here are the recognized keywords

| tag | meaning |
|-|-|
| `prune-line` (*) | remove just that one line from the output |
| `prune-cell` | remove this cell from the output |
| `prune-begin` | remove this cell and the ones below from the output |
| `prune-end` | remove this cell, but resume insertion on the next cell |
| `prune-begin-next` (**) | keep this cell from the output, and start pruning at the next one |
| `prune-end-previous` (**) | stop pruning, and insert the current cell |

**NOTES**
* (*) `prune-line` of course is not relevant, and ignored, if set in the cell's metadata tags
* (**) because `prune-begin-next` and `prune-end-previous` appear in a cell that is visible, the whole line containing the tag is removed from the output, so it is probably best to keep these tags on a separate

## line format

the tool will consider a tag is present in a cell if any line in the cell
contains one of the above keywords, with the beginning of the line containing
only `#` and spaces or tabs

so for exemple

| line | match |
|:-|-|
| prune-cell | yes |
| # prune-cell | yes |
| # # prune-cell | yes | 
| some code prune-cell | no |

## cell metadata

the tags can also be set in the cell's metadata as well (except for `prune-line`) ; something like this

```json
{
  "tags": [
    "prune-cell"
  ]
}
```

## examples

so that these 2 scenarios are equivalent

| cell | tag | preserved |
|-|-|-|
| 1 | | y |
| 2 | `prune-cell` | n |
| 3 | | y |
| 4 | | y |
| 5 | `prune-begin-next` | y |
| 6 | | n |
| 7 | | n |
| 8 | | n |
| 9 | `prune-end-previous` | y |
| 10 | | y |

----
or

----

| cell | tag | preserved |
|-|-|-|
| 1 | | y |
| 2 | `prune-cell` | n |
| 3 | | y |
| 4 | | y |
| 5 | | y |
| 6 | `prune-begin` | n |
| 7 | | n |
| 8 | `prune-end` | n |
| 9 | | y |
| 10 | | y |

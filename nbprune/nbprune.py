#!/usr/bin/env python

from pathlib import Path
from argparse import ArgumentParser
import re

from typing import Optional


#import nbformat
import jupytext


# we need this ordered so that longest matches come first
TAGS = [
    'prune-line',
    'prune-cell',
    'prune-begin-next',
    'prune-end-previous',
    'prune-begin',
    'prune-end',
]

VERBOSE = False

def verbose(*args, **kwds):
    if VERBOSE:
        print(*args, **kwds)



def pruned_copy(notebook):
    result = notebook.copy()
    new_cells = []
    copying = True

    # for searching in lines
    pattern = f"^[ \t#]*({'|'.join(TAGS)})"

    # for searching in metadata
    def tag_in_metadata(cell):
        cell_tags = cell.get('metadata', {}).get('tags', [])
        for tag in TAGS:
            if tag in cell_tags:
                return tag

    for cellno, cell in enumerate(result.cells, 1):
        cell_in_output = copying
        lines = []
        tag = tag_in_metadata(cell)
        if tag:
            verbose(f"found tag {tag} in metadata of cell #{cellno}")
        for lineno, line in enumerate(cell.source.split("\n"), 1):
            line_in_output = True
            if match := re.search(pattern, line):
                tag = match.group(1)
                verbose(f"found tag {tag} in line #{lineno} of cell #{cellno}")
                if tag in ('prune-line', 'prune-begin-next', 'prune-end-previous'):
                    line_in_output = False
            if line_in_output:
                lines.append(line)
        if tag == 'prune-cell':
            cell_in_output = False
        elif tag == 'prune-begin':
            copying = False
            cell_in_output = False
        elif tag == 'prune-begin-next':
            copying = False
            cell_in_output = True
        elif tag == 'prune-end':
            copying = True
            cell_in_output = False
        elif tag == 'prune-end-previous':
            copying = True
            cell_in_output = True
        if cell_in_output:
            cell.source = "\n".join(lines)
            new_cells.append(cell)
    result.cells = new_cells
    return result


def prune_solution(in_filename, out_filename):
    with open(in_filename) as reader:
        notebook_in = jupytext.read(reader)
        notebook_out = pruned_copy(notebook_in)
        jupytext.write(notebook_out, out_filename)


def output_filename(in_filename: str) -> Optional[str]:
    """
    very rustic for now; the input is expected to contain
    either -corrige or -solution, that gets removed
    """
    # xxx need some way to configure this
    result = (in_filename
                .replace("-solution", "")
                .replace("-corrige", "")
                .replace(".solutions/", "")
                .replace(".solution/", "")
                .replace(".corriges/", "")
                .replace(".corrige/", "")
    )
    # IMPORTANT
    # this means we can't guess a decent output filename
    # from the input name - we MUST NOT run on those files
    if result == in_filename:
        return None
    return result

DESCRIPTION = f"""
prune some pieces of a notebook, based on the presence of tags such as

{' '.join(sorted(TAGS))}
"""
def main():
    retcod = 0
    parser = ArgumentParser(description=DESCRIPTION)
    parser.add_argument("-o", "--output", default=None,
                        help="""set output filename - only for one input solution
                        """)
    parser.add_argument("-f", "--force", default=False, action='store_true')
    parser.add_argument("-v", "--verbose", default=False, action='store_true')
    parser.add_argument("-V", "--version", default=False, action='store_true')
    parser.add_argument("solutions", nargs="*")

    cli_args = parser.parse_args()
    solutions = cli_args.solutions
    global VERBOSE
    VERBOSE = cli_args.verbose

    if cli_args.version:
        from nbprune import __version__
        print(f"nbprune {__version__}")
        return 0

    # solutions is mandatory - but we can't declare it nargs='+'
    # because of --version
    if not solutions:
        parser.print_help()

    # the --output option
    if cli_args.output:
        if len(solutions) == 1:
            students = [cli_args.output]
        else:
            print(f"option --output makes sense only with exactly one input")
            return 1
    else:
        students = [output_filename(solution) for solution in solutions]


    for solution, student in zip(solutions, students):
        if not student:
            verbose(f"ignoring {solution} - does not comply with naming conventions")
            retcod = 1
            continue

        p1, p2 = Path(solution), Path(student)
        if not p1.exists():
            print(f"{p1} not found")
            retcod = 1
            continue
        if not cli_args.force and p2.exists() and p2.stat().st_mtime > p1.stat().st_mtime:
            verbose(f"ignoring {p1}, as {p2} is more recent")
            continue
        message = "created" if not p2.exists() else "overwritten"
        prune_solution(solution, student)
        print(f"{student} {message}")
    return retcod

if __name__ == '__main__':
    main()

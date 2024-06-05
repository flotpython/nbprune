#!/usr/bin/env python

from pathlib import Path
from argparse import ArgumentParser
import re

from typing import Optional

#import nbformat
import jupytext
from jupytext.config import find_jupytext_configuration_file, load_jupytext_configuration_file

from nbprune import __version__


def jupytext_config():
    config_file = find_jupytext_configuration_file('.')
    config = load_jupytext_configuration_file(config_file)
    return config


# we need this ordered so that longest matches come first
TAGS_LINE = [
    'prune-line-begin',
    'prune-line-end',
    'prune-line',
]
TAGS_CELL = [
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
    pattern_line_bol = f"^[ \t#]*({'|'.join(TAGS_LINE)})"
    pattern_line_eol = f"#.*({'|'.join(TAGS_LINE)})[ \t]*$"
    pattern_cell = f"^[ \t#]*({'|'.join(TAGS_CELL)})"

    # for searching in metadata
    def tag_in_metadata(cell):
        cell_tags = cell.get('metadata', {}).get('tags', [])
        # line-oriented tags don't make sense in a cell
        for tag in TAGS_CELL:
            if tag in cell_tags:
                return tag

    for cellno, cell in enumerate(result.cells, 1):
        cell_in_output = copying
        lines = []
        skipping_lines = False
        tag = tag_in_metadata(cell)
        if tag:
            verbose(f"found tag {tag} in metadata of cell #{cellno}")
        for lineno, line in enumerate(cell.source.split("\n"), 1):
            line_in_output = True
            if match := (re.search(pattern_line_bol, line) or
                         re.search(pattern_line_eol, line) or
                         re.search(pattern_cell, line)):
                tag = match.group(1)
                verbose(f"found tag {tag} in line #{lineno} of cell #{cellno}")
                match tag:
                    case 'prune-line' | 'prune-begin-next' | 'prune-end-previous':
                        line_in_output = False
                    case 'prune-line-begin':
                        skipping_lines = True
                    case 'prune-line-end':
                        skipping_lines = False
                        line_in_output = False
            if skipping_lines or not line_in_output:
                pass
            else:
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
        notebook_in = jupytext.read(reader, config=jupytext_config())
        notebook_out = pruned_copy(notebook_in)
        jupytext.write(notebook_out, out_filename, config=jupytext_config())


def output_filename(in_filename: str) -> Optional[str]:
    """
    very rustic for now, something like
    */.teacher/*-corrige* -> \1\2\3
    with the ability to omit the initial /
    """
    regexp = r"(?P<prefix>.*/)?\.teacher/(?P<stem>.*)-corrige(?P<suffix>.*)$"
    def filename_rewriter(match):
        # this is None if first group is not there
        prefix = match.group('prefix') or ""
        return f"{prefix}{match.group('stem')}{match.group('suffix')}"
    result = re.sub(regexp, filename_rewriter, in_filename)
    # IMPORTANT
    # this means we can't guess a decent output filename
    # from the input name - we MUST NOT run on those files
    if result == in_filename:
        return None
    return result


DESCRIPTION = f"""
prune some pieces of a notebook, based on the presence of tags such as

{' '.join(sorted(TAGS_LINE + TAGS_CELL))}

The command supports other convenience modes (see e.g. --jupyter)
that change its behaviour and thus cannot be cumulated;
for instance if you mention --jupyter --list it will only do --jupyter
"""
def main():
    retcod = 0
    parser = ArgumentParser(description=DESCRIPTION)
    parser.add_argument("-o", "--output", default=None,
                        help="set output filename - only for a single input")
    parser.add_argument("-f", "--force", default=False, action='store_true')
    parser.add_argument("-j", "--jupyter", default=False, action='store_true',
                        help="returns 0 if all inputs are notebooks, 1 otherwise;"
                             " no output unless -v is given")
    parser.add_argument("-l", "--list", default=False, action='store_true',
                        help="only lists output files on stdout and exits")
    parser.add_argument("-L", "--list-different", default=False, action='store_true',
                        help="like --list, but only when the pruned version differs")
    parser.add_argument("-d", "--diff",  default=False, action='store_true',
                        help="like --list, but display a list of diff commands")
    parser.add_argument("-v", "--verbose", default=False, action='store_true')
    parser.add_argument("-V", "--version", default=False, action='store_true')
    parser.add_argument("solutions", nargs="*")

    cli_args = parser.parse_args()
    solutions = cli_args.solutions
    global VERBOSE
    VERBOSE = cli_args.verbose

    if cli_args.version:
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

    # jupyter mode (check if proper notebook)

    if cli_args.jupyter:
        success = True
        for solution in solutions:
            try:
                with open(solution) as reader:
                    notebook_in = jupytext.read(reader, config=jupytext_config())
                    # actually jupytext.read() is very permissive and will accept to open
                    # raw .md or .py files, and we need to be a little picky
                    # so: if the metadata keys is reduced to a single 'jupytext' entry,
                    # it is considered a plain file
                    if list(notebook_in.metadata.keys()) == ['jupytext']:
                        verbose(f"{solution} is a plain file")
                        success = False
            except Exception as exc:
                success = False
                verbose(f"{solution} is not a notebook ({type(exc)})")

        return 0 if success else 1

    # list files mode

    if cli_args.list or cli_args.list_different or cli_args.diff:
        for solution, student in zip(solutions, students):
            if cli_args.diff:
                comment = "# " if not student else ""
                print(f"{comment}diff {solution} {student} >& /dev/null || echo {solution}")
                continue
            if not student:
                continue
            if cli_args.list:
                verbose(f"{solution} -> ", end='')
                print(student)
                continue
            try:
                with open(solution) as reader:
                    v1 = reader.read()
                with open(student) as reader:
                    v2 = reader.read()
                if v1 == v2:
                    continue
            except FileNotFoundError:
                pass
            verbose(f"{solution} -> ", end='')
            print(student)
        return 0

    for solution, student in zip(solutions, students):
        if not student:
            verbose(f"ignoring {solution} - does not comply with naming conventions")
            # not a big deal
            # retcod = 1
            continue

        p1, p2 = Path(solution), Path(student)
        if not p1.exists():
            print(f"{p1} not found")
            retcod = 1
            continue
        if not cli_args.force and p2.exists() and p2.stat().st_mtime > p1.stat().st_mtime:
            verbose(f"leaving  {p2} that is more recent than {p1}")
            continue
        message = "created" if not p2.exists() else "overwritten"
        verbose(f"dealing with {solution}")
        prune_solution(solution, student)
        print(f"{student} {message}")
    return retcod

if __name__ == '__main__':
    main()

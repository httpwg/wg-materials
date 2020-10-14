import re
import os
from os import path
import sys

ignore_things = ['lib', 'assets', 'README.md', 'badge']
ignore_prefixes = ['.', '_']
sep = "\n\n---\n\n"

def spider (directory):
    index = []
    sys.stderr.write(f"* scanning {directory}...\n")
    dirs = []
    files = []
    for i in os.scandir(directory):
        if filter_thing(i):
            if i.is_dir():
                dirs.append(i.name)
            elif i.is_file():
                files.append(i.name)
    for name in nat_sort(dirs):
        index.append(f"- [{pretty_dir(name)}/]({name}/README.md)")
    for name in nat_sort(files):
        index.append(f"- [{name}]({name})")
    write_index(directory, index)
    for dir_name in dirs:
        spider(path.join(directory, dir_name))

def filter_thing(thing):
    if thing.name in ignore_things: return False
    for ignore in ignore_prefixes:
        if thing.name.startswith(ignore): return False
    return True

def nat_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

def pretty_dir(name):
    if "/" in name:
        cleaned = name.split("/")[-1]
    else:
        cleaned = name
    if cleaned.startswith("ietf"):
        return f"IETF {cleaned[4:]}"
    if cleaned.startswith("interim-"):
        return f"Interim meeting: {cleaned[8:]}"
    return name

def write_index(directory, index):
    readme_path = f"{directory}/README.md"
    if path.exists(readme_path):
        with open(readme_path, 'r') as fh:
            existing = fh.read()
            try:
                text = existing[:existing.index(sep)+len(sep)]
            except ValueError:
                text = f"{existing}{sep}"
    else:
        text = sep
    with open(readme_path, 'w') as fh:
        fh.write(text)
        if directory != ".":
            fh.write(f"## {pretty_dir(directory)}\n\n")
        fh.write("\n".join(index))



if __name__ == "__main__":
    import sys
    spider(sys.argv[1])

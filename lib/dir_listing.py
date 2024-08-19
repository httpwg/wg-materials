import re
import os
from os import path
import sys

ignore_things = ['lib', 'assets', 'README.md', 'badge']
ignore_prefixes = ['.', '_']
sep = "\n\n---\n\n"

def spider(directory, reverse=False):
    index = []
    sys.stderr.write(f"* scanning {directory}...\n")
    dirs = []
    files = []
    for i in os.scandir(directory):
        if filter_thing(i):
            if i.is_dir():
                dirs.append(i)
            elif i.is_file():
                files.append(i)
    for dir_ in nat_sort(dirs, reverse):
        extra = []
        if path.exists(f"{dir_.path}/agenda.md"):
            extra.append(f"[agenda]({dir_.name}/agenda.md)")
        if path.exists(f"{dir_.path}/minutes.md"):
            extra.append(f"[minutes]({dir_.name}/minutes.md)")
        extra_str = ""
        if extra:
            extra_str = f": {', '.join(extra)}"
        index.append(f"- [{pretty_dir(dir_.name)}]({dir_.name}/){extra_str}")
    for file_ in nat_sort(files):
        pretty_name, extra = pretty_file(file_)
        index.append(f"- [{pretty_name}]({file_.name}) {extra}")
    write_index(directory, index)
    for dir_ in dirs:
        spider(path.join(directory, dir_.name))

def filter_thing(thing):
    if thing.name in ignore_things: return False
    for ignore in ignore_prefixes:
        if thing.name.startswith(ignore): return False
    return True

def nat_sort(l, reverse=False):
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key.name) ] 
    out = sorted(l, key = alphanum_key)
    if reverse:
        out.reverse()
    return out

def pretty_dir(name, with_path=False):
    if name.endswith("/"):
        name = name[:-1]
    if "/" in name and with_path:
        cleaned = " : ".join(name.split("/"))
    else:
        cleaned = name.split("/")[-1]
    if cleaned[:4] == "ietf":
        cleaned = f"IETF {cleaned[4:]}"
    else:
        cleaned = cleaned.title()
    return f"🗂️ {cleaned}"

def pretty_file(file_):
    name = file_.name
    ext = ""
    extra = ""
    if "." in file_.name:
        name, ext = file_.name.rsplit(".", 1)
        if ext.lower() not in ['md', 'html']:
            extra = f"_{ext}_"
    name = re.sub(r"([a-z])-", r"\1 ", name)
    name = re.sub(r"-([a-z])", r" \1", name)
    if ext.lower() == "md" and "agenda" not in name and "minutes" not in name:
        return extract_md_heading(file_, name), extra
    return name.title().replace("Http", "HTTP"), extra

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

def extract_md_heading(fileobj, fallback):
    try:
        with open(fileobj.path) as fh:
            lines = fh.readlines()
    except IOError as why:
        sys.stderr.write(f"Error reading {filename}: {why}\n")
        return fallback
    for line in lines:
        if line.startswith("# "):
            return line[1:].strip()
    return fallback


if __name__ == "__main__":
    import sys
    for directory in sys.argv[1:]:
        spider(directory, True)

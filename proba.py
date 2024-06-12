import re
from itertools import combinations
from json import dump


def add_to_tree(tree: dict, keys: list, value: str | dict) -> None:
    if len(keys) == 1:
        tree[keys[0]] = value
    elif keys != []:    
        add_to_tree(tree[keys[0]], keys[1:], value)


def backtracking(tree: dict, state: list, names: str, length: int) -> None:
    if len(names) == 1:
        add_to_tree(tree, state, "end")            
    elif len(names) > 0:
        add_to_tree(tree, state, dict())
    else:
        return

    for iNames in combinations(names, length):
        iNames = "".join(iNames)
        state.append(iNames)
        backtracking(tree, state, iNames, len(iNames) - 1)
        state.pop()


tree = dict()
state = []
names_pattern = re.compile("^[A-Z]{1}[a-z]{2,10}(\s?[A-Z]{1}[a-z]{2,10}){1,}$")


if __name__ == "__main__":
    user_names = input(
"""
PROVIDE :
Name1 Name2 Name3 Name4 ...
OR "default" to pick default names
"""
        )
    if user_names == "default":
        names = [
            "Arthur",
            "Béatrice",
            "Chloé",
            "David",
        ]
    elif names_pattern.search(user_names):
        names = user_names.split(" ")
    else:
        raise Exception("Sorry, your entry did not match the correct format.")

    root = "".join([name[0] for name in names])  #  initials (ABCD for default names)
    backtracking(tree, state, root, len(root) - 1)
    with open("output.json", "w") as fp:
        dump(tree, fp, indent=4)
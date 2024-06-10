from itertools import permutations
from json import dump

def access_to_dic_from(
    tree: dict[..., [dict]], 
    keys: list, 
    value: str | dict
    ) -> None:
    if len(keys) == 1:
        tree[keys[0]] = value
    elif keys != []:
        access_to_dic_from(tree[keys[0]], keys[1:], value)


def backtracking(tree: dict, state: list, names: str):
    if len(names) == 1:
        access_to_dic_from(tree, state, names)
    elif len(names) > 0:
        access_to_dic_from(tree, state, {names: "end"})
    else:
        return

    for iNames in permutations(names):
        iNames = "".join(iNames)
        state.append(iNames)        
        #  ignore the last name
        result = backtracking(tree, state, iNames[:-1])
        state.pop()


names = [
    "Arthur",
    "Béatrice",
    "Chloé",
    "David",
]

root = "".join([name[0] for name in names]) #  ABCD

if __name__ == "__main__":
    tree = dict()
    state = []
    backtracking(tree, state, root)
    with open("output.json", "w") as fp:
        dump(tree, fp, indent=1)
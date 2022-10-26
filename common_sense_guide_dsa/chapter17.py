"""
Chapter 17 exercises of "A Common-Sense Guide to Data Structures and Algorithms"
"""

class Trie:
    def __init__(self, root_node=None):
        self.root = root_node   

    def print_trie(self, node=None):
        if node == "*":
            return
        if node is None:
            node = self.root
        for k, v in node.items():
            print(k)
            self.print_trie(node=v)

    def create_new_word(self, prefix, dict):
        if "*" in dict:
            return prefix
        pair = next(iter(dict.items()))
        key = pair[0]
        value = pair[1]
        return self.create_new_word(prefix + key, value)

    def auto_correct(self, word):
        curr_dict = self.root
        new_word = ""
        for c in word:
            if c in curr_dict:
                new_word += c
                curr_dict = curr_dict[c]
            else:
                break

        return self.create_new_word(new_word, curr_dict)

def create_dicts():
    b4 = {"*": "*"}
    b3 = {"t": b4}
    b2 = {"a": b3}
    t5 = {"*": "*"}
    t4 = {"d": t5}
    t3 = {"a": t4}
    t2 = {"o": t3}
    root = {"b": b2, "t": t2}
    return root

def main():
    print("Testing")
    root = create_dicts()
    trie = Trie(root_node=root)

    print("Testing print_trie()")
    trie.print_trie()

    print("Autocorrect for bta")
    print(trie.auto_correct("bta"))

    print("Autocorrect for che")
    print(trie.auto_correct("che"))

    print("Autocorrect for tord")
    print(trie.auto_correct("tord"))

    print("Autocorrect for toad")
    print(trie.auto_correct("toad"))

main()
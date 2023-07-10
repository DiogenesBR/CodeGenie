from tree_sitter import Language, Parser
from entities.node import Node
import os

class TreeSitterHandler:
    def __init__(self):
        self.language = Language('build/my-languages.so', 'c_sharp')
        self.parser = Parser()
        self.parser.set_language(self.language)

    def parse_directory(self, dir):
        nodes = []
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith('.cs') or file.endswith('.csproj'):
                    path = os.path.join(root, file)
                    with open(path, 'r') as f:
                        code = f.read()
                    tree = self.parser.parse(bytes(code, 'utf8'))
                    nodes.append(self.create_node(tree, path))
        return nodes

    def create_node(self, tree, path):
        root_node = tree.root_node
        node = Node(
            name=root_node.type,
            class_type='Block',
            path=path,
            language='C#',
            content=root_node.text
        )
        return node

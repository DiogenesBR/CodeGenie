from typing import List, Dict, Optional

class Node:
    def __init__(self, 
                 name: str,
                 path: str,
                 language: str, # C#, Python, JavaScript, etc...
                 block_type: str, # Class, Method, Function, etc... each language has its own types
                 signature: str,
                 id: Optional[str]=None,
                 references: Optional[List["Node"]]=None, 
                 content: Optional[str]=None, 
                 description: Optional[str]=None):
        self.name = name
        self.block_type = block_type
        self.path = path
        self.language = language
        self.signature = signature
        self.id = id
        self.references = references if references is not None else []
        self.content = NodeContent(content) if content is not None else None
        self.description = NodeDescription(description) if description is not None else None

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'path': self.path,
            'signature': self.signature,
            'language': self.language,
            'block_type': self.block_type,
            'properties': {
                'references': [reference.to_dict() for reference in self.references],
                'content': self.content.content if self.content is not None else None,
                'description': self.description.content if self.description is not None else None,
            },
        }

class NodeContent:
    def __init__(self, content: str):
        self.content = content

class NodeDescription:
    def __init__(self, content: str):
        self.content = content

class Repository:
    def __init__(self, 
                 name: str,
                 path: str,
                 git_url: str,
                 nodes: Optional[List[Node]]=None):
        self.name = name
        self.path = path
        self.git_url = git_url
        self.nodes = nodes if nodes is not None else []
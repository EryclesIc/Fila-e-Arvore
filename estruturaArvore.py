class CORD_19:
    def __init__(self, index_key, line):
        self.line = line
        if index_key == 0:
            self.key = self.line.aux_key
        elif index_key == 1:
            self.key = self.line.cord_uid
        elif index_key == 2:
            self.key = self.line.sha
        elif index_key == 3:
            self.key = self.line.source_x
        elif index_key == 4:
            self.key = self.line.title
        elif index_key == 5:
            self.key = self.line.doi
        elif index_key == 6:
            self.key = self.line.pmcid
        elif index_key == 7:
            self.key = self.line.pubmed_id
        elif index_key == 8:
            self.key = self.line.license
        elif index_key == 9:
            self.key = self.line.abstract
        elif index_key == 10:
            self.key = self.line.publish_time
        elif index_key == 11:
            self.key = self.line.authors
        elif index_key == 12:
            self.key = self.line.journal
        elif index_key == 13:
            self.key = self.line.mag_id
        elif index_key == 14:
            self.key = self.line.who_covidence_id
        elif index_key == 15:
            self.key = self.line.arxiv_id
        elif index_key == 16:
            self.key = self.line.pdf_json_files
        elif index_key == 17:
            self.key = self.line.pmc_json_files
        elif index_key == 18:
            self.key = self.line.urlrecovered
        elif index_key == 19:
            self.key = self.line.s2_id
        else:
            self.key = self.line.aux_key
        self.left = None
        self.right = None

    def __str__(self):
        return "{0}||{1}||{2}||{3}||{4}||{5}||{6}||{7}||{8}||{9}||{10}||{11}||{12}||{13}||{14}||{15}||{16}||{17}||{18}||{19}".format(self.line.aux_key,
                                                                                                                                     self.line.cord_uid, 
                                                                                                                                     self.line.sha,
                                                                                                                                     self.line.source_x,
                                                                                                                                     self.line.title,
                                                                                                                                     self.line.doi,
                                                                                                                                     self.line.pmcid,
                                                                                                                                     self.line.pubmed_id,
                                                                                                                                     self.line.license,
                                                                                                                                     self.line.abstract,
                                                                                                                                     self.line.publish_time,
                                                                                                                                     self.line.authors,
                                                                                                                                     self.line.journal,
                                                                                                                                     self.line.mag_id,
                                                                                                                                     self.line.who_covidence_id,
                                                                                                                                     self.line.arxiv_id,
                                                                                                                                     self.line.pdf_json_files,
                                                                                                                                     self.line.pmc_json_files,
                                                                                                                                     self.line.urlrecovered,
                                                                                                                                     self.line.s2_id)
 
    def add(self, node):
        if not node:
            return self
        if self.key < node.key:
            node.left = self.add(node.left)
        else:
            node.right = self.add(node.right)
        return node

    def traverse(self):
        if self.left:
            self.left.traverse()
        print(self)
        if self.right:
            self.right.traverse()
    
    # Busca um dado
    def search(self, aux_key):
        if self.key == aux_key:
            return self
        if self.key > aux_key:
            if not self.left:
                return None
            return self.left.search(aux_key)
        if not self.right:
            return None
        return self.right.search(aux_key)

    # busca um nó e seu pai
    def node_dad_search(self, aux_key):
        current = self
        node_dad = None
        while current:
            if current.chave == aux_key:
                return current, node_dad
            node_dad = current
            if current.chave > aux_key:
                current = current.left
            else:
                current = current.right
        return None, node_dad
    
    # deleta toda a árvore
    def delete_tree(self):
        if self.left:
            self.left.delete_tree()
        if self.right:
            self.right.delete_tree()
        del self

class BinaryTree:
    def __init__(self, index_key=0):
        self.index_key = index_key
        self.root = None

    def show_tree(self):
        if not self.root:
            return
        self.root.show_tree()

    def search(self, aux_key):
        if not self.root:
            return None
        return self.root.search(aux_key)

    def insert(self, line):
        self.root = CORD_19(self.index_key, line).insert(self.root)

    def delete(self, aux_key):
        if not self.root:
            return
        node, dad = self.root.node_dad_search(aux_key)
        if not node:
            return
        if not node.left or not node.right:
            if not node.left:
                n = node.right
            else:
                n = node.left
        else:
            m = node
            n = node.left
            while n.right:
                m = n
                n = n.right
            if m != node:
                m.right = n.left
                n.left = node.left
            n.right = node.right
        if dad:
            if aux_key < dad.key:
                dad.left = n
            else:
                dad.right = n
        else:
            self.root = n
        del node
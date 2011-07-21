


class NgramTreeProcessor():
    
    def tokens_to_tree(self,tokens):
        tree = {'#':1}
        working_tree = tree
        for token in tokens:
            #working_tree['#'] = 1
            working_tree[token] = {'#':1}
            working_tree = working_tree[token]
        return tree
    
    def combine_trees(self,tree1,tree2 = None):
        if tree2 == None:
            tree2 = {'#':0}
        for token, tree in tree2.iteritems():
            if token == '#':
                tree1['#']=tree1['#']+tree
            else:
                tree1[token]=self.combine_trees(tree,tree1.get(token))
        return tree1
                
        
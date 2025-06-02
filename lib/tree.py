class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    if not self.root:
      return None

    stack = [self.root]

    while stack:
      node = stack.pop()
      if node.get('id') == id:
        return node
      # Add children to stack for depth-first traversal
      children = node.get('children', [])
      if children:
        stack.extend(children)

    return None

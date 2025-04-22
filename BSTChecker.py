from BSTNode import BSTNode

class BSTChecker:
    # check_BST_validity() determines if the tree is a valid BST. If so, None
    # is returned. If not, the first (in preorder traversal) node in violation
    # of BST requirements is returned. Such a node will be one of the following:
    # - A node X is in the left subtree of ancestor Y with X's key >= Y's key (corrected from prompt)
    # - A node X is in the right subtree of ancestor Y with X's key <= Y's key (corrected from prompt)
    # - A node that is encountered more than once during traversal
    @staticmethod
    def check_BST_validity(root_node):
        """
        Checks if the tree rooted at 'root_node' is a valid BST.

        Args:
            root_node: The root node of the BST (or None for an empty tree).

        Returns:
            None if the tree is a valid BST.
            The first problematic node encountered (in preorder traversal)
            if the tree is invalid.
        """
        # Use a set to track nodes visited during this specific check
        # The set stores the actual node objects (memory addresses)
        visited_nodes = set()

        # Start the recursive check with initial infinite bounds
        # (-inf, +inf) and the empty visited set.
        return BSTChecker._check_recursive(root_node, float('-inf'), float('+inf'), visited_nodes)

    @staticmethod
    def _check_recursive(node, min_key, max_key, visited_nodes):
        """
        Recursive helper function for BST validation using preorder traversal logic.

        Args:
            node: The current node being checked.
            min_key: The minimum allowed key value (exclusive) for this node
                     based on its ancestors.
            max_key: The maximum allowed key value (exclusive) for this node
                     based on its ancestors.
            visited_nodes: A set containing node objects visited so far in the
                           current check_BST_validity call.

        Returns:
            None if the subtree rooted at 'node' is valid within the given bounds
            and hasn't been visited before in this traversal.
            The first problematic node encountered otherwise.
        """
        # Base case: An empty subtree (represented by None) is valid.
        if node is None:
            return None

        # --- Preorder Check 1: Visited Node (Child-related problems) ---
        # Check if this specific node object has been encountered before.
        if node in visited_nodes:
            # Found a cycle or shared child node. Return this node as the problem.
            return node

        # Add the current node object to the set of visited nodes.
        visited_nodes.add(node)

        # --- Preorder Check 2: Key Validity (Key-related problems) ---
        # Check if the node's key adheres to the BST property within the
        # bounds set by its ancestors. Bounds are exclusive.
        # Using node.get_key() based on the provided BSTNode class
        current_key = node.get_key()
        if not (min_key < current_key < max_key):
            # Key is out of the valid range defined by ancestors. Return this node.
            return node

        # --- Recursive Steps (Left Subtree, then Right Subtree) ---

        # Check the left subtree using node.get_left()
        # The valid range for the left child is updated: max_key becomes current_key.
        problem_in_left = BSTChecker._check_recursive(node.get_left(), min_key, current_key, visited_nodes)
        if problem_in_left:
            # If a problem was found, propagate it up immediately.
            return problem_in_left

        # Check the right subtree using node.get_right()
        # The valid range for the right child is updated: min_key becomes current_key.
        problem_in_right = BSTChecker._check_recursive(node.get_right(), current_key, max_key, visited_nodes)
        if problem_in_right:
            # If a problem was found, propagate it up immediately.
            return problem_in_right

        # If we reach here, the node itself is valid, and its subtrees are valid.
        # Do not remove from visited_nodes, as required for detecting cycles/shared nodes
        # across different branches visited later in the traversal.
        return None
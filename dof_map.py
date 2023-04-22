from node2D import Node2D

class DOF_Mapper:
    """
    Maps the degrees of freedom for a given structural model.
    """
    def __init__(self) -> None:
        pass

    def map(self, structure) -> list:
        """
        Assign element degrees of freedom an equation number for assembly. A
        value of 0 means the degree of freedom is inactive and will be omitted
        from the analysis.
        """

        # importing here allows the type hint without a 
        # circular dependency error
        from structure import Structure

        structure: Structure
        num_nodes = structure.get_num_nodes
        
        dof_map = [
            [0 for i in range(num_nodes)]
            for i in range(structure.dofs_per_node)
        ]

        node: Node2D
        node_index = 0
        eq_no = 1
        for node in structure.nodes:
            for dof in range(structure.dofs_per_node):
                if node.get_dof(dof):  # the degree of freedom is active
                    dof_map[dof][node_index] = eq_no
                    eq_no += 1
            node_index += 1

        return dof_map

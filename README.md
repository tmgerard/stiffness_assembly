# Stiffness Matrix Assembly

This is my playground for creating a simple scheme for the assembly of a global stiffness matrix. I am currently focusing on the direct stiffness method to understand the basic principles. I would like to progress to improving the code for use in finite element analysis.

The code here will mostly be as minimal as possible for simplicity.

The first version of the code is following the basic implementation procedures found in K.J. Bathe's "Finite Element Procedures."

## Structure Definition
### Define Nodes
Nodes on the structure are defined using cartesian coordinates. These points define joints in the structures, notable regions of cross-section change along a span, or a position of interest for the analysis of the structure.

The individual degrees of freedom for each node can be designated as active or inactive for the analysis. Active degrees of freedom will be used in the structural solution, while inactive nodes will not. Inactive nodes are often the supports of the structure.

### Define Elements
Elements representing the physical structural members are defined using the defined nodal locations. For this repository, simple line elements are considered only. These elemets will have a node defined at the start and end of the element.

### Define Structure Loads
Structure loads represent the external forces applied to the structure that will affect the response of the structure. These can be applied at the nodes or directly to an element. Element loads must be converted into ficticious nodal loads using fixed-end-forces to be handled in the assembly and solution of the structural system.

When only nodal loads are applied, the following equation must be solved.

$$
    \{F\} = [K_{global}]\{\delta\}
$$

When considering element loads, the ficticious forces must be accounted for.

$$
    \begin{aligned}
        \{F\} = [K_{global}]\{\delta\} + \{F_{fef}\} \\
        \{F - F_{fef}\} = [K_{global}]\{\delta\}
    \end{aligned}
$$

## Structure Assembly
With the structure and loads defined, the above equations must be assembled so they can be solved using an equation solution technique, such as gaussian elimination, LUP Decomposition, or Cholesky Decomposition to name a few.

### Establish ID Array
Following Bathe's "Finite Elmenet Procedures," an ID array can be used to assign each degree of freedom in a system to an equation position in the systems linear equation. A matrix with rows representing the degrees of freedom available in the system and columns representing each node in the system is constructed. The degrees of freedom active in the solution are assigned and equation number, while inactive degrees of freedom are set to zero.

### Connectivity Array
Using the ID array, an element connectivity array can be created. The connectivity array is created by combining the columns from the ID array that correspond to the nodes that define the boundaries of an element. The connectivity array is used to place degree of freedom from the element's local stiffness matrix into the systems global stiffness matrix.

Snippt from [assember.py](assembler.py) using the connectivity array to build the global stiffness matrix.

```python
element: Beam2D
        for element in self.structure.elements:
            # calculate the elements stiffness matrix
            k_element = element.k_global()
            # obtain the element connectivity array
            con_array = self.get_connectivity_array(element)
            for i in range(len(con_array)):
                for j in range(len(con_array)):
                    if not con_array[i] == 0 and not con_array[j] == 0:
                        k_global[con_array[i] - 1][con_array[j] - 1] += k_element[i][j]        
        return k_global
```

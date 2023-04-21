from point2D import Point2D
from node2D import Node2D
from node2D_list import Node2DList
from beam_element import Beam2D
from bar_element import Bar2D
from structure import Structure
from assembler import Assembler
from structure_types import StructureType


def truss_example():
    
    # nodes
    nodes = Node2DList()
    nodes.append(Node2D(Point2D(0, 0)))
    nodes.append(Node2D(Point2D(100, 0)))
    nodes.append(Node2D(Point2D(0, 100)))

    # assign support conditions
    nodes[0].set_constraints(False, True, False)
    nodes[1].set_constraints(False, False, False)

    # check that node ids assigned properly
    for node in nodes:
        print("id: " + str(node.get_ID()))
    
    elastic_modulus = 100
    area = 10

    # create element list
    elements = [
        Bar2D(nodes[0], nodes[1], area, elastic_modulus),
        Bar2D(nodes[1], nodes[2], area, elastic_modulus),
        Bar2D(nodes[2], nodes[0], area, elastic_modulus)
    ]

    elements[0].set_ID(0)
    elements[1].set_ID(1)
    elements[2].set_ID(2)

    structure = Structure(StructureType.PLANE_TRUSS, nodes, elements)

    map = structure.get_dof_map()

    print()
    print("Degree of Freedom Map")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
      for row in map]))
    
    assembler = Assembler(structure)
    k_global = assembler.assemble()

    print()
    print("Global Stiffness Matrix")
    print('\n'.join(['   '.join(['{:.1f}'.format(item) for item in row]) 
      for row in k_global]))


def continuous_beam_example():

    # create node list
    nodes = Node2DList()
    nodes.append(Node2D(Point2D(0, 0)))
    nodes.append(Node2D(Point2D(100, 0)))
    nodes.append(Node2D(Point2D(200, 0)))
    nodes.append(Node2D(Point2D(300, 0)))
    nodes.append(Node2D(Point2D(400, 0)))
    nodes.append(Node2D(Point2D(500, 0)))
    nodes.append(Node2D(Point2D(600, 0)))

    # assign support conditions
    nodes[0].set_to_pin_support()
    nodes[1].set_to_roller_support()
    nodes[2].set_to_pin_support()
    nodes[4].set_to_pin_support()
    nodes[6].set_constraints(True, True, True)  # free

    # check that node ids assigned properly
    for node in nodes:
        print("id: " + str(node.get_ID()))
    
    elastic_modulus = 29000
    moment_of_inertia = 144
    area = 20
    
    # create element list
    elements = [
        Beam2D(nodes[0], nodes[1], area, moment_of_inertia, elastic_modulus),
        Beam2D(nodes[1], nodes[2], area, moment_of_inertia, elastic_modulus),
        Beam2D(nodes[2], nodes[3], area, moment_of_inertia, elastic_modulus),
        Beam2D(nodes[3], nodes[4], area, moment_of_inertia, elastic_modulus),
        Beam2D(nodes[4], nodes[5], area, moment_of_inertia, elastic_modulus),
        Beam2D(nodes[5], nodes[6], area, moment_of_inertia, elastic_modulus)
    ]

    elements[0].set_ID(0)
    elements[1].set_ID(1)
    elements[2].set_ID(2)
    elements[3].set_ID(3)
    elements[4].set_ID(4)
    elements[5].set_ID(5)

    structure = Structure(StructureType.PLANE_FRAME,nodes, elements)

    map = structure.get_dof_map()

    print()
    print("Degree of Freedom Map")
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
      for row in map]))
    
    assembler = Assembler(structure)
    k_global = assembler.assemble()

    print()
    print("Global Stiffness Matrix")
    print('\n'.join(['   '.join(['{:.1f}'.format(item) for item in row]) 
      for row in k_global]))
    
def frame_example():
  """
  Example 16.4 from "Fundamentals of Structural Analysis"
  by Kenneth M. Leet
  """

  # nodes
  nodes = Node2DList()
  nodes.append(Node2D(Point2D(0, 0)))
  nodes.append(Node2D(Point2D(360, 480)))
  nodes.append(Node2D(Point2D(960, 480)))

  # assign support conditions
  nodes[0].set_constraints(False, False, False)  # fixed
  nodes[2].set_constraints(False, False, False)  # fixed

  elastic_mod = 1_000_000
  area = 0.72
  inertia = 24

  # create element list
  elements = [
      Beam2D(nodes[0], nodes[1], area, inertia, elastic_mod),  # ab
      Beam2D(nodes[1], nodes[2], area, inertia, elastic_mod),  # bc

  ]

  elements[0].set_ID(0)
  elements[1].set_ID(1)

  structure = Structure(StructureType.PLANE_FRAME,nodes, elements)

  map = structure.get_dof_map()

  print()
  print("Degree of Freedom Map")
  print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) 
    for row in map]))
  
  assembler = Assembler(structure)
  k_global = assembler.assemble()

  print()
  print("Global Stiffness Matrix")
  print('\n'.join([' '.join(['{:2f}'.format(item) for item in row]) 
    for row in k_global]))


if __name__ == "__main__":
    truss_example()

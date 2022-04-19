#import Network from pyvis library
from turtle import color
from pyvis.network import Network

net = Network()

#add nodes
net.add_nodes([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
              label=['Software Engineering', 'Devops',"low level programming","High level Programming","Graphic Programming","Data Structures and Algorithms",
                     "Reverse engineering and Security", "Unix Programming", "Databases","Object Oriented Programming", "Python","Front- End", 
                     "Linux/Command Line", "Soft Skills", "Infrastructure design and management","C programming and algorithms in C" ],
              )
net.add_edges([(1,2), (1, 4), (1, 3), (2, 14), (2, 15),
               (2,13), (3, 16),(3,5),(3,8),(3,6),(3,7),
               (4,11), (4, 12),(4, 10),(4, 9),
               ])
'''net.add_node(1, label='https://alx-intranet.hbtn.io/curriculums/17/overview')
net.add_node(2, label="Devops")
net.add_node(3, label="low level programming")
net.add_node(4, label="High level Programming")
net.add_node(5, label="Graphic Programming")
net.add_node(6, label="Data Structures and Algorithms")
net.add_node(7, label="Reverse engineering and Security")
net.add_node(8, label="Unix Programming")
net.add_node(9, label="Databases")
net.add_node(10, label="Object Oriented Programming")
net.add_node(11, label="Python")
net.add_node(12, label="Front- End")
net.add_node(13, label="Linux/Command Line")
net.add_node(14, label="Soft Skills")
net.add_node(15, label="Infrastructure design and management")
net.add_node(16, label="C programming and algorithms in C")
#net.add_node(17, label="Devops")'''

net.repulsion(node_distance=200, spring_length=250)
net.toggle_hide_nodes_on_drag(True)
net.show('output.html') 


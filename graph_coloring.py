import networkx as nx
import matplotlib.pyplot as plt
import time

class ColorGraph:
    def __int__(self, graph, color_list):
        self.graph=graph
        self.color_list=color_list


    def plot_graph(self):
        """
        plot the graph, in a new windpw, sets the nodes size and style and shows the assignment of colors of nodes
        :return:
        """
        plt.clf()
        node_colors = [self.graph.nodes[node]['color'] for node in self.graph.nodes]
        node_border_color = 'black'  # Border color for nodes
        node_size = 1000  # Increase the size of nodes
        pos = nx.spring_layout(self.graph, seed=42)  # Set the seed for consistent layout
        nx.draw_networkx(self.graph, pos=pos, with_labels=True, font_weight='bold', node_color=node_colors,
                         edgecolors=node_border_color, node_size=node_size)
        plt.pause(0.3)
        plt.draw()

    def consistent(self, node, color, assignment):
        """
        check if the assignment of node with a color is consistent witg the other assignments
        :param node: node in a graph
        :param color: the dom
        :param assignment: a list of tuples (node, color)
        :param value is a tuple of node name and his color
        :return: if the (node, color) is consistent with the constraints
        """
        for value in assignment:
            if value[1] == color and value[0] in self.graph.neighbors(node):
                return False
        return True

    def assign(self, node, color, assignment):

        """
        assign color to a node in the graph
        :param node: variable
        :param color:dom
        :param assignment:
        :return: returns the new assignment
        """
        self.graph.nodes[node]['color'] = color
        self.graph.nodes[node]['colors'] = [color]
        assignment.append((node, color))
        self.plot_graph(self)
        time.sleep(1)  # Add a pause to visualize the assigned color
        return assignment

    def remove_assignment(self, node, assignment):
        """
        delete the node assign from the assignment list
        :param node: a node in the graph
        :param assignment: the assignment of (node, color)
        :return: retruns the updated assignment
        """
        self.graph.nodes[node]['color'] = 'white'
        self.graph.nodes[node]['colors'] = self.color_list
        assignment = [(Xi, Di) for (Xi, Di) in assignment if Xi != node]
        self.plot_graph()
        time.sleep(1)  # Add a pause to visualize the removed assignment
        return assignment

import networkx as nx
import matplotlib.pyplot as plt
import time


def color_graph(graph, num_of_colors, colors_list):
    """
    Colors the graph using the Backtracking Search algorithm.

    Parameters:
        - graph: The graph to be colored.
        - num_of_colors: The number of colors available for coloring.
        - colors_list: A list of colors to be used for coloring.

    Returns:
        - The colored graph if a valid coloring is found, False otherwise.
    """
    nx.set_node_attributes(graph, 'white', 'color') #first sets all to white
    nx.set_node_attributes(graph, colors_list, 'colors')
    plt.ion()
    plot_graph(graph) #start the plot
    res = backtracking_search(graph,colors_list)
    #apply the colors to the nodes
    if res:
        for node, color in res:
            graph.nodes[node]['color'] = color
        return graph
    else:
        print("No valid coloring exists for the graph.")
        return False



def backtracking_search(graph,colors_list):
    """
    Applies the Backtracking Search algorithm to find a valid coloring for the graph.

    Parameters:
        - graph: The graph to be colored.
        - colors_list: A list of colors available for coloring.

    Returns:
        - A list of node-color assignments if a valid coloring is found, None otherwise.
    """
    return backtrack(graph, [],colors_list)

def backtrack(graph, assignment, colors_list):
    """
     Recursive function that performs the backtracking search for coloring the graph.

     Parameters:
         - graph: The graph to be colored.
         - assignment: A list of current node-color assignments.
         - colors_list: A list of colors available for coloring.

     Returns:
         - A list of node-color assignments if a valid coloring is found, None otherwise.
     """
    if is_assignment_completed(assignment, graph):
        return assignment
    if ac_3(graph):
        print(graph.nodes(data=True))
        var = select_unassigned_variable(graph, assignment)
        colors = nx.get_node_attributes(graph, 'colors')
        for color in colors[var]:
            if consistent(graph, var, color, assignment):
                assign(graph, var, color, assignment)
                result = backtrack(graph, assignment,colors_list)
                if result is not None:
                    return result
            assignment = remove_assignment(graph, var, colors_list, assignment)
    return None

def ac_3(graph):
    """
    Applies the AC-3 algorithm to enforce arc consistency on the graph.

    Parameters:
        - graph: The graph to be processed.

    Returns:
        - True if the graph is arc consistent after applying AC-3, False otherwise.
    """
    queue = list(graph.edges())

    # Create a list of opposite edges and add them to the queue
    opposite_edges = [(edge[1], edge[0]) for edge in queue]
    queue.extend(opposite_edges)

    while queue:
        (Xi, Xj) = queue.pop()
        if revise(graph, Xi, Xj):
            if len(graph.nodes[Xi]['colors']) == 0:
                return False
            for Xk in graph[Xi]:
                queue.append((Xk, Xi))
    return True
def revise(graph, Xi, Xj):
    """
    Applies the revise operation to make the domain of Xi arc-consistent with Xj.

    Parameters:
        - graph: The graph containing the nodes and their domains.
        - Xi: The first node in the arc.
        - Xj: The second node in the arc.

    Returns:
        - True if the domain of Xi is revised (reduced), False otherwise.
    """
    revised = False
    colors = nx.get_node_attributes(graph, 'colors')
    new_colors = [domx for domx in graph.nodes[Xi]['colors'] if any(domx != domy for domy in graph.nodes[Xj]['colors'])]
    if len(new_colors) < len(graph.nodes[Xi]['colors']):
        graph.nodes[Xi]['colors'] = new_colors
        revised = True
    return revised
def plot_graph(graph):
    """
    Plots the graph with assigned node colors.

    Parameters:
        - graph: The graph to be plotted with node colors.

    Returns:
        None
    """
    plt.clf()
    node_colors = [graph.nodes[node]['color'] for node in graph.nodes]
    node_border_color = 'black'  # Border color for nodes
    node_size = 1000  # Increase the size of nodes
    pos = nx.spring_layout(graph, seed=42)  # Set the seed for consistent layout
    nx.draw_networkx(graph, pos=pos, with_labels=True, font_weight='bold', node_color=node_colors,
                     edgecolors=node_border_color, node_size=node_size)
    plt.pause(0.3)
    plt.draw()



def assign(graph, node, color, assignment):
    """
       Assigns a color to a node in the graph.

       Parameters:
           - graph: The graph.
           - node: The node to be assigned a color.
           - color: The color to assign to the node.
           - assignment: The current list of node-color assignments.

       Returns:
           - The updated list of node-color assignments.
       """
    graph.nodes[node]['color'] = color
    graph.nodes[node]['colors'] = [color]
    assignment.append((node, color))
    plot_graph(graph)
    time.sleep(1)  # Add a pause to visualize the assigned color
    return assignment

def remove_assignment(graph, node, colors, assignment):
    """
    Removes the color assignment from a node in the graph.

    Parameters:
        - graph: The graph.
        - node: The node from which to remove the color assignment.
        - colors: The list of colors available for assignment.
        - assignment: The current list of node-color assignments.

    Returns:
        - The updated list of node-color assignments.
    """

    graph.nodes[node]['color'] = 'white'
    graph.nodes[node]['colors'] = colors
    assignment= [(Xi, Di) for (Xi, Di) in assignment if Xi != node]
    plot_graph(graph)
    time.sleep(1)  # Add a pause to visualize the removed assignment
    return assignment
def is_assignment_completed(assignment, graph):
    """
      Checks if the node-color assignment is completed for the graph.

      Parameters:
          - assignment: The list of node-color assignments.
          - graph: The graph.

      Returns:
          - True if the assignment is completed, False otherwise.
      """
    return len(assignment) == graph.number_of_nodes()

def select_unassigned_variable(graph, assignment):
    """
    Selects an unassigned variable (node) in the graph for coloring.

    Parameters:
        - graph: The graph.
        - assignment: The current list of node-color assignments.

    Returns:
        - The selected unassigned variable (node).
    """
    sorted_degrees = sorted(graph.degree(), key=lambda x: x[1], reverse=True)
    for node, degree in sorted_degrees:
        if node not in [x[0] for x in assignment]:
            return node

def consistent(graph, node, color, assignment):
    """
    Checks if assigning a color to a node is consistent with the graph's constraints.

    Parameters:
        - graph: The graph.
        - node: The node to be assigned a color.
        - color: The color to be assigned.
        - assignment: The current list of node-color assignments.

    Returns:
        - True if the assignment is consistent, False otherwise.
    """
    for val in assignment:
        if val[1] == color and val[0] in graph.neighbors(node):
            return False
    return True

def main():
    """
    The main function that performs the graph coloring algorithm.

    It creates a graph, prompts the user to enter the number of colors, and attempts to color the graph
    using the specified number of colors. If a valid coloring is found, it prints the nodes with their
    assigned colors. Otherwise, it displays a message indicating that no solution was found.

    :return: None
    """
    G = nx.Graph()
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(0, 3)
    G.add_edge(0, 4)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 4)
    colors_list = ["violet", "coral", "cyan", "limegreen", "royalblue", "darkorchid", "orange"]
    num_of_colors = int(input("Enter the number of colors: "))
    colors_list = colors_list[:num_of_colors]

    colored_graph = color_graph(G, num_of_colors, colors_list)
    if colored_graph:
        print(colored_graph.nodes(data=True))
    else:
        print("No solution found. The graph cannot be colored with the given number of colors.")
    plt.show(block=True)
    print("To exit close the pop up plot window please ")
    exit()

if __name__ == "__main__":
    main()
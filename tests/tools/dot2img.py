
import graphviz

# Convert a .dot file to .png
from graphviz import render
render('dot', 'png', '/opt/mybot/story_graph.dot')


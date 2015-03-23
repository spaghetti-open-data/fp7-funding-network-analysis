# Powered by Python 2.7

# project the two-mode to one-mode network

# To cancel the modifications performed by the script
# on the current graph, click on the undo button.

# Some useful keyboards shortcuts : 
#   * Ctrl + D : comment selected lines.
#   * Ctrl + Shift + D  : uncomment selected lines.
#   * Ctrl + I : indent selected lines.
#   * Ctrl + Shift + I  : unindent selected lines.
#   * Ctrl + Return  : run script.
#   * Ctrl + F  : find selected text.
#   * Ctrl + R  : replace selected text.
#   * Ctrl + Space  : show auto-completion dialog.

from tulip import *

# the updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# the pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# the runGraphScript(scriptFile, graph) function can be called to launch another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# the main(graph) function must be defined 
# to run the script on the current graph

def main(graph): 
	Connected_component =  graph.getDoubleProperty("Connected component")
	FM3_OGDF =  graph.getLayoutProperty("FM^3 (OGDF)")
	call =  graph.getStringProperty("call")
	city =  graph.getStringProperty("city")
	coordinator =  graph.getStringProperty("coordinator")
	coordinatorCountry =  graph.getStringProperty("coordinatorCountry")
	country =  graph.getStringProperty("country")
	ecMaxContribution =  graph.getDoubleProperty("ecMaxContribution")
	fundingScheme =  graph.getStringProperty("fundingScheme")
	inDegree =  graph.getDoubleProperty("inDegree")
	inOutDegree =  graph.getDoubleProperty("inOutDegree")
	isCoordinator =  graph.getBooleanProperty("isCoordinator")
	organisationId =  graph.getStringProperty("organisationId")
	organisationName =  graph.getStringProperty("organisationName")
	organisationShortName =  graph.getStringProperty("organisationShortName")
	organizationUrl =  graph.getStringProperty("organizationUrl")
	outDegree =  graph.getDoubleProperty("outDegree")
	programmeCode =  graph.getStringProperty("programmeCode")
	projectNode =  graph.getBooleanProperty("projectNode")
	projectRcn =  graph.getStringProperty("projectRcn")
	projectReference =  graph.getStringProperty("projectReference")
	projectUrl =  graph.getStringProperty("projectUrl")
	rcn =  graph.getStringProperty("rcn")
	reference =  graph.getStringProperty("reference")
	startDate =  graph.getStringProperty("startDate")
	subjects_1 =  graph.getStringProperty("subjects 1")
	subjects_2 =  graph.getStringProperty("subjects 2")
	subjects_3 =  graph.getStringProperty("subjects 3")
	subjects_4 =  graph.getStringProperty("subjects 4")
	subjects_5 =  graph.getStringProperty("subjects 5")
	subjects_6 =  graph.getStringProperty("subjects 6")
	subjects_7 =  graph.getStringProperty("subjects 7")
	subjects_8 =  graph.getStringProperty("subjects 8")
	subprogramme =  graph.getStringProperty("subprogramme")
	title =  graph.getStringProperty("title")
	totalCost =  graph.getDoubleProperty("totalCost")
	viewBorderColor =  graph.getColorProperty("viewBorderColor")
	viewBorderWidth =  graph.getDoubleProperty("viewBorderWidth")
	viewColor =  graph.getColorProperty("viewColor")
	viewFont =  graph.getStringProperty("viewFont")
	viewFontSize =  graph.getIntegerProperty("viewFontSize")
	viewLabel =  graph.getStringProperty("viewLabel")
	viewLabelBorderColor =  graph.getColorProperty("viewLabelBorderColor")
	viewLabelBorderWidth =  graph.getDoubleProperty("viewLabelBorderWidth")
	viewLabelColor =  graph.getColorProperty("viewLabelColor")
	viewLabelPosition =  graph.getIntegerProperty("viewLabelPosition")
	viewLayout =  graph.getLayoutProperty("viewLayout")
	viewMetaGraph =  graph.getGraphProperty("viewMetaGraph")
	viewMetric =  graph.getDoubleProperty("viewMetric")
	viewRotation =  graph.getDoubleProperty("viewRotation")
	viewSelection =  graph.getBooleanProperty("viewSelection")
	viewShape =  graph.getIntegerProperty("viewShape")
	viewSize =  graph.getSizeProperty("viewSize")
	viewSrcAnchorShape =  graph.getIntegerProperty("viewSrcAnchorShape")
	viewSrcAnchorSize =  graph.getSizeProperty("viewSrcAnchorSize")
	viewTexture =  graph.getStringProperty("viewTexture")
	viewTgtAnchorShape =  graph.getIntegerProperty("viewTgtAnchorShape")
	viewTgtAnchorSize =  graph.getSizeProperty("viewTgtAnchorSize")

		
	def two2OneMode (graph, booleanProperty, value):
		'''
		Induces a one-mode network from a bipartite graph based on a Boolean property.
		The induced network is of nodes of the type defined by value (True or False) 
		
		TODO
		'''
		# apply the Equal Value algorithm on the property
		# of the two resulting subgraphs, select the one corresponding to the value you want.
		# in our case the property is projectNode, the value is False
		# back in the 2-mode, iterate over your nodes.
		# for each node of project type iterate over edges to discover the project participants
		# for now, we add one edge per each project that two orgs do together.
		
		
	# before doing anything, run equalValue on the bipartite graph for projectNode
	# this gives two subgraphs, one of which contains only the ogranization-type nodes
	# use the Python shell to rename the graph for projectNode: false to orgsOnly
	
	# store the bipartite in a subgraph before adding any edges
	graph.setName('mainGraph')
	bipartite = graph.addSubGraph('bipartite')
	for n in graph.getNodes():
		bipartite.addNode(n)
	for e in graph.getEdges():
		bipartite.addEdge(e)
		

	# the graph
	onemode = graph.getSubGraph('orgsOnly')
	# initialize the property to store number of projects connecting two orgs
	projectsTogether = onemode.getLocalIntegerProperty('projectsTogether')
	
	for p in graph.getNodes(): # iterate over nodes...
		if projectNode.getNodeValue(p) == True: # .. only of the "project" type
			cost = totalCost.getNodeValue(p)
			sp = subprogramme.getNodeValue(p)
			participants = []
			for e in graph.getInEdges(p): 
				participants.append(graph.source(e))
			for i in range (len(participants)):
				for j in range (i+1, len(participants)):
					newEdge = onemode.addEdge(participants[i], participants[j])
					totalCost[newEdge] = cost
					subprogramme[newEdge] = sp
					

# Powered by Python 2.7

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
import csv

# the updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# the pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# the runGraphScript(scriptFile, graph) function can be called to launch another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# the main(graph) function must be defined 
# to run the script on the current graph

def main(graph): 
	Connected_Component__viewMetric =  graph.getDoubleProperty("Connected Component - (viewMetric)")
	KCores =  graph.getDoubleProperty("K-Cores")
	moneyTogether =  graph.getDoubleProperty("moneyTogether")
	stackedEdgeDegree =  graph.getDoubleProperty("stackedEdgeDegree")
	viewColor =  graph.getColorProperty("viewColor")
	viewLayout =  graph.getLayoutProperty("viewLayout")
	viewMetric =  graph.getDoubleProperty("viewMetric")
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
	projectsTogether =  graph.getIntegerProperty("projectsTogether")
	rcn =  graph.getStringProperty("rcn")
	reference =  graph.getStringProperty("reference")
	startDate =  graph.getStringProperty("startDate")
	deepCollabDegree = graph.getDoubleProperty('deepCollabDegree')
	subprogramme =  graph.getStringProperty("subprogramme")
	title =  graph.getStringProperty("title")
	totalCost =  graph.getDoubleProperty("totalCost")
	viewBorderColor =  graph.getColorProperty("viewBorderColor")
	viewBorderWidth =  graph.getDoubleProperty("viewBorderWidth")
	viewFont =  graph.getStringProperty("viewFont")
	viewFontSize =  graph.getIntegerProperty("viewFontSize")
	viewLabel =  graph.getStringProperty("viewLabel")
	viewLabelBorderColor =  graph.getColorProperty("viewLabelBorderColor")
	viewLabelBorderWidth =  graph.getDoubleProperty("viewLabelBorderWidth")
	viewLabelColor =  graph.getColorProperty("viewLabelColor")
	viewLabelPosition =  graph.getIntegerProperty("viewLabelPosition")
	viewMetaGraph =  graph.getGraphProperty("viewMetaGraph")
	viewRotation =  graph.getDoubleProperty("viewRotation")
	viewSelection =  graph.getBooleanProperty("viewSelection")
	viewShape =  graph.getIntegerProperty("viewShape")
	viewSize =  graph.getSizeProperty("viewSize")
	viewSrcAnchorShape =  graph.getIntegerProperty("viewSrcAnchorShape")
	viewSrcAnchorSize =  graph.getSizeProperty("viewSrcAnchorSize")
	viewTexture =  graph.getStringProperty("viewTexture")
	viewTgtAnchorShape =  graph.getIntegerProperty("viewTgtAnchorShape")
	viewTgtAnchorSize =  graph.getSizeProperty("viewTgtAnchorSize")
	
	dirPath = '/Users/albertocottica/Documents/SOD15Hackathon/'
	output_file = open(dirPath + 'FP7_deathStar2.csv', 'w')
	csvWriter = csv.writer(output_file, delimiter = ',')
	csvWriter.writerow(['country', 'name', 'partners', 'stable partners'])

	for org in graph.getNodes():
		name = organisationName.getNodeValue(org)
		orgCountry = country.getNodeValue(org)
		partners = int(stackedEdgeDegree.getNodeValue(org))
		stablePartners = int (deepCollabDegree.getNodeValue(org))
		csvWriter.writerow([orgCountry, name, partners, stablePartners])
		
	output_file.close()
	print ('The end.')

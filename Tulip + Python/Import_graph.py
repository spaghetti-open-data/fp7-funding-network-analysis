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

import time
import datetime
import csv
from tulip import *

# the updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# the pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# the runGraphScript(scriptFile, graph) function can be called to launch another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# the main(graph) function must be defined 
# to run the script on the current graph

# start the clock
start_script = datetime.datetime.now()

# initialize variables

dirPath = '/Users/albertocottica/Documents/SOD15Hackathon/'

def loadProjects():
	''' loads the projects CSV file and puts the results into a Dict'''
	projectsFile = dirPath + 'FP7_projects.csv'
	projects = csv.DictReader(open(projectsFile, 'rb'), delimiter=',')
	projectsList = []
	for line in projects:
		projectsList.append(line)
	return projectsList
	
def loadOrgs():
	''' loads the orgs CSV file and puts the results into a Dict'''
	orgsFile = dirPath + 'FP7_orgs.csv'
	orgs = csv.DictReader(open(orgsFile, 'rb'), delimiter=',')
	orgsList = []
	for line in orgs:
		orgsList.append(line)
	return orgsList
	
def main(graph): 
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

	for n in graph.getNodes():
		print n
		
	projectNode = graph.getBooleanProperty('projectNode') # this property is common to both node types
	# create node properties: start with properties related to projects
	rcn = graph.getStringProperty('rcn')
	reference = graph.getStringProperty('reference')
	programmeCode = graph.getStringProperty('programmeCode')
	subprogramme = graph.getStringProperty('subprogramme')
	title = graph.getStringProperty('title')
	startDate = graph.getStringProperty('startDate')
	endDate = graph.getStringProperty('startDate')
	projectUrl = graph.getStringProperty('projectUrl')
	totalCost = graph.getDoubleProperty('totalCost')
	ecMaxContribution = graph.getDoubleProperty('ecMaxContribution')
	call = graph.getStringProperty('call')
	fundingScheme = graph.getStringProperty('fundingScheme')
	coordinator = graph.getStringProperty('coordinator')
	organisationId = graph.getStringProperty('organisationId')
	coordinatorCountry = graph.getStringProperty('coordinatorCountry')
	subjects1 = graph.getStringProperty('subjects 1')
	subjects2 = graph.getStringProperty('subjects 2')
	subjects3 = graph.getStringProperty('subjects 3')
	subjects4 = graph.getStringProperty('subjects 4')
	subjects5 = graph.getStringProperty('subjects 5')
	subjects6 = graph.getStringProperty('subjects 6')
	subjects7 = graph.getStringProperty('subjects 7')
	subjects8 = graph.getStringProperty('subjects 8')
	
	# now create the properties of org-type nodes
	projectRcn = graph.getStringProperty('projectRcn')
	projectReference = graph.getStringProperty('projectReference')
	organisationName = graph.getStringProperty('organisationName')
	organisationShortName = graph.getStringProperty('organisationShortName')
	country = graph.getStringProperty('country')
	city = graph.getStringProperty('city')
	organizationUrl = graph.getStringProperty('organizationUrl')
	
	# now create the properties of edges
	isCoordinator = graph.getBooleanProperty('isCoordinator')
				
	projectsList = loadProjects() # we execute the functions to run the files
	orgsList = loadOrgs()

	# add the projects as nodes from a list of projects, assigning their characteristics to node properties
	# requires plenty of OpenRefine
	# create project-type nodes and populate their properties

	p2n = {} # Ben's map trick. This maps the rcn property of projects to their node objects.
	counter = 0
	for p in projectsList:
		counter += 1
		print ('Adding project ' + str(counter))
		n = graph.addNode()
		projectNode[n] = True # this is set to True for all projects!
		rcnCode = p['rcn']
		rcn[n] = rcnCode
		p2n[rcnCode] = n # update the map
		reference[n] = p['reference']
		programmeCode[n] = p['programmeCode']
		subprogramme[n] = p['subprogramme']
		title[n] = p['title']
		try: # this is needed because of difformity in data formats
			startDate[n] = time.mktime(datetime.datetime.strptime(p['startDate'], '%Y-%m-%dT%H:%M:%SZ').timetuple())
		except:
			pass
		try: # ditto
			endDate[n] = time.mktime(datetime.datetime.strptime(p['endDate'], '%Y-%m-%dT%H:%M:%SZ').timetuple())
		except:
			pass
		projectUrl[n] = p['projectUrl']
		totalCost[n] = float(p['totalCost'])
		ecMaxContribution[n] = float(p['ecMaxContribution'])
		call[n] = p['call']
		fundingScheme[n] = p['fundingScheme']	
		coordinator[n] = p['coordinator']
		organisationId[n] = p['organisationId']
		coordinatorCountry[n] = p['coordinatorCountry']
		subjects1[n] = p['subjects 1']
		subjects2[n] = p['subjects 2']
		subjects3[n] = p['subjects 3']
		subjects4[n] = p['subjects 4']
		subjects5[n] = p['subjects 5']
		subjects6[n] = p['subjects 6']
		subjects7[n] = p['subjects 7']
		subjects8[n] = p['subjects 8']
	
	# now add the org-type nodes and populate their properties
	counter = 0
	o2n = {} # Ben's map trick
	for o in orgsList:
		counter += 1
		print ('Adding org ' + str(counter))
		# check that the organisation has not already been added
		oName = o['organisationName']
		oRcn = o['projectRcn']
		if oName not in o2n:
			n = graph.addNode()
			projectNode[n] = False # Set to False for all orgs! 
			projectRcn[n] = oRcn
			projectReference[n] = o['projectReference']
			organisationName[n] = oName
			organisationShortName[n] = o['organisationShortName']
			country[n] = o['country']
			city[n] = o['city']
			organizationUrl[n] = o['organizationUrl']
			o2n[oName] = n
			
		# create an edge	
		n = o2n[oName]
		project = p2n[oRcn]
		try:
			newEdge = graph.addEdge(n, project)
			isCoordinator[newEdge] = False
			if o['organisationRole'] == coordinator:
				isCoordinator[newEdge] = True
		except:
			print ('Could not add org ' + oName + ' to project' + oRcn)

	end_script = datetime.datetime.now()
	running_time = end_script - start_script
	print ('Executed in ' + str(running_time))

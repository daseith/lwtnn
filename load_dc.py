from DeepJetCore.DataCollection import DataCollection
from pprint import pprint

dc = DataCollection()
dc.readFromFile('dc/dataCollection.dc')


six_times = [
    'TagVarCSVTrk_trackJetDistVal',
    'TagVarCSVTrk_trackPtRel',
    'TagVarCSVTrk_trackDeltaR',
    'TagVarCSVTrk_trackPtRatio',
    'TagVarCSVTrk_trackSip3dSig',
    'TagVarCSVTrk_trackSip2dSig',
    'TagVarCSVTrk_trackDecayLenVal'
]


four_times = ['TagVarCSV_trackEtaRel']

variable_list = ['jet_pt', 'jet_eta',
    'TagVarCSV_jetNSecondaryVertices',
    'TagVarCSV_trackSumJetEtRatio', 'TagVarCSV_trackSumJetDeltaR',
    'TagVarCSV_vertexCategory', 'TagVarCSV_trackSip2dValAboveCharm',
    'TagVarCSV_trackSip2dSigAboveCharm', 'TagVarCSV_trackSip3dValAboveCharm',
    'TagVarCSV_trackSip3dSigAboveCharm', 'TagVarCSV_jetNSelectedTracks',
    'TagVarCSV_jetNTracksEtaRel',
    'TagVarCSVTrk_trackJetDistVal',
    'TagVarCSVTrk_trackPtRel',
    'TagVarCSVTrk_trackDeltaR',
    'TagVarCSVTrk_trackPtRatio',
    'TagVarCSVTrk_trackSip3dSig',
    'TagVarCSVTrk_trackSip2dSig',
    'TagVarCSVTrk_trackDecayLenVal',
    'TagVarCSV_trackEtaRel',
    'TagVarCSV_vertexMass',
    'TagVarCSV_vertexNTracks',
    'TagVarCSV_vertexEnergyRatio',
    'TagVarCSV_vertexJetDeltaR',
    'TagVarCSV_flightDistance2dVal',
    'TagVarCSV_flightDistance2dSig',
    'TagVarCSV_flightDistance3dVal',
    'TagVarCSV_flightDistance3dSig']

means = dc.means[0]
stddevs = dc.means[1]
varnames = dc.means.dtype.names

variables = []
for mean, stddev, name in zip(means, stddevs, varnames):
    if name in variable_list:
        if name in six_times:
            for i in range(0, 6):
                var = name+'_'+str(i)
                variables.append( { 'name' : var, 'scale' : stddev, 'offset' : mean , 'defaults' : 0.0 } )
        elif name in four_times:
            for i in range(0, 4):
                var = name+'_'+str(i)
                variables.append( { 'name' : var, 'scale' : stddev, 'offset' : mean , 'defaults' : 0.0 } )
        else:
            var = name
            variables.append( { 'name' : var, 'scale' : stddev, 'offset' : mean , 'defaults' : 0.0} )

#pprint (variables)
variables = [ { 'name' : 'node_0', 'variables' : variables } ]
print len(variables)

outputs = [
        "probb",
        "probbb",
        "probc",
        "probudsg"
    ]


var_dic = {}

var_dic['outputs'] = [{ 'labels' : outputs, 'name' : 'dense_6_0' }]
var_dic['inputs'] = variables
var_dic["input_sequences"] = []
#var_dic['inputs'] = variables
#var_dic['class_labels'] = outputs
#var_dic['keras_version'] = '2.0.0'

pprint (var_dic)

import json
with open('DeepCSV_var.json', 'w') as json_file:
    json.dump(var_dic, json_file)

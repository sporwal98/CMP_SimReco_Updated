# Run arguments file auto-generated on Mon Aug  8 12:06:51 2022 by:
# JobTransform: HITtoRDO
# Version: $Id: trfExe.py 792052 2017-01-13 13:36:51Z mavogel $
# Import runArgs class
from PyJobTransforms.trfJobOptions import RunArguments
runArgs = RunArguments()
runArgs.trfSubstepName = 'HITtoRDO' 

runArgs.maxEvents = 10
runArgs.conditionsTag = 'OFLCOND-MC16-SDR-14'
runArgs.DataRunNumber = 284500
runArgs.postInclude = ['RecJobTransforms/UseFrontier.py']
runArgs.geometryVersion = 'ATLAS-R2-2016-01-00-01_VALIDATION'

# Input data
runArgs.inputHITSFile = ['HITS.pool.root']
runArgs.inputHITSFileType = 'HITS'
runArgs.inputHITSFileNentries = 10L
runArgs.HITSFileIO = 'input'

# Output data
runArgs.outputRDOFile = 'tmp.RDO'
runArgs.outputRDOFileType = 'RDO'

# Extra runargs

# Extra runtime runargs
try:
    runArgs.LowPtMinbiasHitsFile = runArgs.inputLowPtMinbiasHitsFile
except AttributeError:
    print "WARNING - AttributeError for LowPtMinbiasHitsFile"
try:
    runArgs.beamGasHitsFile = runArgs.inputBeamGasHitsFile
except AttributeError:
    print "WARNING - AttributeError for beamGasHitsFile"
try:
    runArgs.cavernHitsFile = runArgs.inputCavernHitsFile
except AttributeError:
    print "WARNING - AttributeError for cavernHitsFile"
try:
    runArgs.HighPtMinbiasHitsFile = runArgs.inputHighPtMinbiasHitsFile
except AttributeError:
    print "WARNING - AttributeError for HighPtMinbiasHitsFile"
try:
    runArgs.beamHaloHitsFile = runArgs.inputBeamHaloHitsFile
except AttributeError:
    print "WARNING - AttributeError for beamHaloHitsFile"

# Literal runargs snippets

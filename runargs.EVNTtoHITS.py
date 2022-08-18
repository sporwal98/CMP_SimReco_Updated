# Run arguments file auto-generated on Thu Aug  4 10:50:56 2022 by:
# JobTransform: EVNTtoHITS
# Version: $Id: trfExe.py 792052 2017-01-13 13:36:51Z mavogel $
# Import runArgs class
from PyJobTransforms.trfJobOptions import RunArguments
runArgs = RunArguments()
runArgs.trfSubstepName = 'EVNTtoHITS' 

runArgs.conditionsTag = 'OFLCOND-MC16-SDR-14'
runArgs.physicsList = 'FTFP_BERT_ATL_VALIDATION'
runArgs.truthStrategy = 'MC15aPlusLLP'
runArgs.simulator = 'FullG4_LongLived'
runArgs.preInclude = ['SimulationJobOptions/preInclude.BeamPipeKill.py', 'SimulationJobOptions/preInclude.FrozenShowersFCalOnly.py', 'SimulationJobOptions/preInclude.ExtraParticles.py', 'SimulationJobOptions/preInclude.G4ExtraProcesses.py']
runArgs.postInclude = ['RecJobTransforms/UseFrontier.py']
runArgs.preExec = ['simFlags.SimBarcodeOffset.set_Value_and_Lock(200000)', 'simFlags.TRTRangeCut=30.0;simFlags.TightMuonStepping=True']
runArgs.geometryVersion = 'ATLAS-R2-2016-01-00-01_VALIDATION'
runArgs.maxEvents = 10
runArgs.DataRunNumber = 284500

# Input data
runArgs.inputEVNTFile = ['EVNT.pool.root']
runArgs.inputEVNTFileType = 'EVNT'
runArgs.inputEVNTFileNentries = 100L
runArgs.EVNTFileIO = 'input'

# Output data
runArgs.outputHITSFile = 'HITS.pool.root'
runArgs.outputHITSFileType = 'HITS'

# Extra runargs

# Extra runtime runargs

# Literal runargs snippets

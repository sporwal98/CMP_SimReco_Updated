# Run arguments file auto-generated on Mon Aug  8 12:09:04 2022 by:
# JobTransform: ESDtoAOD
# Version: $Id: trfExe.py 792052 2017-01-13 13:36:51Z mavogel $
# Import runArgs class
from PyJobTransforms.trfJobOptions import RunArguments
runArgs = RunArguments()
runArgs.trfSubstepName = 'ESDtoAOD' 

runArgs.conditionsTag = 'OFLCOND-MC16-SDR-14'
runArgs.DataRunNumber = 284500
runArgs.postInclude = ['RecJobTransforms/UseFrontier.py']
runArgs.athenaopts = ['--preloadlib=/cvmfs/atlas-nightlies.cern.ch/repo/sw/21.0_Athena_x86_64-centos7-gcc62-opt/2022-08-02T2111/AthenaExternals/21.0.135/InstallArea/x86_64-centos7-gcc62-opt/lib/libintlc.so.5:/cvmfs/atlas-nightlies.cern.ch/repo/sw/21.0_Athena_x86_64-centos7-gcc62-opt/2022-08-02T2111/AthenaExternals/21.0.135/InstallArea/x86_64-centos7-gcc62-opt/lib/libimf.so']
runArgs.geometryVersion = 'ATLAS-R2-2016-01-00-01_VALIDATION'

# Explicitly added to process all events in this step
runArgs.maxEvents = -1

# Input data
runArgs.inputESDFile = ['tmp.ESD']
runArgs.inputESDFileType = 'ESD'
runArgs.inputESDFileNentries = None
runArgs.ESDFileIO = 'temporary'

# Output data
runArgs.outputAODFile = 'AOD.root'
runArgs.outputAODFileType = 'AOD'

# Extra runargs

# Extra runtime runargs

# Literal runargs snippets

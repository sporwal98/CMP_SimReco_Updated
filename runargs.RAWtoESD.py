# Run arguments file auto-generated on Mon Aug  8 12:08:20 2022 by:
# JobTransform: RAWtoESD
# Version: $Id: trfExe.py 792052 2017-01-13 13:36:51Z mavogel $
# Import runArgs class
from PyJobTransforms.trfJobOptions import RunArguments
runArgs = RunArguments()
runArgs.trfSubstepName = 'RAWtoESD' 

runArgs.conditionsTag = 'OFLCOND-MC16-SDR-14'
runArgs.DataRunNumber = 284500
runArgs.postInclude = ['RecJobTransforms/UseFrontier.py']
runArgs.athenaopts = ['--preloadlib=/cvmfs/atlas-nightlies.cern.ch/repo/sw/21.0_Athena_x86_64-centos7-gcc62-opt/2022-08-02T2111/AthenaExternals/21.0.135/InstallArea/x86_64-centos7-gcc62-opt/lib/libintlc.so.5:/cvmfs/atlas-nightlies.cern.ch/repo/sw/21.0_Athena_x86_64-centos7-gcc62-opt/2022-08-02T2111/AthenaExternals/21.0.135/InstallArea/x86_64-centos7-gcc62-opt/lib/libimf.so']
runArgs.geometryVersion = 'ATLAS-R2-2016-01-00-01_VALIDATION'

# Explicitly added to process all events in this step
runArgs.maxEvents = -1

# Input data
runArgs.inputRDOFile = ['tmp.RDO']
runArgs.inputRDOFileType = 'RDO'
runArgs.inputRDOFileNentries = 10L
runArgs.RDOFileIO = 'temporary'

# Output data
runArgs.outputESDFile = 'tmp.ESD'
runArgs.outputESDFileType = 'ESD'

# Extra runargs

# Extra runtime runargs

# Literal runargs snippets

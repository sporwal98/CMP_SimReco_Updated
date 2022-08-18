#! /bin/sh
# DBRelease setup
echo Setting up DBRelease /cvmfs/atlas.cern.ch/repo/sw/database/DBRelease/current environment
export DBRELEASE=current
export CORAL_AUTH_PATH=/cvmfs/atlas.cern.ch/repo/sw/database/DBRelease/current/XMLConfig
export CORAL_DBLOOKUP_PATH=/cvmfs/atlas.cern.ch/repo/sw/database/DBRelease/current/XMLConfig
export TNS_ADMIN=/cvmfs/atlas.cern.ch/repo/sw/database/DBRelease/current/oracle-admin
DATAPATH=/cvmfs/atlas.cern.ch/repo/sw/database/DBRelease/current:$DATAPATH
# Customised environment
athena.py --preloadlib=/cvmfs/atlas-nightlies.cern.ch/repo/sw/21.0_Athena_x86_64-centos7-gcc62-opt/2022-08-02T2111/AthenaExternals/21.0.135/InstallArea/x86_64-centos7-gcc62-opt/lib/libintlc.so.5:/cvmfs/atlas-nightlies.cern.ch/repo/sw/21.0_Athena_x86_64-centos7-gcc62-opt/2022-08-02T2111/AthenaExternals/21.0.135/InstallArea/x86_64-centos7-gcc62-opt/lib/libimf.so runargs.HITtoRDO.py SimuJobTransforms/skeleton.HITtoRDO.py

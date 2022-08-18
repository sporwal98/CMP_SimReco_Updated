Reco_tf.py --inputHITSFile HITS.pool.root \
--outputAODFile AOD.root \
--preExec "EVNTtoHITS:simFlags.SimBarcodeOffset.set_Value_and_Lock(200000)" \
          "EVNTtoHITS:simFlags.TRTRangeCut=30.0;simFlags.TightMuonStepping=True" \
--preInclude "EVNTtoHITS:SimulationJobOptions/preInclude.BeamPipeKill.py,SimulationJobOptions/preInclude.FrozenShowersFCalOnly.py,SimulationJobOptions/preInclude.ExtraParticles.py,SimulationJobOptions/preInclude.G4ExtraProcesses.py" \
--postInclude "default:RecJobTransforms/UseFrontier.py" \
--inputEVNTFile="EVNT.pool.root" \
--DBRelease "all:current" \
--conditionsTag "default:OFLCOND-MC16-SDR-14" \
--geometryVersion="default:ATLAS-R2-2016-01-00-01_VALIDATION" \
--DataRunNumber="284500" \
--maxEvents=10

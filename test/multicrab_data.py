##########################
#                        #
#  2017-01-16 MC         #
#                        #
##########################
dataset = {
#'DoubleEG_Run2016B-03Feb2017-v2_final_resub'  : '/DoubleEG/Run2016B-03Feb2017_ver2-v2/MINIAOD',
#'DoubleEG_Run2016C-03Feb2017-v1_final'  : '/DoubleEG/Run2016C-03Feb2017-v1/MINIAOD',
#'DoubleEG_Run2016D-03Feb2017-v1_final_resub'  : '/DoubleEG/Run2016D-03Feb2017-v1/MINIAOD',           
#'DoubleEG_Run2016E-03Feb2017-v1_final_resub'  : '/DoubleEG/Run2016E-03Feb2017-v1/MINIAOD',            
#'DoubleEG_Run2016F-03Feb2017-v1_final'  : '/DoubleEG/Run2016F-03Feb2017-v1/MINIAOD',            
#'DoubleEG_Run2016G-03Feb2017-v1_final_resub'  : '/DoubleEG/Run2016G-03Feb2017-v1/MINIAOD',            
#'DoubleEG_Run2016H-03Feb2017-v2_final_resub'  : '/DoubleEG/Run2016H-03Feb2017_ver2-v1/MINIAOD',       
#'DoubleEG_Run2016H-03Feb2017-v3_final'  : '/DoubleEG/Run2016H-03Feb2017_ver3-v1/MINIAOD',
#'SingleElectron_Run2016B-03Feb2017-v2_final_resub': '/SingleElectron/Run2016B-03Feb2017_ver2-v2/MINIAOD',
#'SingleElectron_Run2016C-03Feb2017-v1_final': '/SingleElectron/Run2016C-03Feb2017-v1/MINIAOD',
#'SingleElectron_Run2016D-03Feb2017-v1_final_resub': '/SingleElectron/Run2016D-03Feb2017-v1/MINIAOD',
#'SingleElectron_Run2016E-03Feb2017-v1_final_resub': '/SingleElectron/Run2016E-03Feb2017-v1/MINIAOD',
#'SingleElectron_Run2016F-03Feb2017-v1_final': '/SingleElectron/Run2016F-03Feb2017-v1/MINIAOD',
#'SingleElectron_Run2016G-03Feb2017-v1_final_resub': '/SingleElectron/Run2016G-03Feb2017-v1/MINIAOD',
#'SingleElectron_Run2016H-03Feb2017-v2_final_resub': '/SingleElectron/Run2016H-03Feb2017_ver2-v1/MINIAOD',
#'SingleElectron_Run2016H-03Feb2017-v3_final': '/SingleElectron/Run2016H-03Feb2017_ver3-v1/MINIAOD',

#'MET_Run2016B-03Feb2017-v2_0510': '/MET/Run2016B-03Feb2017_ver2-v2/MINIAOD',
'MET_Run2016C-03Feb2017-v1_0510': '/MET/Run2016C-03Feb2017-v1/MINIAOD',
#'MET_Run2016D-03Feb2017-v1_0510': '/MET/Run2016D-03Feb2017-v1/MINIAOD',
#'MET_Run2016E-03Feb2017-v1_0510': '/MET/Run2016E-03Feb2017-v1/MINIAOD',
#'MET_Run2016F-03Feb2017-v1_0510': '/MET/Run2016F-03Feb2017-v1/MINIAOD',
#'MET_Run2016G-03Feb2017-v1_0510': '/MET/Run2016G-03Feb2017-v1/MINIAOD',
#'MET_Run2016H-03Feb2017-v2_0510': '/MET/Run2016H-03Feb2017_ver2-v1/MINIAOD',
#'MET_Run2016H-03Feb2017-v3_0510': '/MET/Run2016H-03Feb2017_ver3-v1/MINIAOD'
}

nfiles = {
}

filesPerJob = {
}

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand

    def submit(config):
        res = crabCommand('submit', config = config)

    from CRABClient.UserUtilities import config
    config = config()

    name = '_data'
    config.General.workArea = 'crab_projects_0510'
    config.General.transferLogs = False
    config.General.transferOutputs = True
    config.JobType.pluginName = 'Analysis'
    config.JobType.psetName = 'IIHE.py'
    config.JobType.inputFiles   = ['data','rcdata.2016.v3']
    config.JobType.pyCfgParams = ['DataProcessing=rerecodata']
#    config.JobType.pyCfgParams = ['DataProcessing=promptdata']
    config.Data.inputDBS = 'global'
    config.Data.splitting = 'LumiBased'
    config.Data.unitsPerJob = 10
    config.Data.publication = False
    config.Data.ignoreLocality = True
    config.Data.lumiMask = '/user/wenxing/MiniAOD_170223/CMSSW_8_0_25/src/UserCode/IIHETree/test/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON_reReco_final.txt'
#    config.Data.lumiMask = '/user/wenxing/FINAL_code_170407/CMSSW_8_0_26_patch1/src/UserCode/IIHETree/test/resubmit_DoubleEG.json'
#    config.Data.lumiMask = '/user/wenxing/FINAL_code_170407/CMSSW_8_0_26_patch1/src/UserCode/IIHETree/test/resubmit_SingleEG.json'
    config.Site.storageSite = 'T2_BE_IIHE'

    for sample in dataset:
        config.General.requestName = sample
        config.Data.inputDataset = dataset[sample]
#        config.Data.outputDatasetTag = sample
        submit(config)

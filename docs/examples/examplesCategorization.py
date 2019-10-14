
import pyiomica as pio

from pyiomica import categorizationFunctions as cf
from pyiomica import dataStorage as ds

# Unzip sample data
with pio.zipfile.ZipFile(pio.os.path.join(pio.ConstantPyIOmicaExamplesDirectory, 'SLV.zip'), "r") as zipFile:
    zipFile.extractall(path=pio.ConstantPyIOmicaExamplesDirectory)

# Process sample dataset SLV_Hourly1 
dataName = 'SLV_Hourly1TimeSeries'
saveDir = pio.os.path.join('results', dataName, '')
dataDir = pio.os.path.join(pio.ConstantPyIOmicaExamplesDirectory, 'SLV')
df_data = pio.pd.read_csv(pio.os.path.join(dataDir, dataName + '.csv'), index_col=[0,1,2], header=0)
cf.calculateTimeSeriesCategorization(df_data, dataName, saveDir, NumberOfRandomSamples = 10**4)
cf.clusterTimeSeriesCategorization(dataName, saveDir)
cf.visualizeTimeSeriesCategorization(dataName, saveDir)
df_data_processed_H1 = ds.read(dataName+'_df_data_transformed', hdf5fileName=pio.os.path.join('results',dataName,dataName+'.h5'))

# Process sample dataset SLV_Hourly2 
dataName = 'SLV_Hourly2TimeSeries'
saveDir = pio.os.path.join('results', dataName, '')
dataDir = pio.os.path.join(pio.ConstantPyIOmicaExamplesDirectory, 'SLV')
df_data = pd.read_csv(pio.os.path.join(dataDir, dataName + '.csv'), index_col=[0,1,2], header=0)
cf.calculateTimeSeriesCategorization(df_data, dataName, saveDir, NumberOfRandomSamples = 10**3)
cf.clusterTimeSeriesCategorization(dataName, saveDir)
cf.visualizeTimeSeriesCategorization(dataName, saveDir)
df_data_processed_H2 = ds.read(dataName+'_df_data_transformed', hdf5fileName=pio.os.path.join('results',dataName,dataName+'.h5'))

# Use results from processing sample datasets SLV_Hourly1 and SLV_Hourly2 to calculate "Delta"
dataName = 'SLV_Delta'
saveDir = pio.os.path.join('results', dataName, '')
df_data = df_data_processed_H2.compareTwoTimeSeries(df_data_processed_H1, compareAllLevelsInIndex=False, mergeFunction=np.median).fillna(0.)
cf.calculateTimeSeriesCategorization(df_data, dataName, saveDir, NumberOfRandomSamples = 5*10**3)
cf.clusterTimeSeriesCategorization(dataName, saveDir)
cf.visualizeTimeSeriesCategorization(dataName, saveDir)
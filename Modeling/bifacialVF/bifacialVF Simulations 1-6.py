#!/usr/bin/env python
# coding: utf-8

# # bifacial VF Simulations 1-6
# 
# For a view factor simulation, S1 equals S2 in parameters, so we are only doing it once.
# 
# Modeling with bifacialVF the front (and rear where necessary) irradiances. Using pvlib functions to calculate module power output.
# 
# Not considering losses at the moment.
# 
# bifacialVF calculates electrical mismatch factors for bifacial systems (considers front and back). Therefore using them for bifacial systems only at the moment.
# 

# In[1]:


import bifacialvf
import numpy as np
import pandas as pd
import requests
import pvlib
import bifacial_radiance as br


# In[2]:


# Print bifacialvf Version:
bifacialvf.__version__


# In[3]:


print(br.__version__)
print(pvlib.__version__)
#2021 run: 0.3.4+275.ga152a2e.dirty bifacial_radiance
#2021 run: '0.1.7-dev1+33.gf02e57a' bifacialVf


# In[4]:


from datetime import date
date.today()


# # S1

# In[5]:


TMYtoread='../TMY3_Albuquerque_NM.csv'
writefiletitle='bifacialVF_S1.csv'

# Variables
tilt = 35                   # PV tilt (deg)
sazm = 180                  # PV Azimuth(deg) or tracker axis direction
albedo = None               # Use weather file albedo
CW = 2                      # 2 modules in landscape. No spacing between modules provided.
hub_height = 1.5/2          # Hub height Normalized by collector width
pitch = 5.7/2               # row to row spacing in normalized panel lengths. 
rowType = "single"          # RowType(first interior last single)
transFactor = 0             # TransmissionFactor(open area fraction)
sensorsy = 6                # sensorsy  
PVfrontSurface = "glass"    # PVfrontSurface(glass or ARglass)
PVbackSurface = "glass"     # PVbackSurface(glass or ARglass)

# Calculate PV Output Through Various Methods    
calculateBilInterpol = False   
calculatePVMismatch = True
portraitorlandscape='landscape'   # portrait or landscape
cellsnum = 72
bififactor = 0.0

deltastyle='TMY3'

# Tracking instructions
tracking=False
backtrack=False
limit_angle = 60

deltastyle='TMY3'

myTMY3, meta = bifacialvf.bifacialvf.readInputTMY(TMYtoread)

bifacialvf.simulate(myTMY3, meta, writefiletitle=writefiletitle, 
         tilt=tilt, sazm=sazm, pitch=pitch, hub_height=hub_height, 
         rowType=rowType, transFactor=transFactor, sensorsy=sensorsy, 
         PVfrontSurface=PVfrontSurface, PVbackSurface=PVbackSurface, 
         albedo=albedo, tracking=tracking, backtrack=backtrack, 
         limit_angle=limit_angle, calculatePVMismatch=calculatePVMismatch,
         cellsnum = cellsnum, bififactor=bififactor,
         calculateBilInterpol=calculateBilInterpol,
         portraitorlandscape=portraitorlandscape, deltastyle=deltastyle)


# # S3

# In[6]:


TMYtoread='../TMY3_Roskilde_DK.csv'
writefiletitle='bifacialVF_S3.csv'

# Variables
tilt = None                   # PV tilt (deg)
sazm = 180                    # PV Azimuth(deg) or tracker axis direction
albedo = None                 # Use weather file albedo
CW = 3.46404                  # 2 modules of ~1.65952m in portrait with 14.5cm of spacing between modules (ygap).
hub_height = 1.95/CW          # Hub height normalized by collector width
pitch = 12/CW                 # Row to row spacing in normalized panel lengths. 
rowType = "interior"          # RowType(first interior last single)
transFactor = 0.04            # TransmissionFactor(open area fraction)
sensorsy = 12                 # sensorsy
PVfrontSurface = "glass"      # PVfrontSurface(glass or ARglass)
PVbackSurface = "glass"       # PVbackSurface(glass or ARglass)

# Calculate PV Output Through Various Methods    
calculateBilInterpol = False     
calculatePVMismatch = True
portraitorlandscape='portrait'   # portrait or landscape
cellsnum = 72
bififactor = 0

# Tracking instructions
tracking=True
backtrack=True
limit_angle = 60

deltastyle='TMY3'

myTMY3, meta = bifacialvf.bifacialvf.readInputTMY(TMYtoread)

bifacialvf.simulate(myTMY3, meta, writefiletitle=writefiletitle, 
         tilt=tilt, sazm=sazm, pitch=pitch, hub_height=hub_height, 
         rowType=rowType, transFactor=transFactor, sensorsy=sensorsy, 
         PVfrontSurface=PVfrontSurface, PVbackSurface=PVbackSurface, 
         albedo=albedo, tracking=tracking, backtrack=backtrack, 
         limit_angle=limit_angle, calculatePVMismatch=calculatePVMismatch,
         cellsnum = cellsnum, bififactor=bififactor,
         calculateBilInterpol=calculateBilInterpol,
         portraitorlandscape=portraitorlandscape, deltastyle=deltastyle)


# # S4

# In[7]:


TMYtoread='../TMY3_Roskilde_DK.csv'
writefiletitle='bifacialVF_S4.csv'

# Variables
tilt = None                 # PV tilt (deg)
sazm = 180                  # PV Azimuth(deg) or tracker axis direction
albedo = None               # Use weather file albedo
CW = 3.49462                # 2 modules of ~1.67481m in portrait with 14.5cm of spacing between modules (ygap).
hub_height = 1.95/CW        # Hub height Normalized by collector width
pitch = 12/CW               # row to row spacing in normalized panel lengths. 
rowType = "interior"        # RowType(first interior last single)
transFactor = 0.04          # TransmissionFactor(open area fraction)
sensorsy = 12               # sensorsy
PVfrontSurface = "glass"    # PVfrontSurface(glass or ARglass)
PVbackSurface = "glass"     # PVbackSurface(glass or ARglass)

# Calculate PV Output Through Various Methods    
calculateBilInterpol = False   
calculatePVMismatch = True
portraitorlandscape='portrait'   # portrait or landscape
cellsnum = 72
bififactor = 0.65

# Tracking instructions
tracking=True
backtrack=True
limit_angle = 60

deltastyle='TMY3'

myTMY3, meta = bifacialvf.bifacialvf.readInputTMY(TMYtoread)

bifacialvf.simulate(myTMY3, meta, writefiletitle=writefiletitle, 
         tilt=tilt, sazm=sazm, pitch=pitch, hub_height=hub_height, 
         rowType=rowType, transFactor=transFactor, sensorsy=sensorsy, 
         PVfrontSurface=PVfrontSurface, PVbackSurface=PVbackSurface, 
         albedo=albedo, tracking=tracking, backtrack=backtrack, 
         limit_angle=limit_angle, calculatePVMismatch=calculatePVMismatch,
         cellsnum = cellsnum, bififactor=bififactor,
         calculateBilInterpol=calculateBilInterpol,
         portraitorlandscape=portraitorlandscape, deltastyle=deltastyle)


# # S5

# In[8]:


TMYtoread='../TMY3_Roskilde_DK.csv'
writefiletitle='bifacialVF_S5.csv'

# Variables
tilt = 25                   # PV tilt (deg)
sazm = 180                  # PV Azimuth(deg) or tracker axis direction
albedo = None               # Use weather file albedo
CW = 3.46404                # 2 modules of ~1.65952m in portrait with 14.5cm of spacing between modules (ygap).
clearance_height = 1.568016718/CW         # clearance height Normalized by collector width
pitch = 7.6/CW              # row to row spacing in normalized panel lengths. 
rowType = "interior"        # RowType(first interior last single)
transFactor = 0.04          # TransmissionFactor(open area fraction)
sensorsy = 12               # sensorsy
PVfrontSurface = "glass"    # PVfrontSurface(glass or ARglass)
PVbackSurface = "glass"     # PVbackSurface(glass or ARglass)

# Calculate PV Output Through Various Methods    
calculateBilInterpol = False      # Only works with landscape at the moment.
calculatePVMismatch = True
portraitorlandscape='portrait'   # portrait or landscape
cellsnum = 72
bififactor = 0.0

# Tracking instructions
tracking=False
backtrack=False
limit_angle = 60

deltastyle='TMY3'

myTMY3, meta = bifacialvf.bifacialvf.readInputTMY(TMYtoread)

bifacialvf.simulate(myTMY3, meta, writefiletitle=writefiletitle, 
         tilt=tilt, sazm=sazm, pitch=pitch, clearance_height=clearance_height, 
         rowType=rowType, transFactor=transFactor, sensorsy=sensorsy, 
         PVfrontSurface=PVfrontSurface, PVbackSurface=PVbackSurface, 
         albedo=albedo, tracking=tracking, backtrack=backtrack, 
         limit_angle=limit_angle, calculatePVMismatch=calculatePVMismatch,
         cellsnum = cellsnum, bififactor=bififactor,
         calculateBilInterpol=calculateBilInterpol,
         portraitorlandscape=portraitorlandscape, deltastyle=deltastyle)


# # S6

# In[9]:


TMYtoread='../TMY3_Roskilde_DK.csv'
writefiletitle='bifacialVF_S6.csv'

# Variables
tilt = 25                   # PV tilt (deg)
sazm = 180                  # PV Azimuth(deg) or tracker axis direction
albedo = None               # Use weather file albedo
CW = 3.49462                # 2 modules of ~1.67481m in portrait with 14.5cm of spacing between modules (ygap).
clearance_height = 1.561554885/CW         # Hclearance_height Normalized by collector width
pitch = 7.6/CW              # row to row spacing in normalized panel lengths. 
rowType = "interior"        # RowType(first interior last single)
transFactor = 0.04             # TransmissionFactor(open area fraction)
sensorsy = 12               # sensorsy
PVfrontSurface = "glass"    # PVfrontSurface(glass or ARglass)
PVbackSurface = "glass"     # PVbackSurface(glass or ARglass)

# Calculate PV Output Through Various Methods    
calculateBilInterpol = False  
calculatePVMismatch = True
portraitorlandscape='portrait'   # portrait or landscape
cellsnum = 72
bififactor = 0.65

# Tracking instructions
tracking=False
backtrack=False
limit_angle = 60

deltastyle='TMY3'

myTMY3, meta = bifacialvf.bifacialvf.readInputTMY(TMYtoread)

bifacialvf.simulate(myTMY3, meta, writefiletitle=writefiletitle, 
         tilt=tilt, sazm=sazm, pitch=pitch, clearance_height=clearance_height, 
         rowType=rowType, transFactor=transFactor, sensorsy=sensorsy, 
         PVfrontSurface=PVfrontSurface, PVbackSurface=PVbackSurface, 
         albedo=albedo, tracking=tracking, backtrack=backtrack, 
         limit_angle=limit_angle, calculatePVMismatch=calculatePVMismatch,
         cellsnum = cellsnum, bififactor=bififactor,
         calculateBilInterpol=calculateBilInterpol,
         portraitorlandscape=portraitorlandscape, deltastyle=deltastyle)


# # Compile Results for Front and Rear Irradiance Averages

# In[10]:


def mad_fn(data):
    from numpy import mean, absolute
    # EUPVSEC 2019 Chris Version
    # return MAD / Average for a 1D array. Returned as a fraction, not percent
    data = np.array(data) #cdeline included 11/13/20    return np.abs(np.subtract.outer(data,data)).sum()/data.__len__()**2 / mean(data)

    
def vf_LoadAdd(bifacialvf_resultsfile, bifaciality=0.65):
    '''
    vf_LoadAdd(df)
    subroutine to calculate POA_X (total POA) for each cell
    
    inputs:  bifacialvf_resultsfile  (vf results.csv file).  
    '''
    
    (df, meta) = bifacialvf.loadVFresults(bifacialvf_resultsfile)
    
    df_filter2 = [col for col in df if col.endswith('_RowFrontGTI')]
    df_filter3 = [col for col in df if col.endswith('_RowBackGTI')]
    
    nCells = df_filter2.__len__()  #nCells: number of cells in the scan
    
    df['Grear']=df[df_filter3].sum(axis=1)/nCells
    df['Gfront']=df[df_filter2].sum(axis=1)/nCells

    for i in range(1,nCells+1):            
        # Calculating Standard Deviation of POA 'Total_stdev/POA':'stdev'
        df['POA_'+str(i)]=df['No_'+str(i)+'_RowFrontGTI']+df['No_'+str(i)+'_RowBackGTI']
    
    df_filter = [col for col in df if col.startswith('POA_')]
    df_GTI = df[df_filter]

    # Calculate 'Total_POA_avg': poat
    df['Poat']=df_GTI.sum(axis=1)/nCells
    df['stdev'] = df_GTI.std(axis=1)/df['Poat']*100
    df['MAD_Total/G_Total'] = df_GTI.apply(mad_fn,axis=1)*100
    df['MAD_Total/G_Total**2'] = df['MAD_Total/G_Total']**2

    #df['datetime'] = pd.to_datetime({'Year':df['Year'], 'Month':df['Month'], 'Day':df['Day'], 'Hour':df['Hour'], 
    #                                 'Minute':df['Minute']})
    df = df.set_index(pd.DatetimeIndex(df.date)) # use first column of df for index.  .iloc[:,0]
    return df, meta


# In[11]:


# Load
(bvf1, metadata_bvf1) = vf_LoadAdd('bifacialVF_S1.csv')
#(bvf2, metadata_bvf2) = vf_LoadAdd('bifacialVF_S2.csv')
(bvf3, metadata_bvf3) = vf_LoadAdd('bifacialVF_S3.csv')
(bvf4, metadata_bvf4) = vf_LoadAdd('bifacialVF_S4.csv')
(bvf5, metadata_bvf5) = vf_LoadAdd('bifacialVF_S5.csv')
(bvf6, metadata_bvf6) = vf_LoadAdd('bifacialVF_S6.csv')


# #### Bringing the METEO data to align data with original hours, because bifacialVF only reports back non-zero rows

# In[12]:


rsk = pd.read_excel('..\..\Roskilde_DK_meteo.xlsx', skiprows=2)
rsk = rsk.iloc[: , :-1] # Dropping the last column because it was saved as Unnamed due to being some white space on the xlsx
realtimestamps = pd.to_datetime(rsk[['Year','Month','Day','Hour']])
rsk['Year'] = 2019
timestamps = pd.to_datetime(rsk[['Year','Month','Day','Hour']])
rsk.index = timestamps
rsk=rsk.tz_localize('ETC/GMT-1')
rsk['RSK_Timestamp'] = realtimestamps.values


# In[13]:


abq = pd.read_excel('..\..\Albuquerque_NM_meteo.xlsx', skiprows=2)
abq = abq.iloc[: , :-1] # Dropping the last column because it was saved as Unnamed due to being some white space on the xlsx
abq['Year'] = 2019
timestamps = pd.to_datetime(abq[['Year','Month','Day','Hour']])
abq.index = timestamps
abq=abq.tz_localize('ETC/GMT+7')
abq['ABQ_Timestamp'] = abq.index


# In[14]:


bvf1 = pd.concat([abq, bvf1], axis=1)
bvf3 = pd.concat([rsk, bvf3], axis=1)
bvf4 = pd.concat([rsk, bvf4], axis=1)
bvf5 = pd.concat([rsk, bvf5], axis=1)
bvf6 = pd.concat([rsk, bvf6], axis=1)


# In[15]:


# Checking Alignment
print('weather file', bvf1['DNI (W/m2)'][10])
print('results', bvf1['DNI'][10])


# In[16]:


# Reseting index so we can do one single DF with all results
#bvf1 = bvf1.rename_axis('ABQ_Timestamp')
bvf1 = bvf1.reset_index(drop=True)

#bvf3 = bvf3.rename_axis('RSK_Timestamp')
bvf3 = bvf3.reset_index(drop=True)
bvf4 = bvf4.reset_index(drop=True)
bvf5 = bvf5.reset_index(drop=True)
bvf6 = bvf6.reset_index(drop=True)


# ### Saving one dataframe with desired results to report

# In[17]:


df=pd.DataFrame()


# In[18]:


bifacialityfactor = 0.65


# In[19]:


bvf1.keys()


# In[21]:


bvf3.keys()


# In[23]:


df['ABQ_Timestamp'] = bvf1['ABQ_Timestamp']
df['ABQ_DNI'] = bvf1['DNI']
df['ABQ_TEMP'] = bvf1['Ambient Temp (°C) ']
df['ABQ_WSPD'] = bvf1['VWind']# Wind Speed (m/s)']
df['S1_Gfront'] = bvf1['Gfront']
df['S2_Gfront'] = bvf1['Gfront']

df['RSK_Timestamp'] = bvf3['RSK_Timestamp']
df['RSK_DNI'] = bvf3['DNI']
df['RSK_TEMP'] = bvf3['Ambient Temp (°C) ']
df['RSK_WSPD'] = bvf3['VWind'] # Wind Speed (m/s)']
df['S3_Gfront'] = bvf3['Gfront']
df['S4_Gfront'] = bvf4['Gfront']
df['S4_Grear'] = bvf4['Grear']
df['S4_GPOAeff'] = df['S4_Gfront'] + df['S4_Grear']*bifacialityfactor 
df['S5_Gfront'] = bvf5['Gfront']
df['S6_Gfront'] = bvf6['Gfront']
df['S6_Grear'] = bvf6['Grear']
df['S6_GPOAeff'] = df['S6_Gfront'] + df['S6_Grear']*bifacialityfactor 


# * S1 = SANYO ELECTRIC CO LTD OF PANASONIC GROUP VBHN325SA16
# * S2 = Canadian Solar Inc. CS6K-275M
# * S35 = Trina Solar TSM-305DD05A.05(II)
# * S46 = Trina Solar TSM-295DEG5C.07(II)
# 
#     

# # Calculate Power 

# <div class="alert alert-block alert-warning">
# <b>Note:</b> As of Oct 7th, the SAM GUI version corresponds to the 'patch' branch. This has a more updated version of the CEC csv. This might not be necessary or might change later on
# </div>
# 

# In[76]:


#url = 'https://raw.githubusercontent.com/NREL/SAM/master/deploy/libraries/CEC%20Modules.csv'
#url = 'https://raw.githubusercontent.com/NREL/SAM/develop/deploy/libraries/CEC%20Modules.csv'
#url = 'https://raw.githubusercontent.com/NREL/SAM/patch/deploy/libraries/CEC%20Modules.csv'
#db = pd.read_csv(url, index_col=0)
db = pvlib.pvsystem.retrieve_sam(name='CECMod').T

modfilter1 = db.index.str.startswith('SANYO') & db.index.str.endswith('VBHN325SA16')
modfilter2 = db.index.str.startswith('Canadian') & db.index.str.endswith('CS6K_275M')
modfilter35 = db.index.str.startswith('Trina') & db.index.str.contains('305DD05A_05_')
modfilter46 = db.index.str.startswith('Trina') & db.index.str.contains('295DEG5C')

mymod1 = db[modfilter1]
mymod2 = db[modfilter2]
mymod35 = db[modfilter35]
mymod46 = db[modfilter46]


# In[78]:


from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS
tpm1235 = ( TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_polymer']) # temperature_model_parameters
tpm46 = ( TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']) # temperature_model_parameters


# In[79]:


df['S1_celltemp'] = pvlib.temperature.sapm_cell(df.S1_Gfront, df.ABQ_TEMP, df.ABQ_WSPD, tpm1235['a'], tpm1235['b'], tpm1235['deltaT'])
df['S2_celltemp'] = pvlib.temperature.sapm_cell(df.S1_Gfront, df.ABQ_TEMP, df.ABQ_WSPD, tpm1235['a'], tpm1235['b'], tpm1235['deltaT'])
df['S3_celltemp'] = pvlib.temperature.sapm_cell(df.S3_Gfront, df.RSK_TEMP, df.RSK_WSPD, tpm1235['a'], tpm1235['b'], tpm1235['deltaT'])
df['S4_celltemp'] = pvlib.temperature.sapm_cell(df.S4_GPOAeff, df.RSK_TEMP, df.RSK_WSPD, tpm46['a'], tpm46['b'], tpm46['deltaT'])
df['S5_celltemp'] = pvlib.temperature.sapm_cell(df.S5_Gfront, df.RSK_TEMP, df.RSK_WSPD, tpm1235['a'], tpm1235['b'], tpm1235['deltaT'])
df['S6_celltemp'] = pvlib.temperature.sapm_cell(df.S6_GPOAeff, df.RSK_TEMP, df.RSK_WSPD, tpm46['a'], tpm46['b'], tpm46['deltaT'])


# In[80]:


def calculatePerformance(effective_irradiance, temp_cell, CECMod):
    r'''
    The module parameters are given at the reference condition. 
    Use pvlib.pvsystem.calcparams_cec() to generate the five SDM 
    parameters at your desired irradiance and temperature to use 
    with pvlib.pvsystem.singlediode() to calculate the IV curve information.:
    
    Inputs
    ------
    df : dataframe
        Dataframe with the 'effective_irradiance' columns and 'temp_cell'
        columns.
    CECMod : Dict
        Dictionary with CEC Module PArameters for the module selected. Must 
        contain at minimum  alpha_sc, a_ref, I_L_ref, I_o_ref, R_sh_ref,
        R_s, Adjust
    '''
    
    IL, I0, Rs, Rsh, nNsVth = pvlib.pvsystem.calcparams_cec(
        effective_irradiance=effective_irradiance,
        temp_cell=temp_cell,
        alpha_sc=float(CECMod.alpha_sc),
        a_ref=float(CECMod.a_ref),
        I_L_ref=float(CECMod.I_L_ref),
        I_o_ref=float(CECMod.I_o_ref),
        R_sh_ref=float(CECMod.R_sh_ref),
        R_s=float(CECMod.R_s),
        Adjust=float(CECMod.Adjust)
        )
    
    IVcurve_info = pvlib.pvsystem.singlediode(
        photocurrent=IL,
        saturation_current=I0,
        resistance_series=Rs,
        resistance_shunt=Rsh,
        nNsVth=nNsVth 
        )
    
    return IVcurve_info['p_mp']


# In[82]:


df['S1_dcP'] = calculatePerformance(df.S1_Gfront, df.S2_celltemp, mymod2)
df['S2_dcP'] = calculatePerformance(df.S1_Gfront, df.S2_celltemp, mymod2)
df['S3_dcP'] = calculatePerformance(df.S3_Gfront, df.S3_celltemp, mymod35)
df['S4_dcP'] = calculatePerformance(df.S4_GPOAeff, df.S4_celltemp, mymod46)
df['S5_dcP'] = calculatePerformance(df.S5_Gfront, df.S5_celltemp, mymod35)
df['S6_dcP'] = calculatePerformance(df.S6_GPOAeff, df.S6_celltemp, mymod46)


# In[83]:


df['S1_dcP'] = df['S1_dcP']*12
df['S2_dcP'] = df['S2_dcP']*12
df['S3_dcP'] = df['S3_dcP']*88
df['S4_dcP'] = df['S4_dcP']*88*(1-0.00153) # Yearly Front and Rear Mismatch Loss
df['S5_dcP'] = df['S5_dcP']*88
df['S6_dcP'] = df['S6_dcP']*88*(1-0.021)  # Yearly Front and Rear Mismatch Loss


# In[84]:


df = df.reindex(columns=sorted(df.columns)).fillna(0)


# In[85]:


df.to_csv('bifacialVFresults.csv')


# In[86]:


df.head(12)


# In[ ]:





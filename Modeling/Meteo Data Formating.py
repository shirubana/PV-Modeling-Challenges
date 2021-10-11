#!/usr/bin/env python
# coding: utf-8

# In[1]:


def saveSAMWeatherFile(df, savefile='SAM_ABQ.csv', metdataABQorDK='ABQ', includeminute = False):
    """
    Saves a dataframe with weather data from SRRL on SAM-friendly format.

    INPUT:
    df -- dataframe with all the weather data
    savefile
    metdataABQorDK : str
        Options 'ABQ' and 'DK'. There are nicer programatic ways to pass this data but since it's only two sites, 
        and the provided format does not have all the standard parameters, it was easier to pass this way. 
    includeminute  -- especially for hourly data, if SAM input does not have Minutes, it assuems it's TMY3 format and 
                      calculates the sun position 30 minutes prior to the hour (i.e. 12 timestamp means sun position at 11:30)
                      If minutes are included, it will calculate the sun position at the time of the timestamp (12:00 at 12:00)
                      Include minutes if resolution of data is not hourly duh. (but it will calculate at the timestamp)
                      
    Headers expected by SAM:
    ************************* 
    # Source	Location ID	City	State	Country	Latitude	Longitude	Time Zone	Elevation		

    Column names
    *************
    # Year	Month	Day	Hour	Minute    Dew Point   Wspd	Tdry	DHI	DNI	GHI	Albedo

    OR
    # Year	Month	Day	Hour	Dew Point  Wspd	Tdry	DHI	DNI	GHI	Albedo

    """

    import pandas as pd

    if metdataABQorDK == 'ABQ':
        header = "Source,Location ID,City,State,Country,Latitude,Longitude,Time Zone,Elevation,,,,,,,,,,\n" +                 "Measured,999999,ABQ,NM,USA,35.05,-106.64,-7,1600,,,,,,,,,,\n"
    elif metdataABQorDK == 'DK':
        header = "Source,Location ID,City,State,Country,Latitude,Longitude,Time Zone,Elevation,,,,,,,,,,\n" +                 "Measured,999999,Roskilde,SL,DK,55.696,12.104,1,15,,,,,,,,,,\n"

    if includeminute:
        savedata = pd.DataFrame({'Year':df.index.year, 'Month':df.index.month, 'Day':df.index.day,
                                'Hour':df.index.hour, 'Minute':df.index.minute,
# In case you want 1-24. But sam uses 0-23 too.
#       savedata = pd.DataFrame({'Year':df['Year'], 'Month':df['Month'], 'Day':df['Day'],
#                                'Hour':df['Hour'], 'Minute':df.index.minute,
                                 'rh': df['Relative Humidity (%)'],
                                 'Wspd':df['Wind Speed (m/s)'],
                                 'Tdry':df['Ambient Temp (°C) '],
                                 'DHI':df['DHI (W/m2)'],
                                 'DNI':df['DNI (W/m2)'],
                                 'GHI':df['GHI (W/m2)'],
                                 'Albedo':df['Albedo']
                                 })
    else:
         savedata = pd.DataFrame({'Year':df.index.year, 'Month':df.index.month, 'Day':df.index.day,
                                 'Hour':df.index.hour,
# In case you want 1-24. But sam uses 0-23 too.
#        savedata = pd.DataFrame({'Year':df['Year'], 'Month':df['Month'], 'Day':df['Day'],
#                            'Hour':df['Hour'], 
                            'rh': df['Relative Humidity (%)'],
                             'Wspd':df['Wind Speed (m/s)'],
                             'Tdry':df['Ambient Temp (°C) '],
                             'DHI':df['DHI (W/m2)'],
                             'DNI':df['DNI (W/m2)'],
                             'GHI':df['GHI (W/m2)'],
                             'Albedo':df['Albedo']
                                 })
    with open(savefile, 'w', newline='') as ict:
        # Write the header lines, including the index variable for
        # the last one if you're letting Pandas produce that for you.
        # (see above).
        for line in header:
            ict.write(line)

        savedata.to_csv(ict, index=False)


def save_TMY3(df, savefile='Bifacial_TMYfileAll2019_15.csv', metdataABQorDK='ABQ', includeTrackerData=False):
    """
    NEW Routine to save TMY3 , assuming the columsn Date and Time already exist and are in the right
    1-24 hour format. (this can be done previous to submitting to this function by
    reading a real CSV and joining those columns.)
    This is because pandas uses format 0-23 hours, but TMY3 uses 1-24.
    
    Saves a dataframe with weathe data from SRRL in TMY3 data format.
    
    if includeTrackerData is True, it will also save the tracker data column.
    

    Headers expected by TMY3:
    ************************* 
    # Location ID	City	State	Time Zone	Latitude	Longitude	Elevation

    Column names
    *************
    # Date (MM/DD/YYYY)		Time (HH:MM)	GHI (W/m^2))	DNI (W/m^2))	DHI (W/m^2)		Wspd (m/s)	
    Dry-bulb (C)	Alb (unitless)	

    """

    import pandas as pd

    header = "999999, ABQ, NM, -7, 35.05,-106.64, 1600\n"

    if metdataABQorDK == 'ABQ':
        header = "999999, ABQ, NM, -7, 35.05,-106.64, 1600\n"
    elif metdataABQorDK == 'DK':
        header = "999999, Roskilde, DK, 1, 55.696, 12.104, 15\n"

# If using dataframe index
#    dates = df.index.strftime('%#m/%#d/%Y') #TODO: Test if in linux, do '%-m/%-d/%Y' instead
#    hours = df.index.strftime('%H:%M')  #TODO: Test if in linux, do '%-H:%-M' instead

#    savedata = pd.DataFrame({'Date (MM/DD/YYYY)':dates,
#                             'Time (HH:MM)':hours,


    savedata = pd.DataFrame({'Date (MM/DD/YYYY)':df['Date (MM/DD/YYYY)'],
                             'Time (HH:MM)':df['Time (HH:MM)'],
                             'Wspd (m/s)':df['Wind Speed (m/s)'],
                             'Dry-bulb (C)':df['Ambient Temp (°C) '],
                             'DHI (W/m^2)':df['DHI (W/m2)'],
                             'DNI (W/m^2)':df['DNI (W/m2)'],
                             'GHI (W/m^2)':df['GHI (W/m2)'],
                             'RHum (%)': df['Relative Humidity (%)'],
                             'Alb (unitless)':df['Albedo']})

    if includeTrackerData:
        savedata['Tracker Angle (degrees)'] = df['Tracker Angle (degrees)']

    with open(savefile, 'w', newline='') as ict:
        # Write the header lines, including the index variable for
        # the last one if you're letting Pandas produce that for you.
        # (see above).
        for line in header:
            ict.write(line)

        savedata.to_csv(ict, index=False)


# In[2]:


import pandas as pd


# In[3]:


import pvlib


# In[4]:


rsk = pd.read_excel('..\Roskilde_DK_meteo.xlsx', skiprows=2)
rsk = rsk.iloc[: , :-1] # Dropping the last column because it was saved as Unnamed due to being some white space on the xlsx
print(len(rsk))
rsk.head(14)


# In[5]:


rsk['Year'] = 2019
timestamps = pd.to_datetime(rsk[['Year','Month','Day','Hour']])
rsk.index = timestamps


# Note: There is an extra space after Ambient Temp on the xlsx. joy.
# 

# In[6]:


# Set albedos
rsk_alb = [0.192, 0.206, 0.228, 0.229, 0.221, 0.222, 0.218, 0.206, 0.213, 0.220, 0.207, 0.200]
rsk['Albedo'] = 0.0
for ii in range (1, 13):
    rsk.loc[rsk.index.month==ii, ['Albedo']] = rsk_alb[ii-1] #


# In[7]:


# Replace with Hours 1-24 correct text from a TMY3
real_tmy=r'C:\Users\sayala\Documents\GitHub\bifacialvf\bifacialvf\data\724010TYA.CSV'
real_tmy = pd.read_csv(real_tmy, skiprows = [0])
real_tmy.index = rsk.index
rsk['Date (MM/DD/YYYY)'] = real_tmy['Date (MM/DD/YYYY)']
rsk['Time (HH:MM)'] = real_tmy['Time (HH:MM)']
rsk['Date (MM/DD/YYYY)']=rsk['Date (MM/DD/YYYY)'].map(lambda x: str(x)[:-4])+'2019'
rsk['Date (MM/DD/YYYY)']


# In[8]:


# SAVE
save_TMY3(rsk, savefile='TMY3_Roskilde_DK.csv', metdataABQorDK='DK')


# In[9]:


print(len(rsk))
rsk.head(3)


# In[10]:


rsk2 = rsk[:-1].copy()
starttime = pd.to_datetime('%s-%s-%s %s:%s' % (rsk.index.year[0],1,1,0,0 ) )#.tz_localize(tzinfo)
rsk2.loc[starttime] = 0
rsk2=rsk2.sort_index()
rsk2.loc[starttime, 'Year'] = 2019
rsk2.loc[starttime, 'Month'] = 1
rsk2.loc[starttime, 'Day'] = 1


# In[11]:


print(len(rsk2))
rsk2.head(14)


# In[12]:


saveSAMWeatherFile(rsk2, savefile='SAM_Roskilde_DK.csv', metdataABQorDK='DK', includeminute = False)


# In[13]:


rsk3=rsk2.copy().shift(-60, freq='T')
rsk3.head(14)
rsk3 = rsk3[1:]
rsk3.loc[rsk2.index[-1]] = 0
saveSAMWeatherFile(rsk3, savefile='SAM_Roskilde_DK_Shifted.csv', metdataABQorDK='DK', includeminute = False)


# In[ ]:





# In[ ]:





# ## Now for ABQ

# In[14]:


abq = pd.read_excel('..\Albuquerque_NM_meteo.xlsx', skiprows=2)
abq = abq.iloc[: , :-1] # Dropping the last column because it was saved as Unnamed due to being some white space on the xlsx
print(len(abq))
abq.head(14)


# In[15]:


abq.loc[:,'Year'] = 2019


# In[16]:


timestamps = pd.to_datetime(abq[['Year','Month','Day','Hour']])
abq.index = timestamps


# In[17]:


# Set albedos
abq_alb = [0.192, 0.194,0.190,0.191,0.194,0.191,0.189,0.191,0.191,0.193,0.200,0.203]
abq['Albedo'] = 0.0
for ii in range (1, 13):
    abq.loc[abq.index.month==ii, ['Albedo']] = abq_alb[ii-1] #


# In[18]:


# Replace with Hours 1-24 correct text from a TMY3
real_tmy.index = abq.index
#real_tmy.index = abq.index
abq['Date (MM/DD/YYYY)'] = real_tmy['Date (MM/DD/YYYY)']
abq['Time (HH:MM)'] = real_tmy['Time (HH:MM)']
abq['Date (MM/DD/YYYY)']=abq['Date (MM/DD/YYYY)'].map(lambda x: str(x)[:-4])+'2019'
abq['Date (MM/DD/YYYY)']


# In[19]:


# SAVE
save_TMY3(abq, savefile='TMY3_Albuquerque_NM.csv', metdataABQorDK='ABQ')


# In[20]:


abq2 = abq[:-1].copy()
starttime = pd.to_datetime('%s-%s-%s %s:%s' % (abq2.index.year[0],1,1,0,0 ) )#.tz_localize(tzinfo)
abq2.loc[starttime] = 0
abq2=abq2.sort_index()
abq2.loc[starttime, 'Year'] = 2019
abq2.loc[starttime, 'Month'] = 1
abq2.loc[starttime, 'Day'] = 1
saveSAMWeatherFile(abq2, savefile='SAM_Albuquerque_NM.csv', metdataABQorDK='ABQ', includeminute = False)


# # Adding a -1 hour shift for SAM

# In[22]:


abq3=abq2.copy().shift(-60, freq='T')
abq3 = abq3[1:]
abq3.loc[abq2.index[-1]] = 0
saveSAMWeatherFile(abq3, savefile='SAM_Albuquerque_NM_Shifted.csv', metdataABQorDK='ABQ', includeminute = False)


# In[ ]:





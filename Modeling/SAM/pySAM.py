#!/usr/bin/env python
# coding: utf-8

# # pySAM Simulations
# 
# This loads the JSons saved from the SAM.GUI version, runs the simulations, compiles the desired outputs and losses and saves them as a csv file for copying into the Results format.
# 
# For the DC Power data, it selects the desired year based on how long the system has been installed since commisioning.
# The DC Power data saved is at the Inverter input, which reflects both MPPT and both strings in each MPPT input. Hence, values are divided by 4.
# 
# 
# ### SAM GUI Version: 2020.11.29
# 

# In[1]:


import PySAM.Pvsamv1 as pv
import PySAM
import xlsxwriter
import json
import pandas as pd
import os
import pprint as pp


# In[2]:


PySAM.__version__


# In[3]:


sam1 = pv.default("FlatPlatePVSingleOwner")


# In[4]:


def setNewValues(dic):

    newval = {'CECPerformanceModelWithModuleDatabase': {'cec_a_ref': dic['cec_a_ref'],
        'cec_adjust': dic['cec_adjust'],
        'cec_alpha_sc': dic['cec_alpha_sc'],
        'cec_area': dic['cec_area'],
        'cec_array_cols': dic['cec_array_cols'],
        'cec_array_rows': dic['cec_array_rows'],
        'cec_backside_temp': dic['cec_backside_temp'],
        'cec_beta_oc': dic['cec_beta_oc'],
        'cec_bifacial_ground_clearance_height': dic['cec_bifacial_ground_clearance_height'],
        'cec_bifacial_transmission_factor': dic['cec_bifacial_transmission_factor'],
        'cec_bifaciality': dic['cec_bifaciality'],
        'cec_gamma_r': dic['cec_gamma_r'],
        'cec_gap_spacing': dic['cec_gap_spacing'],
        'cec_heat_transfer': dic['cec_heat_transfer'],
        'cec_height': dic['cec_height'],
        'cec_i_l_ref': dic['cec_i_l_ref'],
        'cec_i_mp_ref': dic['cec_i_mp_ref'],
        'cec_i_o_ref': dic['cec_i_o_ref'],
        'cec_i_sc_ref': dic['cec_i_sc_ref'],
        'cec_is_bifacial': dic['cec_is_bifacial'],
        'cec_module_length': dic['cec_module_length'],
        'cec_module_width': dic['cec_module_width'],
        'cec_mounting_config': dic['cec_mounting_config'],
        'cec_mounting_orientation': dic['cec_mounting_orientation'],
        'cec_n_s': dic['cec_n_s'],
        'cec_r_s': dic['cec_r_s'],
        'cec_r_sh_ref': dic['cec_r_sh_ref'],
        'cec_standoff': dic['cec_standoff'],
        'cec_t_noct': dic['cec_t_noct'],
        'cec_temp_corr_mode': dic['cec_temp_corr_mode'],
        'cec_transient_thermal_model_unit_mass': dic['cec_transient_thermal_model_unit_mass'],
        'cec_v_mp_ref': dic['cec_v_mp_ref'],
        'cec_v_oc_ref': dic['cec_v_oc_ref']},

    'Inverter': {'inv_cec_cg_eff_cec': dic['inv_cec_cg_eff_cec'],
        'inv_cec_cg_paco': dic['inv_cec_cg_paco'],
        'inv_ds_eff': dic['inv_ds_eff'],
        'inv_ds_paco': dic['inv_ds_paco'],
        'inv_num_mppt': dic['inv_num_mppt'],
        'inv_pd_eff': dic['inv_pd_eff'],
        'inv_pd_paco': dic['inv_pd_paco'],
        'inv_snl_eff_cec': dic['inv_snl_eff_cec'],
        'inv_snl_paco': dic['inv_snl_paco'],
        'inverter_count': dic['inverter_count'],
        'inverter_model': dic['inverter_model'],
        'mppt_hi_inverter': dic['mppt_hi_inverter'],
        'mppt_low_inverter': dic['mppt_low_inverter']},

    'InverterCECDatabase': {'inv_snl_c0': dic['inv_snl_c0'],
        'inv_snl_c1': dic['inv_snl_c1'],
        'inv_snl_c2': dic['inv_snl_c2'],
        'inv_snl_c3': dic['inv_snl_c3'],
        'inv_snl_paco': dic['inv_snl_paco'],
        'inv_snl_pdco': dic['inv_snl_pdco'],
        'inv_snl_pnt': dic['inv_snl_pnt'],
        'inv_snl_pso': dic['inv_snl_pso'],
        'inv_snl_vdcmax': dic['inv_snl_vdcmax'],
        'inv_snl_vdco': dic['inv_snl_vdco'],
        'inv_tdc_cec_db': dic['inv_tdc_cec_db']},

    'InverterDatasheet': {'inv_ds_eff': dic['inv_ds_eff'],
        'inv_ds_paco': dic['inv_ds_paco'],
        'inv_ds_pnt': dic['inv_ds_pnt'],
        'inv_ds_pso': dic['inv_ds_pso'],
        'inv_ds_vdcmax': dic['inv_ds_vdcmax'],
        'inv_ds_vdco': dic['inv_ds_vdco'],
        'inv_tdc_ds': dic['inv_tdc_ds']},

    'Layout': {'module_aspect_ratio': dic['module_aspect_ratio'],
        'subarray1_mod_orient': dic['subarray1_mod_orient'],
        'subarray1_nmodx': dic['subarray1_nmodx'],
        'subarray1_nmody': dic['subarray1_nmody'],
        'subarray2_mod_orient': dic['subarray2_mod_orient'],
        'subarray2_nmodx': dic['subarray2_nmodx'],
        'subarray2_nmody': dic['subarray2_nmody'],
        'subarray3_mod_orient': dic['subarray3_mod_orient'],
        'subarray3_nmodx': dic['subarray3_nmodx'],
        'subarray3_nmody': dic['subarray3_nmody'],
        'subarray4_mod_orient': dic['subarray4_mod_orient'],
        'subarray4_nmodx': dic['subarray4_nmodx'],
        'subarray4_nmody': dic['subarray4_nmody']},

    'Losses': {'acwiring_loss': dic['acwiring_loss'],
        'dcoptimizer_loss': dic['dcoptimizer_loss'],
        'en_snow_model': dic['en_snow_model'],
        'subarray1_dcwiring_loss': dic['subarray1_dcwiring_loss'],
        'subarray1_diodeconn_loss': dic['subarray1_diodeconn_loss'],
        'subarray1_mismatch_loss': dic['subarray1_mismatch_loss'],
        'subarray1_nameplate_loss': dic['subarray1_nameplate_loss'],
        'subarray1_rear_irradiance_loss': dic['subarray1_rear_irradiance_loss'],
        'subarray1_soiling': dic['subarray1_soiling'],
        'subarray1_tracking_loss': dic['subarray1_tracking_loss'],
        'subarray2_dcwiring_loss': dic['subarray2_dcwiring_loss'],
        'subarray2_diodeconn_loss': dic['subarray2_diodeconn_loss'],
        'subarray2_mismatch_loss': dic['subarray2_mismatch_loss'],
        'subarray2_nameplate_loss': dic['subarray2_nameplate_loss'],
        'subarray2_rear_irradiance_loss': dic['subarray2_rear_irradiance_loss'],
        'subarray2_soiling': dic['subarray2_soiling'],
        'subarray2_tracking_loss': dic['subarray2_tracking_loss'],
        'subarray3_dcwiring_loss': dic['subarray3_dcwiring_loss'],
        'subarray3_diodeconn_loss': dic['subarray3_diodeconn_loss'],
        'subarray3_mismatch_loss': dic['subarray3_mismatch_loss'],
        'subarray3_nameplate_loss': dic['subarray3_nameplate_loss'],
        'subarray3_rear_irradiance_loss': dic['subarray3_rear_irradiance_loss'],
        'subarray3_soiling': dic['subarray3_soiling'],
        'subarray3_tracking_loss': dic['subarray3_tracking_loss'],
        'subarray4_dcwiring_loss': dic['subarray4_dcwiring_loss'],
        'subarray4_diodeconn_loss': dic['subarray4_diodeconn_loss'],
        'subarray4_mismatch_loss': dic['subarray4_mismatch_loss'],
        'subarray4_nameplate_loss': dic['subarray4_nameplate_loss'],
        'subarray4_rear_irradiance_loss': dic['subarray4_rear_irradiance_loss'],
        'subarray4_soiling': dic['subarray4_soiling'],
        'subarray4_tracking_loss': dic['subarray4_tracking_loss'],
        'transformer_load_loss': dic['transformer_load_loss'],
        'transformer_no_load_loss': dic['transformer_no_load_loss'],
        'transmission_loss': dic['transmission_loss']},

    'Module': {'module_model': dic['module_model']},

    'Shading': {'subarray1_shade_mode': dic['subarray1_shade_mode'],
        'subarray2_shade_mode': dic['subarray2_shade_mode'],
        'subarray3_shade_mode': dic['subarray3_shade_mode'],
        'subarray4_shade_mode': dic['subarray4_shade_mode']},

    'SolarResource': {'albedo': dic['albedo'],
        'irrad_mode': dic['irrad_mode'],
        'sky_model': dic['sky_model'],
        'use_wf_albedo': dic['use_wf_albedo']},

    'SystemDesign': {'enable_mismatch_vmax_calc': dic['enable_mismatch_vmax_calc'],
        'inverter_count': dic['inverter_count'],
        'subarray1_azimuth': dic['subarray1_azimuth'],
        'subarray1_backtrack': dic['subarray1_backtrack'],
        'subarray1_gcr': dic['subarray1_gcr'],
        'subarray1_modules_per_string': dic['subarray1_modules_per_string'],
        'subarray1_monthly_tilt': dic['subarray1_monthly_tilt'],
        'subarray1_mppt_input': dic['subarray1_mppt_input'],
        'subarray1_nstrings': dic['subarray1_nstrings'],
        'subarray1_rotlim': dic['subarray1_rotlim'],
        'subarray1_tilt': dic['subarray1_tilt'],
        'subarray1_tilt_eq_lat': dic['subarray1_tilt_eq_lat'],
        'subarray1_track_mode': dic['subarray1_track_mode'],
        'subarray2_azimuth': dic['subarray2_azimuth'],
        'subarray2_backtrack': dic['subarray2_backtrack'],
        'subarray2_enable': dic['subarray2_enable'],
        'subarray2_gcr': dic['subarray2_gcr'],
        'subarray2_modules_per_string': dic['subarray2_modules_per_string'],
        'subarray2_monthly_tilt': dic['subarray2_monthly_tilt'],
        'subarray2_mppt_input': dic['subarray2_mppt_input'],
        'subarray2_nstrings': dic['subarray2_nstrings'],
        'subarray2_rotlim': dic['subarray2_rotlim'],
        'subarray2_tilt': dic['subarray2_tilt'],
        'subarray2_tilt_eq_lat': dic['subarray2_tilt_eq_lat'],
        'subarray2_track_mode': dic['subarray2_track_mode'],
        'subarray3_azimuth': dic['subarray3_azimuth'],
        'subarray3_backtrack': dic['subarray3_backtrack'],
        'subarray3_enable': dic['subarray3_enable'],
        'subarray3_gcr': dic['subarray3_gcr'],
        'subarray3_modules_per_string': dic['subarray3_modules_per_string'],
        'subarray3_monthly_tilt': dic['subarray3_monthly_tilt'],
        'subarray3_mppt_input': dic['subarray3_mppt_input'],
        'subarray3_nstrings': dic['subarray3_nstrings'],
        'subarray3_rotlim': dic['subarray3_rotlim'],
        'subarray3_tilt': dic['subarray3_tilt'],
        'subarray3_tilt_eq_lat': dic['subarray3_tilt_eq_lat'],
        'subarray3_track_mode': dic['subarray3_track_mode'],
        'subarray4_azimuth': dic['subarray4_azimuth'],
        'subarray4_backtrack': dic['subarray4_backtrack'],
        'subarray4_enable': dic['subarray4_enable'],
        'subarray4_gcr': dic['subarray4_gcr'],
        'subarray4_modules_per_string': dic['subarray4_modules_per_string'],
        'subarray4_monthly_tilt': dic['subarray4_monthly_tilt'],
        'subarray4_mppt_input': dic['subarray4_mppt_input'],
        'subarray4_nstrings': dic['subarray4_nstrings'],
        'subarray4_rotlim': dic['subarray4_rotlim'],
        'subarray4_tilt': dic['subarray4_tilt'],
        'subarray4_tilt_eq_lat': dic['subarray4_tilt_eq_lat'],
        'subarray4_track_mode': dic['subarray4_track_mode'],
        'system_capacity': dic['system_capacity']}
             }

    return newval


# In[49]:


def runAndCompileSAMResults(SimFile, yy, metdataABQorDK='ABQ', bifacial=False, includeMeteo = False):

    with open(SimFile) as f:
        dic = json.load(f)

    newval = setNewValues(dic)
    sam1.assign(newval)
    sam1.SolarResource.solar_resource_file = dic['solar_resource_file']
    sam1.execute()

    results = sam1.Outputs.export()
    rear = list(results['subarray1_poa_rear'])
    front = list(results['subarray1_poa_front'])
    celltemp = list(results['subarray1_celltemp'])
    power = list(results['dc_net'])

    df = pd.DataFrame(list(zip(front)),
                   columns =['Gfront']) 
    if bifacial:
        df['Grear'] = rear
    df['cellTemp'] = celltemp
    df['DCP String 1 [W]'] = power
    df['DCP String 1 [W]'] = df['DCP String 1 [W]'] *1000/4 # Converting to Watts and dividing by the strings entering the inverter.
                             
    if metdataABQorDK == 'ABQ':
        df = df[8760*yy:8760*yy+8760]
    else:
        # For Roskilde, Weather data is provided for second half of 2019 and first half of 2020. 
        # This selects that data and puts it in the order of the weather file.
        df2 = df[(2160+8760*yy):8760*(yy+1)].copy()
        df3 = df[8760*(yy+1):8760*(yy+1)+2160].copy()
        df = df3.append(df2, sort=False)
    
    df.reset_index()
    if includeMeteo:
        df['DNI'] = list(results['dn'])
        df['DHI'] = list(results['df'])
        df['Alb'] = list(results['alb'])

    weatherfile = pd.read_csv(dic['solar_resource_file'], skiprows=2)
    weatherfile['Year'] = 2020
    timestamps = pd.to_datetime(weatherfile[['Year','Month','Day','Hour']])
    df.index = timestamps
    # Shifting back so results match the provided timestamps
    df = df.shift(60, freq='T')

    if metdataABQorDK == 'DK':
        rsk = pd.read_excel('..\..\Roskilde_DK_meteo.xlsx', skiprows=2)
        rsk = rsk.iloc[: , :-1] # Dropping the last column because it was saved as Unnamed due to being some white space on the xlsx
        timestamps = pd.to_datetime(rsk[['Year','Month','Day','Hour']])
        df.index = timestamps

    #LOSSES
    # Standard
    soiling = sam1.Outputs.annual_poa_soiling_loss_percent
    moduleMismatch = sam1.Outputs.annual_dc_mismatch_loss_percent
    diodesandConnections = sam1.Outputs.annual_dc_diodes_loss_percent

    # Calculated
    shading = sam1.Outputs.annual_poa_shading_loss_percent
    reflectionIAM = sam1.Outputs.annual_poa_cover_loss_percent
    moduledeviationfromSTC = sam1.Outputs.annual_dc_module_loss_percent

    losses = {'soiling': soiling,
             'moduleMismatch': moduleMismatch,
              'diodesandConnections':diodesandConnections,
              'shading': shading,
              'reflectionIAM': reflectionIAM,
              'moduledeviationfromSTC': moduledeviationfromSTC
             }
        
    return df, losses


# In[9]:


# Prism File
S1file = "JSONS_SAM\S1.json"
S2file = "JSONS_SAM\S2.json"
S3file = "JSONS_SAM\S3.json"
S4file = "JSONS_SAM\S4.json"
S5file = "JSONS_SAM\S5.json"
S6file = "JSONS_SAM\S6.json"


# In[50]:


resS1, losses1 = runAndCompileSAMResults (S1file, 2, 'DK', False, True)
resS2, losses2  = runAndCompileSAMResults (S2file, 3, 'DK', False, False)
resS3, losses3  = runAndCompileSAMResults (S3file, 1, 'DK', False, True)
resS4, losses4  = runAndCompileSAMResults (S4file, 1, 'DK', True, False)
resS5, losses5  = runAndCompileSAMResults (S5file, 1, 'DK', False, False)
resS6, losses6  = runAndCompileSAMResults (S6file, 1, 'DK', True, False)


# In[51]:


resS1 = resS1.reset_index().add_prefix('S1_')
resS2 = resS2.reset_index().add_prefix('S2_')
resS3 = resS3.reset_index().add_prefix('S3_')
resS4 = resS4.reset_index().add_prefix('S4_')
resS5 = resS5.reset_index().add_prefix('S5_')
resS6 = resS6.reset_index().add_prefix('S6_')


# In[63]:


result = pd.concat([resS1, resS2, resS3, resS4, resS5, resS6], axis=1)


# In[64]:


result.to_csv('SAM Results Compiled.csv')


# In[60]:


losses = pd.DataFrame([losses1, losses2,losses3, losses4, losses5, losses6], index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
losses.to_csv('SAM Losses Compiled.csv')


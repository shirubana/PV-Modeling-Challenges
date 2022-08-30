# PVPMC-Challenge-2021
 
This repository shows the modeling steps, intermediate resutls and final results submitted for bifacialVF and SAM (pySAM) models for the [2021 PVPMC Blind Modeling Round Robin](https://pvpmc.sandia.gov/pv-research/blind-pv-modeling-comparison/).

All files used are included:
- Weather file processing into TMY3 and SAM
- pySAM loading of SAM simulation jsons, modifications and compiling. NOTC temperature model used.
- bifacialVF front, rear, and electrical mismatch calculations, plus PVlib single diode modeling from the CEC parameters of the modules and SAPM model for temperature.

Results are in the `Modeling` folder

Other particularities:
- Weather data was corrected for the right-label approach used by SAM (sun position for 8 AM is at 8:30 AM). TMY3 and bifacialVF use left-labeled approach (sun position for 8 AM at 7:30 AM). bifacialVF also applies a sunrise/sunset correction (if sunrise at 7:40, sun position calculated at 7:50)

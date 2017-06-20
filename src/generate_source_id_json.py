#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
convert_sources_table_to_json.py
================================

Converts original table (from Word doc) in JSON file.

"""

import simplejson

HEADERS = "SOURCE_UID|DATA_REPOSITORY|DATA_NAME|SOURCE_NAME|Timestep".split("|")
DATA = """1000001|ghcnd|ghcnd_australia| National Climate Centre Bureau of Meteorology Po Box 1289k Melbourne 3001|DY
1000002|ghcnd|belarus|Data Originated from Pavel Groisman, Ph.D.,Neespi Project Scientist (Http://Neespi.Org), Ucar Project Scientist at Ncdc, National Climatic Data Center, Federal Building, 151 Patton Avenue, Asheville, NC 28801,Ph.: +1 828 271-4347; Fax: +1 828 271-4328,Office E-Mail: Pasha.Groisman@Noaa.Gov, Home E-Mail: Groismanp@Bellsouth.Net|DY
1000003|isti|gsod|Data Originated from NCD’S Global Summary of The Day (GSOD) Product|DY
1000004|isti|uruguay_inia|Data Originated from The Agroclimatic Databank from INIA (Instituto Nacional De Investigacion Agropecuaria) In Uruguay|DY
1000005|isti|antarctic_palmer|Antarctic Meteorological Research Center (Amrc) Iniversity Wisconsin Madison USA|DY
1000006|isti|antarctic_scar_reader|Antarctic Meteorological Research Center (Amrc) Iniversity Wisconsin Madison USA|DY
1000007|isti|greenland|Antarctic Meteorological Research Center (Amrc) Iniversity Wisconsin Madison USA|DY
1000008|isti|isti_australia|Australian Government Bureau of Meteorology|DY
1000009|isti|brazil_inmet|Brazil's Instituto Nacional De Meteorologia (INMET)|DY
1000010|isti|spain|Data For 22 Stations Provided by Manola Brunet|DY
1000011|isti|ispd_ipy|Data originated as source data used to create The International Surface Pressure Databank|DY
1000012|isti|ispd_swiss|Data originated as source data used to create The International Surface Pressure Databank|DY
1000013|isti|ispd_sydney|Data originated as source data used to create The International Surface Pressure Databank|DY
1000014|isti|ispd_tunisia_morroco|Data originated as source data used to create The International Surface Pressure Databank|DY
1000015|isti|swiss_digihom|Data Originated from The Digihom Project, which is a Collaboration Between Meteoswiss and IAC-ETH.|DY
1000016|isti|india|Data Was Provided by Jayashree Revadekar India Meteorological Department|DY
1000017|isti|giessen|Data Was Provided by Juerg Luterbacher|DY
1000018|isti|gsn_sweden|Data Was Provided by Ludvig Isaksson from the Swedish Stations to The GSN Network|DY
1000019|isti|russia|Data Was Provided Via Cd-Rom By Dr V.N. Razuvaev and Dr. O.N. Bulygina Oak Ridge National Laboratory, Oak Ridge, Tennessee, Usa|DY
1000020|isti|vietnam|Data Were Provided by William Angel in March 2011. They Are Data Digitized as Part of The CDMP Program|DY
1000021|isti|ecuador|Instituto Nacional De Meteorologia E HidrologiaI in Ecuador|DY
1000022|isti|usforts|Midwestern Regional Climate Center (MRCC)|DY
1000023|isti|brazil|National Institute for Space Research (Inpe) In Brazil|DY
1000024|isti|argentina|National Institute of Agriculture, And Was Provided by Matilde Rusticucci From the University of Buenos Aires|DY
1000025|isti|pitcairnislands|Data Provided by Howard Diamond On 29 March 2011 and Peter Fisher International Operations Managerscience, Research and Development Division Meteorological Service of New Zealand Limited.|DY
1000026|isti|channel_islands|These Data Originated from Mr. Frank Le Blancq States of Jersey Meteorological Department|DY
1000027|isti|uruguay|The Data Is Qc'd, And Provided by Madeline Renom Institute of Physics Of The Faculty Of Sciences (University Of The Republic) Iguá 4225, Montevideo, URUGUAY 11400|DY
1000028|isti|ecad_non_blend|The European Climate Assessment and Dataset|DY
1000029|isti|sacad_non_blend|The Southeast Asian Climate Assessment and Dataset|DY
1000030|isti|japan|These Data Originated from The Japan Meteorological Agency|DY
1000031|isti|mexico|These Data Were Provided by William Angel in March 2011. They Are Data Digitized as part of The CDMP Program|DY
1000032|isti|hadisd|UK Met Office|DY
1000033|isti|antarctic_scar_reader|Scar Reader Project Antarctic Meteorological Research Center (AMRC) Iniversity Wisconsin Madison USA|M
1000034|isti|russsource_antarctica|Antarctic Meteorological Research Center (AMRC) University Wisconsin Madison USA|M
1000035|isti|histalp|Central Institute for Meteorology and Geodynamics Zamg|M
1000036|isti|canada|Environment Canada National Climate Data and Information Archive|M
1000037|isti|canada_raw|Environment Canada National Climate Data and Information Archive|M
1000038|isti|germany|German Meteorological Service Deutscher Wetterdienst|M
1000039|isti|russsource_argentina|Russource_Argentina_Multiple_Sources|M
1000040|isti|arctic|International Arctic Research Center at the University of Alaska|M
1000041|isti|ak_hi_climat|International Arctic Research Center at the University of Alaska|M
1000042|isti|east_africa|John Christy Of UAH British E Africa Met Dept|M
1000043|isti|mcdw|Monthly Climatic Data of The World (MCDW)|M
1000044|isti|mcdw_unpublished|Monthly Climatic Data of The World (MCDW)|M
1000045|isti|uganda|These Data Originated from John Christy Of Uah|M
1000046|isti|climat_bufr|National Centers For Environmental Information (NCEI)|M
1000047|isti|central_asia|National Snow and Ice Data Center (NSIDC)|M
1000048|isti|eklima|Norweigan Meteorological Institutes EKLIMA Portal|M
1000049|isti|climat_ncdc|NWS Climat Streams That Are Sent to NCDC |M
1000050|isti|climat_prelim|Preliminary Climat Data|M
1000051|ecad|knmi|Royal Netherlands Meteorological Institute (KNMI) Via ECAD|M
1000052|isti|colonialera|Russ Vose Analysis of Mr Griffiths max min data from various countries around the World|M
1000053|isti|russsource_australia _de|Russource_Australia_De_Multiple_Sources|M
1000054|isti|russsource_australia|Russource_Australia_Multiple_Sources|M
1000055|isti|russsource_australia_wwr|Russource_Australia_Wwr_Multiple_Sources|M
1000056|isti|russsource_brazil|Russource_Brazil_Multiple_Sources|M
1000057|isti|russsource_canada|Russource_Canada_Multiple_Sources|M
1000058|isti|russsource_chile|Russource_Chile_Multiple_Sources|M
1000059|isti|russsource_climat|Russource_Climat_Multiple_Sources|M
1000060|isti|russsource_conus_climat|Russource_Conus_Climat_Multiple_Sources|M
1000061|isti|russsource_climat|Russource_Cuba_Multiple_Sources|M
1000062|isti|russsource_fao|Russource_Fao_Multiple_Sources|M
1000063|isti|russsource_fwa|Russource_Fwa_Multiple_Sources|M
1000064|isti|russsource_greece|Russource_Greece_Multiple_Sources|M
1000065|isti|russsource_griffiths|Russource_Griffiths_Multiple_Sources|M
1000066|isti|russsource_griffiths_sa|Russource_Griffiths_Sa_Multiple_Sources|M
1000067|isti|russsource_indonesia|Russource_Indonesia_Multiple_Sources|M
1000068|isti|russsource_iran|Russource_Iran_Multiple_Sources|M
1000069|isti|russsource_ish|Russource_Ish_Multiple_Sources|M
1000070|isti|russsource_mexico|Russource_Mexico_Multiple_Sources|M
1000071|isti|russsource_new_zealand|Russource_New Zealand_Multiple_Sources|M
1000072|isti|russsource_south_africa|Russource_South Africa_Multiple_Sources|M
1000073|isti|russsource_tdxx_merge|Russource_Tdxx_Merge_Multiple_Sources|M
1000074|isti|climat_uk|UK Met Office|M
1000075|isti|crutem3|UK Met Office|M
1000076|isti|crutem4|UK Met Office|M
1000077|isti|ukmet_hist|UK Met Office|M
1000078|isti|wmssc|World Monthly Surface Station Climatology Dataset|M
1000079|isti|wwr|World_Weather_Records_NOAA_multiple_sources|M
1000080|isti|russsource_ghcn|Inventory_Russsource_GHCN|M
1000081|isti|russsource_ghcnd_nonconus|Inventory_Russsource_GHCND_Nonconus|M
1000082|dwd|DWD_Daily|Deutscher Wetterdienst|DY
1000083|dwd|DWD_Sub_daily|Deutscher Wetterdienst|SBDY
1000084|dwd|DWD_Monthly|Deutscher Wetterdienst|M
1000085|ghcnd|canada_ghcnd|Environment Canada National Climate Data and Information Archive|DY
1000086|isti|antartic_southpole|Data Provided by Howard Diamond On 29 March 2011 and Peter Fisher International Operations Manager science, Research and Development Division Meteorological Service of New Zealand Limited. Updated 29th May 3 Extra Stations Via Email from Howard Diamond to Simon Noone of GLAMOD, NUIM, Ireland.|M
1000087|Howard Diamond|Pitcairns islands|Antarctic Meteorological Research Center (AMRC) University Wisconsin Madison USA|M""".split("\n")

def map_header(header):
    _mapping = {'SOURCE_UID': 'source_id',
                'DATA_REPOSITORY': 'data_repository',
                'DATA_NAME': 'label',
                'SOURCE_NAME': 'details',
                'Timestep': 'frequency'}
    return _mapping[header]

def map_frequency(freq):
    _mapping = {'DY': 'day', 'M': 'mon', 'SBDY': '6hr'}
    return _mapping[freq]

def construct_dict(line):
    d = dict([(map_header(HEADERS[i]), line.split("|")[i].strip()) for i in range(len(HEADERS))])
    d['frequency'] = map_frequency(d['frequency']) 
    
    return d 

def process():
    key = "source_id"
    records = {key: {}}
    for line in DATA:
        content = construct_dict(line)
        records[key][content["source_id"]] = content
        
    fname = "GLAMOD_source_id.json"
    with open(fname, "w") as writer:
        simplejson.dump(records, writer, indent=4, sort_keys=True)

    print "Wrote: {}".format(fname)
        
if __name__ == "__main__":

    process()
  

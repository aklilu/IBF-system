from datetime import date, timedelta


##########################
## DEVELOPMENT SETTINGS ##
##########################

# Disable these temporarily to run only the trigger-model part
CALCULATE_EXTENT = True
CALCULATE_EXPOSURE = False

# Use dummy-data and/or overwrite real data
GLOFAS_DUMMY = False
OVERWRITE_DUMMY = True

# Change this date only in case of testing
CURRENT_DATE=date.today()
# CURRENT_DATE=date.today() - timedelta(days=1)


######################
## COUNTRY SETTINGS ##
######################

# For now indicate 1 country. Ultimately we might want to loop over multiple included countries?
COUNTRY_CODE='UGA' #'ZMB'/'UGA'

SETTINGS = {
    "ZMB": {
        "trigger_levels": 'Glofas_station_locations_with_trigger_levels.csv',
        'district_mapping': 'Glofas_station_per_district.csv',
        'flood_extent_admin_boundaries': 'vector/ZMB_adm2_mapshaper_new103_pcode.shp',
        'exposure_admin_boundaries': 'vector/ZMB_adm2_mapshaper_new103_pcode.shp', #ZMB_adm4_mapshaper_reproj
        'trigger_colname': '10yr_threshold',
        'CRA_filename': 'ZMB_CRA_Indicators',
        'lead_times': {
            "short": 3,
            "long": 7
        },
        'EXPOSURE_DATA_SOURCES': {
            # value of pixel (0-100) reflects no. of cropland pixels in original crop-layer, where each pixel stands for 0.02x0.02=0.0004 km2
            "cropland/crop_resampled": 0.0004,
            "population/hrsl_zmb_pop_100_sum": 1,
            "livestock/Chicken": 1,
            "livestock/Cattle": 1,
            "livestock/Goat": 1,
            "livestock/Pig": 1,
            "livestock/Sheep": 1,
        }
    },
    "UGA": {
        "trigger_levels": 'Glofas_station_locations_with_trigger_levels_IARP.csv',
        'district_mapping': 'Glofas_station_per_district_uga.csv',
        'flood_extent_admin_boundaries': 'vector/UGA_adm2_mapshaper.shp',
        'exposure_admin_boundaries': 'vector/UGA_adm2_mapshaper.shp',
        'trigger_colname': '5yr_threshold',
        'CRA_filename': 'ZMB_CRA_Indicators',
        'lead_times': {
            "long": 7
        },
        'EXPOSURE_DATA_SOURCES': {
            "population/hrsl_uga_pop": 1,
        }
    },
}
COUNTRY_SETTINGS = SETTINGS[COUNTRY_CODE]



###################
## MAIN SETTINGS ##
###################



LEAD_TIMES = COUNTRY_SETTINGS['lead_times']

TRIGGER_RP_COLNAME = COUNTRY_SETTINGS['trigger_colname']
TRIGGER_LEVELS = {
    "minimum": 0.6,
    "medium": 0.7,
    "maximum": 0.8
}

EXPOSURE_DATA_SOURCES = COUNTRY_SETTINGS['EXPOSURE_DATA_SOURCES']

#################
## DB SETTINGS ##
#################
SCHEMA_NAME_INPUT = 'IBF-static-input'
SCHEMA_NAME = 'IBF-pipeline-output'
# Other connection-settings in secrets.py

###################
## PATH SETTINGS ##
###################
GEOSERVER_DATA = '../geoserver/geodata/zambia/'
GEOSERVER_INPUT = GEOSERVER_DATA + 'input/'
GEOSERVER_OUTPUT = GEOSERVER_DATA + 'output/'
PIPELINE_DATA = 'data/'
PIPELINE_INPUT = PIPELINE_DATA + 'input/'
PIPELINE_OUTPUT = PIPELINE_DATA + 'output/'
PIPELINE_TEMP = PIPELINE_DATA + 'temp/'

WATERSTATIONS_TRIGGERS = PIPELINE_INPUT + COUNTRY_SETTINGS['trigger_levels']
DISTRICT_MAPPING = PIPELINE_INPUT + COUNTRY_SETTINGS['district_mapping']
VECTOR_DISTRICT_DATA = PIPELINE_INPUT + COUNTRY_SETTINGS['flood_extent_admin_boundaries']
EXPOSURE_BOUNDARY_DATA = PIPELINE_INPUT + COUNTRY_SETTINGS['exposure_admin_boundaries']

    

#########################
## INPUT DATA SETTINGS ##
#########################

# Glofas input
GLOFAS_FTP = 'data-portal.ecmwf.int/ZambiaRedcross_glofas_point/'
GLOFAS_FILENAME = 'glofas_pointdata_ZambiaRedcross'

# CRA input
CRA_FILENAME = COUNTRY_SETTINGS['CRA_filename']

####################
## EMAIL SETTINGS ##
####################

# Notification email
EMAIL_NOTIFICATION = False
EMAIL_WITHOUT_TRIGGER = False

# Notification email (only if hard-coded alternative for mailchimp is used)
EMAIL_LIST_HARDCODE = [
    'jannisvisser@redcross.nl'
]

# Logging email settings
LOGGING = False  # If false send email on error
LOGGLY_LINK = "https://rodekruis.loggly.com/"
FROM_EMAIL = "support@510.global"
FROM_EMAIL_NAME = 'FBF Zambia Flood Trigger system'
EMAIL_USERNAME = "sa_typhoon@redcross.nl" #"510.global.dashboards@gmail.com"
LOGGING_TO_EMAIL_ADDRRESSES = [
    "JannisVisser@redcross.nl"
]



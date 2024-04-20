import csv
import json
from db_inserter import MongoDBInserter
class DataParser:

    inserter = MongoDBInserter()

    def __init__(self):
        None

    def parser(self):

        self.inserter.drop_collection()

        with open('Crash_Reporting_-_drivers_Data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for i in csv_reader:
                data = dict.fromkeys([
                    'acrs_report_type',
                    'date',
                    'time',
                    'collision_type',
                    'weather',
                    'surface_condition',
                    'driver_substance_abuse',
                    'driver_at_fault',
                    'driver_distracted_by',
                    'drivers_license_state',
                    'vehicle_damage_extent',
                    'vehicle_body_type',
                    'speed_limit',
                    'vehicle_year',
                    'vehicle_make',
                    'vehicle_mode'
                ])

                if i[3] is not None:
                    data['acrs_report_type'] = i[3]
                if i[4] is not None:
                    data['date'] = i[4][:10]
                    data['time'] = i[4][11:]
                if i[12] is not None:
                    data['collision_type'] = i[12]
                if i[13] is not None:
                    data['weather'] = i[13]
                if i[14] is not None:
                    data['surface_condition'] = i[14]
                if i[17] is not None:
                    data['driver_substance_abuse'] = i[17]
                if i[20] is not None:
                    data['driver_at_fault'] = i[20]
                if i[23] is not None:
                    data['driver_distracted_by'] = i[23]
                if i[24] is not None:
                    data['drivers_license_state'] = i[24]
                if i[26] is not None:
                    data['vehicle_damage_extent'] = i[26]
                if i[29] is not None:
                    data['vehicle_body_type'] = i[29]
                if i[33] is not None:
                    data['speed_limit'] = i[33]
                if i[36] is not None:
                    data['vehicle_year'] = i[36]
                if i[37] is not None:
                    data['vehicle_make'] = i[37]
                if i[38] is not None:
                    data['vehicle_mode'] = i[38]
                
                self.inserter.insert_data(data)

data_parser= DataParser()
data_parser.parser()

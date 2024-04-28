from data_parser import DataParser
from db_inserter import MongoDBInserter

if __name__ == '__main__':
    target_file = 'Crash_Reporting_-_drivers_Data.csv'
    md_data_parser = DataParser()
    md_data_parser.parser(target_file)
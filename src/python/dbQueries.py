find_tle_by_id = lambda id: f"SELECT * FROM tle WHERE satellite_id = {id};"
drop_table_by_name = lambda table_name: f"DROP TABLE {table_name};"

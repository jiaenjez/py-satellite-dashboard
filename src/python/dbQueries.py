find_tle_all = "SELECT * FROM tle;"
find_tle_by_id = lambda id: f"SELECT * FROM tle WHERE satellite_id = {id};"
drop_table_by_name = lambda table_name: f"DROP TABLE {table_name};"

queries = {
    "find_tle_all": find_tle_all,
    "find_tile_by_id": find_tle_by_id,
    "drop_table_by_name": drop_table_by_name
}


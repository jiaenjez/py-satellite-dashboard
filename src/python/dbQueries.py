queries = {
    "find_tle_all": lambda: "SELECT * FROM TLE;",
    "find_tile_by_id": lambda identifier: f"SELECT * FROM TLE WHERE SATELLITE_ID = {identifier};",
    "drop_table_by_name": lambda table_name: f"DROP TABLE {table_name};",
    "get_tle_timestamp": lambda: "SELECT MIN(UPDATED_AT) FROM TLE;"
}

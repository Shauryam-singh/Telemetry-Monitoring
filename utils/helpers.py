def get_stations(df):
    return sorted(df["station_id"].unique())

def filter_station(df, station):
    return df[df["station_id"] == station]
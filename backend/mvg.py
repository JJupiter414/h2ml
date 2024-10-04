import mvg_api

def get_mvg_departures(station_name):
    departures = mvg_api.get_departures(station_name)
    return [{'line': dep['line'], 'destination': dep['destination'], 'departureTime': dep['departureTime']} for dep in departures]

from crud import get_all_passengers, get_all_flights

def recommend_flights_for_passenger(passenger_id):
    """
    Recommande des vols à un passager en fonction des destinations déjà visitées.
    """
    passengers = get_all_passengers()
    flights = get_all_flights()

    # Vols déjà pris
    taken_flight_ids = [p['flight_id'] for p in passengers if p['passenger_id'] == passenger_id]

    # Destinations déjà visitées
    taken_flights = [f for f in flights if f['flight_id'] in taken_flight_ids]
    destinations = set(f['arrival_airport'] for f in taken_flights)

    # Recommandation : même destination, vol jamais pris
    recommended = [
        f for f in flights
        if f['arrival_airport'] in destinations and f['flight_id'] not in taken_flight_ids
    ]

    return recommended


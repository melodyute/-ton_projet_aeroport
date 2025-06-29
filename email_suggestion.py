from recommender import recommend_flights_for_passenger

def generate_email_suggestion(passenger_id):
    vols = recommend_flights_for_passenger(passenger_id)
    if not vols:
        return "Bonjour ! Nous n'avons pas encore de nouvelle destination à vous recommander. Revenez plus tard !"
    
    vol = vols[0]
    return f"""Bonjour,

Nous avons une suggestion pour vous ✈️

Nous vous recommandons le vol {vol['flight_number']} à destination de {vol['arrival_airport']}, 
prévu le {vol['departure_time']}. Une belle opportunité pour revivre l’expérience que vous avez appréciée !

À bientôt à bord,
Votre équipe Aéroport CDG.
"""

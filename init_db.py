from pymongo import MongoClient

# Connexion MongoDB
uri = "mongodb+srv://melodyuteg:Mongodb1995@clusterairport.lqkqkfo.mongodb.net/?retryWrites=true&w=majority&appName=ClusterAirport"
client = MongoClient(uri)
db = client["airport"]

# Nettoyage des collections
db.flights.delete_many({})
db.passengers.delete_many({})
db.services.delete_many({})

# Vols
flights = [
    {
        "flight_id": 42,
        "flight_number": "CDG42",
        "departure_airport": "CDG",
        "arrival_airport": "NYC",
        "departure_time": "2025-07-10 14:00",
        "arrival_time": "2025-07-10 17:00",
        "status": "On Time",
        "capacity": 300
    },
    {
        "flight_id": 43,
        "flight_number": "CDG43",
        "departure_airport": "CDG",
        "arrival_airport": "LON",
        "departure_time": "2025-08-01 10:00",
        "arrival_time": "2025-08-01 11:30",
        "status": "Delayed",
        "capacity": 250
    }
]
db.flights.insert_many(flights)

# Passagers
passengers = [
    {
        "passenger_id": "P001",
        "flight_id": 42,
        "first_name": "Alice",
        "last_name": "Dupont",
        "passport_number": "X123456",
        "booking_date": "2025-07-01",
        "profile": {
            "preferred_destinations": ["NYC", "LON"],
            "flight_type": "economy"
        }
    },
    {
        "passenger_id": "P002",
        "flight_id": 43,
        "first_name": "Karim",
        "last_name": "Benali",
        "passport_number": "X654321",
        "booking_date": "2025-07-02",
        "profile": {
            "preferred_destinations": ["LON", "MAD"],
            "flight_type": "business"
        }
    },
    {
        "passenger_id": "P003",
        "flight_id": 42,
        "first_name": "Mélanie",
        "last_name": "Nguyen",
        "passport_number": "X789456",
        "booking_date": "2025-07-03",
        "profile": {
            "preferred_destinations": ["NYC"],
            "flight_type": "economy"
        }
    },
    {
        "passenger_id": "P004",
        "flight_id": 43,
        "first_name": "Thomas",
        "last_name": "Morel",
        "passport_number": "X321654",
        "booking_date": "2025-07-04",
        "profile": {
            "preferred_destinations": ["LON", "NYC"],
            "flight_type": "economy"
        }
    }
]
db.passengers.insert_many(passengers)

# Services
services = [
    {
        "service_id": 201,
        "flight_id": 42,
        "type": "Baggage",
        "description": "Bagage enregistré 23kg",
        "service_time": "2025-07-10 12:00",
        "status": "Completed"
    },
    {
        "service_id": 202,
        "flight_id": 43,
        "type": "Security Check",
        "description": "Contrôle de sécurité prioritaire",
        "service_time": "2025-08-01 08:30",
        "status": "In Progress"
    }
]
db.services.insert_many(services)

print("✅ Données enrichies insérées avec succès.")

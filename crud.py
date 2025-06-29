from pymongo import MongoClient

# Connexion MongoDB
uri = "mongodb+srv://melodyuteg:Mongodb1995@clusterairport.lqkqkfo.mongodb.net/?retryWrites=true&w=majority&appName=ClusterAirport"
client = MongoClient(uri)
db = client["airport"]

# === CREATE ===
def add_flight(flight):
    db.flights.insert_one(flight)

def add_passenger(passenger):
    existing = db.passengers.find_one({"passenger_id": passenger["passenger_id"]})
    if existing:
        print("⚠️ Le passager existe déjà !")
    else:
        db.passengers.insert_one(passenger)

def add_service(service):
    db.services.insert_one(service)

# === READ ===
def get_flight_by_number(flight_number):
    return db.flights.find_one({"flight_number": flight_number})

def get_passengers_by_flight_id(flight_id):
    return list(db.passengers.find({"flight_id": flight_id}))

def get_services_by_flight_id(flight_id):
    return list(db.services.find({"flight_id": flight_id}))

# === UPDATE ===
def update_flight_status(flight_number, new_status):
    db.flights.update_one({"flight_number": flight_number}, {"$set": {"status": new_status}})

# === DELETE ===
def delete_passenger(passenger_id):
    db.passengers.delete_many({"passenger_id": passenger_id})

# === Fonctions supplémentaires ===
def get_all_passengers():
    return list(db.passengers.find())

def get_all_flights():
    return list(db.flights.find())


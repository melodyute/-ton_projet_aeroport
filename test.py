from pymongo import MongoClient

# Connexion MongoDB
client = MongoClient("mongodb+srv://melodyuteg:Mongodb1995@clusterairport.lqkqkfo.mongodb.net/?retryWrites=true&w=majority&appName=ClusterAirport")
db = client["airport"]
passengers = db["passengers"]

def test_insert_passenger():
    result = passengers.insert_one({
        "passenger_id": "TEST001",
        "first_name": "Test",
        "last_name": "User",
        "profile": {"preferred_destinations": ["CDG", "NYC"], "flight_type": "economy"}
    })
    assert result.inserted_id is not None
    print("✅ test_insert_passenger passed")

def test_find_passenger():
    result = passengers.find_one({"passenger_id": "TEST001"})
    assert result is not None
    print("✅ test_find_passenger passed")

def test_delete_passenger():
    result = passengers.delete_one({"passenger_id": "TEST001"})
    assert result.deleted_count == 1
    print("✅ test_delete_passenger passed")

if __name__ == "__main__":
    test_insert_passenger()
    test_find_passenger()
    test_delete_passenger()


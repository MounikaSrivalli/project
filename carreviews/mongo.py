# carreviews/mongo.py

from pymongo import MongoClient

# Replace the URI with your MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://Mounika:Car123@cluster0.tcikp.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client['CAR_REVIEWS']


# List of car brand collections
car_brands = [
    'Astonmartin','Audi','Bajaj','Bentley','Bmw','Byd','Citroen','Ferrari','Force','Honda','Hyundai','Isuzu',
    'Jaguar','Jeep','Kia','Lamborghini','Landrover','Lexus','Mahindra','Maruti-Suzuki','Maserati','Mclaren','Mercedes-Benz',
    'Mg','Mini-Cooper','Nissan','PMV','Porsche','Pravaig','Renault','Rolls-Royce','Skoda','Strom-Motors','Tata','Toyota','Volkswagen','Volvo'
]

# Retrieve data from all collections
for brand in car_brands:
    collection = db[brand]
    # Retrieve all documents from the current collection
    data = collection.find()
    
    print(f"Data from {brand} collection:")
    for document in data:
        print(document)
    print("\n")  # Print a newline for better readability

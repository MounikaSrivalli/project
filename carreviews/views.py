from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .mongo import client
from .serializers import CarReviewSerializer

class CarReviewsList(generics.ListAPIView):
    serializer_class = CarReviewSerializer

    def get_queryset(self):
        query = self.build_query()
        results = self.fetch_reviews(query)

        if not results:
            raise NotFound("No reviews found for the specified filters.")

        return results

    def build_query(self):
        query = {}
        car_name = self.request.query_params.get('carname')
        model_name = self.request.query_params.get('model_name')  # Added for model filtering
        ratings = self.request.query_params.get('ratings')
        reviewer_name = self.request.query_params.get('reviewer_name')
        
        if car_name:
            query["Model_Name"] = {"$regex": car_name, "$options": "i"}  # Allows for partial matches on the brand
        if model_name:
            query["Model_Name"] = model_name  # Exact match for model name
        if ratings:
            query["Rating"] = float(ratings)
        if reviewer_name:
            query["Reviewer_Name"] = {"$regex": reviewer_name, "$options": "i"}

        return query

    def fetch_reviews(self, query):
        car_brands = [
            'Astonmartin', 'Audi', 'Bajaj', 'Bentley', 'Bmw', 'Byd', 'Citroen',
            'Ferrari', 'Force', 'Honda', 'Hyundai', 'Isuzu', 'Jaguar', 'Jeep',
            'Kia', 'Lamborghini', 'Landrover', 'Lexus', 'Mahindra', 'Maruti-Suzuki',
            'Maserati', 'Mclaren', 'Mercedes-Benz', 'Mg', 'Mini-Cooper', 'Nissan',
            'PMV', 'Porsche', 'Pravaig', 'Renault', 'Rolls-Royce', 'Skoda',
            'Strom-Motors', 'Tata', 'Toyota', 'Volkswagen', 'Volvo'
        ]

        results = []
        for brand in car_brands:
            collection = client['CAR_REVIEWS'][brand]
            documents = list(collection.find(query))
            
            for document in documents:
                # Create a new dict with keys matching the serializer
                remapped_doc = {
                    '_id': str(document['_id']),  # Convert ObjectId to string
                    'Country': document.get('Country', ''),
                    'Model_Name': document.get('Model_Name', ''),
                    'Reviewer_Name': document.get('Reviewer_Name', document.get('reviewer_name', '')),  # Fallback
                    'Price Range': document.get('Price Range', ''),
                    'Segment': document.get('Segment', ''),
                    'Rating': document.get('Rating', 0.0),
                    'Review_Description': document.get('Review_Description', ''),
                }
                results.append(remapped_doc)

        return results

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

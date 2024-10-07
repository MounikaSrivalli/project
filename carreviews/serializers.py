from rest_framework import serializers

class CarReviewSerializer(serializers.Serializer):
    _id = serializers.CharField()  # Handle ObjectId correctly
    Country = serializers.CharField(max_length=100)  # Country of the car
    Model_Name = serializers.CharField(max_length=100)  # Name of the car model
    Reviewer_Name = serializers.CharField(max_length=100)  # Name of the reviewer
    Price_Range = serializers.CharField(source='Price Range', max_length=100, required=False)  # Price range of the car
    Segment = serializers.CharField(max_length=100)  # Segment of the car
    Rating = serializers.FloatField()  # Rating as a float
    Review_Description = serializers.CharField()  # Review description



from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel', 'hotel_image']


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room', 'room_image']


class RoomListSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'room_status', 'room_price', 'room_images', 'all_inclusive']


class RoomListForBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'room_price', 'all_inclusive']


class RoomDetailSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['room_number', 'hotel_room', 'room_type', 'room_status', 'room_price',
                  'room_images', 'all_inclusive', 'room_description']


class ReviewSerializer(serializers.ModelSerializer):
    user_name = UserProfileSimpleSerializer()

    class Meta:
        model = Review
        fields = ['user_name', 'hotel', 'stars', 'parent', 'text']


class HotelListSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'country', 'city', 'hotel_images', 'hotel_stars', 'average_rating']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class HotelListForBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'city']


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    created_date = serializers.DateField(format='%d-%m-%Y')
    owner = UserProfileSimpleSerializer()
    rooms = RoomListSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'hotel_description', 'country', 'city',
                  'address', 'hotel_stars', 'average_rating', 'hotel_images', 'hotel_video', 'reviews',
                  'created_date', 'owner', 'rooms']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class BookingSerializer(serializers.ModelSerializer):
    check_in = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    check_out = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    hotel_book = HotelListForBookingSerializer()
    room_book = RoomListForBookingSerializer()
    user_book = UserProfileSimpleSerializer()

    class Meta:
        model = Booking
        fields = ['hotel_book', 'room_book', 'user_book', 'check_in',
                  'check_out', 'total_price', 'status_book']
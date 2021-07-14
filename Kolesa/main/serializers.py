from rest_framework import serializers
from .models import *






class CarSerializer(serializers.ModelSerializer):
    subcategory = serializers.SerializerMethodField('get_subcategory')
    class Meta:
        model = Car
        fields = ['id','name', 'description', 'subcategory']

    def validate_car_name(self, car_name):
        if ['@', '%^'] in car_name:
            raise serializers.ValidationError('Not accepting character in name of car')

    def get_subcategory(self, obj):
        subcategory = SubCategory.objects.filter(car_id=obj).values('name')
        return subcategory


class SubCategorySerializer(serializers.ModelSerializer):
    car_id = CarSerializer(many=False, read_only=True)
    car = serializers.IntegerField(write_only=True)
    class Meta:
        model = SubCategory
        fields = ('car_id', 'name', 'car', )

    def create(self, validated_data):
        y = Car.objects.get(id=validated_data['car'])
        x = SubCategory.objects.create(car_id=y,
                                   name=validated_data['name'])

        return x

class CategoryBasicSerializer(serializers.ModelSerializer):
    class Meta:
         model = Category
         fields = ('name',)

class AdvandedSerializer(CategoryBasicSerializer):
    additional_field = serializers.SerializerMethodField()

    def get_additional_field(self, obj):
        return('description',)

    class Meta(CategoryBasicSerializer.Meta):
        fields = CategoryBasicSerializer.Meta.fields + ('additional_field',)



class CarBasicSerializer(serializers.ModelSerializer):
    class Meta:
         model = Car
         fields = ('description',)

class AdvandedSerializer(CarBasicSerializer):
    additional_field = serializers.SerializerMethodField()

    def get_additional_field(self, obj):
        return('name', 'subcategory',)

    class Meta(CarBasicSerializer.Meta):
        fields = CarBasicSerializer.Meta.fields + ('additional_field',)



class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
    def validate_city_name(self, city_name):
        if ['_', '#'] in city_name:
            raise serializers.ValidationError('Not accepting character in name of city')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EngineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineType
        fields = '__all__'



class EngineTypeBasicSerializer(serializers.ModelSerializer):
    class Meta:
         model = Car
         fields = ('name',)

class AdvandedSerializer(EngineTypeBasicSerializer):
    additional_field = serializers.SerializerMethodField()

    def get_additional_field(self, obj):
        return('is_electric',)

    class Meta(EngineTypeBasicSerializer.Meta):
        fields = CarBasicSerializer.Meta.fields + ('additional_field',)



class KPSerializer(serializers.ModelSerializer):
    class Meta:
        model = KP
        fields = '__all__'


class KPBasicSerializer(serializers.ModelSerializer):
    class Meta:
         model = Car
         fields = ('is_full_drive',)

class AdvandedSerializer(KPBasicSerializer):
    additional_field = serializers.SerializerMethodField()

    def get_additional_field(self, obj):
        return('name',)

    class Meta(KPBasicSerializer.Meta):
        fields = CarBasicSerializer.Meta.fields + ('additional_field',)

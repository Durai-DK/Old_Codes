from rest_framework import serializers
from .models import *

class AssestSerializer(serializers.ModelSerializer):

    class Meta:

        model = AssetManagement
        fields = "__all__"

class ShowroomSerializer(serializers.ModelSerializer):

    class Meta:

        model = Showroom_Details
        fields = "__all__"
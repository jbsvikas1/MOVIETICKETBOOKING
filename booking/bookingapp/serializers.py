from rest_framework import serializers


class BookmyshowSerializer(serializers.Serializer):
  
    cancle = serializers.CharField(label="Enter cancle")
    bookticket = serializers.CharField(label="Enter bookticket ")
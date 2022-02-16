from rest_framework import serializers
from .models import Gift, Information


class InformationSerializer(serializers.HyperlinkedModelSerializer):
    gift_id = serializers.PrimaryKeyRelatedField(
        queryset=Gift.objects.all(),
        source='gift'
    )

    owner = serializers.ReadOnlyField(source='owner.username')

    gift = serializers.HyperlinkedRelatedField(
        view_name='gift_detail', read_only=True)

    class Meta:
        model = Information
        fields = ('title', 'gift',
                  'owner', 'gift_id', 'id')


class GiftSerializer(serializers.HyperlinkedModelSerializer):
    information = InformationSerializer(many=True, read_only=True)

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Gift
        fields = ('id', 'name', 'information',  'owner', 'photo')
from django.utils import six
from rest_framework import serializers


class UUIDRelatedField(serializers.RelatedField):
    def to_internal_value(self, value):
        return self.get_queryset().get(uuid=value)

    def to_representation(self, value):
        return six.text_type(value)
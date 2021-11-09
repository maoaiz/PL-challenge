from rest_framework import serializers

from vacation.models import Vacation


class VacationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacation
        fields = [
            'id',
            'user_id',
            'start_date',
            'end_date',
            'approver_id',
            'is_approved',
        ]
        read_only_fields = [
            'is_approved',
        ]


class ApproveVacationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacation
        fields = [
            'id',
            'user_id',
            'start_date',
            'end_date',
            'approved_date',
            'approver_id',
            'is_approved',
        ]
        read_only_fields = [
            'approved_date',
            'approver',

            'start_date',
            'end_date',
        ]

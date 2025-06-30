# reviews/serializers.py
from rest_framework import serializers
from .models import ChartScannerReview

class ChartScannerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartScannerReview
        fields = ['nickname', 'comment', 'created_at']
        read_only_fields = ['created_at']

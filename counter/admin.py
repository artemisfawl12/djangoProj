from django.contrib import admin
from .models import BlogPost
from .models import ChartScannerReview


# Register your models here.


admin.site.register(BlogPost)
@admin.register(ChartScannerReview)
class ChartScannerReviewAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'comment', 'created_at')  # 목록에 표시할 필드
    search_fields = ('nickname', 'comment')               # 검색창에서 찾을 필드
    ordering = ('-created_at',)                            # 최신순 정렬


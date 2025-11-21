from django.urls import path
from . import views

urlpatterns = [
    path("", views.survey),
    path("post/", views.survey_post),
    path("history/", views.history),
    path("history/<int:survey_id>/", views.history_responses),
    path("register-bill/", views.register_bill, name="register_bill"),
    path("bill-chart-data/", views.bill_chart_data, name="bill_chart_data"),
    path("calculator/", views.energy_calculator, name="energy_calculator"),  # ← NUEVA
]

from datetime import datetime, timedelta
from django.utils.timezone import now
import django_filters
from django.forms import CheckboxSelectMultiple, RadioSelect
from django_filters import NumberFilter, DateRangeFilter
from django_filters.filters import _truncate

import products.models
from .models import *


class ProductFilter(django_filters.FilterSet):
    date_choices = [
        ("All Time", "All Time"),
        ("today", "Today"),
        ("yesterday", "Yesterday"),
        ("week", "Past 7 days"),
        ("last 30 days", "Past 30 days"),
        ("last 90 days", "Past 90 days"),
    ]
    date_filters = {
        "All Time": lambda qs, name: qs.filter(
            **{
                "%s__gte" % name: _truncate(now() - timedelta(days=10000)),
                "%s__lt" % name: _truncate(now() + timedelta(days=1)),
            }
        ),
        "today": lambda qs, name: qs.filter(
            **{
                "%s__year" % name: now().year,
                "%s__month" % name: now().month,
                "%s__day" % name: now().day,
            }
        ),
        "yesterday": lambda qs, name: qs.filter(
            **{
                "%s__year" % name: (now() - timedelta(days=1)).year,
                "%s__month" % name: (now() - timedelta(days=1)).month,
                "%s__day" % name: (now() - timedelta(days=1)).day,
            }
        ),
        "week": lambda qs, name: qs.filter(
            **{
                "%s__gte" % name: _truncate(now() - timedelta(days=7)),
                "%s__lt" % name: _truncate(now() + timedelta(days=1)),
            }
        ),
        "last 30 days": lambda qs, name: qs.filter(
            **{
                "%s__gte" % name: _truncate(now() - timedelta(days=30)),
                "%s__lt" % name: _truncate(now() + timedelta(days=1)),
            }
        ),
        "last 90 days": lambda qs, name: qs.filter(
            **{
                "%s__gte" % name: _truncate(now() - timedelta(days=90)),
                "%s__lt" % name: _truncate(now() + timedelta(days=1)),
            }
        ),
    }

    From = NumberFilter(
        field_name='price',
        lookup_expr='gte',
    )  # grater than or equal to "gte"
    To = NumberFilter(
        field_name='price',
        lookup_expr='lte'
    )
    date_added = DateRangeFilter(
        choices=date_choices,
        filters=date_filters,
        field_name='date_added',
        widget=RadioSelect
    )
    tags = django_filters.ModelMultipleChoiceFilter(
       queryset=Tag.objects.all(),
       widget=CheckboxSelectMultiple
    )

    class Meta:
        model = Product
        fields = ['name', 'description', 'tags', 'price']


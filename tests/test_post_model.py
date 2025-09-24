import pytest
from django.db.models import (
    BooleanField, CharField, DateTimeField, ForeignKey, TextField)
from django.db.utils import IntegrityError

from blog.models import Category, Post, User
from tests.conftest import _TestModelAttrs
from typing import Any

pytestmark = [
    pytest.mark.django_db,
]


@pytest.mark.parametrize(
    ('field', 'type', 'params'), [
        ('title', CharField, {'max_length': 256}),
        ('text', TextField, {}),
        ('pub_date', DateTimeField, {'auto_now': False, 'auto_now_add': False}),
        ('author', ForeignKey, {'null': False}),
        ('location', ForeignKey, {'null': True}),
        ('category', ForeignKey, {'null': True, 'blank': False}),
        ('is_published', BooleanField, {'default': True}),
        ('created_at', DateTimeField, {'auto_now_add': True}),
    ])
class TestPostModelAttrs(_TestModelAttrs):

    @property
    def model(self):
        return Post


### django-rest-framework install 
```bash
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```
[drf install](https://www.django-rest-framework.org/#installation)

### Add 'rest_framework' to your INSTALLED_APPS setting.
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

### Add default permission classes.
```python
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
```

### Add restframework urls in urls.py file 
```python
urlpatterns += [path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))]
```

### git push
```bash
git push https://Nandhakumar19dev:password-token@github.com/Nandhakumar19dev/dj_learnings.git --all
```
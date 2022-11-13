### add below specified vars in settings.py file: 

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_HOST_USER = 'nandhakumar_maint@hotmail.com'
print("you should set outlook password in below settings var")
EMAIL_HOST_PASSWORD = 'outlook-password'
EMAIL_PORT = 25
```
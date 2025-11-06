# Django Application Form

A simple Django project demonstrating how to create and process forms using **ModelForms**.

## Features
- ModelForm-based application form
- Form validation
- Saves user input to the database
- Clean and minimal UI

## Model Used
```python
class Application(models.Model):
    full_name = models.CharField(max_length=255)
    linkedin_url = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField(unique=True)
    experience = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


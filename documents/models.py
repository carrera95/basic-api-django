from django.db import models
from django.conf import settings

class Document(models.Model):
    title = models.TextField(max_length=255, help_text='Title of document')
    description = models.TextField(max_length=255, help_text='Brief description for docuemnt contain')
    file =  models.FileField(upload_to='files/%Y/%m/%d', help_text='Track and file')
    created_by = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.SET_NULL,
            blank=False,
            null=True,
            related_name='documents_created',
            help_text='User who uploaded the doc'
    )
    created_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.SET_NULL,
            blank=False,
            null=True,
            related_name='documents_updated',
            help_text='User who updated the doc'
    )
    uploaded_at = models.DateField(auto_now=True)
    type = models.CharField(help_text='PDF, doc, exe, etc', default='doc')
    
    def __str__(self):
        return self.name
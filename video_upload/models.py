from django.db import models
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

#define GD Storage
permission = GoogleDriveFilePermission(
    GoogleDrivePermissionRole.READER,
    GoogleDrivePermissionType.USER,
    'msheinberg@sarhighschool.org'
)
gd_storage = GoogleDriveStorage(permissions=(permission,))

class Map(models.Model):
    id = models.AutoField( primary_key = True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email= models.EmailField()
    map_name = models.CharField(max_length=200)
    map_data = models.FileField(upload_to='/maps', storage=gd_storage)

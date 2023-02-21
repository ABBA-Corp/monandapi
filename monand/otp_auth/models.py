from django.db import models
from .managers import *
# Create your models here.


class MyUser(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(primary_key=True, default=uuid.uuid4, blank=False, unique=True, editable=False,
                               max_length=500, name=("id"), verbose_name=("User ID"))
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    phone = models.CharField(max_length=15, db_index=True, unique=True, name=("phone"), )
    email = models.EmailField()
    is_confirmed = models.BooleanField(default=False) #default is True when not using otp email verification
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_used = models.BooleanField(default=False)  # it becomes true when otp stored in db is already used
    image = models.ImageField(null=True, blank=True)
    new_phone = models.CharField(max_length=15, null=True, blank=True) 
    otp = models.CharField(max_length=10, null=True)
    otp_expire = models.DateTimeField(auto_now_add=False, null=True)
    
    USERNAME_FIELD = 'phone'   #by default it takes username. but we  change  to  email
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return "{}".format(self.phone)

    def check_otp_expire(self, date):
        if date <= self.otp_expire.replace(tzinfo=None):
            return True
        if date > self.otp_expire.replace(tzinfo=None):
            return False


    class Meta:
        db_table = 'MyUser'
        verbose_name = "User"
        managed = True


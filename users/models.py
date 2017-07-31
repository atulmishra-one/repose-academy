# from django.db import models
# from django.contrib.auth.models import User
# from django.utils.translation import ugettext_lazy as _
# from mezzanine.core.fields import FileField
# from django.db.models.signals import post_save
#
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, related_name='user')
#     photo = FileField(verbose_name=_("Profile Picture"),
#                       upload_to=upload_to("main.UserProfile.photo", "profiles"),
#                       format="Image", max_length=255, null=True, blank=True)
#     website = models.URLField(default='', blank=True)
#     bio = models.TextField(default='', blank=True)
#     phone = models.CharField(max_length=20, blank=True, default='')
#     city = models.CharField(max_length=100, default='', blank=True)
#     country = models.CharField(max_length=100, default='', blank=True)
#     organization = models.CharField(max_length=100, default='', blank=True)
#
#     USER_TYPES = Choices('admin', 'staff',
#                          'student')
#     user_type = models.CharField(choices=USER_TYPES, max_length=50)
#
# class Student(UserProfile):
#
#     course = models.CharField(max_length=100, default='', blank=True)
#     batch = models.CharField(max_length=100, default='', blank=True)
#     user_type = models.CharField('student')
#
# class Staff(UserProfile):
#     position = models.CharField(max_length=20)
#     salary = models.CharField(max_length=20)
#     user_type = models.CharField('staff')
#
#
#
#
#
# def create_profile(sender, **kwargs):
#     user = kwargs["instance"]
#     if kwargs["created"]:
#         user_profile = UserProfile(user=user)
#         user_profile.save()
# post_save.connect(create_profile, sender=User)




import re
from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from model_utils import Choices


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        app_label = 'accounts'
        db_table = "user"

    # ordering=["created"]

    username = models.CharField(_('username'), max_length=75, unique=True,
                                help_text=_('Required. 30 characters or fewer. Letters, numbers and '
                                            '@/./+/-/_ characters'),
                                validators=[
                                    validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                              _('Enter a valid username.'), 'invalid')
                                ])
    full_name = models.CharField(_('full name'), max_length=254, blank=True)
    short_name = models.CharField(_('short name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    user = models.OneToOneField(User, related_name='user')
    # photo = FileField(verbose_name=_("Profile Picture"),
    #                   upload_to=upload_to("main.UserProfile.photo", "profiles"),
    #                   format="Image", max_length=255, null=True, blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    course = models.CharField(max_length=100, default='', blank=True)
    batch = models.CharField(max_length=100, default='', blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.email

    USER_TYPES = Choices('admin', 'staff',
                         'student')
    user_type = models.CharField(choices=USER_TYPES, max_length=50)

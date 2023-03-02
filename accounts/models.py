from django.db import models
from django.contrib.auth.models import Group, User

from general.encryption import encrypt
from general.functions import get_auto_id
from general.middlewares import RequestMiddleware
from general.models import BaseModel


class UserProfile(BaseModel):
    username = models.CharField(max_length=128)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    password = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.creator:
            # First we need create an instance of that and later get the current_request assigned
            request = RequestMiddleware(get_response=None)
            request = request.thread_local.current_request

            if self._state.adding:
                auto_id = get_auto_id(UserProfile)

                chief_username = self.username
                password = User.objects.make_random_password(length=12, allowed_chars="abcdefghjkmnpqrstuvwzyx#@*%$ABCDEFGHJKLMNPQRSTUVWXYZ23456789")

                user = User.objects.create_user(
                    username=chief_username,
                    password=password
                )

                chief_group, created = Group.objects.get_or_create(name='user')
                chief_group.user_set.add(user)

                self.creator = request.user
                self.updater = request.user
                self.auto_id = auto_id
                self.user = user
                self.password = encrypt(password)

        super(UserProfile, self).save(*args, **kwargs)

    class Meta:
        db_table = 'accounts_user_profile'
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'
        ordering = ('auto_id',)


class AdminProfile(BaseModel):
    username = models.CharField(max_length=128)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    password = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.creator:
            # First we need create an instance of that and later get the current_request assigned
            request = RequestMiddleware(get_response=None)
            request = request.thread_local.current_request

            if self._state.adding:
                auto_id = get_auto_id(AdminProfile)

                admin_username = self.username
                password = User.objects.make_random_password(length=12, allowed_chars="abcdefghjkmnpqrstuvwzyx#@*%$ABCDEFGHJKLMNPQRSTUVWXYZ23456789")

                user = User.objects.create_user(
                    username=admin_username,
                    password=password
                )

                chief_group, created = Group.objects.get_or_create(name='admin')
                chief_group.user_set.add(user)

                self.creator = request.user
                self.updater = request.user
                self.auto_id = auto_id
                self.user = user
                self.password = encrypt(password)

        super(AdminProfile, self).save(*args, **kwargs)

    class Meta:
        db_table = 'accounts_admin_profile'
        verbose_name = 'Admin profile'
        verbose_name_plural = 'Admin profiles'
        ordering = ('auto_id',)


class SuperAdminProfile(BaseModel):
    username = models.CharField(max_length=128)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    password = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.creator:
            # First we need create an instance of that and later get the current_request assigned
            request = RequestMiddleware(get_response=None)
            request = request.thread_local.current_request

            if self._state.adding:
                auto_id = get_auto_id(SuperAdminProfile)

                super_admin_username = self.username
                password = User.objects.make_random_password(length=12, allowed_chars="abcdefghjkmnpqrstuvwzyx#@*%$ABCDEFGHJKLMNPQRSTUVWXYZ23456789")

                user = User.objects.create_user(
                    username=super_admin_username,
                    password=password
                )

                chief_group, created = Group.objects.get_or_create(name='super_admin')
                chief_group.user_set.add(user)

                self.creator = request.user
                self.updater = request.user
                self.auto_id = auto_id
                self.user = user
                self.password = encrypt(password)

        super(SuperAdminProfile, self).save(*args, **kwargs)

    class Meta:
        db_table = 'accounts_super_admin_profile'
        verbose_name = 'Super Admin profile'
        verbose_name_plural = 'Super Admin profiles'
        ordering = ('auto_id',)

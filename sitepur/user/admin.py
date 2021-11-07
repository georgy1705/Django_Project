from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Order
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('email', 'phone',)


    def clean_password2(self):
        #Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return password2

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError('Пользователь с таким номером телефона уже существует')
        return phone

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
        """
        A form for updating users. Includes all the fields on
        the user, but replaces the password field with admin's
        password hash display field.
        """

        password = ReadOnlyPasswordHashField()

        class Meta:
            model = User
            fields = (
                'email',
                'password',
                'first_name',
                'last_name',
                'phone',
                'active',
                'admin',
            )

        def clean_password(self):
            return self.initial["password"]

class UserAdmin(UserAdmin):
#Forms to add and change user instances
        form = UserChangeForm
        add_form = UserCreationForm

        #The fields to be used in displaying User model.
        #These overried the definitions on the base UserAdmin
        #That reference specific fields on auth.User


        list_display = (
            'email', 'phone', 'first_name', 'last_name', 'admin', 'username'
        )
        list_filter = ('admin', 'staff')

        fieldsets = (
            ('Информация о пользователе', {'fields': ('email', 'password')}),
            ('Контактная информация', {'fields': ('phone', 'first_name', 'last_name')}),
            ('Права', {'fields': ( 'admin', 'staff',
                'username',
            )})
        )

        # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
        # overrides get_fieldsets to use this attribute when creating a user.
        add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'phone',
                    'first_name',
                    'last_name',
                    'password1',
                    'password2',
                    'username',
                )}
             ),
        )


        search_fields = ('email', 'phone')
        ordering = ('email',)
        filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Order)

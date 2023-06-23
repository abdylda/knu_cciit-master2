from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def for_networks(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    A decorator to check logged in user could be a student and redirects to the login page if the user isn't authenticated.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.role.title == 'admin' or u.role.title == 'network',
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def for_teachers(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    '''
    A decorator to check whether the logged-in user is a teacher and
    redirect to the login page if the user is not authenticated.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_teacher,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

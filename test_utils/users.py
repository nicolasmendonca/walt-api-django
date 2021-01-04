from django.contrib.auth import get_user_model


def create_user(email='test@email.com', password='testpass', name='Test User', **params):
    # get_user_model() returns the CustomUser model
    return get_user_model().objects.create_user(email=email, password=password, name=name, **params)

Django framework for connecting directly to the pico-uart-hub for control and monitoring. Later I will add an option to interface with the SignalK API which should be used instead of direct connection if SignalK is in use. I need to writeh the SignalK plugin first though.

This is a dev setup only, relying on the Django dev web server and with no thought to security or anything beyond proving it can work as yet.

Install steps:
Create a secret_key.txt file in the same directory as settings.py and populate the secret key I didn't want to commit to github (I'm not yet sure how to regenerate that, I copied the one in my settings.py created on the project creation)

Adjust the allowed hosts config in settings.py to your dev server IP, run with runserver 0:8000 to make it accessible outside localhost

run "python manage.py migrate" to configuure the sqlite DB

Adjust com port definition in views.py to match your host config

Configure the admin console with a superuser: python manage.py createsuperuser

Browse to http://<ip>:8000/admin/ to configure some lights and groups
As yet the group config needs to match that hardcoded in the pico-lights code
Light numbers should match the lights 0-15 available on the lights-pico module

Browse to http://<ip>:8000/lights/ to run the web interface.

verfiier la version de python dans terminal
puis créer environnment virtuel

→ python -m venv env
avec la commande:
→ ls
renvoie:
env
erreur:
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.8-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: ['/home/devon/Documents/DEV/django/env/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']

activer l'environnment virtuel
~/projects/django-web-app
→ source env/bin/activate
(env) ~/projects/django-web-app

Installer django avec pip
(env) ~/projects/django-web-app

→ pip install django
...
Successfully installed asgiref-3.7.2 backports.zoneinfo-0.2.1 django-4.2.9 sqlparse-0.4.4 typing-extensions-4.9.0

créer la liste des packages:
pip freeze > requirements.txt

initialiser le projet
(env) ~/projects/django-web-app
→ django-admin startproject firstone

le fichier manage.py gerera maintenant les depences, 
lançons le serveur de dev:
(env) ~/projects/django-web-app/merchex
→ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
February 07, 2021 - 17:58:59
Django version 3.1.6, using settings 'merchex.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

le terminal indique:
[28/Jan/2024 11:05:06] "GET / HTTP/1.1" 200 10664
Not Found: /favicon.ico
[28/Jan/2024 11:05:07] "GET /favicon.ico HTTP/1.1" 404 2112

Un peu comme avec Rocket en fait.
Créer la bdd:
(env) ~/projects/django-web-app/merchex
→ python3 manage.py migrate
Operations to perform:
Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
Applying ...

Generer le code de départ:
(env) ~/projects/django-web-app/merchex
→ python manage.py startapp listings

La dernière étape de l'ajout de notre application « listings » à notre projet « merchex » consiste à « installer » l'application dans le projet.
Lorsque nous avons généré le code de base de notre projet, l'un des fichiers créés s'appelait settings.py. Ouvrez maintenant ce fichier et trouvez une liste Python appelée INSTALLED_APPS. En bas de cette liste, ajoutez la chaîne de caractères ’listings’:

********* FIN PREMIER ARTICLE *************

ajouter une page
dans les vue de l'app (llistings/views.py)
ajouter 
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

dans projert /urls.py ajouter les nouvelles urls:
# ~/projects/django-web-app/merchex/merchex/urls.py

from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
path('admin/', admin.site.urls),
path('hello/', views.hello)
]

*************************

BASE DE DONNEE

dans models.py:
# listings/models.py

class Band(models.Model):
    name = models.fields.CharField(max_length=100)

opérer la migration
# shell

(env) ~/projects/django-web-app/merchex
→ python manage.py makemigrations
python manage.py makemigrations
Migrations for 'listings':
  listings/migrations/0001_initial.py
    - Create model Band
et appeler migrate
(env) ~/projects/django-web-app/merchex
→ python manage.py migrate
Operations to perform:
Apply all migrations: admin, auth, contenttypes, listings, sessions
Running migrations:
Applying listings.0001_initial... OK

Faire des enregistrement avec le shell
(env) ~/projects/django-web-app/merchex
→ python manage.py shell
>>>

importer le model
>>> from listings.models import Band

creer une nouvelle intance de Band:
>>> band = Band()
>>> band.name = 'De La Soul'

verifier:
>>> band
<Band: Band object (None)>

puis sauvegarder
>>> band.save()

en une ligne:
>>> band = Band.objects.create(name='Foo Fighters')

qq commandes:
>>> Band.objects.count()
3
>>> Band.objects.all()
<QuerySet [<Band: Band object (1)>, <Band: Band object (2)>, <Band: Band object (3)>]>

* Utiliser site d'administration
** creer un super utilisateur

python manage.py createsuperuser
->nom 
-> mail
-> password
dans listing/admin.py
importer Band:
from listings.models import Band

admin.site.register(Band)







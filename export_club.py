import sys
import django
from django.apps import apps
from django.core import serializers

# Configura Django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

# Obtiene todos los modelos de la app 'club'
models = apps.get_app_config('club').get_models()

# Extrae todos los objetos
data = []
for model in models:
    data.extend(model.objects.all())

# Serializa a JSON con indentación
serialized = serializers.serialize('json', data, indent=4)

# Guarda en UTF-8 puro
with open('club/fixtures/club_datos.json', 'w', encoding='utf-8') as f:
    f.write(serialized)

print("Datos exportados correctamente a club/fixtures/club_datos.json")

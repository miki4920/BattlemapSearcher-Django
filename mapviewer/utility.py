import re

from django.http import HttpResponse

from .models import Map
from django.db.models import Q
from django.db import connection


def get_map_or_404(map_id):
    try:
        map_model = Map.objects.get(id=map_id)
    except Map.DoesNotExist:
        response = HttpResponse(status=404, content=f"Map {map_id} not in the database")
        return response
    return map_model


def get_map_query(text):
    maps = (get_name_uploader_query(text) | get_tag_query(text)).distinct()
    return maps


def get_name_uploader_query(text):
    lookup = None
    for word in text:
        if lookup:
            lookup = lookup & (Q(name__icontains=word) | Q(uploader__icontains=word))
        else:
            lookup = (Q(name__icontains=word) | Q(uploader__icontains=word))
    maps = Map.objects.filter(lookup)
    return maps


def get_tag_query(text):
    lookup = ""
    for word in text:
        lookup += f"mapviewer_tag.name LIKE \"{word}\" OR "
    if len(lookup) > 0:
        lookup = lookup[:-3]
        with connection.cursor() as cursor:
            cursor.execute('''SELECT id
               FROM (SELECT mapviewer_map.id, COUNT(*) as Counter FROM mapviewer_map 
               JOIN mapviewer_map_tags ON mapviewer_map.id=map_id 
               JOIN mapviewer_tag ON mapviewer_tag.id = tag_id 
               WHERE %s 
               GROUP BY mapviewer_map.id) as tag_table WHERE Counter > %s;''' % (lookup, len(text)-1))
            maps = cursor.fetchall()
        if len(maps) > 0:
            maps = [map_id[0] for map_id in maps]
            maps = Map.objects.filter(id__in=maps)
        else:
            maps = Map.objects.none()   
    else:
        maps = Map.objects.all()
    return maps


def clean_search(text):
    text = re.sub("[^a-zA-Z0-9 \"]", "", text)
    text = text.lower()
    text = text.split(" ")
    return text

from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model: Note
        fields = '__all__' # scelgo quali campi del modello esporre (in qeusto caso tutti)
        

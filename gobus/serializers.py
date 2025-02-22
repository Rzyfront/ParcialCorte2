from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Agencia, Terminal, Ruta, Bus, Conductor, Pasajero, Boleto, Viaje


# Serializador para el modelo de Usuario de Django
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']


class AgenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agencia
        fields = ['id', 'nombre', 'direccion', 'telefono', 'correo', 'sitio_web', 'horario_atencion']


class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminal
        fields = ['id', 'nombre', 'ubicacion', 'telefono']


class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = ['id', 'origen', 'destino', 'distancia', 'duracion_estimada']


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['id', 'placa', 'capacidad', 'tipo', 'estado']

class ViajeSerializer(serializers.ModelSerializer):
    ruta = RutaSerializer() 
    bus = BusSerializer()    
    class Meta:
        model = Viaje
        fields = ['id', 'ruta', 'bus', 'fecha_viaje', 'hora_salida', 'precio']


class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = ['id', 'nombre', 'licencia', 'telefono', 'anios_experiencia']


class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = ['id', 'documento_identidad', 'nombre']


class BoletoSerializer(serializers.ModelSerializer):
    pasajero = PasajeroSerializer()  # Incluir el pasajero como un nested serializer
    viaje = serializers.PrimaryKeyRelatedField(queryset=Viaje.objects.all())
    class Meta:
        model = Boleto
        fields = ['id','viaje','asiento', 'precio', 'estado', 'pasajero']

    def create(self, validated_data):
        # Extraer datos del pasajero
        pasajero_data = validated_data.pop('pasajero')
        # Crear o obtener el pasajero
        pasajero, created = Pasajero.objects.get_or_create(**pasajero_data)
        # Crear el boleto con el pasajero relacionado
        boleto = Boleto.objects.create(pasajero=pasajero, **validated_data)
        return boleto

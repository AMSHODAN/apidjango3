from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'CPF invalido'})
        if not nome_valido(data['nome']):
              raise serializers.ValidationError({'nome':'Nome não pode conter numeros'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'RG deve ter nove digitos'})
        if not cel_valido(data['celular']):
            raise serializers.ValidationError({'celular':'Celular deve seguir o padrão 12 12345-1234'})
        return data

    
    

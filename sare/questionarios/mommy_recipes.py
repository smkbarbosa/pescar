from model_mommy.recipe import Recipe

from sare.questionarios.models import Questionario

quest = Recipe(
    Questionario,
    nome='Samuel Barbosa',
    cidade='Palmas',
    cpf='12345678901',
    email='samuka1@gmail.com',
    sexo='M'
)
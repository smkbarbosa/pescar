[![Build Status](https://travis-ci.org/smkbarbosa/pescar.svg?branch=master)](https://travis-ci.org/smkbarbosa/pescar)

# PESCAR

É o acrônimo para Programa de Estudo Socioeconômico-cultural, um projeto desenvolvido
pelo setor de assistência estudantil do IFTO
sob a liderança de Sônia Caranhato (Assistente Social).

### Objetivo
Conceber um conjunto de práticas que avaliem a situação
de vulnerabilidade social dos estudantes.

### Sobre este projeto
Como parte do Pescar, o SARE - Sistema de Acompanhamento da Realidade do Estudante
visa fornecer o mapa de vulnerabilidade, através da análise
de formulários socioeconômicos-culturais, dando aos profissionais
um parâmetro para realizar interverções junto aos alunos
em situação mais vulnerável.

Este projeto será utilizado como trabalho de conclusão de curso
de Samuel Barbosa, no curso superior técnológico de Sistemas
para Internet, no Campus Palmas do IFTO.

### Como rodar localmente

```
git clone https://github.com/smkbarbosa/pescar.git
cd pescar
python -m venv .venv
source .venv/bin/activate
PS1="(`basename \"$VIRTUAL_ENV\"`):/\W$ " # opcional (insere nome do virtualenv no terminal)
python -m pip install -r requirements/dev.txt
python contrib/env-sample.py
python manage.py makemigrations
python manage.py migrate
python manage.py test
```

**Atenção:** Caso dê problema com a migração, você pode excluir suas migrações locais 

```
make delete_migrations
```

Depois diginte:

```
make migrate
```


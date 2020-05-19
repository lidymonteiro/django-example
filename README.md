# Django with Github Actions, PostgreSQL and Docker

![alt text](https://github.com/lucasmagnum/django-github-actions-ci/workflows/Python%20application/badge.svg)

#### Executando o projeto em modo desenvolvimento:

- Baixe o projeto: 
```
git clone https://github.com/lidymonteiro/django-example.git
git checkout dev
```

- Instale o Docker Engine: https://docs.docker.com/engine/install/
- Instale o Docker Compose: https://docs.docker.com/compose/install/
- Rodando o projeto no Docker:
```
docker-compose run --rm web python manage.py migrate
docker-compose run --rm web python manage.py createsuperuser
```

Para iniciar a aplicação em em 0.0.0.0:8000, utilize:

```
docker-compose up
```

Se precisar reinstalar as dependências do requirements, faça

```
docker-compose up --build
```

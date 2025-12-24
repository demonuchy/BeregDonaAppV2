# Bereg Dona V2

## Описание проекта 
...
## 🎯 Возможности

Приложение предоставляет удобный интуитивно понятный интерфейс реализующий следующий функционал:
- **Безопасное хранение личных данных**
- **Прием/Отклонение заявок на вступление**
- **Управление данными участников** экспорт в Json Excel и другие форматы 
- **Записть на мероприятия**
- **Оплата взносов**

## 🏗️ Архитектура
Микросервисы 
Выбор архитектуры не случайный в первой версии написанонной на монолите было множество проблем из за жесткой поиаязки бота к единой точке входа так как бот имеет функционал похожий на приложение любое изменение бизнеслогики требовало изменений в боте
блее подробно можно ознакомится с архитектурой в папке **docs**
### Сервисы 
Каждый сервис реализоаан как отделтное независимое приложение за исключением базы данных, база данных являеться общим ресурсом и еднственнвм узлом в программе связывающим сервисы 
### Auth
Сервис авторизации проверяет валидность токена доступа
### User
### Application 
### Bot notification 
## 📦 Быстрый старт
...
## 🔧 Детальная настройка
...
## 🚀 Использование API
...
## 🤖 Работа с ботом


## 🛠️ Технологический стек

### 🔧 Backend

<div style="background: #4d4d4d; padding: 15px; border-radius: 8px; text-align: center;">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg" width="30" height="30" />
</div>

<div style="background: #4d4d4d; padding: 15px; border-radius: 8px; text-align: center;">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="30" height="30" />
</div>

<div style="background: #4d4d4d; padding: 15px; border-radius: 8px; text-align: center;">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="30" height="30" />
</div>

<div style="background: #4d4d4d; padding: 15px; border-radius: 8px; text-align: center;">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="30" height="30" />
</div>

<div style="background: #4d4d4d; padding: 15px; border-radius: 8px; text-align: center;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg" width="30" height="30" style="margin-left: 10px;" />
</div>

<div style="background: #4d4d4d; padding: 15px; border-radius: 8px; text-align: center;">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="30" height="30" />
</div>


### 📱 Frontend

<div style="background: #4d4d4d; padding: 15px; border-radius: 8px; text-align: center;">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="30" height="30"/>
</div>

<div style="background: #4d4d4d; padding: 15px; border-radius: 8px; text-align: center;">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" width="30" height="30" />
</div>

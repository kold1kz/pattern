# pattern

### Перед собиранием контейнера добавить .env файл в корень репозитория

## Правила работы с репозиторием на GitLab (!):

- Разработчики клонируют проект и работают исключительно в своих ветках
- ! Просьба оставлять в коде подробные комментарии на русском языке !
- ! Просьба закрывать чувствительные данные в .env файлы и не пушить их в репозиторий при помощи .gitignore !
- При изменении кода в файлах, рекомендуется своевременно сделать коммит в свою ветку
- Описание коммита должно соответствовать проведённым изменениям (Пример ниже)

> Изменения коснулись папки со скриптами /scripts/
```sh
git commit -m 'Новые скрипты в папке scripts'
```

## Памятка по работе с GIT:
- Посмотреть все ветки - команда покажет локальные ветки и ветки на сервере GitLab
```sh
git branch --all
```
- Перейти в свою ветку, к примеру, backend
```sh
git switch backend
```
- Подтянуть обновления ветки с сервера на компьютер (Рекомендуется выполнять команду перед тем, как приступить к работе)
```sh
git pull
```
Проверить измененные файлы (Рекомендуется переодически проверять что было изменено, а что нет)
```sh
git status
```
- Добавить все файлы в отслеживание
```sh
git add .
```
- Сохранить изменения в системе GIT (Сделать коммит)
```sh
git commit -m "Комментарий"
```
- Загрузить изменения на сервер GitLab в репозиторий
```sh
git push
```


## Памятка по работе с docker:
- собирание docker - команда собирет все докер контейнеры
```sh
sudo docker compose build 
```
or 
```sh
sudo docker-compose build
```
- Запуск docker - команда запустит все докер контейнеры
```sh
sudo docker compose up 
```
or
```sh
sudo docker-compose up
```

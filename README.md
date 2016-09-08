VK auto comment
=====

Скрипт создан для создания массовых комментариев на стенах пользователей и сообществ во Вконтакте.


Создание приложения в VK
-------

1. Зайдите на https://vk.com/editapp?act=create
2. Создайте standalone-приложение
3. Из настроек созданного приложения сохраните "ID приложения" и "Защищенный ключ"


Получение access token
-------

1. Вставляем "ID приложения" в параметр client_id в ссылке https://oauth.vk.com/authorize?client_id=5618632&display=popup&response_type=code&redirect_uri=https://oauth.vk.com/blank.html&scope=groups,wall,offline
2. Переходим по ней и нажимаем разрешить.
3. Ссылка адресной строке браузера изменилась на ссылку вида https://oauth.vk.com/blank.html#code=465de75dbc97d61ec3. Запоминаем параметр code.
4. Вставляем
 * "ID приложения" в параметр client_id 
 * "Защищенный ключ" в параметр client_secret
 * code в параметр code
 
в ссылке https://oauth.vk.com/access_token?client_id=5618632&client_secret=lmx9YRAjH6jrJ2FJBCwh&redirect_uri=https://oauth.vk.com/blank.html&code=465de75dbc97d61ec3  

5. Переходим по получившийся ссылке и получаем access_token
 
 
Использование
-------

1. В settings.py помещаем все настройки скрипта: 
 * access tokens пользователей Вконтакте
 * id стен на которых нужно опубликовать комментарий,
 * количество постов, которые нужно взять с каждой стены
 * набор комментариев
 * attachments
2. Запускаем mass_comment.py

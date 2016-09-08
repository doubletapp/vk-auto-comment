import random
import time
from vk_auto_comment.vk_api import VkAPI
from settings import WALLS_IDS, POSTS_COUNT, COMMENT_MESSAGES, ATTACHMENTS, ACCESS_TOKENS

# набор ботов
vk_bots = [VkAPI(access_token)for access_token in ACCESS_TOKENS]

# собираем POSTS_COUNT последних постов из каждого источника
posts = []
for wall_id in WALLS_IDS:
    posts += [
        (wall_id, item["id"])  # сохраняем пары (id стены, id поста) для дальнейшей публикации
        for item in vk_bots[0].get_posts(wall_id, POSTS_COUNT)['response']['items']
    ]

# перемешиваем посты в случайном порядке для случайного порядка публикации комментариев
random.shuffle(posts)

# публикуем комментарий под каждым постом
for post in posts:
    # создаем комметарий от случайного бота
    result = random.choice(vk_bots).create_comment(
         owner_id=post[0],
         post_id=post[1],
         message=random.choice(COMMENT_MESSAGES),  # случайный заголовок
         attachments=ATTACHMENTS,
    )
    # ссылка на получившийся комментарий
    url = "https://vk.com/wall{owner_id}_{post_id}?w=wall{owner_id}_{post_id}_r{comment_id}".format(
        owner_id=post[0],
        post_id = post[1],
        comment_id = result['response']['comment_id']
    )
    print(url)
    time.sleep(3)

import vk_api, Logger, time, re
from threading import Thread
from config import config

url = input('Введите ссылку на пост!')
link = re.search(r'wall\d+_\d+', url)
if link is None:
    Logger.Rlog('Ссылка инвалидная!')
    exit(0)
else:
    post = link.group(0).replace('wall', '').replace('_', ' ').split()

def core(name, api):
    global post
    Logger.Ylog(f'Группа №{name} запущена')
    i = 1
    while True:
        try:
            api.wall.createComment(owner_id=post[0], post_id=post[1],
                                   message="&#4448;")
            Logger.Pulselog(f'Группа №{name} оставила коммент ({i})')
            i += 1
            time.sleep(1)
        except Exception as s:
            Logger.Rlog(f'Произошел сбой в {name}\n'
                        f'{s.__class__} {s}')
            time.sleep(60)
        except vk_api.exceptions.ApiError:
            Logger.Plog(f'Произошел сбой в {name}\n'
                        f'{s.__class__} {s}')
            break
    Logger.Rlog(f'Группа №{name} закончила свою работу')

def main():
    for x in range(1, len(config['tokens']) + 1):
        token = config['tokens'][x - 1]
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()

        Thread(target=core, args=[x, vk]).start()

if __name__ == '__main__':
    main()
import vk_api, Logger, time, re
from threading import Thread
from config import config


# https://vk.com/dean0n?w=wall242175861_1690
Logger.Blog(">>> Cсылку на пост:")
url = input('')
link = re.search('wall\d+_\d+', url)
if link is None:
    link = re.search('wall-\d+_\d+', url)
    if link is None:
        Logger.Rlog('>>> Неправильная ссылка!')
        exit(0)
    else:
        post = link.group(0).replace('wall', '').replace('_', ' ').split()
else:
    post = link.group(0).replace('wall', '').replace('_', ' ').split()
# &#4448;
Logger.Blog(">>> Текст для отправки:")
text = input('')

def core(name, api):
    global post
    global text
    Logger.Glog(f'>>> Спамер запустил группу №{name}')
    i = 1
    while True:
        try:
            api.wall.createComment(owner_id=post[0], post_id=post[1],
                                   message=text)
            Logger.Pulselog(f'>>> Группа №{name} оставила коммент ({i})')
            i += 1
            time.sleep(0.2)
        except vk_api.exceptions.ApiError as s:
            Logger.Plog(f'Произошел сбой в {name} группе\n'
                        f'{s.__class__} {s}')
            time.sleep(60)
        except Exception as s:
            Logger.Rlog(f'Произошел сбой в {name} группе\n'
                        f'{s.__class__} {s}')
            time.sleep(60)
    Logger.Rlog(f'Группа №{name} закончила свою работу')

def main():
    for x in range(1, len(config['tokens']) + 1):
        token = config['tokens'][x - 1]
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()
        Thread(target=core, args=[x, vk]).start()


if __name__ == '__main__':
    main()
import vk_api, Logger, time
from threading import Thread
from config import config

def core(name, api):
    Logger.Ylog(f'Группа №{name} запущена')
    i = 1
    while True:
        try:
            api.wall.createComment(owner_id='242175861', post_id='1690',
                                   message="&#4448;")
            Logger.Pulselog(f'Группа №{name} оставила коммент ({i})')
            i += 1
            time.sleep(1)
        except Exception as s:
            Logger.Rlog(f'Произошел сбой в {name}\n'
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
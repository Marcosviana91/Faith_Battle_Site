from datetime import datetime
import os
import zipfile

from faith_battle_site.settings import STATICFILES_DIRS

from typing import List


def getAvatarFileList(show_all=False):
    '''
    @ params  
    `show_all` if **True** ignores hidden list

    @ returns a string list of files names to use as avatar
    '''
    AVATAR_DIR = os.path.join(STATICFILES_DIRS[0], "general", "img", "Avatar")
    all_avatar = os.listdir(AVATAR_DIR)
    if show_all:
        return sorted(all_avatar)
    public_avatar = []
    for _avatar in all_avatar:
        if not _avatar.startswith('_'):
            public_avatar.append(_avatar)
    return sorted(public_avatar)


def gerarArquivo(file_name: str, game_files_list: List):
    start = datetime.now().timestamp()
    file_name = file_name.replace(" ", "_")
    # print(game.image.url)
    with zipfile.ZipFile(f'./media/packages/{file_name}.zip', 'w') as arquivo_zip:
        for file in game_files_list:
            arquivo_zip.write(f'.{file}')
    print('pacote criado')
    return {
        'size': os.path.getsize( f'./media/packages/{file_name}.zip'),
        'time_stamp': start,
        'url': f'/media/packages/{file_name}.zip',
    }

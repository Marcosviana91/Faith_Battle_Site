import os

from faith_battle_site.settings import STATICFILES_DIRS

def getAvatarFileList(show_all = False):
    '''
    @ params  
    `show_all` if **True** ignores hidden list
    
    @ returns a string list of files names to use as avatar
    '''
    AVATAR_DIR = os.path.join(STATICFILES_DIRS[0], "general", "img", "Avatar")
    all_avatar = os.listdir(AVATAR_DIR)
    if show_all:
        return all_avatar
    public_avatar = []
    for _avatar in all_avatar:
        if not _avatar.startswith('_'):
            public_avatar.append(_avatar)
    return public_avatar
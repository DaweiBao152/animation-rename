import os


class VideoRename:
    def __init__(self, directory, anim_type, anim_season, anim_format):
        self.directory = directory
        self.anim_type = anim_type
        self.anim_season = anim_season
        self.anim_format = '.' + anim_format

        if not os.path.exists(directory):
            raise FileNotFoundError

    def list_videos(self):
        arr = []
        for v in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory, v)) & v.lower().endswith(self.anim_format):
                arr.append(v)
        return arr

    def rename_anim(self, target_name):
        episode = 0
        for i in self.list_videos():
            episode += 1
            new_name = (f"{target_name} [{self.anim_season}E{episode:0>2}]"
                        f"{self.anim_type}{self.anim_format}")
            os.rename(os.path.join(self.directory, i),
                      os.path.join(self.directory, new_name))
            print("save: " + new_name)


class SubtitleRename:
    def __init__(self, directory, anim_type, anim_season, sub_format):
        self.directory = directory
        self.anim_type = anim_type
        self.anim_season = anim_season
        self.sub_format = '.'+sub_format

        if not os.path.exists(directory):
            raise FileNotFoundError

    def list_subtitle(self):
        return [s for s in os.listdir(self.directory)
                if os.path.isfile(os.path.join(self.directory, s))
                and s.lower().endswith(self.sub_format)]

    def rename_subtitle(self, target_name, target_lang):
        episode = 0
        for i in self.list_subtitle():
            episode += 1
            new_name = (f"{target_name} [{self.anim_season}E{episode:0>2}]"
                        f"{self.anim_type}.{target_lang}{self.sub_format}")
            os.rename(os.path.join(self.directory, i),
                      os.path.join(self.directory, new_name))
            print("save: " + new_name)


def rename_video(directory, anim_type, anim_season, dot_format, new_name):
    video_rename = VideoRename(directory, anim_type, anim_season, dot_format)
    video_rename.rename_anim(new_name)


def rename_subtitle(directory, anim_type, anim_season, dot_format, new_name, language):
    subtitle_rename = SubtitleRename(directory, anim_type, anim_season, dot_format)
    subtitle_rename.rename_subtitle(new_name, language)


if __name__ == '__main__':
    # name to
    target_new_name = 'REBORN'

    # number of season
    target_directory = './Season7'
    decode = '[BD-1080P]'
    season = target_directory[2] + '0' + target_directory[-1]
    animation_format = 'mkv'
    subtitle_format = 'srt'

    rename_video(target_directory, decode, season, animation_format, target_new_name)
    rename_subtitle(target_directory, decode, season, subtitle_format, target_new_name, 'chs')

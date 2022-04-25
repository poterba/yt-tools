
from ytmusicapi import YTMusic
import logging
import coloredlogs
import inquirer
import time


def main():
    ytmusic = YTMusic(auth="headers_auth.json")

    playlists = ytmusic.get_library_playlists()
    src_pl = next(filter(lambda x: x['title']=='Your Likes', playlists), None)
    dest_pl = next(filter(lambda x: x['title']=='JEANNE', playlists), None)
    
    all_songs = ytmusic.get_playlist(src_pl['playlistId'], limit=2000)
    song_ids = list(map(lambda x: x['videoId'], all_songs['tracks']))
    result = ytmusic.add_playlist_items(dest_pl['playlistId'], song_ids, duplicates=True)
    return result


if __name__ == '__main__':
    coloredlogs.install(level=logging.INFO)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    try:
        main()
    except IOError as e:
        logging.error(e)
    except Exception as e:
        logging.exception(e)
    except KeyboardInterrupt as e:
        logging.error('KeyboardInterrupt')

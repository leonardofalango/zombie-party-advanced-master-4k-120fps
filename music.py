import pygame
pygame.init()

def insert_into_playlist(playlist, music_file):
    playlist.append(music_file)

def start_playlist(playList):
    pygame.mixer.music.load(playList[0])
    playList.pop(0)
    pygame.mixer.music.play()
    pygame.mixer.music.queue(playList[0])
    playList.pop(0)
    pygame.mixer.music.set_endevent(pygame.MUSIC_END)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MUSIC_END:
                print('Song Finished')
                if len(playList) > 0:
                    pygame.mixer.music.queue(playList[0])
                    playList.pop(0)
            if not pygame.mixer.music.get_busy():
                print("Playlist completed")
                running = False
                break

if __name__ == '__main__':
    playList = []

    insert_into_playlist(playList, 'Songs/LMFAO 8-Bit.mp3')
    insert_into_playlist(playList, 'Songs/Blinding Lights - 8 Bit.mp3')
    insert_into_playlist(playList, 'Songs/Matuê - 777-666 - 8 Bit.mp3')
    insert_into_playlist(playList, 'Songs/Turn Down For What - 8 Bit.mp3')

    start_playlist(playList)


'''
pygame.init()
pygame.mixer.music.load('Songs/LMFAO 8-Bit.mp3')
pygame.mixer.music.load('Songs/Blinding Lights - 8 Bit.mp3')
pygame.mixer.music.load('Songs/Matuê - 777-666 - 8 Bit.mp3')
pygame.mixer.music.load('Songs/Turn Down For What - 8 Bit.mp3')
pygame.mixer.music.load('Songs/LMFAO 8-Bit.mp3', "LMFAO")
pygame.mixer.music.queue('Songs/Blinding Lights - 8 Bit.mp3', "THE WEEKEND", 0)
pygame.mixer.music.queue('Songs/Matuê - 777-666 - 8 Bit.mp3', "MATUÊ", 0)
pygame.mixer.music.queue('Songs/Turn Down For What - 8 Bit.mp3', "TURN DOWN FOR WHAT", 0)
pygame.mixer.music.play(-1)
pygame.event.wait()
'''
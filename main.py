import yt_dlp
import os
import sys

def download_playlist(url, format_choice):
    ydl_opts = {
        'format': 'bestaudio/best' if format_choice == 'mp3' else 'bestvideo+bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }] if format_choice == 'mp3' else [{
            'key': 'FFmpegVideoConvertor', 
            'preferedformat': 'mp4', 
        }],
        'noplaylist': False,  
        'quiet': False, 
        'progress_hooks': [progress_hook],  
    }

    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\ndownload concluído com sucesso!")
    except KeyboardInterrupt:
        print("\nprocesso interrompido.")
        sys.exit()

def progress_hook(d):
    if d['status'] == 'downloading':

        pass

    elif d['status'] == 'finished':

        pass 

    elif d['status'] == 'error':
        
        pass  

if __name__ == "__main__":
    url = input("insira o link da playlist do youTube: ")
    format_choice = input("Escolha o formato (mp3 ou mp4): ").strip().lower()

    if format_choice not in ['mp3', 'mp4']:
        print("formato inválido. por favor, escolha 'mp3' ou 'mp4'.")
    else:
        print("\niniciando o download...")
        download_playlist(url, format_choice)


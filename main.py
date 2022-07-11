from pytube import YouTube
import os
from os import path
import argparse
import shutil
import sys
import platform


#yt = YouTube('https://www.youtube.com/watch?v=EqwVfjiYhgk')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help="YouTube Link")
    parser.add_argument('-sd', action="store_true", help="480p")
    parser.add_argument('-hd', action="store_true", help="720p")
    parser.add_argument('-fhd', action="store_true", help="1080p")
    parser.add_argument('-a', action="store_true", help="mp3")
    parser.add_argument('-vf', action="store", default='webm' , help='choose the video format you want: mp4, webm, 3gp')
    
    args = parser.parse_args()

    video_format = ['mp4', 'webm', '3gp']

    if args.vf.lower() not in video_format:
        args.vf = 'webm'


    try:
        yt = YouTube(args.url, on_progress_callback=onProgress )
    except:
        print('Download fail, plz check your YouTube link.')
    download_video(yt, args)

    
    
def onProgress(streams, chunk, remaining):
    total = streams.filesize
    percent = (total - remaining)/total * 100
    print('downloading...{:05.2f}%'.format(percent), end='\r' )
    
    
def download_video(yt, args):
    filter = yt.streams.filter
    res_choose = None

    if args.fhd:
        target = filter(type='video', resolution='1080p', subtype=args.vf).first()
        res_choose = '1080p'
    elif args.hd:
        target = filter(type='video', resolution='720p', subtype=args.vf).first()
        res_choose = '720p'
    elif args.sd:
        target = filter(type='video', resolution='480p', subtype=args.vf).first()
        res_choose = '480p'
    elif args.a:
        target = filter(type='audio', subtype=args.vf).first()
        res_choose = 'mp3'
    else:
        target = filter(type='video', subtype=args.vf).first()
        res_choose = target.resolution

        
    try:
        print('Download the {} by {}'.format(args.vf , res_choose))
        target.download(output_path=pyTube_folder())
    except:
        print('There have no {} video can download, plz select the other version: '.format(res_choose))
        res_list = video_res(yt, args)
        for i, res in enumerate(res_list):
            print('{}) {}'.format(i+1, res))
        
        target = filter(type='video', resolution=res_list[int.input("plz input the number (eg. 1):")-1]).first()
        target.download(output_path=pyTube_folder())

        
def pyTube_folder():
    sys = platform.system()
    home = path.expanduser('~')
    
    if sys == 'Windows':
        folder = path.join(home, 'Videos', 'PyTube')
    elif sys == 'Darwin':
        folder = path.join(home, 'Movies', 'PyTube')
    if not os.path.isdir(folder):
        os.mkdir(folder)
    return folder

def video_res(yt, args):
    res_set = set()
    video_list = yt.streams.filter(type='video', subtype= args.vf).all
    
    for v in video_list:
        res_set.add(v.resolution)
    
    return sorted(res_set, reverse=True, key=lambda s:int(s[:-1]))


if __name__ == '__main__':
    main()
        
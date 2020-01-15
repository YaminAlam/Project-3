from flickr import get_urls
from downloader import download_images
import os
import time

all_types = ['indoor', 'outdoor']
train_images = 1400
test_images = 600

def download_train():
    print("Training Set")
    for setting in all_types:

        print('Getting urls for', setting)
        urls = get_urls(setting, train_images)
        
        print('Downloading images for', setting)
        path = os.path.join('data','train', setting)

        download_images(urls, path)

def download_test():
    print("Test Set")
    for setting in all_types:

        print('Getting urls for', setting)
        urls = get_urls(setting, test_images)
        
        print('Downloading images for', setting)
        path = os.path.join('data','test', setting)

        download_images(urls, path)        

if __name__=='__main__':

    start_time = time.time()

    download_train()
    download_test()

    print('Took', round(time.time() - start_time, 2), 'seconds')
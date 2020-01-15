from flickrapi import FlickrAPI

KEY = 'eb73a489c076e2377f60e2be544efd73'
SECRET = '0a32da5306833a88'

SIZES = ["url_z"]  

def get_photos(image_tag):
    extras = ','.join(SIZES)
    flickr = FlickrAPI(KEY,SECRET)
    photos = flickr.walk(text=image_tag,
                            extras = extras,
                            privacy_filter = 1,
                            per_page = 50,
                            sort = 'relevance')
    return photos

def get_url(photo):
    for i in range(len(SIZES)):
        url = photo.get(SIZES[i])
        if url:  # if url is None try with the next size
            return url
            
def get_urls(image_tag, max):
    photos = get_photos(image_tag)
    counter=0
    urls=[]

    for photo in photos:
        if counter < max:
            url = get_url(photo)  # get preffered size url
            if url:
                urls.append(url)
                counter += 1
            # if no url for the desired sizes then try with the next photo
        else:
            break

    return urls
import uuid

from io import BytesIO

from PIL import Image
from PIL import ImageFile

# Geometrizes and tweets an image
def tweet_image(url, username, status_id, api):
    print("Will tweet image")
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    request = requests.get(url, stream = True)
    if request.status_code == 200:
        i = Image.open(BytesIO(request.content))
        filename = 'temp_' + uuid.uuid4() + '.jpg'
        i.save(filename)
        geometrize(filename, '')
        api.update_with_media(image_filename, status = '@{0}'.format(username), in_reply_to_status_id = status_id)
    else:
        print("Failed to download image")
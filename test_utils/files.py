from django.core.files.uploadedfile import SimpleUploadedFile

def get_image_for_upload():
    # 1px gif to use for test uploads
    small_gif = (
        b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
        b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
        b'\x02\x4c\x01\x00\x3b'
    )
    return SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')

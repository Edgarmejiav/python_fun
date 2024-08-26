
from moviepy.editor import VideoFileClip

clip = VideoFileClip('reel.mp4')
clip.write_videofile(
    'video.webm',
            codec='libvpx')

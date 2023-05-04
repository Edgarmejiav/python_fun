from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip


def split_video_into_clips(video_path, clip_length_seconds):
    """Divide un archivo de video en clips y guarda cada clip en un archivo independiente."""
    # Abrir el archivo de video
    video = VideoFileClip(video_path)

    # Calcular el número total de clips
    total_clips = int(video.duration // clip_length_seconds) + 1

    # Dividir el video en clips y guardar cada clip en un archivo independiente
    for i in range(total_clips):
        start_time = i * clip_length_seconds
        end_time = min(start_time + clip_length_seconds, video.duration)
        clip = video.subclip(start_time, end_time)
        clip_resized = CompositeVideoClip([clip.set_pos("center")], size=(clip.w, int(clip.w / 9 * 16)))
        clip_resized.write_videofile(f"./{i}.mp4")


if __name__ == '__main__':
    # Definir la ruta del archivo de video a recortar
    video_path = "./video.mp4"

    # Definir la duración de cada clip en segundos
    clip_length_seconds = 30

    # Dividir el video en clips y guardar cada clip en un archivo independiente
    split_video_into_clips(video_path, clip_length_seconds)

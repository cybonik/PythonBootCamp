from moviepy.editor import *

video = VideoFileClip(r"video.mp4")
video = video.resize(0.5)

txt = TextClip("video", font="Arial -Black",
               fontsize=75, color="white",
               stroke_color="black",
               stroke_width=5).set_position("buttom")\
    .set_duration(1)\
    .set_start(1)

video = CompositeVideoClip([video, txt])
video.write_gif(r"tiktok.gif")

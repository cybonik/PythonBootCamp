import ffmpeg


def video_to_gif():
    stream = ffmpeg.input("video.mp4")
    stream = ffmpeg.filter(stream, "fps", fps=3)
    stream = ffmpeg.output(stream, "gif.gif")
    ffmpeg.run(stream)


def main():
    video_to_gif()


if __name__ == "__main__":
    main()

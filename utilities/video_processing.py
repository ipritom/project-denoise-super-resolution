import moviepy.editor as mp

clip = mp.VideoFileClip("mountainO.mp4") # pass video path
clip_resized = clip.resize(height=480) # According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
clip_resized = clip_resized.subclip(5, 20) # set time duration
clip_resized.write_videofile("mountain480p.mp4")
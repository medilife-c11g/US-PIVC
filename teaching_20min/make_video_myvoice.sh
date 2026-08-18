#!/bin/zsh
set -e
setopt null_glob
mkdir -p seg_mv; rm -f seg_mv/*.mp4 concat_mv.txt
# figure-heavy slides get longer tail padding for reading time
typeset -A PAD
for i in 07 09 10 12 13 14 15; do PAD[$i]=3.5; done
for i in $(seq -w 1 21); do
  p=${PAD[$i]:-1.5}
  ffmpeg -y -v error -loop 1 -framerate 12 -i png/slide$i.png -i audio_myvoice/n$i.wav \
    -af "loudnorm=I=-17:TP=-1.5,apad=pad_dur=$p" -c:v libx264 -preset fast -tune stillimage -crf 22 -pix_fmt yuv420p \
    -c:a aac -b:a 128k -ar 44100 -shortest seg_mv/s$i.mp4
  echo "file 'seg_mv/s$i.mp4'" >> concat_mv.txt
done
ffmpeg -y -v error -f concat -safe 0 -i concat_mv.txt -c copy -movflags +faststart "US-PIVC_20min_teaching_我的聲音.mp4"
afinfo "US-PIVC_20min_teaching_我的聲音.mp4" | grep duration
ls -la "US-PIVC_20min_teaching_我的聲音.mp4"

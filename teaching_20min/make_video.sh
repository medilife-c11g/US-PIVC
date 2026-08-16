#!/bin/zsh
set -e
mkdir -p seg
rm -f seg/*.mp4 concat.txt
for i in $(seq -w 1 21); do
  ffmpeg -y -v error -loop 1 -framerate 12 -i png/slide$i.png -i audio/n$i.aiff \
    -af "apad=pad_dur=0.7" -c:v libx264 -preset fast -tune stillimage -crf 22 -pix_fmt yuv420p \
    -c:a aac -b:a 128k -ar 44100 -shortest seg/s$i.mp4
  echo "file 'seg/s$i.mp4'" >> concat.txt
done
ffmpeg -y -v error -f concat -safe 0 -i concat.txt -c copy -movflags +faststart US-PIVC_20min_teaching.mp4
afinfo US-PIVC_20min_teaching.mp4 2>/dev/null | grep duration || ffprobe -v error -show_entries format=duration -of csv=p=0 US-PIVC_20min_teaching.mp4
ls -la US-PIVC_20min_teaching.mp4

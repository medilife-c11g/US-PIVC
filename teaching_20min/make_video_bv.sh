#!/bin/zsh
# Assemble US-PIVC teaching video from BreezyVoice (Taiwanese-accent) segments.
# Auto-scales per-slide tail padding so the final video reaches >= 20:00.
set -e
setopt null_glob
cd /Users/chencc/Research/US-PIVC/teaching_20min

# 1) total narration duration
total=0
for i in $(seq -w 1 21); do
  d=$(afinfo audio_bv/n$i.wav | awk '/estimated duration/{print $3}')
  total=$(echo "$total + $d" | bc)
done
echo "narration total: ${total}s"

# 2) base pads (figure-heavy slides need reading time), then stretch to hit 20:03
typeset -A PAD
for i in $(seq -w 1 21); do PAD[$i]=1.5; done
for i in 07 09 10 12 13 14 15; do PAD[$i]=3.5; done
base_pad=$(echo "14*1.5 + 7*3.5" | bc)
target=1203
base_total=$(echo "$total + $base_pad" | bc)
extra=$(echo "scale=2; ($target - $base_total)/21" | bc)
if (( $(echo "$extra > 0" | bc) )); then
  echo "short of 20min by $(echo "$target - $base_total" | bc)s -> +${extra}s/slide"
  for i in $(seq -w 1 21); do PAD[$i]=$(echo "${PAD[$i]} + $extra" | bc); done
else
  echo "base assembly already >= 20min (${base_total}s), no stretch needed"
fi

# 3) build per-slide segments
mkdir -p seg_bv; rm -f seg_bv/*.mp4 concat_bv.txt
for i in $(seq -w 1 21); do
  p=${PAD[$i]}
  d=$(afinfo audio_bv/n$i.wav | awk '/estimated duration/{print $3}')
  # explicit -t (= audio + pad) avoids the -loop 1/-shortest video overshoot (~5s frozen tail/segment)
  t=$(echo "scale=3; $d + $p" | bc)
  ffmpeg -y -v error -loop 1 -framerate 12 -i png/slide$i.png -i audio_bv/n$i.wav \
    -af "loudnorm=I=-17:TP=-1.5,apad=pad_dur=$p" -c:v libx264 -preset fast -tune stillimage -crf 22 -pix_fmt yuv420p \
    -c:a aac -b:a 128k -ar 44100 -t "$t" seg_bv/s$i.mp4
  echo "file 'seg_bv/s$i.mp4'" >> concat_bv.txt
done

# 4) concat
ffmpeg -y -v error -f concat -safe 0 -i concat_bv.txt -c copy -movflags +faststart "US-PIVC_20min_teaching_台灣腔.mp4"
afinfo "US-PIVC_20min_teaching_台灣腔.mp4" | grep duration
ls -la "US-PIVC_20min_teaching_台灣腔.mp4"

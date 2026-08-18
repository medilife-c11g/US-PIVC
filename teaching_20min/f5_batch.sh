#!/bin/zsh
set -e
mkdir -p audio_myvoice
python3 - <<'PY' > /tmp/f5_texts.txt
import json
narr = json.load(open('narration.json'))
for k in sorted(narr):
    print(k + '\t' + narr[k].replace('\n',' '))
PY
while IFS=$'\t' read -r k text; do
  echo "=== segment $k ==="
  ./f5env/bin/f5-tts_infer-cli --model F5TTS_v1_Base \
    --ref_audio ref_clip.wav --ref_text "" \
    --gen_text "$text" --speed 0.92 \
    --output_dir audio_myvoice --output_file n$k.wav 2>&1 | tail -1
done < /tmp/f5_texts.txt
echo "ALL DONE"
for f in audio_myvoice/n*.wav; do afinfo "$f" | grep duration | sed "s|^|$f |"; done

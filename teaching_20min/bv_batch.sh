#!/bin/zsh
set -e
cd "$(dirname "$0")"
mkdir -p audio_bv
REF="$(pwd)/ref_clip.wav"
TRANS="大家好,我是陳家慶,急診醫學科醫師。今天想跟大家聊一聊超音波導引的周邊靜脈導管。過去十年,床邊超音波已經改變了我們處理困難靜脈的方式"
python3 - <<'PY' > /tmp/bv_texts.txt
import json
narr = json.load(open('narration.json'))
for k in sorted(narr):
    print(k + '\t' + narr[k].replace('\n',' '))
PY
cd BreezyVoice
while IFS=$'\t' read -r k text; do
  if [ -f "../audio_bv/n$k.wav" ]; then echo "skip $k"; continue; fi
  echo "=== segment $k ($(date +%H:%M)) ==="
  ./bvenv/bin/python single_inference.py \
    --content_to_synthesize "$text" \
    --speaker_prompt_audio_path "$REF" \
    --speaker_prompt_text_transcription "$TRANS" \
    --output_path "../audio_bv/n$k.wav" 2>&1 | grep -E "Generated audio length|Error" || true
done < /tmp/bv_texts.txt
echo "ALL DONE"
for f in ../audio_bv/n*.wav; do afinfo "$f" | grep duration | sed "s|^|$(basename $f) |"; done

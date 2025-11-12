# Known Issues

## Offline TTS Module (offline_tts_stt.py)

### Issue: pyttsx3 generates malformed WAV files on macOS
**Status:** Unresolved
**Severity:** Critical
**Module:** `src/ai_powered_app_voice_assistant/offline_tts_stt.py`

**Description:**
The pyttsx3 library on macOS (using NSSpeechSynthesizer backend) generates WAV files that cannot be decoded by ffmpeg or pydub. This prevents the conversion from WAV to MP3 format needed for browser compatibility.

**Error Messages:**
```
[in#0 @ 0x13cf04370] Error opening input: Invalid data found when processing input
Error opening input file /var/folders/.../tmpxyuq0ebn.wav.
Error opening input files: Invalid data found when processing input
```

```python
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183
```

**Technical Details:**
- pyttsx3.save_to_file() creates a WAV file
- The WAV file has content (size > 0) but is malformed
- ffmpeg cannot process the file format
- This is a known issue with pyttsx3's NSSpeechSynthesizer backend on macOS

**Attempted Solutions:**
1. Added retry logic with delays - Failed (file is created but still malformed)
2. Validated file size and existence - Failed (validation passes but file is still invalid)
3. Installed audioop-lts for Python 3.13 compatibility - Successful installation but doesn't fix WAV format issue

**Current Workaround:**
Use the semi-offline module (`semioffline_tts_stt.py`) which uses:
- Whisper for STT (offline)
- gTTS for TTS (online, generates proper MP3)

**Potential Solutions:**
1. Use macOS native `say` command instead of pyttsx3 (generates proper AIFF files that can be converted)
2. Switch to a different TTS library compatible with macOS
3. Accept that fully offline TTS on macOS requires alternative approaches
4. Use the semi-offline version as the default for macOS systems

**Files Affected:**
- `src/ai_powered_app_voice_assistant/offline_tts_stt.py` (lines 39-131)
- `src/worker.py` (currently imports from offline_tts_stt)

**Related Dependencies:**
- pyttsx3 (>=2.90,<3.0)
- pydub (>=0.25.1,<1.0.0)
- audioop-lts (>=0.2.0,<1.0.0)
- ffmpeg (system dependency)

**Date Reported:** 2025-11-12
**Platform:** macOS (Darwin 24.5.0)
**Python Version:** 3.13

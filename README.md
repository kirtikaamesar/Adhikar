# Adhikar
Adhikar turns complex government schemes into simple personalized opportunity for every citizen.
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Adhikar – अधिकार | India Scheme Finder</title>
<link href="https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Hindi&family=Yatra+One&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<style>
:root {
  --saffron: #FF9933;
  --saffron-dim: rgba(255,153,51,0.15);
  --saffron-glow: rgba(255,153,51,0.35);
  --green: #138808;
  --green2: #22c55e;
  --navy: #000080;
  --bg: #080d14;
  --bg2: #0f1623;
  --bg3: #16202e;
  --card: #111a28;
  --border: rgba(255,153,51,0.18);
  --border-sub: rgba(255,255,255,0.05);
  --text: #dde4f0;
  --muted: #7a8898;
  --white: #ffffff;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'DM Sans', sans-serif;
  background: var(--bg);
  color: var(--text);
  height: 100vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

/* Tricolor top bar */
.tricolor-bar {
  height: 3px;
  background: linear-gradient(90deg, var(--saffron) 33.33%, #fff 33.33% 66.66%, var(--green) 66.66%);
  flex-shrink: 0;
}

/* Background */
body::before {
  content: '';
  position: fixed; inset: 0;
  background:
    radial-gradient(ellipse 60% 40% at 10% 5%, rgba(255,153,51,0.08) 0%, transparent 55%),
    radial-gradient(ellipse 50% 35% at 90% 95%, rgba(19,136,8,0.07) 0%, transparent 50%),
    url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.013'%3E%3Ccircle cx='30' cy='30' r='1'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
  pointer-events: none; z-index: 0;
}

/* === HEADER === */
header {
  position: relative; z-index: 20;
  padding: 0 28px;
  height: 64px;
  display: flex; align-items: center; gap: 14px;
  border-bottom: 1px solid var(--border);
  background: rgba(8,13,20,0.95);
  backdrop-filter: blur(20px);
  flex-shrink: 0;
}

.logo-wrap {
  display: flex; align-items: center; gap: 12px;
  text-decoration: none;
}

.logo-emblem {
  width: 40px; height: 40px;
  background: linear-gradient(135deg, var(--saffron) 0%, #c47300 100%);
  border-radius: 10px;
  display: grid; place-items: center;
  font-size: 20px;
  box-shadow: 0 0 16px var(--saffron-glow);
  flex-shrink: 0;
}

.logo-text { line-height: 1; }
.logo-text .name {
  font-family: 'Yatra One', cursive;
  font-size: 1.35rem;
  color: var(--white);
  letter-spacing: 0.02em;
  background: linear-gradient(135deg, var(--saffron), #ffe0a0, var(--green2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.logo-text .tagline {
  font-size: 0.6rem;
  color: var(--muted);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-top: 1px;
  -webkit-text-fill-color: var(--muted);
}

.header-right {
  margin-left: auto;
  display: flex; align-items: center; gap: 10px;
}

/* Language detected badge */
#langDetectedBadge {
  padding: 5px 12px;
  border-radius: 20px;
  background: rgba(34,197,94,0.1);
  border: 1px solid rgba(34,197,94,0.3);
  font-size: 0.68rem;
  color: var(--green2);
  display: none; align-items: center; gap: 5px;
  animation: fadeIn 0.3s ease;
}

#langDetectedBadge.visible { display: flex; }

@keyframes fadeIn { from { opacity: 0; transform: scale(0.9); } to { opacity: 1; transform: scale(1); } }

.lang-select-wrap {
  display: flex; align-items: center; gap: 6px;
}
.lang-select-wrap label {
  font-size: 0.65rem; color: var(--muted);
  text-transform: uppercase; letter-spacing: 0.08em;
}
#langSelect {
  background: var(--bg3);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--saffron);
  padding: 5px 10px;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.78rem;
  cursor: pointer; outline: none;
}
#langSelect:focus { border-color: var(--saffron); }

.live-dot {
  width: 6px; height: 6px;
  background: var(--green2);
  border-radius: 50%;
  animation: pulse 2s infinite;
}

@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.3;transform:scale(0.6)} }

/* Progress */
.progress-bar { height: 2px; background: rgba(255,255,255,0.04); flex-shrink: 0; position: relative; z-index: 5; }
.progress-fill { height: 100%; background: linear-gradient(90deg, var(--saffron), #fff 50%, var(--green2)); transition: width 0.7s cubic-bezier(.4,0,.2,1); }

/* === LAYOUT === */
main { flex: 1; display: flex; overflow: hidden; position: relative; z-index: 5; }

/* === SIDEBAR === */
.sidebar {
  width: 230px; flex-shrink: 0;
  border-right: 1px solid var(--border-sub);
  background: rgba(8,13,20,0.6);
  display: flex; flex-direction: column;
  overflow-y: auto;
}

.sidebar::-webkit-scrollbar { width: 2px; }
.sidebar::-webkit-scrollbar-thumb { background: var(--border); }

.sb-section { padding: 16px 14px; border-bottom: 1px solid var(--border-sub); }
.sb-section h3 {
  font-size: 0.58rem; text-transform: uppercase;
  letter-spacing: 0.12em; color: var(--muted);
  font-weight: 600; margin-bottom: 10px;
}

.profile-row { margin-bottom: 9px; }
.profile-row:last-child { margin-bottom: 0; }
.pr-label { font-size: 0.6rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.06em; }
.pr-value { font-size: 0.8rem; color: var(--text); font-weight: 500; min-height: 15px; margin-top: 1px; transition: color 0.3s; }
.pr-value.set { color: var(--saffron); }

.info-box {
  background: var(--saffron-dim);
  border: 1px solid var(--border);
  border-radius: 8px; padding: 10px 12px;
  font-size: 0.72rem; color: var(--muted); line-height: 1.6;
}
.info-box strong { color: var(--saffron); }

.lang-chips { display: flex; flex-wrap: wrap; gap: 4px; margin-top: 6px; }
.lang-chip {
  padding: 2px 8px; border-radius: 10px; font-size: 0.6rem;
  background: rgba(19,136,8,0.12); border: 1px solid rgba(19,136,8,0.25);
  color: var(--green2); cursor: default;
}

/* Voice indicator in sidebar */
.voice-status {
  display: flex; align-items: center; gap: 8px;
  padding: 8px 10px;
  border-radius: 8px;
  background: rgba(255,153,51,0.05);
  border: 1px solid var(--border);
  font-size: 0.72rem; color: var(--muted);
  transition: all 0.3s;
}
.voice-status.recording {
  background: rgba(255,60,60,0.1);
  border-color: rgba(255,60,60,0.4);
  color: #ff6b6b;
}
.voice-status .vs-icon { font-size: 14px; }
.voice-status .vs-text { flex: 1; }

/* === CHAT === */
.chat-area { flex: 1; display: flex; flex-direction: column; overflow: hidden; }

.messages {
  flex: 1; overflow-y: auto;
  padding: 22px 28px;
  display: flex; flex-direction: column; gap: 16px;
  scroll-behavior: smooth;
}
.messages::-webkit-scrollbar { width: 3px; }
.messages::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }

.message {
  display: flex; gap: 10px;
  max-width: 88%;
  animation: msgIn 0.35s cubic-bezier(.4,0,.2,1);
}
@keyframes msgIn { from { opacity:0; transform: translateY(12px) scale(0.97); } to { opacity:1; transform: translateY(0) scale(1); } }

.message.user { align-self: flex-end; flex-direction: row-reverse; }

.av {
  width: 32px; height: 32px; border-radius: 50%;
  display: grid; place-items: center;
  font-size: 14px; flex-shrink: 0; margin-top: 3px;
}
.bot .av { background: linear-gradient(135deg, #1a2a50, #0a0f1e); border: 1px solid var(--border); }
.user .av { background: linear-gradient(135deg, var(--saffron), #c47300); }

.bubble {
  padding: 11px 15px;
  border-radius: 16px;
  font-size: 0.845rem; line-height: 1.7;
  max-width: 100%;
}
.bot .bubble {
  background: var(--card);
  border: 1px solid var(--border-sub);
  border-top-left-radius: 4px;
  color: var(--text);
}
.user .bubble {
  background: linear-gradient(135deg, var(--saffron), #c47300);
  color: #fff; font-weight: 500;
  border-top-right-radius: 4px;
}

/* Voice transcription label */
.voice-label {
  font-size: 0.62rem; color: var(--muted);
  display: flex; align-items: center; gap: 4px;
  margin-bottom: 4px;
}

/* Quick options */
.options-wrap { display: flex; flex-wrap: wrap; gap: 7px; margin-top: 10px; }

.opt-btn {
  padding: 7px 14px; border-radius: 20px;
  border: 1px solid var(--border);
  background: rgba(255,153,51,0.05);
  color: #ffb84d;
  font-size: 0.76rem; font-family: 'DM Sans', sans-serif;
  cursor: pointer; transition: all 0.18s;
  font-weight: 500;
}
.opt-btn:hover {
  background: var(--saffron); color: #fff;
  border-color: var(--saffron);
  transform: translateY(-1px);
  box-shadow: 0 4px 14px var(--saffron-glow);
}
.opt-btn:disabled { opacity: 0.4; cursor: not-allowed; transform: none; }

/* Scheme cards */
.schemes-grid { display: flex; flex-direction: column; gap: 9px; margin-top: 10px; }

.scheme-card {
  background: rgba(255,255,255,0.025);
  border: 1px solid rgba(255,153,51,0.2);
  border-left: 3px solid var(--saffron);
  border-radius: 10px; padding: 13px 14px;
  transition: background 0.2s, border-color 0.2s;
}
.scheme-card:hover { background: rgba(255,153,51,0.04); }

.sc-name {
  font-family: 'Yatra One', cursive;
  font-size: 0.95rem; color: #ffcc66;
  margin-bottom: 5px;
}
.sc-tags { display: flex; flex-wrap: wrap; gap: 4px; margin-bottom: 7px; }
.stag {
  padding: 2px 8px; border-radius: 10px;
  font-size: 0.6rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.04em;
}
.stag.o { background: rgba(255,153,51,0.15); color: #ffb347; border: 1px solid rgba(255,153,51,0.25); }
.stag.g { background: rgba(34,197,94,0.12); color: #4ade80; border: 1px solid rgba(34,197,94,0.25); }
.stag.b { background: rgba(96,165,250,0.12); color: #93c5fd; border: 1px solid rgba(96,165,250,0.25); }

.sc-desc { font-size: 0.76rem; color: var(--muted); line-height: 1.6; margin-bottom: 5px; }
.sc-benefit { font-size: 0.76rem; color: #86efac; margin-bottom: 3px; }
.sc-why { font-size: 0.76rem; color: #fde68a; margin-bottom: 9px; }

.apply-link {
  display: inline-flex; align-items: center; gap: 5px;
  padding: 5px 13px;
  background: linear-gradient(135deg, var(--saffron), #c47300);
  color: #fff; border-radius: 6px;
  font-size: 0.7rem; font-weight: 600;
  text-decoration: none; transition: opacity 0.2s;
  letter-spacing: 0.03em;
}
.apply-link:hover { opacity: 0.85; }

/* Typing indicator */
.typing-ind {
  display: flex; gap: 4px; align-items: center;
  padding: 11px 14px;
  background: var(--card);
  border: 1px solid var(--border-sub);
  border-radius: 16px; border-top-left-radius: 4px;
  width: fit-content;
}
.typing-ind span {
  width: 5px; height: 5px;
  background: var(--muted); border-radius: 50%;
  animation: bounce 1.2s infinite;
}
.typing-ind span:nth-child(2) { animation-delay: 0.2s; }
.typing-ind span:nth-child(3) { animation-delay: 0.4s; }
@keyframes bounce { 0%,60%,100%{transform:translateY(0)} 30%{transform:translateY(-6px)} }

/* === INPUT AREA === */
.input-area {
  padding: 14px 28px;
  border-top: 1px solid var(--border-sub);
  background: rgba(8,13,20,0.95);
  backdrop-filter: blur(16px);
  display: flex; gap: 8px; align-items: flex-end;
  flex-shrink: 0;
}

.input-wrap {
  flex: 1; background: var(--bg3);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 12px;
  display: flex; align-items: center; gap: 8px;
  padding: 9px 14px; transition: border-color 0.2s;
}
.input-wrap:focus-within { border-color: var(--saffron); box-shadow: 0 0 0 3px rgba(255,153,51,0.08); }

#userInput {
  flex: 1; background: transparent;
  border: none; outline: none;
  color: var(--text);
  font-family: 'DM Sans', sans-serif;
  font-size: 0.845rem; resize: none;
  max-height: 80px; line-height: 1.5;
}
#userInput::placeholder { color: var(--muted); }

/* Voice button */
.voice-btn {
  width: 34px; height: 34px; border-radius: 50%;
  border: 1px solid var(--border);
  background: transparent;
  display: grid; place-items: center;
  cursor: pointer; flex-shrink: 0;
  transition: all 0.2s;
  color: var(--muted);
  font-size: 16px;
  position: relative;
}
.voice-btn:hover { border-color: var(--saffron); color: var(--saffron); background: var(--saffron-dim); }
.voice-btn.recording {
  border-color: #ff4444;
  background: rgba(255,68,68,0.15);
  color: #ff6b6b;
  animation: voicePulse 1s infinite;
}
@keyframes voicePulse {
  0%,100% { box-shadow: 0 0 0 0 rgba(255,68,68,0.4); }
  50% { box-shadow: 0 0 0 8px rgba(255,68,68,0); }
}

/* Waveform ring */
.voice-btn.recording::before {
  content: '';
  position: absolute;
  inset: -4px;
  border-radius: 50%;
  border: 1px solid rgba(255,68,68,0.3);
  animation: ringExpand 1s infinite;
}
@keyframes ringExpand {
  0% { transform: scale(1); opacity: 0.8; }
  100% { transform: scale(1.5); opacity: 0; }
}

.send-btn {
  width: 42px; height: 42px;
  background: linear-gradient(135deg, var(--saffron), #c47300);
  border: none; border-radius: 10px;
  cursor: pointer; display: grid; place-items: center;
  flex-shrink: 0; color: white; font-size: 16px;
  transition: transform 0.15s, opacity 0.15s;
  box-shadow: 0 4px 12px rgba(255,153,51,0.3);
}
.send-btn:hover { transform: scale(1.05); }
.send-btn:active { transform: scale(0.95); }
.send-btn:disabled { opacity: 0.3; cursor: not-allowed; transform: none; }

/* Voice modal overlay */
.voice-overlay {
  position: fixed; inset: 0;
  background: rgba(0,0,0,0.85);
  backdrop-filter: blur(8px);
  z-index: 100;
  display: none; place-items: center;
  flex-direction: column; gap: 24px;
}
.voice-overlay.active { display: flex; }

.voice-modal {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 40px;
  text-align: center;
  max-width: 360px; width: 90%;
  box-shadow: 0 20px 60px rgba(0,0,0,0.5), 0 0 40px rgba(255,153,51,0.1);
}

.voice-orb {
  width: 100px; height: 100px;
  margin: 0 auto 24px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(255,153,51,0.3) 0%, rgba(255,153,51,0.05) 70%, transparent 100%);
  border: 2px solid var(--saffron);
  display: grid; place-items: center;
  font-size: 42px;
  position: relative;
  animation: orbIdle 3s infinite ease-in-out;
}

.voice-orb.listening {
  animation: orbListen 0.5s infinite alternate ease-in-out;
  border-color: #ff4444;
  background: radial-gradient(circle, rgba(255,68,68,0.25) 0%, rgba(255,68,68,0.05) 70%, transparent 100%);
}

@keyframes orbIdle {
  0%,100% { transform: scale(1); box-shadow: 0 0 20px rgba(255,153,51,0.2); }
  50% { transform: scale(1.04); box-shadow: 0 0 40px rgba(255,153,51,0.35); }
}

@keyframes orbListen {
  0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255,68,68,0.5); }
  100% { transform: scale(1.08); box-shadow: 0 0 0 16px rgba(255,68,68,0); }
}

.voice-orb-rings {
  position: absolute; inset: -16px;
  border-radius: 50%;
  border: 1px solid rgba(255,153,51,0.15);
  animation: ringGrow 2s infinite;
}
.voice-orb-rings:nth-child(2) { inset: -28px; animation-delay: 0.5s; }

@keyframes ringGrow {
  0% { transform: scale(0.8); opacity: 0; }
  50% { opacity: 1; }
  100% { transform: scale(1.1); opacity: 0; }
}

.vm-title {
  font-family: 'Yatra One', cursive;
  font-size: 1.4rem; color: var(--white);
  margin-bottom: 6px;
}

.vm-subtitle { font-size: 0.82rem; color: var(--muted); margin-bottom: 20px; line-height: 1.5; }

/* Waveform bars */
.waveform {
  display: flex; align-items: center; justify-content: center;
  gap: 3px; height: 40px; margin-bottom: 20px;
}
.wave-bar {
  width: 3px; border-radius: 3px;
  background: var(--saffron);
  opacity: 0.4;
  transition: height 0.1s ease;
}
.waveform.active .wave-bar {
  animation: waveDance 0.8s infinite alternate;
  opacity: 0.9;
}
.wave-bar:nth-child(1) { animation-delay: 0s; }
.wave-bar:nth-child(2) { animation-delay: 0.1s; }
.wave-bar:nth-child(3) { animation-delay: 0.2s; }
.wave-bar:nth-child(4) { animation-delay: 0.3s; }
.wave-bar:nth-child(5) { animation-delay: 0.15s; }
.wave-bar:nth-child(6) { animation-delay: 0.25s; }
.wave-bar:nth-child(7) { animation-delay: 0.05s; }
.wave-bar:nth-child(8) { animation-delay: 0.35s; }
.wave-bar:nth-child(9) { animation-delay: 0.1s; }
@keyframes waveDance {
  from { height: 4px; }
  to { height: 32px; }
}

#vmTranscript {
  background: var(--bg);
  border: 1px solid var(--border-sub);
  border-radius: 10px;
  padding: 10px 14px;
  font-size: 0.82rem; color: var(--text);
  min-height: 48px; text-align: left;
  margin-bottom: 16px; line-height: 1.6;
  font-style: italic; color: var(--muted);
}

#vmLangDetected {
  font-size: 0.72rem; color: var(--green2);
  margin-bottom: 14px; min-height: 18px;
  display: flex; align-items: center; justify-content: center; gap: 6px;
}

.vm-actions { display: flex; gap: 10px; justify-content: center; }

.vm-btn {
  padding: 9px 22px; border-radius: 10px;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.8rem; font-weight: 600;
  cursor: pointer; transition: all 0.2s; border: none;
}

.vm-btn.primary {
  background: linear-gradient(135deg, var(--saffron), #c47300);
  color: white;
  box-shadow: 0 4px 12px rgba(255,153,51,0.3);
}
.vm-btn.primary:hover { opacity: 0.9; transform: translateY(-1px); }

.vm-btn.secondary {
  background: var(--bg3); color: var(--muted);
  border: 1px solid var(--border-sub);
}
.vm-btn.secondary:hover { color: var(--text); border-color: var(--border); }

/* Responsive */
@media (max-width: 700px) {
  .sidebar { display: none; }
  .messages { padding: 14px; }
  .input-area { padding: 10px 14px; }
  header { padding: 0 14px; }
}
</style>
</head>
<body>

<div class="tricolor-bar"></div>

<!-- Voice Overlay Modal -->
<div class="voice-overlay" id="voiceOverlay">
  <div class="voice-modal">
    <div class="voice-orb" id="voiceOrb">
      🎙️
      <div class="voice-orb-rings"></div>
      <div class="voice-orb-rings"></div>
    </div>
    <div class="vm-title">बोलिए / Speak</div>
    <div class="vm-subtitle" id="vmStatus">Tap the mic and speak in any Indian language. Adhikar will understand you.</div>

    <div class="waveform" id="waveform">
      <div class="wave-bar" style="height:8px"></div>
      <div class="wave-bar" style="height:16px"></div>
      <div class="wave-bar" style="height:12px"></div>
      <div class="wave-bar" style="height:24px"></div>
      <div class="wave-bar" style="height:10px"></div>
      <div class="wave-bar" style="height:20px"></div>
      <div class="wave-bar" style="height:14px"></div>
      <div class="wave-bar" style="height:18px"></div>
      <div class="wave-bar" style="height:8px"></div>
    </div>

    <div id="vmTranscript">Waiting for your voice…</div>
    <div id="vmLangDetected"></div>

    <div class="vm-actions">
      <button class="vm-btn primary" id="vmMicBtn" onclick="toggleVoiceRecording()">🎙️ Start Speaking</button>
      <button class="vm-btn secondary" id="vmSendBtn" onclick="stopAndSend()" style="display:none">✅ Send</button>
      <button class="vm-btn secondary" onclick="closeVoiceModal()">✕ Cancel</button>
    </div>
  </div>
</div>

<header>
  <div class="logo-wrap">
    <div class="logo-emblem">⚖️</div>
    <div class="logo-text">
      <div class="name">Adhikar</div>
      <div class="tagline">अधिकार · India Scheme Finder · AI Powered</div>
    </div>
  </div>
  <div class="header-right">
    <div id="langDetectedBadge">
      <div class="live-dot"></div>
      <span id="langDetectedText">Language detected</span>
    </div>
    <div class="lang-select-wrap">
      <label>UI Lang</label>
      <select id="langSelect" onchange="changeLanguage(this.value)">
        <option value="en">English</option>
        <option value="hi">हिन्दी</option>
        <option value="bn">বাংলা</option>
        <option value="te">తెలుగు</option>
        <option value="mr">मराठी</option>
        <option value="ta">தமிழ்</option>
        <option value="gu">ગુજરાતી</option>
        <option value="kn">ಕನ್ನಡ</option>
        <option value="ml">മലയാളം</option>
        <option value="pa">ਪੰਜਾਬੀ</option>
        <option value="or">ଓଡ଼ିଆ</option>
      </select>
    </div>
    <div style="display:flex;align-items:center;gap:5px;font-size:0.68rem;color:var(--muted);">
      <div class="live-dot"></div> Active
    </div>
  </div>
</header>

<div class="progress-bar">
  <div class="progress-fill" id="progressFill" style="width:0%"></div>
</div>

<main>
  <div class="sidebar">
    <div class="sb-section">
      <h3>Your Profile</h3>
      <div class="profile-row"><div class="pr-label">State</div><div class="pr-value" id="pState">—</div></div>
      <div class="profile-row"><div class="pr-label">Age</div><div class="pr-value" id="pAge">—</div></div>
      <div class="profile-row"><div class="pr-label">Gender</div><div class="pr-value" id="pGender">—</div></div>
      <div class="profile-row"><div class="pr-label">Occupation</div><div class="pr-value" id="pOcc">—</div></div>
      <div class="profile-row"><div class="pr-label">Category</div><div class="pr-value" id="pCat">—</div></div>
      <div class="profile-row"><div class="pr-label">Qualification</div><div class="pr-value" id="pQual">—</div></div>
      <div class="profile-row"><div class="pr-label">Annual Income</div><div class="pr-value" id="pIncome">—</div></div>
      <div class="profile-row"><div class="pr-label">Marital Status</div><div class="pr-value" id="pMarital">—</div></div>
    </div>
    <div class="sb-section">
      <h3>Voice Status</h3>
      <div class="voice-status" id="voiceStatusCard">
        <span class="vs-icon">🎙️</span>
        <span class="vs-text">Click mic to speak</span>
      </div>
    </div>
    <div class="sb-section">
      <h3>Languages Supported</h3>
      <div class="lang-chips">
        <span class="lang-chip">English</span>
        <span class="lang-chip">हिन्दी</span>
        <span class="lang-chip">বাংলা</span>
        <span class="lang-chip">తెలుగు</span>
        <span class="lang-chip">मराठी</span>
        <span class="lang-chip">தமிழ்</span>
        <span class="lang-chip">ગુજરાતી</span>
        <span class="lang-chip">ಕನ್ನಡ</span>
        <span class="lang-chip">മലയാളം</span>
        <span class="lang-chip">ਪੰਜਾਬੀ</span>
        <span class="lang-chip">ଓଡ଼ିଆ</span>
      </div>
    </div>
    <div class="sb-section">
      <div class="info-box">
        <strong>Adhikar</strong> (अधिकार) means "Right" in Hindi. We help every Indian citizen know and claim their rights through government schemes.
      </div>
    </div>
  </div>

  <div class="chat-area">
    <div class="messages" id="messages"></div>
    <div class="input-area">
      <div class="input-wrap">
        <button class="voice-btn" id="inlineVoiceBtn" title="Speak" onclick="openVoiceModal()">🎙️</button>
        <textarea id="userInput" placeholder="Type or speak your answer…" rows="1"></textarea>
      </div>
      <button class="send-btn" id="sendBtn" onclick="sendMessage()" title="Send">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <line x1="22" y1="2" x2="11" y2="13"></line>
          <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
        </svg>
      </button>
    </div>
  </div>
</main>

<script>
const API_URL = "https://api.anthropic.com/v1/messages";

const LANG_NAMES = {
  en: "English", hi: "Hindi (हिन्दी)", bn: "Bengali (বাংলা)",
  te: "Telugu (తెలుగు)", mr: "Marathi (मराठी)", ta: "Tamil (தமிழ்)",
  gu: "Gujarati (ગુજરાતી)", kn: "Kannada (ಕನ್ನಡ)", ml: "Malayalam (മലയാളം)",
  pa: "Punjabi (ਪੰਜਾਬੀ)", or: "Odia (ଓଡ଼ିଆ)"
};

// Web Speech API lang codes
const LANG_CODES = {
  en: "en-IN", hi: "hi-IN", bn: "bn-IN", te: "te-IN", mr: "mr-IN",
  ta: "ta-IN", gu: "gu-IN", kn: "kn-IN", ml: "ml-IN", pa: "pa-IN", or: "or-IN"
};

// Recognition language detection map
const DETECT_MAP = {
  "hi": "हिन्दी (Hindi)", "bn": "বাংলা (Bengali)", "te": "తెలుగు (Telugu)",
  "mr": "मराठी (Marathi)", "ta": "தமிழ் (Tamil)", "gu": "ગુજરાતી (Gujarati)",
  "kn": "ಕನ್ನಡ (Kannada)", "ml": "മലയാളം (Malayalam)", "pa": "ਪੰਜਾਬੀ (Punjabi)",
  "or": "ଓଡ଼ିଆ (Odia)", "en": "English"
};

let currentLang = "en";
let conversationHistory = [];
let userProfile = {};
let isWaiting = false;

// Speech Recognition state (managed by voice functions below)
let isRecording = false;   // legacy compat
let finalTranscript = "";  // legacy compat
let detectedLang = null;

const SYSTEM_PROMPT = `You are "Adhikar" (अधिकार), a compassionate and knowledgeable AI assistant helping Indian citizens discover government schemes they are eligible for. Adhikar means "Right" — you help people claim what is rightfully theirs.

LANGUAGE RULE: Always respond in {LANG}. Use the native script. Be warm, respectful, and use simple everyday language appropriate for that language.

YOUR CONVERSATION FLOW:
- Ask ONE question at a time to collect: state/UT, age, gender, occupation/livelihood, social category (General/OBC/SC/ST/NT), educational qualification, annual family income, marital status, whether they have BPL/Ration card, disability status, land/property ownership, whether they are a farmer.
- Keep the conversation warm and natural, like a helpful government officer speaking to a citizen.
- After 8-10 questions when you have enough info, generate scheme recommendations.

MANDATORY FORMAT — Every bot response MUST include all applicable tags:

1. Profile update (always include if new info received, at start):
[PROFILE: state="..." age="..." gender="..." occupation="..." category="..." qualification="..." income="..." marital="..."]

2. Quick options (ALWAYS at the end of EVERY message):
[OPTIONS: Option 1 | Option 2 | Option 3 | Option 4 | Option 5]
Options should be specific answers to the question you just asked. For states: list major states. For income: use ranges like "Below ₹1 Lakh | ₹1-2.5 Lakh | ₹2.5-5 Lakh | Above ₹5 Lakh". For gender: Male | Female | Transgender. Always give 4-6 options plus "Other/Skip".

3. For scheme results, format each scheme as:
[SCHEME]
name: Full Official Scheme Name
ministry: Ministry or Department
category: Agriculture | Housing | Education | Health | Women | Youth | Business | Pension | Disability | Farmers
description: What this scheme is about
benefit: Specific benefit amount or what they receive
eligibility_match: Exactly why this user qualifies based on their profile
apply_url: https://official-portal.gov.in
[/SCHEME]

List 10-15 relevant Central + State schemes. Be thorough. Include PM Awas Yojana, PM Kisan, Ayushman Bharat, PM Jan Dhan, Sukanya Samriddhi, etc. when applicable.

After all schemes, add an encouraging closing message in the chosen language, then:
[OPTIONS: Find More Schemes | Check State-Specific Schemes | Start Over | Help with Application]`;

function getSystemPrompt() {
  return SYSTEM_PROMPT.replace("{LANG}", LANG_NAMES[currentLang] || "English");
}

// ===== PROFILE =====
function updateProfile(data) {
  const map = { state:"pState", age:"pAge", gender:"pGender", occupation:"pOcc", category:"pCat", qualification:"pQual", income:"pIncome", marital:"pMarital" };
  let filled = 0;
  for (const [key, id] of Object.entries(map)) {
    if (data[key] && data[key] !== "" && data[key] !== "unknown") {
      const el = document.getElementById(id);
      if (el) { el.textContent = data[key]; el.classList.add("set"); }
      userProfile[key] = data[key];
    }
    if (userProfile[key]) filled++;
  }
  const pct = Math.min((filled / 8) * 80, 80);
  document.getElementById("progressFill").style.width = pct + "%";
}

// ===== PARSE RESPONSE =====
function parseProfile(t) {
  const m = t.match(/\[PROFILE:\s*([^\]]+)\]/);
  if (!m) return null;
  const d = {};
  for (const p of m[1].matchAll(/(\w+)="([^"]*)"/g)) d[p[1]] = p[2];
  return d;
}

function parseOptions(t) {
  const m = t.match(/\[OPTIONS:\s*([^\]]+)\]/);
  if (!m) return [];
  return m[1].split("|").map(s => s.trim()).filter(Boolean);
}

function parseSchemes(t) {
  const schemes = []; const re = /\[SCHEME\]([\s\S]*?)\[\/SCHEME\]/g; let m;
  while ((m = re.exec(t)) !== null) {
    const b = m[1];
    const g = k => { const r = b.match(new RegExp(k + ":\\s*(.+)")); return r ? r[1].trim() : ""; };
    schemes.push({ name:g("name"), ministry:g("ministry"), category:g("category"), description:g("description"), benefit:g("benefit"), eligibility_match:g("eligibility_match"), apply_url:g("apply_url") });
  }
  return schemes;
}

function renderScheme(s) {
  return `<div class="scheme-card">
    <div class="sc-name">🏅 ${s.name}</div>
    <div class="sc-tags">
      <span class="stag o">📂 ${s.category}</span>
      <span class="stag b">🏛️ ${s.ministry}</span>
    </div>
    <div class="sc-desc">${s.description}</div>
    <div class="sc-benefit">✅ <strong>Benefit:</strong> ${s.benefit}</div>
    <div class="sc-why">🎯 <strong>Why you qualify:</strong> ${s.eligibility_match}</div>
    <a href="${s.apply_url}" target="_blank" class="apply-link">Apply Now ↗</a>
  </div>`;
}

function processResponse(raw, isVoice = false) {
  const profile = parseProfile(raw);
  if (profile) updateProfile(profile);

  const options = parseOptions(raw);
  const schemes = parseSchemes(raw);

  let clean = raw
    .replace(/\[PROFILE:[^\]]*\]/g, "")
    .replace(/\[OPTIONS:[^\]]*\]/g, "")
    .replace(/\[SCHEME\][\s\S]*?\[\/SCHEME\]/g, "")
    .trim();

  let html = "";

  if (isVoice) {
    html += `<div class="voice-label">🎙️ Voice response</div>`;
  }

  if (clean) html += `<div>${clean.replace(/\n/g, "<br>")}</div>`;

  if (schemes.length > 0) {
    document.getElementById("progressFill").style.width = "100%";
    html += `<div class="schemes-grid">${schemes.map(renderScheme).join("")}</div>`;
  }

  if (options.length > 0) {
    const btns = options.map(o =>
      `<button class="opt-btn" onclick="selectOption(this,'${o.replace(/'/g, "\\'")}')">${o}</button>`
    ).join("");
    html += `<div class="options-wrap">${btns}</div>`;
  }

  // Speak response if last input was voice
  if (isVoice && clean) speakText(clean);

  return html;
}

// ===== MESSAGES =====
function addMsg(role, content, isHTML = true) {
  const msgs = document.getElementById("messages");
  const wrap = document.createElement("div");
  wrap.className = `message ${role}`;
  const av = document.createElement("div");
  av.className = "av";
  av.textContent = role === "bot" ? "⚖️" : "👤";
  const bub = document.createElement("div");
  bub.className = "bubble";
  if (isHTML) bub.innerHTML = content; else bub.textContent = content;
  wrap.appendChild(av); wrap.appendChild(bub);
  msgs.appendChild(wrap);
  msgs.scrollTop = msgs.scrollHeight;
}

function showTyping() {
  const msgs = document.getElementById("messages");
  const wrap = document.createElement("div");
  wrap.className = "message bot"; wrap.id = "typing-wrap";
  const av = document.createElement("div"); av.className = "av"; av.textContent = "⚖️";
  const ind = document.createElement("div"); ind.className = "typing-ind";
  ind.innerHTML = "<span></span><span></span><span></span>";
  wrap.appendChild(av); wrap.appendChild(ind);
  msgs.appendChild(wrap);
  msgs.scrollTop = msgs.scrollHeight;
}

function removeTyping() {
  document.getElementById("typing-wrap")?.remove();
}

// ===== SEND =====
let lastInputWasVoice = false;

async function sendToAPI(text) {
  conversationHistory.push({ role: "user", content: text });
  const res = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      model: "claude-sonnet-4-20250514",
      max_tokens: 4000,
      system: getSystemPrompt(),
      messages: conversationHistory
    })
  });
  const data = await res.json();
  const reply = data.content[0].text;
  conversationHistory.push({ role: "assistant", content: reply });
  return reply;
}

async function sendMessage(text = null, isVoice = false) {
  const input = document.getElementById("userInput");
  const msg = text || input.value.trim();
  if (!msg || isWaiting) return;
  input.value = ""; input.style.height = "auto";
  isWaiting = true;
  document.getElementById("sendBtn").disabled = true;

  if (isVoice) {
    addMsg("user", `<div class="voice-label">🎙️ Voice input</div>${msg}`, true);
  } else {
    addMsg("user", msg, false);
  }
  showTyping();

  try {
    const reply = await sendToAPI(msg);
    removeTyping();
    addMsg("bot", processResponse(reply, isVoice), true);
  } catch (e) {
    removeTyping();
    addMsg("bot", "⚠️ Connection issue. Please try again.", false);
  }

  isWaiting = false;
  document.getElementById("sendBtn").disabled = false;
  input.focus();
}

function selectOption(btn, val) {
  btn.closest(".options-wrap")?.querySelectorAll(".opt-btn").forEach(b => b.disabled = true);
  document.getElementById("userInput").value = val;
  sendMessage();
}

// ===== LANGUAGE =====
async function changeLanguage(lang) {
  currentLang = lang;
  if (conversationHistory.length === 0) return;
  const note = `The user has switched to ${LANG_NAMES[lang]}. Please continue in ${LANG_NAMES[lang]} from now on, using native script. Briefly acknowledge the switch and re-ask the last question in the new language. Always include [OPTIONS:...] at the end.`;
  isWaiting = true;
  document.getElementById("sendBtn").disabled = true;
  showTyping();
  try {
    const reply = await sendToAPI(note);
    removeTyping();
    addMsg("bot", processResponse(reply), true);
  } catch(e) { removeTyping(); }
  isWaiting = false;
  document.getElementById("sendBtn").disabled = false;
}

// ===== TEXT TO SPEECH =====
function speakText(text) {
  if (!window.speechSynthesis) return;
  window.speechSynthesis.cancel();
  const clean = text.replace(/<[^>]*>/g, "").replace(/\[.*?\]/g, "").trim().slice(0, 300);
  const utt = new SpeechSynthesisUtterance(clean);
  utt.lang = LANG_CODES[currentLang] || "en-IN";
  utt.rate = 0.9;
  window.speechSynthesis.speak(utt);
}

// ===== VOICE RECOGNITION — BULLETPROOF IMPLEMENTATION =====
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
let currentRecognition = null;
let accumulatedTranscript = "";
let silenceTimer = null;
let recognitionActive = false;
let voiceModalOpen = false;

// Detect language from unicode script ranges
function detectLangFromTranscript(text) {
  const scripts = [
    { code: "bn", re: /[\u0980-\u09FF]/ },
    { code: "te", re: /[\u0C00-\u0C7F]/ },
    { code: "kn", re: /[\u0C80-\u0CFF]/ },
    { code: "ml", re: /[\u0D00-\u0D7F]/ },
    { code: "ta", re: /[\u0B80-\u0BFF]/ },
    { code: "gu", re: /[\u0A80-\u0AFF]/ },
    { code: "pa", re: /[\u0A00-\u0A7F]/ },
    { code: "or", re: /[\u0B00-\u0B7F]/ },
    { code: "hi", re: /[\u0900-\u097F]/ }, // Devanagari last (catches Hindi & Marathi)
  ];
  for (const { code, re } of scripts) {
    if (re.test(text)) return code;
  }
  return "en";
}

function setVoiceUI(state) {
  // state: "idle" | "listening" | "done" | "error" | "sending"
  const orb = document.getElementById("voiceOrb");
  const waveform = document.getElementById("waveform");
  const btn = document.getElementById("vmMicBtn");
  const sendBtn = document.getElementById("vmSendBtn");
  const status = document.getElementById("vmStatus");
  const sideCard = document.getElementById("voiceStatusCard");

  orb.classList.toggle("listening", state === "listening");
  waveform.classList.toggle("active", state === "listening");
  sendBtn.style.display = (state === "done") ? "inline-flex" : "none";

  if (state === "idle") {
    btn.innerHTML = "🎙️ Start Speaking";
    btn.disabled = false;
    status.textContent = "Press Start Speaking and talk in any Indian language.";
    sideCard.className = "voice-status";
    sideCard.querySelector(".vs-text").textContent = "Click mic to speak";
  } else if (state === "listening") {
    btn.innerHTML = "⏹️ Stop";
    btn.disabled = false;
    status.textContent = "🔴 Listening… Speak clearly. It auto-sends after a pause.";
    sideCard.className = "voice-status recording";
    sideCard.querySelector(".vs-text").textContent = "Recording…";
  } else if (state === "done") {
    btn.innerHTML = "🔄 Speak Again";
    btn.disabled = false;
    status.textContent = "✅ Captured! Click Send or speak again to add more.";
    sideCard.className = "voice-status";
    sideCard.querySelector(".vs-text").textContent = "Ready to send";
  } else if (state === "error") {
    btn.innerHTML = "🎙️ Try Again";
    btn.disabled = false;
    sideCard.className = "voice-status";
    sideCard.querySelector(".vs-text").textContent = "Error — try again";
  } else if (state === "sending") {
    btn.innerHTML = "⏳ Sending…";
    btn.disabled = true;
    status.textContent = "Sending your voice message…";
    sideCard.className = "voice-status";
    sideCard.querySelector(".vs-text").textContent = "Sending…";
  }
}

function showLangDetected(langCode) {
  const name = DETECT_MAP[langCode] || "English";
  document.getElementById("vmLangDetected").innerHTML = `🌐 Detected: <strong>${name}</strong>`;
  document.getElementById("langDetectedText").textContent = name + " detected";
  document.getElementById("langDetectedBadge").classList.add("visible");
  // Auto-switch
  if (langCode !== currentLang) {
    currentLang = langCode;
    const sel = document.getElementById("langSelect");
    if (sel.querySelector(`option[value="${langCode}"]`)) sel.value = langCode;
  }
}

function killRecognition() {
  recognitionActive = false;
  if (silenceTimer) { clearTimeout(silenceTimer); silenceTimer = null; }
  if (currentRecognition) {
    currentRecognition.onresult = null;
    currentRecognition.onerror = null;
    currentRecognition.onend = null;
    try { currentRecognition.abort(); } catch(e) {}
    currentRecognition = null;
  }
}

function startListening() {
  if (!SpeechRecognition) {
    setVoiceUI("error");
    document.getElementById("vmStatus").textContent = "⚠️ Your browser does not support voice input. Please use Chrome or Edge.";
    return;
  }

  killRecognition(); // clean slate
  accumulatedTranscript = "";
  document.getElementById("vmTranscript").textContent = "Listening… speak now!";
  document.getElementById("vmLangDetected").textContent = "";
  setVoiceUI("listening");

  // Always start with a broad language — use selected language or hi-IN
  const startLang = LANG_CODES[currentLang] || "hi-IN";

  function createAndStart(langCode) {
    const rec = new SpeechRecognition();
    rec.continuous = false;         // IMPORTANT: false avoids browser lockup bugs
    rec.interimResults = true;
    rec.lang = langCode;
    rec.maxAlternatives = 1;
    currentRecognition = rec;
    recognitionActive = true;

    let sessionInterim = "";

    rec.onresult = (e) => {
      sessionInterim = "";
      let sessionFinal = "";
      for (let i = e.resultIndex; i < e.results.length; i++) {
        if (e.results[i].isFinal) {
          sessionFinal += e.results[i][0].transcript + " ";
        } else {
          sessionInterim += e.results[i][0].transcript;
        }
      }
      if (sessionFinal) accumulatedTranscript += sessionFinal;
      const displayText = (accumulatedTranscript + sessionInterim).trim();
      document.getElementById("vmTranscript").textContent = displayText || "Listening…";

      // Detect language from what we've heard
      if (displayText.length > 2) {
        showLangDetected(detectLangFromTranscript(displayText));
      }

      // Reset silence auto-send timer — 2.5s after last speech → auto stop
      if (silenceTimer) clearTimeout(silenceTimer);
      silenceTimer = setTimeout(() => {
        if (recognitionActive && accumulatedTranscript.trim()) {
          stopAndSend();
        }
      }, 2500);
    };

    rec.onerror = (e) => {
      if (e.error === "aborted") return; // We triggered this, ignore
      if (e.error === "no-speech") {
        // Restart silently if user just hasn't spoken yet
        if (recognitionActive) {
          setTimeout(() => { if (recognitionActive) createAndStart(langCode); }, 300);
          return;
        }
      }
      if (e.error === "not-allowed" || e.error === "permission-denied") {
        setVoiceUI("error");
        document.getElementById("vmStatus").textContent = "❌ Microphone permission denied. Please allow mic access in your browser settings and try again.";
        recognitionActive = false;
        return;
      }
      // Other errors — try restarting
      if (recognitionActive) {
        setTimeout(() => { if (recognitionActive) createAndStart(langCode); }, 400);
      }
    };

    rec.onend = () => {
      // If still supposed to be listening (no manual stop), restart for continuous feel
      if (recognitionActive) {
        // Detect if language changed and we should re-init with different lang
        const detectedCode = accumulatedTranscript.length > 3
          ? detectLangFromTranscript(accumulatedTranscript)
          : null;
        const nextLang = detectedCode ? (LANG_CODES[detectedCode] || langCode) : langCode;
        setTimeout(() => { if (recognitionActive) createAndStart(nextLang); }, 200);
      }
    };

    try {
      rec.start();
    } catch(e) {
      setVoiceUI("error");
      document.getElementById("vmStatus").textContent = "Could not access microphone. Make sure you are on HTTPS or localhost and have allowed mic permission.";
      recognitionActive = false;
    }
  }

  // Request mic permission explicitly first
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
      // Permission granted — stop the stream immediately (speech API manages its own)
      stream.getTracks().forEach(t => t.stop());
      createAndStart(startLang);
    })
    .catch(err => {
      setVoiceUI("error");
      document.getElementById("vmStatus").textContent = "❌ Microphone access denied. Please click the 🔒 icon in your browser address bar and allow microphone.";
    });
}

function stopListening() {
  if (silenceTimer) { clearTimeout(silenceTimer); silenceTimer = null; }
  recognitionActive = false;
  if (currentRecognition) {
    try { currentRecognition.stop(); } catch(e) {}
  }
  const text = accumulatedTranscript.trim();
  if (text) {
    setVoiceUI("done");
    document.getElementById("vmTranscript").textContent = text;
    document.getElementById("vmStatus").textContent = "✅ Captured! Click Send or speak again to add more.";
  } else {
    setVoiceUI("idle");
    document.getElementById("vmTranscript").textContent = "Nothing captured. Please try again.";
  }
}

function stopAndSend() {
  if (silenceTimer) { clearTimeout(silenceTimer); silenceTimer = null; }
  recognitionActive = false;
  if (currentRecognition) {
    try { currentRecognition.stop(); } catch(e) {}
    currentRecognition = null;
  }
  const text = accumulatedTranscript.trim();
  if (!text) { setVoiceUI("idle"); return; }
  setVoiceUI("sending");
  setTimeout(() => {
    closeVoiceModal();
    sendMessage(text, true);
  }, 400);
}

function toggleVoiceRecording() {
  if (recognitionActive) {
    // User manually stops mid-recording
    stopListening();
  } else {
    // Either idle start OR "speak again" after done
    accumulatedTranscript = "";
    document.getElementById("vmTranscript").textContent = "Listening… speak now!";
    document.getElementById("vmLangDetected").textContent = "";
    startListening();
  }
}

function openVoiceModal() {
  voiceModalOpen = true;
  accumulatedTranscript = "";
  finalTranscript = "";
  document.getElementById("voiceOverlay").classList.add("active");
  document.getElementById("vmTranscript").textContent = "Press 'Start Speaking' and talk in any language…";
  document.getElementById("vmLangDetected").textContent = "";
  setVoiceUI("idle");
}

function closeVoiceModal() {
  voiceModalOpen = false;
  killRecognition();
  document.getElementById("voiceOverlay").classList.remove("active");
  setVoiceUI("idle");
  document.getElementById("voiceStatusCard").querySelector(".vs-text").textContent = "Click mic to speak";
}

function updateVoiceStatus() {} // legacy stub

// ===== INPUT EVENTS =====
document.getElementById("userInput").addEventListener("input", function() {
  this.style.height = "auto";
  this.style.height = Math.min(this.scrollHeight, 80) + "px";
});

document.getElementById("userInput").addEventListener("keydown", function(e) {
  if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); sendMessage(); }
});

// ===== INIT =====
async function init() {
  conversationHistory = [];
  showTyping();
  try {
    const greeting = "Namaste! I want to find Indian government schemes I am eligible for. Please start in English.";
    conversationHistory.push({ role: "user", content: greeting });
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        model: "claude-sonnet-4-20250514",
        max_tokens: 1500,
        system: getSystemPrompt(),
        messages: conversationHistory
      })
    });
    const data = await res.json();
    const reply = data.content[0].text;
    conversationHistory.push({ role: "assistant", content: reply });
    removeTyping();
    addMsg("bot", processResponse(reply), true);
  } catch(e) {
    removeTyping();
    addMsg("bot", `<div>🙏 <strong>Namaste! Welcome to Adhikar (अधिकार)</strong> — your guide to Indian government schemes.<br><br>I'll ask you a few simple questions to find all schemes you are eligible for. You can speak to me in any Indian language!<br><br>Let's start — <strong>which state are you from?</strong></div><div class="options-wrap"><button class="opt-btn" onclick="selectOption(this,'Uttar Pradesh')">Uttar Pradesh</button><button class="opt-btn" onclick="selectOption(this,'Maharashtra')">Maharashtra</button><button class="opt-btn" onclick="selectOption(this,'Bihar')">Bihar</button><button class="opt-btn" onclick="selectOption(this,'West Bengal')">West Bengal</button><button class="opt-btn" onclick="selectOption(this,'Rajasthan')">Rajasthan</button><button class="opt-btn" onclick="selectOption(this,'Other State')">Other State</button></div>`, true);
  }
}

init();
</script>
</body>
</html>

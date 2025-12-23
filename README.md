# Rejoin Tool v2.0.0

Auto-rejoin Roblox ke Private Server untuk Termux/Android (Cloud Phone).

![Version](https://img.shields.io/badge/version-2.0.0-green)
![Platform](https://img.shields.io/badge/platform-Android-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)

## ✨ Features

- 🔍 **Auto-detect Packages** - Scan `com.roblox.*` otomatis
- 🔗 **Private Server URL** - Support share links
- 🍪 **Cookie Management** - Add/list/remove cookies
- 🔔 **Discord Webhook** - Alerts saat app crash
- 📜 **Script Injection** - Deploy ke autoexecute folder
- 🎭 **Username Masking** - Sembunyikan nama package

---

## 📝 Installation Guide

### Step 1: Enable Freeform Windows (Android)

1. **Enable Developer Options:** 
   - Settings > About Phone > Tap Build Number 7 times
2. **Enable Flags:** 
   - Go to System > Developer Options > Under Apps, enable:
   - ✅ Enable freeform windows
   - ✅ Force activities to be resizable
   - ✅ Enable non-resizable in multi-window
3. **Reboot your device**

### Step 2: Configure Root & Termux

1. Enable **Magisk** or **KernelSU**
2. Open Magisk > Superuser > Grant **Termux** root access

### Step 3: Install Dependencies (Termux)

Open Termux and run this command:

```bash
termux-setup-storage && pkg update -y && pkg upgrade -y && pkg install -y lua53 tsu python figlet android-tools curl && pip install pyfiglet rich
```

**Packages installed:**
| Package | Purpose |
|---------|---------|
| `lua53` | Run Lua scripts |
| `tsu` | Root access from Termux |
| `python` | Python helper scripts |
| `figlet` | ASCII art banners |
| `android-tools` | ADB commands |
| `curl` | Download files & webhooks |
| `pyfiglet` | Python figlet library |
| `rich` | Rich terminal UI |

### Step 4: Download Script

**Option A: From GitHub (after upload)**
```bash
curl -L -o /sdcard/download/rejoin.lua https://raw.githubusercontent.com/YOUR_USERNAME/rejoin-tool/main/rejoin.lua
```

**Option B: Manual copy via ADB**
```bash
adb push rejoin.lua /sdcard/download/
```

---

## 🚀 Usage

### Run the tool
```bash
lua /sdcard/download/rejoin.lua
```

### Reset configuration
```bash
lua /sdcard/download/rejoin.lua --reset
```

### Menu Options
```
1) Setup Configuration (First Run)
2) Run Script (Launch apps + optimizations)
3) Cookie Management
4) Exit
```

---

## ⚙️ Configuration

Config saved at: `/sdcard/download/rejoin_config.json`

```json
{
  "packages": ["com.roblox.clientv", "com.roblox.clientw"],
  "private_server_url": "https://www.roblox.com/share?code=xxx",
  "discord_webhook": "https://discord.com/api/webhooks/...",
  "mask_username": true,
  "inject_scripts": true,
  "delay_between_launch": 3,
  "delay_before_rejoin": 5
}
```

---

## 📤 Upload to GitHub

### Step 1: Create GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Repository name: `rejoin-tool`
3. Description: "Auto-rejoin Roblox to Private Server for Termux/Android"
4. Make it **Public** or **Private**
5. Click **Create repository**

### Step 2: Push Files

Run these commands in PowerShell (from project folder):

```powershell
# Initialize git
cd "c:\Users\faris\OneDrive\Desktop\redo"
git init

# Add files
git add .

# Commit
git commit -m "Initial commit - Rejoin Tool v2.0.0"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/rejoin-tool.git

# Push
git branch -M main
git push -u origin main
```

### Step 3: Get Raw URL

After push, your download URL will be:
```
https://raw.githubusercontent.com/YOUR_USERNAME/rejoin-tool/main/rejoin.lua
```

---

## 🧪 Testing Checklist

- [ ] Run `lua /sdcard/download/rejoin.lua`
- [ ] Menu displays correctly
- [ ] Auto-detect finds Roblox packages
- [ ] Config saves to JSON file
- [ ] Apps launch to private server
- [ ] Monitoring loop detects crashes
- [ ] Discord webhook sends alerts (if configured)

---

## 📁 File Structure

```
rejoin-tool/
├── rejoin.lua          # Main script
├── ui_helper.py        # Python UI helper (optional)
└── README.md           # This file
```

## 📄 License

MIT License - Free to use and modify.

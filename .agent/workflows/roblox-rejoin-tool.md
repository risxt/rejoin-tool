---
description: How to build Roblox auto-rejoin tools for Termux/Android
---

# Roblox Rejoin Tool Development Guide

Dokumentasi lengkap untuk membuat tools auto-rejoin Roblox di Termux/Android.

## Key Learnings & Common Errors

### ❌ Error 1: Activity Class Not Found (SOLVED)

**Problem:**
```
Error: Activity class {com.roblox.clientv/com.roblox.client.ActivitySplash} does not exist
```

**Wrong approach:**
```lua
-- JANGAN pakai ini untuk cloned apps!
am start -n com.roblox.clientv/com.roblox.client.ActivitySplash -d "roblox://..."
```

**Correct approach - Use VIEW Intent:**
```lua
-- PAKAI ini! Android otomatis cari activity yang benar
am start -a android.intent.action.VIEW -d "roblox://placeId=X&linkCode=Y" -p com.roblox.clientv --windowingMode 5
```

**Why it works:**
- Cloned apps (clientv, clientw, clientx) punya activity names berbeda
- VIEW intent biarkan Android resolve activity yang handle `roblox://` scheme
- Flag `-p <package>` memastikan package yang benar yang launch

---

### ❌ Error 2: Ctrl+C Doesn't Stop Script

**Problem:** Lua tidak handle SIGINT dengan baik di Termux

**Solution:** Stop dari terminal lain:
```bash
pkill -f rejoin
```

---

### ❌ Error 3: GitHub Raw File Cache

**Problem:** Setelah push fix, download masih dapat versi lama

**Solution:** Cache-bust URL atau hapus file dulu:
```bash
rm /sdcard/download/rejoin.lua
curl -L -o /sdcard/download/rejoin.lua https://raw.githubusercontent.com/USER/REPO/main/rejoin.lua
```

---

## Working Launch Command Template

```bash
# Template yang benar untuk launch Roblox ke private server
su -c "am start -a android.intent.action.VIEW -d \"roblox://placeId=PLACE_ID\&linkCode=LINK_CODE\" -p PACKAGE_NAME --windowingMode 5"
```

**Parameters:**
| Parameter | Description |
|-----------|-------------|
| `-a android.intent.action.VIEW` | Intent action untuk open URL |
| `-d "roblox://..."` | Deep link URL |
| `-p PACKAGE_NAME` | Target package (e.g., com.roblox.clientv) |
| `--windowingMode 5` | Freeform window mode |

---

## Deep Link URL Format

**Private Server URL (from Roblox website):**
```
https://www.roblox.com/games/12345?privateServerLinkCode=XXXXX
https://www.roblox.com/share?code=XXXXX
```

**Parsed to Deep Link:**
```
roblox://placeId=12345&linkCode=XXXXX
```

**Parsing code (Lua):**
```lua
local function parse_private_server_url(url)
    local place_id = url:match("games/(%d+)") or url:match("placeId=(%d+)")
    local link_code = url:match("privateServerLinkCode=([%w_-]+)") or 
                      url:match("linkCode=([%w_-]+)") or
                      url:match("code=([%w_-]+)")
    return place_id, link_code
end
```

---

## Package Detection

**Auto-detect Roblox packages:**
```bash
pm list packages | grep -i roblox | sed 's/package://g'
```

**Common package names:**
- `com.roblox.client` - Original Roblox
- `com.roblox.clientv` - Clone V
- `com.roblox.clientw` - Clone W
- `com.roblox.clientx` - Clone X

---

## Process Detection

**Check if app is running:**
```bash
pidof com.roblox.clientv
```

**Force stop app:**
```bash
su -c "am force-stop com.roblox.clientv"
```

---

## Required Dependencies (Termux)

```bash
pkg install lua53 tsu python figlet android-tools curl
pip install pyfiglet rich
```

| Package | Purpose |
|---------|---------|
| `lua53` | Run Lua scripts |
| `tsu` | Root access |
| `android-tools` | ADB/am commands |
| `curl` | Download & webhooks |

---

## File Locations

| File | Path |
|------|------|
| Script | `/sdcard/download/rejoin.lua` |
| Config | `/sdcard/download/rejoin_config.json` |
| Cookies | `/sdcard/download/rejoin_cookies.txt` |
| Scripts | `/sdcard/download/rejoin_scripts/` |
| Autoexec | `/data/data/<package>/files/autoexecute/` |

---

## Android Requirements

1. **Root access** (Magisk/KernelSU)
2. **Developer Options enabled:**
   - Enable freeform windows
   - Force activities to be resizable
   - Enable non-resizable in multi-window
3. **Termux granted root access**

---

## Git Workflow for Updates

```powershell
# From project folder
& "C:\Program Files\Git\bin\git.exe" add .
& "C:\Program Files\Git\bin\git.exe" commit -m "Description of fix"
& "C:\Program Files\Git\bin\git.exe" push
```

---

## Quick Reference Commands

```bash
# Download script
curl -L -o /sdcard/download/rejoin.lua https://raw.githubusercontent.com/risxt/rejoin-tool/main/rejoin.lua

# Run script
lua /sdcard/download/rejoin.lua

# Reset config
lua /sdcard/download/rejoin.lua --reset

# Stop script
pkill -f rejoin

# Manual launch test
su -c "am start -a android.intent.action.VIEW -d \"roblox://placeId=63&linkCode=test\" -p com.roblox.clientv --windowingMode 5"
```

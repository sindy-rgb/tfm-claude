# TFM Vault Onboarding Guide for Lays Paiva

**What this is:** The TFM vault is our shared knowledge base in Obsidian. It syncs through GitHub so everyone sees the same files. This guide will get you set up from scratch.

**What you need before starting:**
- Obsidian (you already have this)
- A GitHub account (free)
- About 15-20 minutes

---

## STEP 1 — Create a GitHub Account (if you don't already have one)

1. Go to https://github.com/join
2. Sign up with your email (your TFM email or personal is fine)
3. Choose the free plan
4. Send Jay your GitHub username so he can add you to the `thefeedmedia` organization and grant access to the private `tfm-vault` repo

Wait for Jay to confirm you've been added before continuing to Step 2. You'll receive an email invitation from GitHub — accept it.

---

## STEP 2 — Install Git on Your Computer

Git is the tool that syncs files behind the scenes. The Obsidian Git plugin needs it installed.

**If you're on Mac:**
1. Open the Terminal app (search "Terminal" in Spotlight)
2. Type `git --version` and press Enter
3. If Git is already installed, you'll see a version number — skip to Step 3
4. If a popup appears asking you to install developer tools, click "Install" and wait for it to finish
5. After it finishes, type `git --version` again to confirm it worked

**If you're on Windows:**
1. Go to https://git-scm.com/download/win
2. Download and run the installer
3. Use all the default settings (just click Next through everything)
4. When it finishes, restart your computer

---

## STEP 3 — Create a Personal Access Token on GitHub

This is like a password that lets Obsidian connect to GitHub. You only need to do this once.

1. Go to https://github.com/settings/tokens?type=beta (make sure you're logged in)
2. Click "Generate new token"
3. Give it a name like `Obsidian TFM Vault`
4. Under "Repository access," select "Only select repositories" and choose `thefeedmedia/tfm-vault`
5. Under "Permissions," expand "Repository permissions" and set "Contents" to "Read and write"
6. Click "Generate token"
7. **IMPORTANT:** Copy the token immediately and save it somewhere safe (a note on your phone, a password manager, etc.). GitHub will never show it again.

---

## STEP 4 — Clone the Vault

This downloads the entire vault to your computer.

**If you're on Mac:**
1. Open Terminal
2. Type the following and press Enter:
   ```
   git clone https://github.com/thefeedmedia/tfm-vault.git ~/Documents/tfm-vault
   ```
3. When prompted for your username, enter your GitHub username
4. When prompted for your password, paste the Personal Access Token from Step 3 (not your GitHub password)
5. Wait for it to finish downloading

**If you're on Windows:**
1. Open Git Bash (it was installed with Git in Step 2 — search for it in the Start menu)
2. Type the following and press Enter:
   ```
   git clone https://github.com/thefeedmedia/tfm-vault.git ~/Documents/tfm-vault
   ```
3. When prompted for your username, enter your GitHub username
4. When prompted for your password, paste the Personal Access Token from Step 3
5. Wait for it to finish downloading

---

## STEP 5 — Open the Vault in Obsidian

1. Open Obsidian
2. Click "Open folder as vault"
3. Navigate to `Documents` and select the `tfm-vault` folder
4. Click Open
5. If Obsidian asks "Trust this vault?" or asks about enabling community plugins, click Yes / Trust / Enable

---

## STEP 6 — Install and Configure the Obsidian Git Plugin

1. In Obsidian, open Settings (the gear icon in the bottom-left corner)
2. Go to "Community plugins" in the left sidebar
3. If community plugins are not enabled yet, click "Turn on community plugins"
4. Click "Browse" to search the community plugin catalog
5. Search for **"Obsidian Git"** (by Vinzent)
6. Click Install, then click Enable
7. Go back to Settings and find "Obsidian Git" in the left sidebar under Community Plugins
8. Set these settings:
   - **Auto backup after stop editing:** ON
   - **Auto backup interval (minutes):** 10
   - **Auto pull interval (minutes):** 10
   - **Pull on startup:** ON
   - **Pull before push:** ON
   - **Sync method:** Merge
9. Close Settings

---

## STEP 7 — Save Your Git Credentials (So You're Not Asked Every Time)

**If you're on Mac:**
1. Open Terminal
2. Type this and press Enter:
   ```
   git config --global credential.helper osxkeychain
   ```
3. The next time Obsidian Git pushes or pulls, it'll ask for your username and token one more time, then remember it.

**If you're on Windows:**
1. Open Git Bash
2. Type this and press Enter:
   ```
   git config --global credential.helper manager
   ```
3. Same as above — it'll ask once more, then remember it.

---

## STEP 8 — Set Your Git Identity

So your edits show your name in the change history:

1. Open Terminal (Mac) or Git Bash (Windows)
2. Run these two commands (replace with your info):
   ```
   git config --global user.name "Lays Paiva"
   git config --global user.email "lays@thefeedmedia.com"
   ```

---

## STEP 9 — Verify Everything Works

1. In Obsidian, open the Command Palette (press `Cmd+P` on Mac or `Ctrl+P` on Windows)
2. Type "Obsidian Git: Pull" and select it
3. You should see a small notification that says something like "Already up to date" or shows pulled changes
4. Open any file, add a blank line at the bottom, delete it, then save
5. Open the Command Palette again and type "Obsidian Git: Push"
6. If it pushes without errors, you're fully set up

---

## YOUR CLIENT FILES

These are the folders and files you'll work with most:

- `clients/workweek/workweek.md` — WorkWeek client intelligence
- `clients/jay-shetty/jay-shetty.md` — Jay Shetty client intelligence
- `clients/how-to-ai/how-to-ai.md` — How to AI client intelligence

Each client folder also contains:
- `client-config.md` — Campaign configuration details
- `deep-enrichment.md` — Detailed research and enrichment data
- `claude-chat-project.md` — Claude Chat project instructions for that client

Other useful folders:
- `reports/` — Weekly and bi-weekly ad reports
- `research/` — Industry research, strategy docs

---

## WHAT NOT TO TOUCH

Please don't edit these folders or files — they control how the vault operates:

- `.obsidian/` — Plugin settings and Obsidian configuration
- `system/` — Framework files, automation state, data infrastructure
- `templates/` — Shared templates used by automations
- `.gitignore` — Controls which files sync to GitHub
- `CLAUDE.md` — Claude Code project instructions
- `CLIENT-INTELLIGENCE-SUMMARY.md` — Auto-generated; don't edit directly

If you're unsure whether you should edit something, just ask Jay or post in Slack.

---

## DAILY WORKFLOW

You don't need to think about syncing. Once set up, the Obsidian Git plugin will:
- **Automatically pull** other people's changes every 10 minutes
- **Automatically push** your changes every 10 minutes after you stop editing
- **Pull on startup** every time you open Obsidian

If you ever see a merge conflict notification, don't panic. Just message Jay and he'll walk you through it.

---

## TROUBLESHOOTING

- **"Authentication failed"** — Your Personal Access Token may have expired. Create a new one (repeat Step 3) and try again.
- **"Push rejected"** — Someone else pushed changes. Open Command Palette, run "Obsidian Git: Pull" first, then try pushing again.
- **Plugin not working** — Make sure Git is installed (Step 2). Restart Obsidian after installing the plugin.
- **Vault looks empty** — Make sure you opened the correct folder (`tfm-vault`, not a parent folder).

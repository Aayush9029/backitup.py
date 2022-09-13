#!/usr/bin/python3
import os
from datetime import datetime

# PATHS
BACKUP_SCRIPT = os.path.realpath(__file__)
BACKUP_DIR = os.path.expanduser('~/Documents/configs/backup')
BREW_OUT = os.path.join(BACKUP_DIR, "brew.out")


ZSHRC = os.path.expanduser('~/.zshrc')
# OHMYZSH = os.path.expanduser('~/.oh-my-zsh')
VIMRC = os.path.expanduser('~/.vimrc')
# VIMFOLDER = os.path.expanduser('~/.vim')
SSHFOLDER = os.path.expanduser('~/.ssh')
POWER10KZSH = os.path.expanduser('~/.p10k.zsh')
GITCONFIG = os.path.expanduser('~/.gitconfig')
GITIGNORE = os.path.expanduser('~/.gitignore')
RAYCAST = os.path.expanduser('~/Documents/configs/raycast')
STREAMLINK_CONFIG = os.path.expanduser('~/.config/streamlink')


all_dirs = [BACKUP_SCRIPT, ZSHRC, VIMRC,
            SSHFOLDER, POWER10KZSH, GITCONFIG, GITIGNORE, RAYCAST, STREAMLINK_CONFIG]


#  Brew Helpers
def get_brew_leaves():
    command = "brew leaves | xargs -n1 brew desc --eval-all"
    brew_leaves = os.popen(command).read().splitlines()
    return brew_leaves


def get_brew_casks():
    command = "brew list --casks| xargs -n1 brew desc --eval-all"
    brew_casks = os.popen(command).read().splitlines()
    return brew_casks


def get_brew_formula_install():
    command = " brew leaves | xargs -n1 echo"
    brew_formula_install = os.popen(command).read().splitlines()
    one_line = f"brew install {' '.join(brew_formula_install)}"
    return one_line


def get_brew_formula_cask_install():
    command = "brew list --casks | xargs -n1 echo "
    brew_formula_cask_install = os.popen(command).read().splitlines()
    one_line = f"brew install --cask {' '.join(brew_formula_cask_install)}"
    return one_line

# Helpers


def new_line(count):
    return "\n" * count


def copy_configs():
    print("⚙️  Copying config files / folders to folder")
    for folders in all_dirs:
        if os.path.exists(folders):
            backup_full_path = f"{BACKUP_DIR}/{folders.split('/')[-1].replace('.', '_', 1)}"
            os.system(f"cp -r {folders} {backup_full_path}")
            print(
                f"📋 {folders.split('/')[-1]:12s}  {'➡️':4}  {backup_full_path}")

# Main-ish


def save_brew_leaves_casks():
    print("\n🍺 Saving brew leaves and casks to brew.out")
    brew_leaves = get_brew_leaves()
    print(f"🍃 {len(brew_leaves)} brew leaves found")
    brew_casks = get_brew_casks()
    print(f"📦 {len(brew_casks)} brew casks found")

    brew_leaves_casks = brew_leaves + ["\n"] + brew_casks

    with open(BREW_OUT, 'w') as f:
        f.write("# Command to install brew leaves and casks\n")
        f.write(new_line(1))
        f.write(get_brew_formula_install())
        f.write(new_line(2))
        f.write(get_brew_formula_cask_install())
        f.write(new_line(4))

        f.write("# Brew leaves and casks details\n")
        for line in brew_leaves_casks:
            f.write(line)
            f.write(new_line(1))


def git_push():
    print("🌐 Pushing to git")
    os.system("git add .")
    os.system(f"git commit -m 'backup @ {datetime.now()}'")
    os.system("git push --quiet")


def main():
    print("\n💼 Starting backup script\n")
    copy_configs()
    save_brew_leaves_casks()
    print()
    # delete any .git folders in backup folder
    os.system(f"find {BACKUP_DIR} -name '.git' -type d -delete")
    git_push()
    print("\n✅ Backup script finished")


main()

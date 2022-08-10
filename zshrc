# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="powerlevel10k/powerlevel10k"

# Oh My Zsh Update Configs
zstyle ':omz:update' mode disabled  # disable automatic updates
zstyle ':omz:update' mode reminder  # just remind me to update when it's time
zstyle ':omz:update' frequency 14

plugins=(
    git
    zsh-autosuggestions
    )

source $ZSH/oh-my-zsh.sh

# Homebrew Settings
export HOMEBREW_NO_AUTO_UPDATE=1
export HOMEBREW_NO_ANALYTICS=1

# Paths
export PATH="/opt/homebrew/opt/python@3.10/bin:$PATH"
export PATH="/usr/local/bin:$PATH"
export LANG=en_US.UTF-8

# Custom 
export EDITOR=vim
export PAGER=bat

# QOL Aliases
alias cp='cp -i'
alias mv='mv -i'

# Custom Functions
lsgrep() {
    ls -a|grep "$1" --color=auto
}

histgrep() {        
    history|grep "$1" --color=auto
}

histdelete(){
    history -c
}

streamhttp() {
    streamlink "twitch.tv/$1" best --player-external-http --player-external-http-port 1000
}

caffinate☕() {
    echo "☕ *sip*"
    caffeinate -d -i -s -u
}

# "Apps"
transfer() {
	curl --progress-bar --upload-file "$1" https://transfer.sh/$(basename "$1") | tee /dev/null;
	echo
}

google() {
    search=""
    echo "Googling: $@"
    for term in $@; do
        search="$search%20$term"
    done
    open "http://www.google.com/search?q=$search"
}

# Aliases
alias size='du -sh'
alias pingg='ping google.com'
alias pyhost='python3 -m http.server 8000'
alias gitpush='git add .;git commit -m "updated few files"; git push'
alias temp="sudo powermetrics --samplers smc |grep -i "CPU die temperature""
alias hist=history
alias :wq=exit

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

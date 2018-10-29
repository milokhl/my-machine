# my-machine
Setup for my Ubuntu environment.

## Sublime Text 3
Copy stuff from ```sublime/``` into ```~/.config/sublime-text-3/Packages/User/```


## Indicator Multiload

https://askubuntu.com/questions/406204/how-can-i-add-the-current-cpu-usage-to-my-menu-bar-as-a-percentage

```
sudo add-apt-repository ppa:indicator-multiload/stable-daily 
sudo apt-get update 
sudo apt-get install indicator-multiload
```

## Git Setup
```
git config --global user.name "Milo Knowles"
git config --global user.email "mknowles@mit.edu"
git config --global push.default simple
```

## Apt Packages
```
sudo apt install git
```

## Terminator
Solarized dark color, infinite scrollback.
```
cp terminal/terminator-config ~/.config/terminator/config
```

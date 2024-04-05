```
Publish: True
Date: 2023-08-08 22:26:27 +0100
Title:" I got carried away with using Python to commit my Obsidian vault to GitHub"
Description: "In a previous post, I came up with a solution to commit 
my obsidian vault to GitHub, I took it a bit further..."
```

In the persuit to make my obsidian vault more portable, I came up with a solution to commit my vault to GitHub.

It was a fairly simple solution, two py files in the route of the vault that holds the code to commit the vault to
GitHub using subprocess. It got really annoying right-clicking a file, then clicking to open in system file explorer,
then right-clicking to open a terminal here, then typing `python3 git-push.py` to commit the vault.

A little convoluted, but it worked, I guess.

Anyway... I built an Obsidian plugin. It's called Gnome Terminal Loader, and it does just that, loads the Gnome
Terminal.

Here's the code:

```typescript
import {Platform, Plugin} from 'obsidian';
import {spawn} from "child_process";

export default class GnomeTerminal extends Plugin {

    async onload() {

        if (Platform.isDesktopApp) {
            const loadGnomeTerminal = this.addRibbonIcon(
                'terminal-square', 'Gnome Terminal', (evt: MouseEvent) => {
                    const {spawn} = require('child_process');
                    //@ts-ignore
                    let openTerminalAtPath = spawn('gnome-terminal', {cwd: this.app.vault.adapter.basePath});
                    openTerminalAtPath.on('error', (err: Error) => {
                        console.log(err);
                    });
                });

            const pythonGnomeTerminal = this.addRibbonIcon(
                'file-terminal', 'main.py (Gnome Terminal)', (evt: MouseEvent) => {
                    const {spawn} = require('child_process');

                    const command = 'gnome-terminal'
                    const cmd_args = ["--", "python3", "main.py"]

                    console.log(command)

                    let openTerminalAtPath = spawn(command, cmd_args, {
                        shell: true, //@ts-ignore
                        cwd: this.app.vault.adapter.basePath
                    });
                    openTerminalAtPath.on('error', (err: Error) => {
                        console.log(err);
                    });
                });
        }

    }

    onunload() {

    }

}
```

This is distilled from the Obsidian sample plugin, found
here: [https://github.com/obsidianmd/obsidian-sample-plugin](https://github.com/obsidianmd/obsidian-sample-plugin)

It adds two icons to the ribbon, one to open the terminal, and one to run the python script.

![](https://raw.githubusercontent.com/CheeseCake87/gnome-terminal-loader/master/assets/gnome_terminal.png)

![](https://raw.githubusercontent.com/CheeseCake87/gnome-terminal-loader/master/assets/main_py_gnome_terminal.png)

As you can guess from the name, Gnome Terminal Loader is only compatible 
with a Linux OS with gnome-terminal and python installed. I'm sure it could 
be adapted for other OS's, but I don't have the time or the inclination to do that.

The decision to incorporate the python script into the plugin was an interesting thought to me. I initially started
attempting to build in git functionality, showing push and pull icons. However, you can quickly open a can of worms
when trying to deal with private repos. So, I decided to keep it simple, and run the python script.

My solution for the python script was to have a main.py file in the root of the vault, that contains a simple cli menu
that I can extend in functionality. So I adapted the `git-push.py` and `git-pull.py` scripts into the `main.py` file,
controlled by a simple cli menu.

```python
import subprocess


def git_pull():
    try:
        subprocess.run(['git', 'config', 'credential.helper', 'store'])
        subprocess.run(['git', 'config', 'credential.helper', 'cache --timeout 7200'])
        subprocess.run(['git', 'pull', 'origin', 'master'])
        print('git pull success')
    except Exception as e:
        print(e)


def git_push():
    try:
        subprocess.run(['git', 'config', 'credential.helper', 'store'])
        subprocess.run(['git', 'config', 'credential.helper', 'cache --timeout 7200'])
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', 'update'])
        subprocess.run(['git', 'push', 'origin', 'master'])
        print('git push success')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    menu = -1
    while menu != 0:
        menu = int(input('1. git pull\n2. git push\n0. exit\n'))
        if menu == 1:
            git_pull()
        elif menu == 2:
            git_push()
        elif menu == 0:
            break
        else:
            print('null')
```

Not the prettiest code, but it works.

A big missing thing from this solution is the ability to use other python libraries, to extend the
functionality beyond the python standard library. Maybe it would be a good idea to bake in a virtual environment with
some setup and checks? The purpose of the plugin was to create a python entry point, which it does.

The Beauty of this solution for me is that the main.py file follows the vault around in my commit to GitHub use case.

This obsidian plugin is available on GitHub, under an MIT license. Feel free to go wild with it.

[https://github.com/CheeseCake87/gnome-terminal-loader](https://github.com/CheeseCake87/gnome-terminal-loader)

I have submitted the plugin to the Obsidian community plugins, so hopefully it will be available there soon.

OK, that's it for now.

_I got carried away with my using python to commit my Obsidian vault to GitHub by David Carmichael_
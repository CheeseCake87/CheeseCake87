```
Publish = True
Date = 2023-08-07 10:14:32 +0100
Title = GitHub and Obsidian with the help of Python
Description = I explain how I used a small amount of Python 
to take most of the pain out of committing my Obsidian markdown 
library to GitHub.
```

At the time of writing this Obsidian sync, the service that Obsidian offers to allow you to synchronise all your notes
between computers is $10 a month (if you choose a monthly commitment) This price is shown to me with a geolocation of
the UK, so it may be different in your country.

There are far too many SaaS (Software as a Service) products to pay for these days, it's annoying. I paid £10 for an
online SVG animation application about 2 weeks ago to be able to export the animation in a different format - *arrh,* I
get people should get paid for their software, but it can get annoying; I know - I know, "don't use it then" you're
probably saying. Well, this is that effort.

The goal here is to get my software note-taking much better and Obsidian is perfect for that. I'm also on GitHub all the
time, and storing all my notes on a private repo seems like a good idea to me. The Problem is Obsidian has no Git
management. I
suppose this is a tactical move for you to buy their storage. Which is fair enough.

My solution is to use Python with subprocess to do a block of git commands to push and pull from GitHub. You'll need to
have git installed for this, obviously.

**For people that want to steam ahead, here's the code:**

`git-pull.py`

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


if __name__ == '__main__':
    git_pull()

```

`git-push.py`

```python
import subprocess


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
    git_push()

```

These py files are in the root directory of the GitHub Repo:

```
└── Repo/
    ├── .obsidian/
    ├── .git/
    ├── flask-notes/
    ├── python-notes/
    ├── ...
    ├── git-push.py
    └── git-pull.py
```

**For the people that want more of an explanation on how to set this up:**

To get started, create a GutHub repo with your desired name. In my case, I called mine Obsidian, which I made private.
Making your repo private will mean you'll need some sort of password to be able to clone.

Log in to GitHub then go to your settings (click the profile picture top right, then settings)

At the bottom of the left-hand menu, click Developer settings, then Personal access tokens.

Now, I'm pretty lazy. In may case, I created a classic token by clicking Tokens (classic) then setting the token scopes
for Full control of private repositories, and setting it to never expire.

After setting that up, it will show you the token. I stored this in my password manager.

Now we want to make a local folder on your system. In my case I created a folder called Obsidian, `/home/david/Obsidian`

Navigate to this folder and run the following command:

`git clone https://github.com/<your_username_here>/Obsidian.git .`

This will create a `.git` hidden folder in the directory.

Set your Obsidian app to work from the same directory. Now when you create any folders and files you can commit them to
the git repo.

Navigating to the repo folder and running a terminal window from there will ensure that your current working directory
is correct. Then you can run the commands:

`python git-push.py`

and or

`python git-pull.py`

As you may have noticed, there are two private folders in there. `.obsidian` and `.git`, I'm not familiar with how
important these two are to keep private, by that I mean not make public. In any case I made the code work with git
authentication, so you can make the repo private.

This process is fairly manual, but better than paying $10 a month, right?

Enjoy, bye!

*GitHub and Obsidian with the help of Python by David Carmichael*
### Flask-SSG (static site generator)

### Setup

(This assumes you have Python installed)

1. Download or Clone this repository.
2. Open terminal (Linux) / powershell (Windows) and cd to the directory of the project.

```text
# Linux
cd /path/to/clone

# Windows
cd C:\path\to\clone
```

---

### Linux

**Create a virtual environment and activate it.**

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

**Install the requirements.**

```bash
pip install -r requirements.txt
```

**run**

```bash
flask run
```

or

```bash
python3 run.py
```

---

### Windows

**Create a virtual environment and activate it.**

```bash
python -m venv venv
```

```bash
.\venv\Scripts\activate
```

**Install the requirements.**

```bash
pip install -r requirements.txt
```

**run**

```bash
flask run
```

Ensure your folder structure is like the following:

```text
repo/
  docs/
    static/
      imgs & css
    [html files will be generated here]
  markdown/
    any_posts.md
  [the rest of the project files]
```

The markdown posts should be in the following format:

```text
'''
Publish = True
date = 0000-00-00 00:00:00 +0100 or set-at-publish
Title = title
Description = description
'''

Markdown here...
```

run the following command to generate the html files (remember to activate the virtual env):

```bash
flask compile
```

If you change the design of your template file
and need to update all posts, running this command will re-generate all the html files:

```bash
flask recompile
```

You can also generate a new post markdown file with the following command:

```bash
flask new
```
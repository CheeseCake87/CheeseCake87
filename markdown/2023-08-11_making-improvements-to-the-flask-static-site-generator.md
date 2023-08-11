```
Publish = True
date = 2023-08-11 20:37:22 +0100
title = Making improvements to the Flask Static Site Generator
description = In this post, I talk about the improvements I've made to the Flask static site generator.
```

If you haven't already seen the previous post about how I use Flask to statically generate this site, you
should check it out.

Here's a link: [Flask as a Static Site Generator](/2023-08-06_flask-as-a-static-site-generator.html).

First, let's start with the structure. I moved all the code to a package folder called `ssg`, making the code easier to
work with and maintain.

```text
└── ssg/
    ├── __init__.py
    ├── compiler.py
    ├── exceptions.py
    ├── helpers.py
    └── render_engines.py
```

`compiler.py` is the main entry point to the static site generator. It's responsible for firing all the function calls
in the correct order. It's changed a lot from its original version.

I originally had the meta of a post set by its filename `date_title-of-post`, As you can imagine,
this was very limited.

I then moved to attempting to define some information about the post in the markdown file itself, at the
top. After throwing some hacky code at the process, I landed on the following:

```text
date="0000-00-00 00:00:00 +0100";
title="title";
description="description";

::::

Markdown here...
```

I was splitting the file on the `::::` marker, and using the first part to get the meta information, and the second
part to get the markdown content. Also using `;` and `"` as split markers to get the individual meta information.

Although this method worked, I thought it looked very ugly. So I eventually changed it to:

```text
'''
Publish = True
date = 2023-08-11 20:37:22 +0100
Title = title
Description = description
'''

Markdown here...
```

This is much cleaner and easier to read, it also fits nicely into the way markdown works.
In the example above `'` are stand-ins for the ``` ` ``` character used to denote code blocks in markdown.

So, at the top of the markdown file for the post, there is a neat little meta section,
done in a code block. Which looks nice, in my opinion.

With this change to the way meta is defined, I redesigned how the compiler function finds the meta information.

```python
publish_ptn = re.compile(r'Publish =(.*?)\n', re.IGNORECASE)
date_ptn = re.compile(r'Date =(.*?)\n', re.IGNORECASE)
title_ptn = re.compile(r'Title =(.*?)\n', re.IGNORECASE)
description_ptn = re.compile(r'Description =(.*?)\n', re.IGNORECASE)
```

As you can see, I went for a regex solution. The file's text is split on the code block characters
`markdown.split("'''")` first. The index location of the meta section is pulled out and processed via the above regex,
and the rest is joined back together `"'''".join(markdown_list[1:])` to get the markdown content.

This solution seems to work really well.

I cleaned up the rest of the code base, and I also changed to working more with datetimes, rather than dates as strings.

Here's a small list of the rest of the notable changes:

- A date that cannot be converted to a datetime object from the meta information is generated at publication time. This
  also updates the file name and date within the original markdown file.
- Addition of exception handling, if the meta section is not found, or incorrectly setup.

No doubt there will be more changes to come, but for now, I'm happy with the way it's working. I only usually
tackle changes, as and when they are needed, and it seems to be working well. Maybe I'll build in unit tests at some
point, not sure if this is needed for such a small project.

I hope you enjoyed this short post, if you want to have a look at the code, you can find it on my GitHub:

[https://github.com/CheeseCake87/CheeseCake87](https://github.com/CheeseCake87/CheeseCake87)

Most of the good stuff is in the `ssg` folder.

Thanks for reading!

_Making improvements to the Flask static site generator by David Carmichael_
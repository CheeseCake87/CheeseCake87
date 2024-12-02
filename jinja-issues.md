## Info

Still collecting issues and running example code. Some issues on ths list
may not be matched to any PRs associated with them yet.

Statuses:

* |LATER| - Not a priority, but could be included in a future release.
* |CLOSE| - Issue is resolved, or not an issue, or not a priority.
* |MOVE| - Issue is a question or discussion, not an issue.
* |INCLUDE| - Issue is valid and should be included in an upcoming release.
* |INVESTIGATE| - Issue needs more investigation.
* |IMPROVE| - A PR is available, but could be improved.
* |UNSURE| - Don't know enough about the issue to make an educated suggestion.



<!-- TOC -->
  * [Info](#info)
    * [(1413) Namespace multi-variable assignment:](#1413-namespace-multi-variable-assignment)
    * [(1478) Loop-variables are not accessible in @pass_context / @contextfilter](#1478-loop-variables-are-not-accessible-in-pass_context--contextfilter)
    * [(1624) Can't use a test decorated with `@pass_context` in `select`](#1624-cant-use-a-test-decorated-with-pass_context-in-select)
    * [(1661) Add searchpath to TemplateNotFound exception message](#1661-add-searchpath-to-templatenotfound-exception-message)
    * [(1675) Faulty handling of UNC paths (pathlib in PackageLoader)](#1675-faulty-handling-of-unc-paths-pathlib-in-packageloader)
    * [(1687) `lexer.Token.value` has wrong type](#1687-lexertokenvalue-has-wrong-type)
    * [(1688) `Failure.__call__` provides wrong arguments to `self.error_class`](#1688-failure__call__-provides-wrong-arguments-to-selferror_class)
    * [(1701) TypeError: sequence item 0: expected str instance, int found](#1701-typeerror-sequence-item-0-expected-str-instance-int-found)
    * [(1705) The error message from PackageLoader could be more helpful](#1705-the-error-message-from-packageloader-could-be-more-helpful)
    * [(1718) debug extension pprinting in html](#1718-debug-extension-pprinting-in-html)
    * [(1720) Negative number raised to even power gives negative result if exponent is a variable](#1720-negative-number-raised-to-even-power-gives-negative-result-if-exponent-is-a-variable)
    * [(1722) Bug with right-left associativity of exponent](#1722-bug-with-right-left-associativity-of-exponent)
    * [(1737) Missing line info from syntax error message](#1737-missing-line-info-from-syntax-error-message)
    * [(1738) Template caching does not take environment configuration into account](#1738-template-caching-does-not-take-environment-configuration-into-account)
    * [(1755) explain associativity and precedence between operators](#1755-explain-associativity-and-precedence-between-operators)
    * [(1763) Configurable behavior when translated string interpolation fails.](#1763-configurable-behavior-when-translated-string-interpolation-fails)
    * [(1766) Contains as a new Test (flipped operation of in)](#1766-contains-as-a-new-test-flipped-operation-of-in)
    * [(1769) Undefined name `autoescape` in custom filter example](#1769-undefined-name-autoescape-in-custom-filter-example)
    * [(1775) Support accurate dependency tracking including dynamic inheritance or inclusion](#1775-support-accurate-dependency-tracking-including-dynamic-inheritance-or-inclusion)
    * [(1781) unique filter does not work when chain with a filter that returns async generator](#1781-unique-filter-does-not-work-when-chain-with-a-filter-that-returns-async-generator)
    * [(1792) f-string sytax error when importing macro in a template which filename is also a template](#1792-f-string-sytax-error-when-importing-macro-in-a-template-which-filename-is-also-a-template)
    * [(1803) Extension: Support saving arbitrary data with AssignmentBlock](#1803-extension-support-saving-arbitrary-data-with-assignmentblock)
    * [(1825) Docs update re triple quotes and block assignments](#1825-docs-update-re-triple-quotes-and-block-assignments)
    * [(1861) Enhance Default Exceptions to include Line Number.](#1861-enhance-default-exceptions-to-include-line-number)
    * [(1862) Allow passing multiple templates to import, just like include](#1862-allow-passing-multiple-templates-to-import-just-like-include)
    * [(1871) DebugUndefined does not handle object.value replacements](#1871-debugundefined-does-not-handle-objectvalue-replacements)
    * [(1882) Escape newlines for tojson filter as Django](#1882-escape-newlines-for-tojson-filter-as-django)
    * [(1889) injecting tokens in filter_stream fails with "expected token end of print statement"](#1889-injecting-tokens-in-filter_stream-fails-with-expected-token-end-of-print-statement)
    * [(1890) `select_autoescape` default value for `default_for_string` should be](#1890-select_autoescape-default-value-for-default_for_string-should-be)
    * [(1898) Autoescape does not work well across blocks/inheritance](#1898-autoescape-does-not-work-well-across-blocksinheritance)
    * [(1921) The `int` filter throws](#1921-the-int-filter-throws)
    * [(1925) Leading newline after](#1925-leading-newline-after)
    * [(1934) `tojson` always do autoescape](#1934-tojson-always-do-autoescape)
    * [(1945) urlize support for quotes](#1945-urlize-support-for-quotes)
    * [(1950) filters.map: apply filter to attribute ("mapattr")](#1950-filtersmap-apply-filter-to-attribute-mapattr)
    * [(1962) Allow to customize some behaviors of Lexer, so that Extension instances get can the raw block begin and end info.](#1962-allow-to-customize-some-behaviors-of-lexer-so-that-extension-instances-get-can-the-raw-block-begin-and-end-info)
    * [(1967) Option to preserve comments in the AST](#1967-option-to-preserve-comments-in-the-ast)
    * [(1978) refactor `PackageLoader` to use `importlib.resources`](#1978-refactor-packageloader-to-use-importlibresources)
    * [(1983) Type annotation wrong on TemplateStream.dump?](#1983-type-annotation-wrong-on-templatestreamdump)
    * [(1992) Support explicitly disabling positional arguments in macros](#1992-support-explicitly-disabling-positional-arguments-in-macros)
    * [(1995) PackageLoader raises misleading error when template directory does not exist.](#1995-packageloader-raises-misleading-error-when-template-directory-does-not-exist)
    * [(2003) Mark output of Template(..., autoescape=True).render() as safe](#2003-mark-output-of-template-autoescapetruerender-as-safe)
    * [(2010) Support for SandboxedNativeEnvironment](#2010-support-for-sandboxednativeenvironment)
    * [(2015) Incorrect list comprehension](#2015-incorrect-list-comprehension)
    * [(2016) indent filter uses \n always rather than following api newline_sequence](#2016-indent-filter-uses-n-always-rather-than-following-api-newline_sequence)
    * [(2020) Allow to apply certain filters by default (e.g. urlencode)](#2020-allow-to-apply-certain-filters-by-default-eg-urlencode)
    * [(2021) non-deterministic output from compile templates when using tuple unpacking](#2021-non-deterministic-output-from-compile-templates-when-using-tuple-unpacking)
    * [(2024) jinja filters converts none to string 'none'](#2024-jinja-filters-converts-none-to-string-none)
    * [(2025) Undefined objects can't be copied or pickled by Python > 3.5](#2025-undefined-objects-cant-be-copied-or-pickled-by-python--35)
    * [(2027) Cannot pickle `jinja2.utils.missing`](#2027-cannot-pickle-jinja2utilsmissing)
    * [(2030) Cannot refer to a variable named](#2030-cannot-refer-to-a-variable-named)
    * [(2032) `MutableSequence` coverage in `ImmutableSandboxedEnvironment`](#2032-mutablesequence-coverage-in-immutablesandboxedenvironment)
    * [(2035) Support generic `Traversable` in `FileSystemLoader`](#2035-support-generic-traversable-in-filesystemloader)
    * [(2036) Sandbox format_map in for loop: TypeError: format_map() takes exactly one argument 2 given](#2036-sandbox-format_map-in-for-loop-typeerror-format_map-takes-exactly-one-argument-2-given)
    * [(2039) template.stream().dump( ) could take a path like object.](#2039-templatestreamdump--could-take-a-path-like-object)
    * [(2050) Reconsider returning the configured undefined for else-less ifs](#2050-reconsider-returning-the-configured-undefined-for-else-less-ifs)
    * [=== Filter Tool](#-filter-tool)
<!-- TOC -->

---

### (1413) Namespace multi-variable assignment:

https://github.com/pallets/jinja/issues/1413

|LATER|

Makes sense to include, a task for later.

---

### (1478) Loop-variables are not accessible in @pass_context / @contextfilter

https://github.com/pallets/jinja/issues/1478

|LATER|

Suggested lost of speed if included. Maybe make this a feature flag?

Would require investigation and more code than you likely think.

---

### (1624) Can't use a test decorated with `@pass_context` in `select`

https://github.com/pallets/jinja/issues/1624

|UNSURE|

Unable to get example working.

---

### (1661) Add searchpath to TemplateNotFound exception message

https://github.com/pallets/jinja/issues/1661

|INCLUDE|

This one looks like a good one to include, or to think about.

---

### (1675) Faulty handling of UNC paths (pathlib in PackageLoader)

https://github.com/pallets/jinja/issues/1675

|LATER|

Suggested code changes in a tag:
https://github.com/UlrichEckhardt/jinja/releases/tag/jfrog-dev1

Haven't looked at this. It's one for later.

---

### (1687) `lexer.Token.value` has wrong type

https://github.com/pallets/jinja/issues/1687

|CLOSE|

Typing issue, looks like it has already changed to `t.Any`

It really should be `t.Union[str, int, float]` (for prior python support)

---

### (1688) `Failure.__call__` provides wrong arguments to `self.error_class`

https://github.com/pallets/jinja/issues/1688

|CLOSE|

Look like this is correct:
`lexer.py > line 266`
`exceptions.py > line 91`

There's no kwargs used so the order looks out, but it looks like
`exceptions.py > line 115` does some checking for this. So maybe a close? -
wouldn't be a big task to be explicit here though.

---

### (1701) TypeError: sequence item 0: expected str instance, int found

https://github.com/pallets/jinja/issues/1701

|CLOSE|

Looks like this only happens when using `NativeEnvironment`, I tested using
`Environment` and the code worked fine.

Ah, OK. `NativeEnvironment().from_string` looks like the issue.

This works:

```
from jinja2.nativetypes import NativeEnvironment

env = NativeEnvironment()
out = env.from_string("""
        {% block test %}
            {% for i in range(1) %}
                {{ loop.index }}
            {% endfor %}
        {% endblock %}
        """).render()

print(out)
```

---

### (1705) The error message from PackageLoader could be more helpful

https://github.com/pallets/jinja/issues/1705

|INCLUDE|

`ValueError: The '1705' package was not installed in a way that PackageLoader understands.`
is set in `loaders.py > line 326` Which could do with a better explination or
the error, if possible.

---

### (1718) debug extension pprinting in html

https://github.com/pallets/jinja/issues/1718

|INVESTIGATE|

Possible Close.
Not really sure if I understand what the request is here. Do they want to
remove the pprint line break seen after values? - Not sure about this, looks
like it might just be a close.

---

### (1720) Negative number raised to even power gives negative result if exponent is a variable

https://github.com/pallets/jinja/issues/1720

|INCLUDE|

If time is available. `**` math issue

---

### (1722) Bug with right-left associativity of exponent

https://github.com/pallets/jinja/issues/1722

|INCLUDE|

Looks like this is related to the issue above. May be worth just doing it...

---

### (1737) Missing line info from syntax error message

https://github.com/pallets/jinja/issues/1737

|CLOSE|

This is asking for better error messaging. I would close with a message that
this might be included in a future version, but no plans for it at the moment.

---

### (1738) Template caching does not take environment configuration into account

https://github.com/pallets/jinja/issues/1738

|LATER|

Large job that requires redesign.

---

### (1755) explain associativity and precedence between operators

https://github.com/pallets/jinja/issues/1755

|INCLUDE|

Related to [#379](https://github.com/pallets/jinja/issues/379) - Write docs to
explain operators

---

### (1763) Configurable behavior when translated string interpolation fails.

https://github.com/pallets/jinja/issues/1763

|UNSURE|

Not entirely sure on what this is talking about, I'm not familiar with
translation strings.

---

### (1766) Contains as a new Test (flipped operation of in)

https://github.com/pallets/jinja/issues/1766

|LATER|

This is a feature request, set aside for later. They would like to see:
`['Mike','Joe','Michael'] | select('contains', 'Mi') | list` returning
`['Mike', 'Michael']`

---

### (1769) Undefined name `autoescape` in custom filter example

https://github.com/pallets/jinja/issues/1769

|INCLUDE|

Accurate, Docs update required.

[https://jinja.palletsprojects.
com/en/stable/api/#custom-filters:~:text=the%20output%20safe.-,import%20re,-from%20jinja2%20import](https://jinja.palletsprojects.com/en/stable/api/#custom-filters:~:text=the%20output%20safe.-,import%20re,-from%20jinja2%20import)

---

### (1775) Support accurate dependency tracking including dynamic inheritance or inclusion

https://github.com/pallets/jinja/issues/1775

|INVESTIGATE|

Wants to dynamically inheriting `jinja2.meta.find_referenced_templates`

I'm not sure on the use case of this...

---

### (1781) unique filter does not work when chain with a filter that returns async generator

https://github.com/pallets/jinja/issues/1781

|LATER|

I suspect this won't be easy to implement. Maybe for the eventual re-write?
Needs a complete code example.

---

### (1792) f-string sytax error when importing macro in a template which filename is also a template

https://github.com/pallets/jinja/issues/1792

|INCLUDE|

If possible. This is related to the security issue with filenames:

https://github.com/pallets/jinja/security/advisories/GHSA-gmj6-6f8f-6699

---

### (1803) Extension: Support saving arbitrary data with AssignmentBlock

https://github.com/pallets/jinja/issues/1803

|LATER|

This is related to a closed issue: https://github.com/pallets/jinja/issues/714

The person that has made this issue has offered to do a PR, maybe leave a
comment asking if they will still be interested?

---

### (1825) Docs update re triple quotes and block assignments

https://github.com/pallets/jinja/issues/1825

|INCLUDE|

Documentation update that makes sense.

---

### (1861) Enhance Default Exceptions to include Line Number.

https://github.com/pallets/jinja/issues/1861

|CLOSE|

This looks like it has been done?

I ran the code and got `File "<template>", line 2, in top-level template code`

That looks like a line number to me.

---

### (1862) Allow passing multiple templates to import, just like include

https://github.com/pallets/jinja/issues/1862

|LATER|

This a potential close. It's a feature request that would be more suited to
a re-write.

---

### (1871) DebugUndefined does not handle object.value replacements

https://github.com/pallets/jinja/issues/1871

|INCLUDE|

This makes sense to include in an upcoming release. Although maybe my
understanding of what the `DebugUndefined` class does is incorrect.

The request here is that when the `DebugUndefined` class is used, it should
not raise an error when `object.value` is used, but instead should return
`<Undefined>`.

---

### (1882) Escape newlines for tojson filter as Django

https://github.com/pallets/jinja/issues/1882

|INVESTIGATE|

I'm relly not sure what the request is here. I think it's asking for a
change to allow `tojson` to safely escape code in some way?

This seems more like a 'parsing on user input' issue.

---

### (1889) injecting tokens in filter_stream fails with "expected token end of print statement"

https://github.com/pallets/jinja/issues/1889

|INCLUDE|

This looks like a documentation error?

Example code on the ticket is working with `==` but the docs say use `is`.

---

### (1890) `select_autoescape` default value for `default_for_string` should be

`False`

https://github.com/pallets/jinja/issues/1890

|CLOSE|

This issue details that if no template name is provided, and you would like
to autoescape, `select_autoescape()`'s `default_for_string` argument should
be `False`.

I feel setting this is in itself an action to autoescape strings, as it
wouldn't
make sense to set this, and not have it autoescape strings by default.

---

### (1898) Autoescape does not work well across blocks/inheritance

https://github.com/pallets/jinja/issues/1898

|LATER|

Feature request. Wants to be able to wrap blocks in base templates to
`autoescape false`:

```jinja
# base.html
{% autoescape false %}
    {% block content %}{% endblock %}
{% endautoescape %}

# child.html
{% extends "base.html" %}
{% block content %}
    {{ '<' }}
{% endblock %}
```

Works as expected if you do:

```jinja
# child.html
{% extends "base.html" %}
{% block content %}
    {% autoescape false %}
        {{ '<' }}
    {% endautoescape %}
{% endblock %}
```

---

### (1921) The `int` filter throws

`OverflowError` when the incoming string looks like scientific notation

https://github.com/pallets/jinja/issues/1921

|INCLUDE|

PR: https://github.com/pallets/jinja/pull/1984

PyCon Sprint

Milestone: 3.2

---

### (1925) Leading newline after

`trans` block with Jinja trim options results in translation lookup failure

https://github.com/pallets/jinja/issues/1925

|LATER|

Work was being done on this at a sprint, no PR or update since.

---

### (1934) `tojson` always do autoescape

https://github.com/pallets/jinja/issues/1934

|CLOSE|

PR: https://github.com/pallets/jinja/pull/1937

Findings:

My initial thoughts were that the minimal example should really 
raise a TypeError, as JSON (I'm sure) should always start and end with 
`{ / [ ... ] / }` and not a string.

This would be a better example:

```Python
print(t.render(x={"html": "<p class=\"this\"> foo and 'bar' </p>"}))
```

Results in:

```text
{"html": "\u003cp class=\"this\"\u003e foo and \u0027bar\u0027 \u003c/p\u003e"}
```

Although, the behavior of `json.dumps` accepts stings:

```Python
value = "<p class=\"this\"> foo and 'bar' </p>"
print(json.dumps(value))
```

Results in:

```text
"<p class=\"this\"> foo and 'bar' </p>"
```

So this change makes sense to match the expected behavior of `json.dumps`.

It looks like this change should be made in `utils.py`.  It looks 
like `< > & '` are being explicitly escaped in `htmlsafe_json_dumps`, I'm not 
sure yet of the reasoning behind this.

Setting `env.policies["json.dumps_function"]` has no effect on the output, 
as this is passed to `htmlsafe_json_dumps`

Close this. The function is specifically for making JSON safe for HTML, 
`autoescape` is False by default, doing this change would make it default 
unsafe.

```
Serialize an object to a string of JSON, and mark it safe to
render in HTML.
```

---

### (1945) urlize support for quotes

https://github.com/pallets/jinja/issues/1945

|LATER|

Running this with; `{{ "lorem ipsum 'example.org'." | urlize }}` gives me;
`lorem ipsum &#39;example.org&#39;.` Placing whitespace between the quote and
the URL works as expected. `' example.org '.`

Suggested fix:

https://github.com/pallets/jinja/commit/19817a6b7fff6159e28e962deb06109545987d87

---

### (1950) filters.map: apply filter to attribute ("mapattr")

https://github.com/pallets/jinja/issues/1950

|LATER|

They are willing to do a PR for this, but it's a feature request.

---

### (1962) Allow to customize some behaviors of Lexer, so that Extension instances get can the raw block begin and end info.

https://github.com/pallets/jinja/issues/1962

|LATER|

Feature request.

---

### (1967) Option to preserve comments in the AST

https://github.com/pallets/jinja/issues/1967

|INCLUDE|

PR: https://github.com/pallets/jinja/pull/2037

---

### (1978) refactor `PackageLoader` to use `importlib.resources`

https://github.com/pallets/jinja/issues/1978

|INCLUDE|

PR: https://github.com/pallets/jinja/pull/1985/files

Has conflicts, needs review.

Milestone: 3.2

---

### (1983) Type annotation wrong on TemplateStream.dump?

https://github.com/pallets/jinja/issues/1983

|LATER|

Looks like a simple fix, but not a priority. Type hinting issue (mypy).

---

### (1992) Support explicitly disabling positional arguments in macros

https://github.com/pallets/jinja/issues/1992

|LATER|

Feature request for forced named arguments in macros.

---

### (1995) PackageLoader raises misleading error when template directory does not exist.

https://github.com/pallets/jinja/issues/1995

|IMPROVE|

Can be included if improved.

PR: https://github.com/pallets/jinja/pull/1996

---

### (2003) Mark output of Template(..., autoescape=True).render() as safe

https://github.com/pallets/jinja/issues/2003

|CLOSE|

This is confusion on what is the definition of 'template data'

They are rendering a template, saving it into a variable, then passing that
variable to another template render, and expecting it not to be escaped.

Advise to use `| safe` or `Markup` and explain the template is now a string,
and not a 'template object'.

---

### (2010) Support for SandboxedNativeEnvironment

https://github.com/pallets/jinja/issues/2010

|INVESTIGATE|

Feature request for a sandboxed native environment. They are not sure if
they are missing something. I'm not sure either.

---

### (2015) Incorrect list comprehension

https://github.com/pallets/jinja/issues/2015

|INCLUDE|

Docs update.

PR: https://github.com/pallets/jinja/pull/2017

---

### (2016) indent filter uses \n always rather than following api newline_sequence

https://github.com/pallets/jinja/issues/2016

|INCLUDE|

PR: https://github.com/pallets/jinja/pull/2031

Millstone: 3.2

---

### (2020) Allow to apply certain filters by default (e.g. urlencode)

https://github.com/pallets/jinja/issues/2020

|MOVE|

This is a question, not an issue. Move to discussions.

---

### (2021) non-deterministic output from compile templates when using tuple unpacking

https://github.com/pallets/jinja/issues/2021

|INCLUDE|

PR: https://github.com/pallets/jinja/pull/2022

---

### (2024) jinja filters converts none to string 'none'

https://github.com/pallets/jinja/issues/2024

|CLOSE|

Jinja variable set to none is of type `None` during `if` checks, but a
string when used in filters. Advise to check if none before using filters?

---

### (2025) Undefined objects can't be copied or pickled by Python > 3.5

https://github.com/pallets/jinja/issues/2025

|INVESTIGATE|

PR: https://github.com/pallets/jinja/pull/2026

I had this in include, but it's related to another pr that's attempting to
build in pickling of some sort.

---

### (2027) Cannot pickle `jinja2.utils.missing`

https://github.com/pallets/jinja/issues/2027

|INVESTIGATE|

PR: https://github.com/pallets/jinja/pull/2029

Related to above. Some movement towards pickling. A quick reminder is the
PRs want to push around defined type for a reason to implement a feature in
another product.

---

### (2030) Cannot refer to a variable named
`self` that was set in an enclosing context

https://github.com/pallets/jinja/issues/2030

|CLOSE|

Not sure if there's much that can be done here. Returning `{{ self }}`
seems like it would be normal to expect it to be the `self` object.

---

### (2032) `MutableSequence` coverage in `ImmutableSandboxedEnvironment`

https://github.com/pallets/jinja/issues/2032

|INVESTIGATE|

PR: https://github.com/pallets/jinja/pull/2033

Don't know enough about the `ImmutableSandboxedEnvironment` to make an
educated decision on this.

---

### (2035) Support generic `Traversable` in `FileSystemLoader`

https://github.com/pallets/jinja/issues/2035

|LATER|

Feature request. Something for later.

---

### (2036) Sandbox format_map in for loop: TypeError: format_map() takes exactly one argument 2 given

https://github.com/pallets/jinja/issues/2036

|INVESTIGATE|

This error is only happening inside the for loop.

Note: there was a change to the `format_map` in a sandboxed environment here:
https://jinja.palletsprojects.com/en/stable/changes/#version-2-10-1

---

### (2039) template.stream().dump( ) could take a path like object.

https://github.com/pallets/jinja/issues/2039

|LATER|

Or close. Pathlib integration request.

---

### (2050) Reconsider returning the configured undefined for else-less ifs

https://github.com/pallets/jinja/issues/2050

|INVESTIGATE|

Asking for a revert to old behavior?

---

### === Filter Tool

```python
from pathlib import Path

jinja_issues = (Path.cwd() / 'jinja-issues.md').read_text().split('---')[1:-1]
filter_ = 0
filters_ = {0: "all",
            1: "|LATER|", 2: "|CLOSE|", 3: "|MOVE|", 4: "|INCLUDE|",
            5: "|INVESTIGATE|", 6: "|IMPROVE|", 7: "|UNSURE|", 8: "PR:"}
for issue in jinja_issues:
    if "=== Filter Tool" in issue: continue
    if filters_[filter_] in issue if filter_ != 0 else True:
        print("-" * 80)
        print(issue)
        print("-" * 80)
```

---

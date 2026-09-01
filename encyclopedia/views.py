from django.shortcuts import render
from . import util
import re


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "error": f"The requested page named '{title}' was not found."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": converter(content)
        })

def converter(text):
    text = re.sub(r"^# (.+?)$", r"<h1>\1</h1>", text, flags=re.MULTILINE)
    text = re.sub(r"^## (.+?)$", r"<h2>\1</h2>", text, flags=re.MULTILINE)
    text = re.sub(r"^### (.+?)$", r"<h3>\1</h3>", text, flags=re.MULTILINE)
    text = re.sub(r"^\*\*(.+?)\*\*$", r"<strong>\1</strong>", text, flags=re.MULTILINE)
    text = re.sub(r"\n", r"<br>\n", text)
    text = re.sub(r"^\[([a-zA-Z]+)\]\(/wiki/([a-zA-Z]+)\)$", r'<a href="/wiki/\2">\1</a>', text, flags=re.MULTILINE)

    return text
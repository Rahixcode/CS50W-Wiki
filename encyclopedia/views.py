from django.shortcuts import render, redirect
from . import util
import re
import random


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
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\n", r"<br>\n", text)
    text = re.sub(r"\[([^\]]+)\]\(\/wiki\/([^)]+)\)", r'<a href="/wiki/\2">\1</a>', text)

    return text


def random_page(request):
    entries = util.list_entries()
    if not entries:
        return render(request, "encyclopedia/error.html", {
            "error": "No encyclopedia entries exist yet."
        })

    title = random.choice(entries)
    return redirect("wiki:entry", title=title)

def add_page(request):
    return render(request, "encyclopedia/new_page.html")

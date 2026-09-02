from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
import re
import random
from django import forms


class NewENtry(forms.Form):
    title = forms.CharField(
        label= "",
        widget=forms.TextInput(attrs={
            "class": "title",
        }),
        )

    content = forms.CharField(
        label= "",
        widget=forms.Textarea(attrs={
            "class": "inp_content",
            "rows": 0,
            "placeholder": "Write your page content here...",
        }),
        )


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "nav": ""
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


def edit_page(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "error": f"The requested page named '{title}' was not found."
        })

    if request.method == "POST":
        form = NewENtry(request.POST)
        if form.is_valid():
            util.save_entry(title, form.cleaned_data["content"])
            return redirect("wiki:entry", title=title)
    else:
        form = NewENtry(initial={"title": title, "content": content})

    return render(request, "encyclopedia/edit_page.html", {
        "title": title,
        "form": form
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
    if request.method == "POST":
        form = NewENtry(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            if any(title.casefold() == name.casefold() for name in util.list_entries()):
                form.add_error("title", "An entry with this title already exists.")
                return render(request, "encyclopedia/new_page.html", {
                    "form": form,
                })
            util.save_entry(form.cleaned_data["title"], form.cleaned_data["content"])
            return HttpResponseRedirect(reverse("wiki:index"))
        else:
            return render(request, "encyclopedia/new_page.html", {
                "form" : form,
            })

    return render(request, "encyclopedia/new_page.html", {
        "form" : NewENtry()
    })


def edit_page(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "error": f"The requested page named '{title}' was not found."
        })

    if request.method == "POST":
        form = NewENtry(request.POST)
        if form.is_valid():
            util.save_entry(title, form.cleaned_data["content"])
            return redirect("wiki:entry", title=title)
    else:
        form = NewENtry(initial={
            "title": title,
            "content": content,
        })

    return render(request, "encyclopedia/edit_page.html", {
        "form": form,
        "title": title,
    })


def search(request):
    ...

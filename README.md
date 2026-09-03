# CS50W Wiki

A Django-based encyclopedia application for the CS50 Web Programming with Python and JavaScript Wiki project.

## Features

- Browse all encyclopedia entries.
- Search for entries by title.
- View entries rendered from Markdown.
- Create new entries.
- Edit existing entries.
- Open a random entry.
- Navigate between entries with Markdown links.

## Requirements

- Python 3
- Django

## Specification

This project implements a Wikipedia-like encyclopedia using Django and Markdown files.

- The index page displays every available entry and links to each entry page.
- Each entry page displays its title and rendered content. Missing entries show an error page.
- The search form finds an exact entry or displays matching entry names when the query is partial.
- Users can create entries with a title and Markdown content. Titles are case-insensitively checked to prevent duplicates.
- Users can edit an existing entry and save the updated Markdown content.
- A random-entry link opens one available entry selected at random.
- Markdown conversion supports headings, bold text, italic text, unordered lists, and links to other encyclopedia entries.
- Entries are stored as `.md` files in the `entries/` directory.
# <p align="center" style="color: #A7D8F0">CS50W Wiki</p>

<p align="center">
  <img src="https://img.shields.io/badge/CS50W-Project%200-blue?style=for-the-badge&logo=harvard" alt="CS50W Project 0">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
</p>

<p align="center" style="color: #F6E7A1">
  <b>A Django-based encyclopedia application for the CS50 Web Programming with Python and JavaScript Wiki project.</b>
</p>

---
<p align="center" style="color: #B8E0D2">Video Demo: <a href="https://youtu.be/LH6NxV8UAFE">link</a></p>

---

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

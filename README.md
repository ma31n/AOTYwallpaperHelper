# AOTY Wallpaper Helper

A simple Python backend that fetches user rating data from AlbumOfTheYear. Exposed through a simple HTTP API for use in [AOTY-Wallpaper](https://github.com/ma31n/AOTY-Wallpaper).

This service is intended to be deployed (e.g., on Render) and consumed by a Web wallpaper via `fetch()`.

---

## Overview

This project:

- Uses [AlbumOfTheYearAPI](https://github.com/JahsiasWhite/AlbumOfTheYearAPI) by JahsiasWhite.
- Exposes a REST endpoint via Flask
- Is designed with Wallpaper Engine Web wallpapers in mind (though it can be loaded in any program supporting web wallpapers)

---

## API Endpoint

### GET /user/<username>

Returns all ratings for the specified AlbumOfTheYear user.

Example:

[https://your-backend-url.onrender.com/user/ma31n](https://aotywallpaperhelper-1.onrender.com/user/ma31n)

Response: JSON containing user rating data.

---

## Tech Stack

- Python 3
- Flask
- album-of-the-year-api
- Gunicorn (production server)

---

## Notes

- CORS is enabled for cross-origin access.
- Functionality depends on the current structure of AlbumOfTheYear.

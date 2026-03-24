# Flask for railway.app

![Template Header](./template-header.svg)

Minimal Flask app served with Gunicorn for Railway.

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/new/template)

## Environment

| Variable | Description |
|----------|-------------|
| `PORT` | Set by Railway (Gunicorn bind) |

## Local

```bash
docker build -t railwayapp-flask .
docker run --rm -p 8000:8000 -e PORT=8000 railwayapp-flask
```

<!-- footer -->

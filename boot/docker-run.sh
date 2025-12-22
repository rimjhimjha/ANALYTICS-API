source /opt/venv/bin/activate
cd /app
RUN_PORT=${RUN_PORT:-8000}
RUN_HOST=${RUN_HOST:-0.0.0.0}

exec gunicorn -k uvicorn.workers.UvicornWorker --bind ${RUN_HOST}:${RUN_PORT} --workers 4 --timeout 120 main:app
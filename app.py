from datetime import datetime, timezone
import os
import socket

from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Data contoh (fiktif). Penyimpanan permanen baru dibuat pada M05.
PENEMPATAN = [
    {"siswa": "Siswa A", "tempat": "PT Contoh Teknologi", "periode": "Jan-Mar 2027", "status": "Berjalan"},
    {"siswa": "Siswa B", "tempat": "CV Contoh Digital", "periode": "Jan-Mar 2027", "status": "Berjalan"},
    {"siswa": "Siswa C", "tempat": "Dinas Contoh Kominfo", "periode": "Feb-Apr 2027", "status": "Menunggu"},
]


@app.get("/")
def index():
    return render_template(
        "index.html",
        app_env=os.getenv("APP_ENV", "development"),
        hostname=socket.gethostname(),
        penempatan=PENEMPATAN,
    )


@app.get("/health")
def health():
    return jsonify(
        status="ok",
        environment=os.getenv("APP_ENV", "development"),
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


@app.get("/api/info")
def info():
    return jsonify(
        course="Cloud Computing",
        code="PTI 2802",
        meeting=3,
        milestone="M03",
        project="Aplikasi PKL SMK",
        deployment="VPS Ubuntu Server 24.04",
    )


@app.get("/api/penempatan")
def penempatan():
    return jsonify(PENEMPATAN)

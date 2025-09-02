import os
import json
import uuid
import hashlib
from datetime import datetime, timedelta
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

DATA_FILE = "pastes.json"
LINK_FILE = "list_link.txt"

# -----------------------
# Helper Functions
# -----------------------
def load_pastes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
        except:
            return []

def save_pastes(pastes):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(pastes, f, indent=2, ensure_ascii=False)

def add_link(paste_id):
    link = f"/paste/{paste_id}"
    with open(LINK_FILE, "a", encoding="utf-8") as f:
        f.write(link + "\n")

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def check_expired(paste):
    if paste["expire"] == "never":
        return False
    try:
        expire_time = datetime.fromisoformat(paste["expire_time"])
        return datetime.now() > expire_time
    except:
        return False

def format_expire(expire_str, created_at):
    if expire_str == "never":
        return "Tidak Expire"
    mapping = {"10m": "10 Menit", "1h": "1 Jam", "1d": "1 Hari"}
    return mapping.get(expire_str, "Tidak Dikenal")

# -----------------------
# Routes
# -----------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "Anonim")
        content = request.form.get("content", "")
        language = request.form.get("language", "text")
        expire = request.form.get("expire", "never")

        use_password = request.form.get("use_password")
        password = request.form.get("password") if use_password else ""
        password_hash = hash_password(password) if password else ""

        paste_id = str(uuid.uuid4())[:8]

        # expire time
        expire_time = None
        if expire == "10m":
            expire_time = datetime.now() + timedelta(minutes=10)
        elif expire == "1h":
            expire_time = datetime.now() + timedelta(hours=1)
        elif expire == "1d":
            expire_time = datetime.now() + timedelta(days=1)

        paste = {
            "id": paste_id,
            "name": name,
            "content": content,
            "language": language,
            "expire": expire,
            "expire_time": expire_time.isoformat() if expire_time else "never",
            "password": password_hash,
            "created_at": datetime.now().isoformat()
        }

        pastes = load_pastes()
        pastes.append(paste)
        save_pastes(pastes)
        add_link(paste_id)

        # tampilkan link hasil paste
        paste_link = url_for("view_paste", paste_id=paste_id, _external=True)
        return render_template("success.html", paste_link=paste_link)

    return render_template("index.html")

@app.route("/paste/<paste_id>", methods=["GET", "POST"])
def view_paste(paste_id):
    pastes = load_pastes()
    paste = next((p for p in pastes if p["id"] == paste_id), None)

    if not paste:
        return render_template("not_found.html", message="Paste tidak ditemukan."), 404

    if check_expired(paste):
        return render_template("not_found.html", message="Paste sudah expired."), 410

    # Jika ada password
    if paste["password"]:
        if request.method == "POST":
            input_pass = request.form.get("password", "")
            if hash_password(input_pass) == paste["password"]:
                return render_template(
                    "view_paste.html",
                    paste_id=paste["id"],
                    name=paste["name"],
                    content=paste["content"],
                    language=paste["language"],
                    lang_class=f"language-{paste['language']}",
                    expire_str=format_expire(paste["expire"], paste["created_at"])
                )
            else:
                return render_template("password_prompt.html", error="Password salah.")
        else:
            return render_template("password_prompt.html")

    # Jika tidak ada password
    return render_template(
        "view_paste.html",
        paste_id=paste["id"],
        name=paste["name"],
        content=paste["content"],
        language=paste["language"],
        lang_class=f"language-{paste['language']}",
        expire_str=format_expire(paste["expire"], paste["created_at"])
    )

@app.route("/list", methods=["GET"])
def list_links():
    pastes = load_pastes()
    items = []
    for p in pastes:
        items.append({
            "id": p["id"],
            "name": p["name"],
            "language": p["language"],
            "expire": format_expire(p["expire"], p["created_at"]),
            "link": url_for("view_paste", paste_id=p["id"])
        })
    return render_template("list_links.html", items=items)

# -----------------------
# Main
# -----------------------
if __name__ == "__main__":
    app.run(debug=True)
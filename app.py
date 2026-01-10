from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import os
import hashlib
import secrets
from user import User

app = Flask(__name__)
# Gizli anahtarı koda gömmek yerine ortam değişkeninden okuyun.
# Windows'ta örnek: set FLASK_SECRET_KEY=<SECRET_KEY_PLACEHOLDER>
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)

# Excel yerine CSV kullanarak openpyxl bağımlılığını tamamen kaldırıyoruz.
FILE_NAME = "users.csv"
COLUMNS = ["first_name", "last_name", "email", "password", "age"]


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def _ensure_user_store_exists() -> None:
    """Veri dosyası yoksa, doğru kolonlarla oluşturur."""
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(FILE_NAME, index=False, encoding="utf-8")


def load_users():
    _ensure_user_store_exists()

    df = pd.read_csv(FILE_NAME, dtype=str, keep_default_na=False, encoding="utf-8")

    # Kolonlar eksik/bozuksa toparla (uzun vadede daha dayanıklı)
    for col in COLUMNS:
        if col not in df.columns:
            df[col] = ""

    users = []
    for _, row in df.iterrows():
        users.append(
            User(
                row.get("first_name", ""),
                row.get("last_name", ""),
                row.get("email", ""),
                row.get("password", ""),
                row.get("age", ""),
            )
        )
    return users


def append_user(user_dict: dict) -> None:
    """Yeni kullanıcıyı CSV'ye ekler."""
    _ensure_user_store_exists()

    df = pd.read_csv(FILE_NAME, dtype=str, keep_default_na=False, encoding="utf-8")
    df_new = pd.DataFrame([user_dict], columns=COLUMNS)
    df = pd.concat([df, df_new], ignore_index=True)
    df.to_csv(FILE_NAME, index=False, encoding="utf-8")


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fname = request.form["name"].strip()
        lname = request.form["surname"].strip()
        email = request.form["email"].strip().lower()
        password = hash_password(request.form["password"])
        age = request.form["age"].strip()

        users = load_users()
        if any((u.email or "").strip().lower() == email for u in users):
            flash("Bu e-posta zaten kayıtlı!", "danger")
            return redirect(url_for("register"))

        new_user = {
            "first_name": fname,
            "last_name": lname,
            "email": email,
            "password": password,
            "age": age,
        }
        #templates
        append_user(new_user)

        flash("Başarıyla kayıt oldunuz!", "success")
        return redirect(url_for("/login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip().lower()
        password = hash_password(request.form["password"])

        users = load_users()
        for u in users:
            if (u.email or "").strip().lower() == email and u.password == password:
                flash(f"Hoş geldin {u.first_name}!", "success")
                return redirect(url_for("/index"))
            else:
                flash("E-posta veya şifre hatalı!", "danger")
                return redirect(url_for("login"))

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
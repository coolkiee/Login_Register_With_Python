import pandas as pd
import os
import hashlib
from user import User


class UserManager:
    # Kolon isimleri app.py ile birebir aynı
    _COLUMNS = ['first_name', 'last_name', 'email', 'password', 'age']

    def __init__(self, file_name="users.csv"):
        self.file_name = file_name
        self.users = self._load_users()

    @staticmethod
    def _hash_password(password):
        """Şifreyi SHA256 ile hashler."""
        return hashlib.sha256(password.encode()).hexdigest()

    def _load_users(self):
        """CSV dosyasından kullanıcıları yükler."""
        if not os.path.exists(self.file_name):
            return []
        try:
            # CSV
            df = pd.read_csv(self.file_name, dtype=str, keep_default_na=False, encoding="utf-8")

            return [
                User(row['first_name'], row['last_name'], row['email'], row['password'], row['age'])
                for _, row in df.iterrows()
            ]
        except Exception:
            return []

    def _save_users(self):
        """Kullanıcı listesini CSV dosyasına kaydeder."""
        try:
            user_data = []
            for u in self.users:
                user_data.append({
                    'first_name': u.first_name,
                    'last_name': u.last_name,
                    'email': u.email,
                    'password': u.password,
                    'age': u.age
                })
            df = pd.DataFrame(user_data, columns=self._COLUMNS)
            df.to_csv(self.file_name, index=False, encoding="utf-8")
        except Exception as e:
            print(f"CSV Kayıt Hatası: {e}")

    def check_email_exists(self, email):
        """E-posta adresi sistemde var mı kontrol eder."""
        email = email.strip().lower()
        return any((user.email or "").strip().lower() == email for user in self.users)

    def register_user(self, first_name, last_name, email, password, age):
        """Yeni kullanıcı kaydeder. E-posta varsa False döner."""
        if self.check_email_exists(email):
            return False

        hashed_password = self._hash_password(password)
        new_user = User(first_name, last_name, email, hashed_password, age)
        self.users.append(new_user)
        self._save_users()
        return True

    def login(self, email, password):
        """Giriş kontrolü yapar. Başarılıysa kullanıcı nesnesini, değilse None döner."""
        email = email.strip().lower()
        hashed_password = self._hash_password(password)

        for user in self.users:
            if (user.email or "").strip().lower() == email and user.password == hashed_password:
                return user
        return None
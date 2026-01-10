import pandas as pd
import os 
import hashlib
from user import User

class UserManager:

    _COLUMNS = ['first_name', 'last_name', 'email', 'password', 'age']

    def __init__(self, file_name="users.xlsx"):
        self.file_name = file_name
        self.users = self._load_users()

    @staticmethod
    def _hash_password(password):
        """Hashes the given password with SHA256."""
        return hashlib.sha256(password.encode()).hexdigest()
 
    def _load_users(self):
        if not os.path.exists(self.file_name):
            try:
                df = pd.DataFrame(columns=self._COLUMNS)
                df.to_excel(self.file_name, index=False)
                return []
            except IOError:
                return []
        try:
            df = pd.read_excel(self.file_name)
           
            if not all(col in df.columns for col in self._COLUMNS):
                
                return []
            return [
                User(row['first_name'], row['last_name'], row['email'], row['password'], row['age'])
                for _, row in df.iterrows()
            ]
        except Exception:
            return []

    def _save_users(self):
        try:
            user_data = [vars(u) for u in self.users]
            df = pd.DataFrame(user_data, columns=self._COLUMNS)
            df.to_excel(self.file_name, index=False)
        except IOError:
            pass

    def check_email_exists(self, email):
        return any(user.email == email for user in self.users)

    def register_user(self, first_name, last_name, email, password, age):
        
        if self.check_email_exists(email):
            return False  

        hashed_password = self._hash_password(password)
        new_user = User(first_name, last_name, email, hashed_password, age)
        self.users.append(new_user) 
        self._save_users()
        return True  

    def login(self, email, password):

        hashed_password = self._hash_password(password)
        for user in self.users:
            if user.email == email and user.password == hashed_password:
                return True  
        return False
    #templates
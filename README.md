# 🚀 Django Setup Guide (Windows CMD)

This guide walks you through setting up a Django project using **Windows Command Prompt (CMD)**.

---

## 📌 1. Create a Virtual Environment (CMD)
```cmd
python -m venv <yourVirtualEnvName>
```

---

## 📌 2. Activate the Virtual Environment (CMD)
```cmd
<yourVirtualEnvName>\Scripts\activate
```

After activation, you should see **<yourVirtualEnvName>** before your command prompt.

---

## 📌 3. Install Django (CMD)
```cmd
pip install django
```

---

## 📌 4. Create a New Django Project (CMD)
```cmd
django-admin startproject <projectName>
```

---

## 📌 5. Navigate Into Your Project Folder (CMD)
```cmd
cd <projectName>
```

---

## 📌 6. Run the Development Server (CMD)
```cmd
python manage.py runserver
```

Your project will be available at:  
👉 http://127.0.0.1:8000/

---

## 📌 7. Create a Django App (CMD)
```cmd
django-admin startapp <yourAppName>
```

---

## ✅ You're All Set!

You now have:

- A virtual environment  
- Django installed  
- A Django project created  
- A Django app ready to develop  

Happy coding! 🎉
# 📄 get-papers-list-ramesh  

### Fetch PubMed Papers & Identify Non-Academic Authors  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Manager-orange)

## 📌 Overview  
This project fetches **research papers** from **PubMed** based on a user-specified query, identifies papers with at least one **pharmaceutical/biotech-affiliated author**, and exports the results as a CSV file.  

### ✨ Features  
✔ Fetch research papers using the **PubMed API**  
✔ Filter papers by **non-academic authors** (biotech/pharma)  
✔ Export results as a **CSV file**  
✔ Supports **command-line options** (`-h`, `-d`, `-f`)  
✔ **Published on TestPyPI**  

---

## 🚀 Installation  

### **1️⃣ Install Python (3.8+)**  
Ensure you have Python installed. You can check your version with:  
```sh
python --version
```

### **2️⃣ Install Poetry (Dependency Manager)**  
```sh
pip install poetry
```

### **3️⃣ Install the Package from TestPyPI**  
```sh
pip install -i https://test.pypi.org/simple/ get-papers-list-ramesh
```

### **4️⃣ Clone the Repository (If Running Locally)**  
```sh
git clone https://github.com/yourusername/get-papers-list.git
cd get-papers-list
poetry install
```

---

## 📌 Usage  

### **Basic Command**  
```sh
get-papers-list "cancer therapy"
```

### **Save Output to CSV**  
```sh
get-papers-list "cancer therapy" -f results.csv
```

### **Enable Debug Mode**  
```sh
get-papers-list "cancer therapy" -d
```

### **Show Help Menu**  
```sh
get-papers-list -h
```

---

## 🏗 Project Structure  
```
get-papers-list/
│── papers_fetcher/       
│   ├── __init__.py      
│   ├── fetch.py         
│   ├── filter.py         
│   ├── export.py         
│── cli.py                
│── tests/                
│── pyproject.toml        
│── README.md             
│── poetry.lock           
│── .gitignore            
```

---

## 🛠 Dependencies  
This project uses the following libraries:  

- [`requests`](https://pypi.org/project/requests/) - For making API calls  
- [`pandas`](https://pypi.org/project/pandas/) - For handling tabular data  
- [`argparse`](https://pypi.org/project/argparse/) - For command-line arguments  
- [`lxml`](https://pypi.org/project/lxml/) - For XML processing  

All dependencies are managed via **Poetry**.

---

## 🛠 Development & Contribution  
### **Setup Development Environment**  
```sh
git clone https://github.com/yourusername/get-papers-list.git
cd get-papers-list
poetry install
```

### **Run Tests** (If Implemented)  
```sh
pytest tests/
```

### **Publish to TestPyPI (For Maintainers)**  
```sh
poetry build
poetry publish -r testpypi
```

---

## 📜 License  
This project is licensed under the **MIT License**.

---

## 🌐 Project Link  
🔗 **TestPyPI Package:** [get-papers-list-ramesh](https://test.pypi.org/project/get-papers-list-ramesh/)  
🔗 **GitHub Repo:** [your-github-repo-link](https://github.com/yourusername/get-papers-list)  

---

## 📧 Contact  
For any issues or feature requests, please raise an **Issue** on GitHub.  
```


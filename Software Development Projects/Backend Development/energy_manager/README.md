
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)  
![License](https://img.shields.io/badge/License-MIT-green.svg)  
![Status](https://img.shields.io/badge/Status-Active-success)  
![Last Commit](https://img.shields.io/github/last-commit/yourusername/energy-manager)  
![Issues](https://img.shields.io/github/issues/yourusername/energy-manager)  
![Pull Requests](https://img.shields.io/github/issues-pr/yourusername/energy-manager)  

---
# ⚡ Energy Manager App

The **Energy Manager App** is a Python-based tool that helps users monitor and manage home energy consumption.  
The tool is designed to build your energy consumption profile from an atomic level, so as to provide the most accurate result and insghts.
It calculates the cost of running household devices and provides **AI-powered insights** on how to optimize energy usage.
The AI integration is built on Microsft's Semantic Kernel chat completion function, So, it is still crude.

---
# 💡 Backstory

One evening, while reviewing the mounting energy bills for our family home and small business. Despite turning off lights, shifting usage to off-peak hours, and installing basic monitoring, costs kept climbing. It became clear that, much like with money, it's the small, continuous expenses that silently add up.

This realization sparked an idea: to measure and analyze energy consumption on a granular, second-by-second basis. This wouldn't just be about tracking usage; it would be about finding and highlighting those "little expenses" that were draining our wallets.

Around the same time, I completed my Microsoft AI engineering certification. I saw an opportunity to integrate what I'd learned into this project, using AI to not only collect data but also to identify patterns and suggest actionable, personalized solutions for reducing energy consumption.

What started as a personal quest to help my family became the foundation for this tool. I hope it helps you and your family gain control over your energy usage and, in turn, your bills.

---

## 🚀 Features
- 🔹 Calculate **cost per second, per hour, and per month** for any device  
- 🔹 Save and load device usage history in **JSON format**  
- 🔹 **Summarize total energy cost** of all devices  
- 🔹 Get **AI-generated recommendations** on energy efficiency  
- 🔹 Simple **command-line interface (CLI)** for easy interaction  
---

## 🛠️ Tech Stack
- **Python 3.9+**
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) – AI integration
- OpenAI API (GPT models)
- JSON for data storage

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/energy-manager.git
   cd energy-manager
````

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set your OpenAI API key**
   In `energy_manager.py`, replace:

   ```python
   api_key = "your_openai_api_key"
   ```

   with your actual key, or load it from environment variables for security:

   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

You’ll see an interactive menu:

```
===== Energy Manager Menu =====
1. Show consumption per second
2. Show consumption per hour
3. Show consumption per month
4. Calculate total cost of all devices
5. Get AI-generated feedback on consumption
0. Exit
```

---

## 📊 Example

```
Enter device name: Refrigerator
Enter number of this device: 1
Enter power rating of device in watts (W): 150
Enter your currency: $
Enter electricity cost per kWh: 0.15

Using Refrigerator costs $ 0.0000416667 per second.
```

---

## 🔮 Roadmap

* [ ] Add **unit tests** with `pytest`
* [ ] Build a **GUI interface** (Tkinter / PyQt)
* [ ] Data **visualizations with charts**
* [ ] Cloud sync for energy data
* [ ] Mobile app (Flutter/React Native frontend)

---

## 📜 License
This repository is licensed under the **MIT License** – you are free to use, modify, and build upon these concepts, provided proper attribution is given.  
*(You may update the license type if you prefer more restrictive terms.)*

---

## 🤝 Contributing
Contributions are welcome! Please fork the repo and submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License** – free to use and modify.

---

## 👨‍💻 Author

Developed by **\[4syT Labs]**
🔗 [LinkedIn](https://linkedin.com/in/bunaminadams) | [GitHub](https://github.com/Iam4syT)

---

## 📧 Contact
Created and maintained by **Bunamin Adams (4syt Integrated Solution)**  
- 🌐 [think4syt.com](https://think4syt.com)  
- ✉️ [bunamin@think4syt.com] 

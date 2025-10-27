# Smart Data Automation
### IoT-based Industry 4.0 Automation Project

This project demonstrates how sensor data from an ESP32 microcontroller can be processed, stored, and automated using Python, MySQL, and n8n on a Proxmox-based server infrastructure.

---

## 🔧 Architecture Overview

**Components:**
- Proxmox host running Ubuntu Server VM
- ESP32 WROOM (temperature sensor)
- Python API to receive and store sensor data
- MySQL database for persistent storage
- n8n workflows for automation and visualization
- Optional: AI analysis via Deepseek API

---

## 🧠 Goals
- Demonstrate integration of hardware and software automation  
- Showcase DevOps-oriented setup and scripting skills  
- Present real-world Industry 4.0 workflow  

---

## ⚙️ System Setup
| Component | Technology |
|------------|-------------|
| Virtualization | Proxmox VE |
| Server OS | Ubuntu 22.04 |
| Database | MySQL |
| Workflow Automation | n8n |
| Hardware | ESP32 WROOM |
| Scripting | Python 3 |
| Visualization | n8n Dashboard / Flask |

---

## 📊 Data Flow
ESP32 → Python API → MySQL → n8n → Dashboard/Notifications

![Architecture Diagram](docs/architecture.png)

---

## 🚀 Quick Start
```bash
git clone https://github.com/up-44/smart-data-automation.git
cd python
pip install -r requirements.txt
python receiver.py

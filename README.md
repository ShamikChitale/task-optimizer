# 🧠 Daily Task Optimizer

> An intelligent productivity assistant that recommends the **best combination of daily tasks** using **prescriptive analytics** and the **knapsack optimization model**.

---

## 🎯 The Problem

Students and professionals often struggle with packed schedules and limited time. Choosing *which* tasks to prioritize becomes stressful and inefficient — especially when tasks have different durations, importance levels, and deadlines.

Without a structured decision model, people tend to:

- Waste time on low-value tasks  
- Underestimate how long tasks will take  
- Fail to select the optimal mix of tasks  
- Reduce productivity due to poor prioritization  

This leads to stress, missed deadlines, and lower performance.

---

## 💡 The Solution

**Daily Task Optimizer** applies *prescriptive analytics* to help you make smarter daily decisions.

Using the **0/1 knapsack optimization model**, the app:

- Selects the **best combination of tasks** given your available time  
- Maximizes total **productivity score** (task importance)  
- Creates a **timeline schedule**  
- Generates **what-if scenarios** for different time budgets  

Your daily planning becomes a mathematical optimization — not guesswork.

---

## 🚀 Live Demo

👉 **Try the live app:**  
https://task-optimizer-udtmhvby4egwtchvxn2uxt.streamlit.app

*(Insert a real screenshot here once you capture one)*  
`![Screenshot of the app](screenshot.png)`

---

## ⚙️ How It Works

### 1. **User Inputs Availability**
You tell the system how many hours you have today.

### 2. **Add Tasks**
For each task, you enter:
- Task name  
- Time required  
- Importance (1–5)  
- Category (Work, School, Personal, Health, Other)

### 3. **Optimization Engine**
Using brute-force knapsack logic (`itertools`), the app finds the **highest-value combination** of tasks that fits within your time.

### 4. **Recommendations**
The app outputs:
- ✔️ Tasks to complete  
- ❌ Tasks to postpone  
- ⏱️ Time used vs available  
- ⭐ Productivity score  
- 📅 Timeline (Gantt-style)  
- 🔍 What-If Analysis  

---

## 🔬 The Analytics Behind It

### **Data Used**
User-entered task list with:
- Name  
- Duration  
- Importance  
- Category  

### **Model Used**
**Binary Knapsack Optimization**
- Each task → binary variable  
- Objective → maximize importance  
- Constraint → total time ≤ available time  

### **Recommendation Logic**
- Generate all task combinations  
- Filter feasible options  
- Select combination with max total importance  
- Generate schedule + insights  

---

## 📊 Example Output

**Recommended Tasks**
- Study for Exam — 3 hours — Importance 5  
- Work Project — 2 hours — Importance 4  
- Gym — 1 hour — Importance 3  

**Postponed Tasks**
- Laundry  
- Grocery Shopping  

**Total Productivity Score:** 12  
**Time Used:** 6 / 8 hours  

**What-If Analysis**
- 1 hour less → Score = 9  
- 1 hour extra → Score = 13  
- 2 hours extra → Score = 15  

---

## 🛠️ Technology Stack

- **Frontend:** Streamlit  
- **Optimization:** Python (itertools brute-force knapsack)  
- **Data Handling:** Pandas  
- **Visualization:** Streamlit components  
- **Hosting:** Streamlit Cloud  
- **Version Control:** GitHub  

---

## 🎓 About This Project

Built for **ISOM 839 – Prescriptive Analytics**  
Sawyer Business School, **Suffolk University**

**Author:** Shamik Chitale  
**LinkedIn:** https://linkedin.com/in/shamikchitale  
**Email:** shamik.chitale@su.suffolk.edu  

---

## 🔮 Future Possibilities

Potential enhancements include:

- NLP to automatically extract tasks from text  
- Machine-learning prediction for task duration  
- Multi-day scheduling with rolling optimization  
- Deadline + urgency scoring  
- Google Calendar integration  
- Personalized learning from user behavior  

---

# 🚀 Satellite Signal Performance Analysis Dashboard  
### Machine Learning-Based Satellite Communication Monitoring & Signal Analysis System  

📡 An ML-driven system for predictive satellite signal monitoring, performance analysis, and intelligent decision-making.

---

## 📑 Table of Contents

- [📌 Overview](#-overview)
- [❗ Problem Statement](#-problem-statement)
- [🎯 Objectives](#-objectives)
- [🛰️ System Architecture](#-system-architecture)
- [📊 Dataset Description](#-dataset-description)
- [⚙️ Methodology](#️-methodology)
- [🧠 Machine Learning Model](#-machine-learning-model)
- [📈 Dashboard & Visualization](#-dashboard--visualization)
- [📊 Results & Performance](#-results--performance)
- [🔍 Key Insights](#-key-insights)
- [🛰️ Satellite Behavior Analysis](#️-satellite-behavior-analysis)
- [📉 Quadrant Analysis](#-quadrant-analysis)
- [🧪 Engineering Interpretation](#-engineering-interpretation)
- [🌍 Applications](#-applications)
- [🔮 Future Scope](#-future-scope)
- [📂 Project Structure](#-project-structure)
- [⚙️ Tech Stack](#️-tech-stack)
- [📚 References](#-references)

---

## 📌 Overview

Satellite communication forms the backbone of global connectivity, enabling weather forecasting, navigation, broadcasting, and defense systems.

This project focuses on **analyzing and predicting satellite signal performance** using Machine Learning techniques based on:

- Signal Strength (dBm)  
- Elevation Angle (Degrees)  
- Packet Transmission Data  

📊 The goal is to move from **reactive monitoring → predictive intelligence**.

---

## ❗ Problem Statement

Traditional satellite monitoring systems face major challenges:

- ⚠️ Manual and reactive monitoring  
- ⏱️ Delay in detecting signal degradation  
- 💰 High operational costs (OPEX)  
- 🧠 Lack of predictive intelligence  

👉 Result: Reduced Quality of Service (QoS) and inefficiency in communication systems. :contentReference[oaicite:0]{index=0}  

---

## 🎯 Objectives

- 🔹 Develop predictive ML models for signal strength  
- 🔹 Analyze key influencing parameters  
- 🔹 Detect anomalies and signal degradation  
- 🔹 Build interactive dashboards for insights  

---

## 🛰️ System Architecture
Data Collection → Data Processing → ML Model → Visualization Dashboard

### 🔄 Pipeline Breakdown

- 📥 Data Sources: Kaggle RF Dataset, SatNOGS  
- 🧹 Preprocessing: Cleaning, normalization  
- 🧠 Model: Random Forest Regression  
- 📊 Output: Tableau Dashboard  

---

## 📊 Dataset Description

### 📁 Data Sources

- Kaggle RF Dataset  
- SatNOGS Database  
- Satellite Quality Insights  

### 📌 Features Used

| Parameter            | Description                          |
|---------------------|--------------------------------------|
| Signal Strength     | Power level (dBm)                   |
| Elevation Angle     | Satellite position (Degrees)        |
| Packets Processed   | Data transmission rate             |

---

## ⚙️ Methodology

1. Data Cleaning & Normalization  
2. Feature Selection  
3. Model Training  
4. Performance Evaluation  

📊 Data Split: **80% Training / 20% Testing**

---

## 🧠 Machine Learning Model

### 🌲 Random Forest Regression

- Handles **non-linear relationships**
- Captures **complex signal patterns**
- Provides **high prediction accuracy**

📈 Evaluation Metric:
- R² Score (Coefficient of Determination)

---

## 📈 Dashboard & Visualization

Interactive dashboard built using Tableau:

### 📊 Key Components

- Signal Strength Distribution  
- Elevation vs Signal Scatter Plot  
- Satellite-wise Filtering  
- KPI Performance Metrics  

📌 Example Insights:
- Avg Signal: **~ -49 dBm**
- Best Case: **~ -43 dBm**
- Worst Case: **~ -55 dBm**

---

## 📊 Results & Performance

- Model successfully predicted signal trends across **30 satellites**
- Captured non-linear behavior effectively  
- Achieved reliable baseline prediction accuracy  

---

## 🔍 Key Insights

- 📈 Strong correlation between elevation and signal strength  
- ⚠️ Signal anomalies due to RF interference  
- 📊 Most signals cluster around **-49 dBm (stable zone)**  
- 🔄 Signal behavior is highly **non-linear**  

---

## 🛰️ Satellite Behavior Analysis

| Satellite Type | Behavior |
|---------------|---------|
| NOAA          | Stable and predictable |
| ISS           | Highly dynamic |
| CubeSats      | Weak signals |
| INSAT/GSAT    | High stability & traffic |

👉 Elevation angle remains the **dominant predictor** across all categories. :contentReference[oaicite:1]{index=1}  

---

## 📉 Quadrant Analysis

Signal categorized using:

- X-axis → Elevation Angle  
- Y-axis → Signal Strength  

### Zones:

- 🟢 Optimal → High elevation + strong signal  
- 🟡 Favorable → Low elevation but good signal  
- 🔴 Risk → Weak signal despite high elevation  
- ⚠️ Attention → Low elevation + weak signal  

---

## 🧪 Engineering Interpretation

### 📡 Key Physical Factors

- Higher elevation → Less atmospheric loss  
- Weather & RF interference → Signal degradation  

### 🤖 ML Contribution

- Detects hidden patterns  
- Enables predictive monitoring  
- Reduces dependency on manual systems  

---

## 🌍 Applications

- 📡 Satellite Communication Optimization  
- 🚨 Disaster Monitoring Systems  
- 🌐 Satellite IoT (SIoT)  
- 🛡️ Defense & Surveillance  

---

## 🔮 Future Scope

- 🔹 LSTM for time-series prediction  
- 🔹 Reinforcement Learning for optimization  
- 🔹 Edge Computing (Raspberry Pi / FPGA)  
- 🔹 5G/6G Satellite Integration  

---

## 📂 Project Structure

---

## ⚙️ Tech Stack

- Python (Pandas, NumPy, Scikit-learn)  
- Tableau  
- Data Analysis & Visualization  

---

## 📚 References

- IEEE Research Papers on Satellite ML  
- SatNOGS Open Database  
- Kaggle RF Dataset  
- IQT Labs RF Classification  

---

## ✨ Conclusion

This project demonstrates how Machine Learning transforms satellite systems from:

➡️ Reactive → Predictive  
➡️ Manual → Automated  
➡️ Delayed → Real-time  

📡 Enabling smarter, more efficient global communication systems.

End-to-end pipeline:

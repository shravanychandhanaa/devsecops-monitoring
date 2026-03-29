# 🔐 DevSecOps Monitoring Platform

## 📌 Project Overview
This project is a **DevSecOps Monitoring Platform** that tracks and visualizes security vulnerabilities from CI/CD pipelines. It integrates security scanning, data processing, and dashboard visualization to provide actionable insights.

---

## 🚀 Problem Statement
- Security scans generate large amounts of data but lack visibility  
- No tracking of vulnerability trends over time  
- Difficult to measure security improvement  

---

## 🎯 Objectives
- Track vulnerabilities over time  
- Visualize severity distribution  
- Enable proactive security decisions  

---

## 🏗️ Architecture

GitHub Actions → JSON Reports → Render API → Grafana Dashboard

---

## ⚙️ Tools & Technologies
- GitHub (CI/CD & scan storage)  
- Trivy (Security scanning)  
- Python (Flask API)  
- Render (API hosting)  
- Grafana (Dashboard & visualization)  

---

## 🔄 Workflow
1. Run security scan using GitHub Actions  
2. Store scan results as JSON  
3. Fetch and parse JSON using Python API  
4. Visualize processed data in Grafana  

---

## 📊 Features
- Vulnerability count by severity (Critical, High, Medium)  
- Pie chart for severity distribution  
- Alerting for high-risk vulnerabilities  
- Live dashboard updates  

---

## 📈 Dashboard Panels

### 📊 Vulnerability Count
Displays total vulnerabilities categorized by severity.

### 🥧 Severity Distribution
Pie chart showing proportion of vulnerabilities.

### 🚨 Alerts
Triggers alert when:

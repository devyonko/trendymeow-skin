<div align="center">

# 🌸 K13 Skin Studio

<a href="https://www.trendymeow.shop">
  <img src="https://readme-typing-svg.herokuapp.com?font=M+PLUS+Rounded+1c&weight=800&size=30&duration=4000&pause=1000&color=F75C7E&center=true&vCenter=true&width=500&lines=Create+Custom+Phone+Skins;Anime+Aesthetic+UI;Precision+Oppo+K13+Cutouts;Print+Ready+A4+PDF" alt="Typing SVG" />
</a>

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://www.trendymeow.shop)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Style](https://img.shields.io/badge/Style-Anime%20Aesthetic-pink?style=for-the-badge&logo=dribbble&logoColor=white)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<br>

**The ultimate tool for creating DIY custom back skins for the Oppo K13 / K12x series.** *Upload Art. Align. Print.*

[🔴 **Launch Live App**](https://www.trendymeow.shop) · [🐞 Report Bug](https://github.com/yourusername/trendymeow-skin/issues) · [✨ Request Feature](https://github.com/yourusername/trendymeow-skin/issues)

</div>

---

## 🎐 About The Project

**K13 Skin Studio** is a web application designed to solve a specific problem: mobile skins are expensive and hard to find for specific models. This app allows anyone to create professional-grade skins at home using a standard A4 printer and a sticker sheet.

It features a **"Your Name" (Kimi no Na wa)** inspired interface, complete with falling sakura petals, glassmorphism UI, and Japanese typography.

### 📸 Preview
![App Screenshot](https://via.placeholder.com/800x400.png?text=Use+Screenshot+of+Your+App+Here)

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| 🌸 **Anime UI** | A fully animated interface with falling sakura petals and a dynamic sky gradient. |
| 📐 **Precision Cutouts** | Exact engineered dimensions for the **Oppo K13** camera module (19mm & 8mm sensors). |
| 🖨️ **A4 Print Ready** | Generates a 300 DPI PDF centered on an A4 page with a **5cm scale check line**. |
| 🎛️ **Live Calibration** | Sidebar sliders let you nudge the holes (X/Y axis) by millimeters for a perfect fit. |
| 🖼️ **Auto-Scaling** | Upload any image aspect ratio; the smart engine fills the skin frame automatically. |

---

## 🚀 Quick Start

To run this application locally on your machine, follow these steps.

### Prerequisites

* Python 3.8+
* Pip

### Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/yourusername/trendymeow-skin.git](https://github.com/yourusername/trendymeow-skin.git)
    cd trendymeow-skin
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app**
    ```bash
    streamlit run app.py
    ```

---

## 🛠️ Tech Stack

* **Frontend & Logic:** [Streamlit](https://streamlit.io/)
* **Image Processing:** [Pillow (PIL)](https://python-pillow.org/)
* **Styling:** Custom CSS3 & Keyframe Animations
* **Fonts:** Google Fonts (Potta One, M PLUS Rounded 1c)

---

## 🎨 Layout Specifications

If you are modifying the code for a different phone, here are the variable references in `app.py`:

```python
# Oppo K13 / K12x Dimensions (mm)
PHONE_W_MM = 76.1
PHONE_H_MM = 163.2

# Camera Module
R_BIG = 9.5         # Radius of big lens
GAP_LEFT_VERT = 2.5 # Vertical gap between big lenses
GAP_HORIZ = 6.0     # Horizontal gap between columns

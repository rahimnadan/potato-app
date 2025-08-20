
# 🍃 Potato Leaf Disease Classification

An interactive web application built with **Streamlit** that classifies potato leaf diseases using a trained YOLOv5 model deployed via the **Roboflow API**.
This project helps farmers and researchers quickly detect crop diseases, enabling timely action to protect yields.

---

## 🚀 Features

* 🌿 **Potato Leaf Disease Detection** – Upload a potato leaf image and get disease predictions with confidence scores.
* 🖼️ **User-Friendly Interface** – Built using Streamlit with a clean, modern design.
* 📊 **Model Performance** – Achieves **98% accuracy** on test data.
* 📦 **Easy Deployment** – Lightweight, runs anywhere with Python + Streamlit.
* 🔗 **Tabs for Navigation** – Home, Project Info, and About Us sections.
* 📱 **Responsive Layout** – Works on desktop and mobile.

---

## 📂 Project Structure

```bash
Potato-Leaf-Disease-Classification/
│── app.py              # Main Streamlit app
│── requirements.txt    # Project dependencies
│── README.md           # Documentation
```

---

## 🛠️ Tech Stack

* **Frontend & Deployment**: Streamlit
* **Model**: YOLOv5 (trained on PlantVillage dataset)
* **Backend API**: Roboflow Inference API
* **Libraries**: Pillow, Requests, Streamlit

---

## 📊 Dataset

* **Name**: PlantVillage
* **Description**: A large dataset of healthy and diseased plant leaves used for agricultural disease classification.
* **Classes**: Potato leaf disease stages (including blight).

---

## ⚡ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rahimnadan/Potato-Leaf-Disease-Classification.git
cd Potato-Leaf-Disease-Classification
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

The app will open in your browser at **[http://localhost:8501](http://localhost:8501)** 🎉

---

## 🖼️ Usage

1. Navigate to the **Home** tab.
2. Upload an image of a potato leaf (`.jpg`, `.jpeg`, `.png`).
3. Click **Predict** to classify the disease.
4. View results with confidence percentages.




## 📬 Contact

For queries or collaborations:
📞 **+92 3251556457**
🔗 [LinkedIn – Abdur Rahim](https://www.linkedin.com/in/abdur-rahim-718ba4227)

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify with attribution.


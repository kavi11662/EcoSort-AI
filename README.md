# EcoSort-AI ♻️  
### Intelligent Waste Segregation System  

EcoSort-AI is an AI-powered waste classification and segregation system built to identify waste categories and provide eco-friendly disposal suggestions. Its goal is to foster **green skills**, align with sustainability goals, and support the internship project by Edunet + AICTE + Shell.

---

## 🚀 Features  
- Deep-learning image classification for waste: metal, organic, paper, plastic  
- Stylish Streamlit interface with modern UI  
- Upload or camera input (planned upgrade)  
- Audio tips: the system *speaks* eco-friendly disposal suggestions  
- Progress bar & impact estimator: shows how your disposal helps the environment  
- Downloadable model and dataset for customization and reuse  

---

## 🧠 Model  
The trained model is based on a Convolutional Neural Network (CNN) and saved in `.h5` format.  
**Download the trained model here:**  
[Download .h5 Model](https://drive.google.com/file/d/1EVplF4V5lNQNl8ldCP4KZIut3pB7JyrM/view?usp=sharing)  

✅ After download, place the `EcoSortAI_model.h5` file inside the `model/` folder in your project.

---

## 📂 Dataset  
The dataset contains labeled images of waste categories (metal, organic, paper, plastic).  
**Download the dataset here:**  
[Download Dataset Folder](https://drive.google.com/drive/folders/1JtWjXr7LejjZYUZTwvtoqoeozl5XYWv8?usp=sharing)  

✅ After download, place the folder inside your project directory under `dataset/`.

---

## ⚙️ Installation  
Follow these steps to run the project locally:

bash
git clone https://github.com/kavi11662/EcoSort-AI.git
cd EcoSort-AI
pip install -r requirements.txt
streamlit run app.py





**Project folder structure in vscode**



EcoSort-AI/
│
├── app.py                # Streamlit main UI application  
├── requirements.txt      # Python dependencies  
├── model/                # Folder to store the trained model (.h5)  
│   └── EcoSortAI_model.h5  
├── dataset/              # Folder to store dataset images (optional local copy)  
│   ├── metal/  
│   ├── organic/  
│   ├── paper/  
│   └── plastic/  
└── README.md             # This file  

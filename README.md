# 🥔 Potato Leaf Disease Classification

A production-ready web application that uses deep learning to detect potato leaf diseases with **96.5% accuracy**. Help farmers identify Early Blight, Late Blight, and Healthy leaves in real-time.

![Potato Disease Classification](https://img.shields.io/badge/Accuracy-96.5%25-brightgreen)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68-blue)
![React](https://img.shields.io/badge/React-18-61dafb)

## 🚀 Features

- **Real-time Disease Detection**: Upload potato leaf images for instant classification
- **High Accuracy**: 96.5% test accuracy on three disease categories
- **Multi-Platform Deployment**: Docker containers + Google Cloud Functions
- **Production Ready**: Error handling, logging, and health monitoring
- **Farmer-Friendly**: Simple web interface accessible on any device

## 📊 Disease Classes

1. **Early Blight** - Alternaria solani
2. **Late Blight** - Phytophthora infestans  
3. **Healthy** - Disease-free potato leaves

## 🏗️ Architecture
Frontend (React)  -> FastAPI Gateway (Port 8001) -> TensorFlow Serving (Port 8601) -> ML Model (SavedModel) -> Google Cloud Functions (Backup)


## 🛠️ Tech Stack

### Backend & ML
- **FastAPI** - High-performance API gateway
- **TensorFlow Serving** - Production model inference
- **TensorFlow/Keras** - Deep learning model
- **Google Cloud Functions** - Serverless backup

### Frontend
- **React.js** - User interface
- **Axios** - API communication

### Infrastructure
- **Docker** - Containerization
- **Google Cloud Platform** - Cloud deployment
- **Google Cloud Storage** - Model storage

## 📈 Model Performance

| Metric | Score |
|--------|-------|
| Test Accuracy | 96.52% |
| Validation Accuracy | 98.44% |
| Test Loss | 0.076 |
| Model Size | 1.06 MB |

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- TensorFlow 2.x
- Node.js 14+
- Docker

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/potato-leaf-disease-detection.git
cd potato-leaf-disease-detection
```

2. **Backend Setup**
```bash
cd docker-serving
pip install -r requirements.txt
```

3. **Start TensorFlow Serving**
```bash
docker build -t potato-model-serving .
docker run -p 8601:8601 potato-model-serving
```

4. **Start FastAPI Server**
```bash
python fastapi_app.py
```

5. **Frontend Setup**
```bash
cd frontend
npm install
npm start
```

## 🐳 Docker Deployment

**Build and Run**
```commandline
# Build the serving container
cd docker-serving
docker build -t potato-disease-app .

# Run the application
docker run -p 8001:8001 -p 8601:8601 potato-disease-app
```

## ☁️ Google Cloud Deployment

**Deploy to Cloud Functions**
```commandline
cd gcp
gcloud functions deploy predict-potato-disease \
    --runtime python38 \
    --trigger-http \
    --allow-unauthenticated \
    --memory 2048MB
```

**Upload Model to GCS**
```commandline
gsutil cp training/potatoes.h5 gs://your-bucket/models/
```
## 🔧 API Endpoints

### FastAPI Gateway (:8001)
- `GET /ping` - Health check
- `POST /predict` - Image classification

### TensorFlow Serving (:8601)
- `POST /v1/models/potatoes_model:predict` - Model inference
- `GET /v1/models/potatoes_model` - Model info
- `GET /health` - Service health

## 🧪 Model Training

The CNN model was trained on 1,506 images with data augmentation. Model achieves 96.5% accuracy with optimized 1MB size for fast inference.

### Training Parameters
- **Image Size**: 256×256×3
- **Batch Size**: 32
- **Epochs**: 20
- **Optimizer**: Adam
- **Loss**: Sparse Categorical Crossentropy

## 🤝 Contributing

We welcome contributions! Please feel free to submit pull requests:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dataset sourced from PlantVillage
- TensorFlow Team for excellent ML tools
- FastAPI for high-performance web framework

---

**⭐ Star this repo if you found it helpful!**

**Made with ❤️ for the farming community**


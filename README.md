# 🔄 DataFlow Pipeline

![CI Pipeline](https://github.com/NilkeshTrivedi/dataflow-pipeline/actions/workflows/ci.yml/badge.svg)

A production-grade **ETL Data Pipeline** built with Python, FastAPI, PostgreSQL, and Docker. Automatically ingests data from multiple sources, transforms and validates it, loads it into a database, and exposes it via a REST API — all running on an automated schedule.

---

## 🏗 Architecture

Data Sources → Ingestion → Transformation → Validation → PostgreSQL → FastAPI → Client
(API + CSV)   (Python)     (Pandas)        (Custom)    (Docker)    (REST)

---

## ✨ Features

- **Multi-source ingestion** — REST API + CSV file data sources
- **Pandas transformation** — cleans, normalizes, and structures raw data
- **Data validation** — detects missing values, invalid entries, duplicates before loading
- **PostgreSQL storage** — structured relational data warehouse
- **FastAPI REST API** — exposes analytics with filters, pagination and Swagger docs
- **APScheduler** — pipeline runs automatically every hour
- **Docker** — fully containerized, runs with one command
- **27 Pytest tests** — unit + integration test coverage
- **GitHub Actions CI/CD** — tests run automatically on every push

---

## 🚀 Quick Start

### Prerequisites
- Docker Desktop installed and running
- Git

### Run the entire app

```bash
git clone https://github.com/NilkeshTrivedi/dataflow-pipeline.git
cd dataflow-pipeline
cp .env.example .env        # update values if needed
docker-compose up --build
```

Visit:
- API docs → http://localhost:8000/docs
- Health check → http://localhost:8000/health

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root health check |
| GET | `/health` | Service status |
| GET | `/api/v1/users` | All users (filter by `?city=`) |
| GET | `/api/v1/users/{id}` | Single user by ID |
| GET | `/api/v1/posts` | All posts (filter by `?user_id=`) |
| GET | `/api/v1/posts/{id}` | Single post by ID |
| GET | `/api/v1/employees` | All employees (filter by `?department=`) |
| GET | `/api/v1/stats` | Analytics — counts, avg salary, departments |
| GET | `/api/v1/pipeline/status` | Pipeline schedule and status |

---

## 🗂 Project Structure

dataflow-pipeline/
├── app/
│   ├── ingestion/          # API + CSV data fetching
│   ├── transformation/     # Pandas data cleaning
│   ├── validation/         # Data quality checks
│   ├── loader/             # PostgreSQL data loading
│   ├── api/                # FastAPI routes + schemas
│   ├── scheduler/          # APScheduler automation
│   ├── config.py           # Environment settings
│   ├── database.py         # SQLAlchemy engine
│   └── models.py           # Database table definitions
├── tests/                  # 27 pytest tests
├── data/                   # CSV data sources
├── .github/workflows/      # GitHub Actions CI/CD
├── Dockerfile              # App containerization
├── docker-compose.yml      # Multi-container setup
└── requirements.txt        # Python dependencies

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11 |
| API Framework | FastAPI |
| Database | PostgreSQL 15 |
| ORM | SQLAlchemy |
| Data Processing | Pandas |
| Scheduling | APScheduler |
| Containerization | Docker + Docker Compose |
| Testing | Pytest |
| CI/CD | GitHub Actions |

---

## 🧪 Running Tests Locally

```bash
# Activate virtual environment
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# Start database
docker-compose up -d postgres

# Run tests
pytest -v
```

---

## 🌱 Environment Variables

Create a `.env` file in the root folder:

```env
DB_HOST=127.0.0.1
DB_PORT=5433
DB_NAME=dataflow
DB_USER=your_db_user
DB_PASSWORD=your_db_password
API_URL=https://jsonplaceholder.typicode.com
```

---

## 📈 Future Improvements

- Swap JSONPlaceholder with real-time financial or weather API
- Add anomaly detection on incoming data
- Add email alerts for pipeline failures
- Deploy to AWS/GCP with managed PostgreSQL
- Add data lineage tracking

---

## 👨‍💻 Author

**Nilkesh Trivedi**
- GitHub: [@NilkeshTrivedi](https://github.com/NilkeshTrivedi)
- LinkedIn: [linkedin.com/in/nilkesh-trivedi](https://linkedin.com/in/nilkesh-trivedi)
- Email: nptrivedi2005@gmail.com


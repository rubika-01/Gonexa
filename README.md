# GONEXA — Measurement-Aware Rehabilitation Assistant

**From Movement Data to Real Progress.**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 💡 What is GONEXA?

GONEXA is a measurement-aware rehabilitation assistant that transforms movement data into:

**Measurement → Validation → Progress → Understanding → Report**

It combines movement analysis with an AI-assisted interface to help rehabilitation professionals understand measurements and track progress across sessions.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🎯 The Problem

Traditional rehabilitation measurement can involve:

• Manual goniometer measurements
• Repeated measurements and documentation
• Difficulty comparing sessions
• Difficulty tracking long-term progress
• Measurement-quality issues
• Costly specialized digital tools
• Limited affordability for students learning rehabilitation
• Cost barriers for small clinics and rehabilitation centres

### The Question

**Can we make movement measurement smarter, easier to track, and more accessible?**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🚀 What Does GONEXA Do?

### 1. Measure

GONEXA analyzes movement data to determine:

• Joint angle
• Range of Motion (ROM)
• Repetitions
• Movement quality
• Measurement confidence

### 2. Validate

GONEXA checks whether a measurement can be trusted.

It can detect:

• Measurement displacement
• Potentially unreliable measurements
• Measurement-quality issues

### 3. Correct

When an issue is detected, the clinician remains in control:

**Auto-Correct → Recalibrate → Mark Invalid**

Every correction is recorded in an audit trail.

### 4. Track Progress

Session results become part of the patient's history.

This allows review of:

• Previous sessions
• Measurements
• Movement quality
• Reports
• Progress over time

### 5. Ask GONEXA

Ask questions about:

• Patients
• Sessions
• Measurements
• Progress
• Measurement quality

The AI layer helps interpret structured results in an understandable way.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔄 How It Works

Movement Data
↓
Measure
↓
Validate
↓
Check Measurement Quality
↓
Correct if Required
↓
Store Session
↓
Track Progress
↓
Ask GONEXA
↓
Understand & Report

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🧠 Measurement + AI

A key design principle of GONEXA:

**AI should understand measurements, not invent them.**

The deterministic measurement engine remains the source of truth for numerical results.

Movement Data
↓
Deterministic Measurement Engine
↓
Angle + ROM + Repetitions
↓
Quality + Confidence + Displacement
↓
Structured Results
↓
Strands Agent
↓
Amazon Bedrock
↓
Ask GONEXA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ☁️ AWS Integration

AWS forms the foundation of the AI layer and planned cloud architecture.

### AWS Strands Agents SDK

Used to build the agent layer behind Ask GONEXA.

**User Question → Strands Agent → GONEXA Information → AI Response**

### Amazon Bedrock

Used as the intended foundation-model inference layer for the AI assistant.

**Ask GONEXA → Strands Agent → Amazon Bedrock → AI Understanding**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🏗️ Planned AWS Architecture

GONEXA UI
↓
API Gateway
↓
AWS Lambda
↓
DynamoDB + S3
↓
Measurement Engine
↓
Strands Agent
↓
Amazon Bedrock
↓
Ask GONEXA

### AWS Services

• AWS Strands Agents SDK → AI agent orchestration
• Amazon Bedrock → Foundation-model inference
• Amazon API Gateway → API request handling
• AWS Lambda → Backend processing
• Amazon DynamoDB → Structured application and session data
• Amazon S3 → Movement data and file storage

**Note:** The current prototype is primarily local. API Gateway, Lambda, DynamoDB, and S3 represent the planned cloud deployment architecture.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🛠️ Technology Stack

### Frontend

• React
• TypeScript
• Vite
• Tailwind CSS

### Backend

• Python
• FastAPI

### AI & AWS

• AWS Strands Agents SDK
• Amazon Bedrock

### Planned Cloud Services

• Amazon API Gateway
• AWS Lambda
• Amazon DynamoDB
• Amazon S3

### Core System

• Movement analysis
• ROM calculation
• Repetition detection
• Movement-quality evaluation
• Confidence estimation
• Displacement detection
• Measurement correction
• Session history
• Progress tracking
• AI-assisted querying

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 💥 Challenge & Recovery

During development, live Amazon Bedrock inference was not available on the AWS account used for development.

Instead of presenting simulated responses as real Bedrock output, GONEXA uses a controlled offline fallback.

**Ask GONEXA**
↓
**Strands + Bedrock**
↓
Model Available?
↓
YES → AI Response
NO → Offline Fallback

This clearly separates:

**STRANDS + BEDROCK**

from

**OFFLINE FALLBACK**

### Key Lesson

**A reliable system should handle failure, not only the happy path.**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🖥️ Prototype Features

• Dashboard
• Patient profiles
• Live measurement session
• ROM and angle measurement
• Repetition detection
• Movement-quality indicators
• Confidence estimation
• Measurement displacement detection
• Auto-correction
• Manual recalibration
• Invalid measurement workflow
• Audit trail
• Session history
• Reports
• Ask GONEXA
• Strands + Bedrock integration path
• Controlled offline fallback

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🧪 Data

The prototype uses:

**Synthetic patient data + synthetic movement data**

No real patient information is included.

This allows the complete workflow to be demonstrated without exposing personal health information.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 👥 Who Is GONEXA For?

### Primary Focus

• Physiotherapists
• Rehabilitation professionals
• Rehabilitation centres
• Clinics and hospitals

### Potential Applications

• Occupational therapy
• Sports and movement analysis
• Athletes
• Gyms
• Physiotherapy students
• Rehabilitation students
• Small clinics
• Research and education

### Long-Term Goal

**Make rehabilitation measurement technology more accessible and affordable.**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🚀 Future Vision

GONEXA is currently a software prototype.

The long-term vision is to develop a complete hardware + software rehabilitation platform.

**Software Prototype**
↓
**Affordable Hardware**
↓
**Real Movement Capture**
↓
**Real-Time Measurement**
↓
**Cloud Processing**
↓
**Longitudinal Intelligence**
↓
**Accessible Rehabilitation Technology**

Future development:

• Affordable movement-sensing hardware
• Real-time movement measurement
• Hardware-to-cloud integration
• AWS cloud deployment
• Live AI inference
• Longitudinal rehabilitation intelligence
• Real-world validation
• Sports and rehabilitation applications
• More accessible tools for students and small clinics

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔐 Safety & Limitations

GONEXA is currently a technology prototype.

• Uses synthetic data
• Does not use real patient information
• Does not replace professional clinical judgment
• Is not a medical diagnostic system
• Real hardware integration is future work
• Full cloud deployment is future work
• Clinical validation is future work

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📁 Project Structure

GONEXA/
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── app/
│   ├── tests/
│   └── requirements.txt
│
├── docs/
├── README.md
├── .gitignore
└── .env.example

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ▶️ Running Locally

### Frontend

Install dependencies:

npm install

Start the development server:

npm run dev

Frontend:

[http://127.0.0.1:5173](http://127.0.0.1:5173)

### Backend

Create a virtual environment:

python -m venv .venv

Install dependencies:

pip install -r requirements.txt

Start FastAPI:

uvicorn app.main:app --reload

Backend:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

API documentation:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔑 Environment Configuration

Never upload AWS credentials or secret keys.

Use .env.example as a template.

Example:

AWS_REGION=your-region
BEDROCK_MODEL_ID=your-model-id
AWS_BEDROCK_ENABLED=false

Never commit:

.env
AWS credentials
Access keys
Secret keys

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🧪 Testing

The prototype was tested across multiple layers:

### Backend

• Measurement functionality
• AI functionality
• API behaviour
• Failure handling

### Frontend

• Production build
• TypeScript compilation
• User workflows

### End-to-End

• Main application workflows
• Measurement scenarios
• AI assistant workflows
• Error and fallback behaviour

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🌱 The Vision

A rehabilitation measurement should be more than just a number.

It should help answer:

**What happened?**

**Can I trust the measurement?**

**What changed?**

**Is the patient progressing?**

**What should I understand from this session?**

That is the idea behind GONEXA.

**Movement → Measurement → Validation → Understanding → Progress**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🏆 Built For

**AWS First Commit — Bharat Builds Tour 2026**

A student project exploring:

**AI + AWS + Movement Analysis + Rehabilitation Technology**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔗 Project Links

🎥 **Demo Video:** [YouTube link](https://youtu.be/za74z2f1W80?si=JMJL7hU8lJlyIY5J)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# GONEXA

**From Movement Data to Real Progress.**

**Measure. Validate. Understand. Progress.**

*Built with curiosity, continuous learning, and a lot of debugging.* 🚀

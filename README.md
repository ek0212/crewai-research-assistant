# CrewAI Assistant

An AI-powered research assistant that leverages CrewAI to generate comprehensive responses on any topic. Built with FastAPI and Google's Gemini model.

## Demo
<video src="./demo.mp4" controls></video>

## Features

- AI-powered research and content generation
- Real-time progress tracking
- Markdown-formatted responses
- Web interface with Play/Stop controls
- Streaming updates during processing

## Prerequisites

- Python 3.8+
- Google Gemini API key
- Serper API key

## Getting API Keys

### Google Gemini API Key
1. Go to the [Google AI Studio](https://aistudio.google.com/) website.  
2. Sign in with your Google account.  
3. Click on **Get API Key** under the Gemini API section.  
4. Copy your API key and store it securely.  

### Serper API Key
1. Visit the [Serper API website](https://serper.dev/).  
2. Sign up for an account if you don’t have one.  
3. Navigate to the **API Keys** section in your dashboard.  
4. Generate a new API key and copy it. 

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd testCrew
```

2. Set up Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file:
```env
GEMINI_API_KEY=your-gemini-api-key
SERPER_API_KEY=your-serper-api-key
```

## Usage

1. Start the server:
```bash
uvicorn app:app --reload
```

2. Open http://localhost:8000 in your browser

3. Enter your research topic and click Play

4. View real-time progress and final output in markdown format

## Project Structure

```
testCrew/
├── app.py              # FastAPI application
├── crews/
│   └── basic_crew.py   # CrewAI implementation
├── static/
│   └── style.css       # Web interface styles
├── templates/
│   └── index.html      # HTML template
├── requirements.txt    # Python dependencies
└── .env               # API keys (not in git)
```

## Development

The application uses:
- FastAPI for the web server
- CrewAI for orchestrating AI agents
- Google Gemini for language processing
- Jinja2 for templating
- Markdown for formatting output

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

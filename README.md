# YouTube Transcript Extractor

This project provides a simple GUI application to extract transcripts from YouTube videos. It allows users to input a YouTube video URL and generates the corresponding transcript.

## Features

- User-friendly graphical interface
- Supports various YouTube URL formats
- Displays the full transcript in a readable format
- Error handling for invalid URLs or unavailable transcripts

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/YouTube-Transcript-Extractor.git
   cd YouTube-Transcript-Extractor
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install youtube_transcript_api PyQt5
   ```

## Usage

1. Run the application:
   ```
   python youtube_transcript_generator.py
   ```

2. The application window will open.

3. Enter a YouTube video URL in the input field.

4. Click the "Generate Transcript" button.

5. The transcript will appear in the text area below.

## Troubleshooting

If you encounter a `ModuleNotFoundError`, ensure that you have installed all required packages as described in the Installation section.

## Contributing

Contributions to this project are welcome. Please feel free to fork the repository and submit pull requests.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

If you have any questions or feedback, please open an issue in this repository.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtCore import Qt
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

class TranscriptGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # URL input
        url_layout = QHBoxLayout()
        url_label = QLabel('YouTube URL:')
        self.url_input = QLineEdit()
        url_layout.addWidget(url_label)
        url_layout.addWidget(self.url_input)
        layout.addLayout(url_layout)

        # Generate button
        self.generate_button = QPushButton('Generate Transcript')
        self.generate_button.clicked.connect(self.generate_transcript)
        layout.addWidget(self.generate_button)

        # Transcript display
        self.transcript_display = QTextEdit()
        self.transcript_display.setReadOnly(True)
        layout.addWidget(self.transcript_display)

        self.setLayout(layout)
        self.setWindowTitle('YouTube Transcript Generator')
        self.setGeometry(300, 300, 600, 400)

    def generate_transcript(self):
        video_url = self.url_input.text()
        transcript = get_transcript(video_url)
        self.transcript_display.setText(transcript)

def get_video_id(url):
    """Extract the video ID from a YouTube URL."""
    query = urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    return None

def get_transcript(video_url):
    """Get the transcript of a YouTube video."""
    video_id = get_video_id(video_url)
    if not video_id:
        return "Invalid YouTube URL"
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return ' '.join([entry['text'] for entry in transcript])
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TranscriptGenerator()
    ex.show()
    sys.exit(app.exec_())
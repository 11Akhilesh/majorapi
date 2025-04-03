import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Copilot Sidebar UI")
        self.setGeometry(100, 100, 600, 1600)  # x, y, width, height
        self.setStyleSheet("background-color: #12131A; color: white; border-radius: 15px;")

        # Layout setup
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)  # Align items to the top

        # Title Label
        title = QLabel("Explore this page")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        title.setStyleSheet("padding: 10px;")

        # Buttons
        summary_button = QPushButton("Create a Summary")
        expand_button = QPushButton("Expand on this Topic")

        # Styling buttons
        button_style = """
            QPushButton {
                background-color: #222437;
                color: white;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2E2F47;
            }
        """
        summary_button.setStyleSheet(button_style)
        expand_button.setStyleSheet(button_style)

        # Add widgets to layout
        layout.addWidget(title)
        layout.addWidget(summary_button)
        layout.addWidget(expand_button)

        # Set layout
        self.setLayout(layout)

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Sidebar()
    window.show()
    sys.exit(app.exec_())

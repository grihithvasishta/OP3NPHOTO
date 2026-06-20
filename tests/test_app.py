import pytest
from PyQt6.QtWidgets import QApplication
from openphoto.app import OpenPhotoApp

def test_app_title(qtbot):
    """Test that the application window has the correct title."""
    app = OpenPhotoApp()
    qtbot.addWidget(app)
    assert "OpenPhoto" in app.windowTitle()

def test_app_status_bar(qtbot):
    """Test that the status bar initializes with 'Ready'."""
    app = OpenPhotoApp()
    qtbot.addWidget(app)
    assert app.statusBar().currentMessage() == "Ready"

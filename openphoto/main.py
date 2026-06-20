import sys
from PyQt6.QtWidgets import QApplication
from openphoto.app import OpenPhotoApp

def main():
    app = QApplication(sys.argv)
    
    # Set modern dark style similar to Photoshop
    app.setStyle("Fusion")
    
    window = OpenPhotoApp()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

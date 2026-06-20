import sys
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QMenuBar, QMenu, QToolBar, QStatusBar, QFileDialog,
    QLabel, QScrollArea
)
from PyQt6.QtGui import QAction, QPixmap, QImage, QColor, QPalette, QPainter, QPen
from PyQt6.QtCore import Qt, QPoint

class Canvas(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.setStyleSheet("background-color: #2b2b2b;")
        
        # Default blank canvas
        self.image = QPixmap(800, 600)
        self.image.fill(Qt.GlobalColor.white)
        self.setPixmap(self.image)
        
        self.drawing = False
        self.brush_size = 5
        self.brush_color = Qt.GlobalColor.black
        self.last_point = QPoint()
        
        self.current_tool = "brush"

    def set_tool(self, tool_name):
        self.current_tool = tool_name

    def load_image(self, file_name):
        self.image = QPixmap(file_name)
        self.setPixmap(self.image)
        self.resize(self.image.width(), self.image.height())

    def save_image(self, file_name):
        self.image.save(file_name)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.last_point = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.MouseButton.LeftButton) and self.drawing:
            painter = QPainter(self.image)
            
            if self.current_tool == "brush":
                painter.setPen(QPen(self.brush_color, self.brush_size, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
            elif self.current_tool == "eraser":
                # Assuming background is white for eraser currently
                painter.setPen(QPen(Qt.GlobalColor.white, self.brush_size * 2, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
                
            painter.drawLine(self.last_point, event.position().toPoint())
            self.last_point = event.position().toPoint()
            self.setPixmap(self.image)
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False


class OpenPhotoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenPhoto - The Open Source Image Editor")
        self.setGeometry(100, 100, 1280, 720)
        
        self._setup_dark_theme()
        self._create_actions()
        self._create_menu_bar()
        self._setup_central_widget()
        self._create_tool_bars() # after central widget so canvas exists
        
        self.statusBar().showMessage("Ready")

    def _setup_dark_theme(self):
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
        palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
        self.setPalette(palette)

    def _create_actions(self):
        # File Actions
        self.open_action = QAction("Open...", self)
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.triggered.connect(self.open_image)

        self.save_action = QAction("Save As...", self)
        self.save_action.setShortcut("Ctrl+Shift+S")
        self.save_action.triggered.connect(self.save_image)

        self.exit_action = QAction("Exit", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.triggered.connect(self.close)

    def _create_menu_bar(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

    def _create_tool_bars(self):
        tools_bar = QToolBar("Tools")
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, tools_bar)
        
        brush_action = QAction("Brush (B)", self)
        brush_action.triggered.connect(lambda: self.canvas.set_tool("brush"))
        tools_bar.addAction(brush_action)

        eraser_action = QAction("Eraser (E)", self)
        eraser_action.triggered.connect(lambda: self.canvas.set_tool("eraser"))
        tools_bar.addAction(eraser_action)

    def _setup_central_widget(self):
        self.canvas = Canvas()
        
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.canvas)
        self.scroll_area.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.setCentralWidget(self.scroll_area)

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp)")
        if file_name:
            self.canvas.load_image(file_name)
            self.statusBar().showMessage(f"Loaded {file_name}")

    def save_image(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG Files (*.png);;JPEG Files (*.jpg *.jpeg)")
        if file_name:
            self.canvas.save_image(file_name)
            self.statusBar().showMessage(f"Saved {file_name}")

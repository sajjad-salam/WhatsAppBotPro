import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont
from src.ui.main_window import WhatsAppBotWindow


def main():
    app = QApplication(sys.argv)

    # Configuração Global de Fonte
    app.setFont(QFont("Segoe UI", 9))

    print("="*60)
    print("📱 بوت واتساب - نظام إرسال الرسائل")
    print("="*60)
    print("نظام إرسال الرسائل النصية")
    print("ستظهر السجلات التفصيلية في المحطة")
    print("="*60)
    print()

    window = WhatsAppBotWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

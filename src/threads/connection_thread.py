from PySide6.QtCore import QThread, Signal


class ConnectionThread(QThread):
    log_signal = Signal(str, str)
    status_signal = Signal(bool)

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    def run(self):
        self.log_signal.emit("▸ جارٍ بدء النظام...", "system")

        if self.bot.iniciar(headless=False):
            self.log_signal.emit(
                "✓ فتح المتصفح. جارٍ التحقق من الجلسة...", "info")
            if self.bot.aguardar_login():
                self.log_signal.emit("✓✓✓ متصل! ✓✓✓", "success")
                self.log_signal.emit("▸ تم حفظ الجلسة.", "success")
                self.status_signal.emit(True)
            else:
                self.log_signal.emit("✗ انتهت المهلة: لم يتم قراءة رمز الاستجابة السريعة.", "error")
                self.bot.fechar()
                self.status_signal.emit(False)
        else:
            self.log_signal.emit("✗ خطأ حرج أثناء فتح المتصفح.", "error")
            self.status_signal.emit(False)

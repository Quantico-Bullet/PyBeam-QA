from PySide6.QtWidgets import QWidget, QFileDialog

def worksheet_save_report(parent: QWidget = None):
    file_path = QFileDialog.getSaveFileName(caption="Save To File...", 
                                            filter="PDF (*.pdf)",
                                            parent=parent)
        
    if file_path[0] != "":
        path = file_path[0].split("/")
            
        if not path[-1].endswith(".pdf"):
            path[-1] = path[-1] + ".pdf"

        return "/".join(path)

    else:
        return ""
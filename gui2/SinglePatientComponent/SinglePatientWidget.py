from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QPushButton, QSplitter, QDialog
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Qt, QSize, Signal

import os
from utils.software_config import SoftwareConfigResources
from gui2.SinglePatientComponent.PatientResultsSidePanel.PatientResultsSinglePatientSidePanelWidget import PatientResultsSinglePatientSidePanelWidget
from gui2.SinglePatientComponent.CentralDisplayArea.CentralDisplayAreaWidget import CentralDisplayAreaWidget
from gui2.SinglePatientComponent.CentralAreaWidget import CentralAreaWidget
from gui2.SinglePatientComponent.LayersInteractorSidePanel.LayersInteractorSinglePatientSidePanelWidget import LayersInteractorSinglePatientSidePanelWidget
from gui2.UtilsWidgets.ImportDataQDialog import ImportDataQDialog
from gui2.UtilsWidgets.ImportDICOMDataQDialog import ImportDICOMDataQDialog


class SinglePatientWidget(QWidget):
    """

    """
    import_data_triggered = Signal()
    import_patient_triggered = Signal()

    def __init__(self, parent=None):
        super(SinglePatientWidget, self).__init__()
        self.parent = parent
        self.widget_name = "single_patient_widget"
        self.__set_interface()
        self.__set_stylesheets()
        self.__set_connections()

    def __set_interface(self):
        self.setBaseSize(self.parent.baseSize())
        self.__top_logo_options_panel_interface()
        self.__left_results_panel_interface()
        self.__center_display_panel_interface()
        self.__right_options_panel_interface()
        self.central_label = QLabel()
        self.central_label.setFixedSize(QSize(self.parent.baseSize().width(), self.parent.baseSize().height()))
        # self.central_label.setFixedSize(QSize(1440, 850))
        self.central_label.setContentsMargins(0, 0, 0, 0)
        self.central_layout = QHBoxLayout()
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setSpacing(0)
        # self.central_layout.addStretch(1)
        self.central_layout.addLayout(self.left_panel_layout)
        # self.central_layout.addWidget(self.right_panel_label)
        # self.central_layout.addStretch(1)
        self.central_label.setLayout(self.central_layout)

        self.layout = QVBoxLayout(self)
        self.center_widget_container_layout = QGridLayout()
        self.layout.addLayout(self.top_logo_panel_layout, Qt.AlignTop)
        self.center_widget_container_layout.addWidget(self.central_label, 0, 0, Qt.AlignCenter)
        self.layout.addLayout(self.center_widget_container_layout)

        self.import_data_dialog = ImportDataQDialog(self)
        self.import_dicom_dialog = ImportDICOMDataQDialog(self)

    def __top_logo_options_panel_interface(self):
        self.top_logo_panel_layout = QHBoxLayout()
        self.top_logo_panel_label = QLabel()
        self.top_logo_panel_label.setPixmap(QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                                 '../Images/raidionics-logo.png')).scaled(150, 30, Qt.KeepAspectRatio))
        self.top_logo_panel_label.setFixedSize(QSize(150, 30))
        self.top_logo_panel_layout.addWidget(self.top_logo_panel_label, Qt.AlignLeft)
        self.top_logo_panel_label_import_file_pushbutton = QPushButton()
        self.top_logo_panel_label_import_file_pushbutton.setFixedSize(QSize(30, 30))
        self.top_logo_panel_label_import_file_pushbutton.setIcon(QIcon(QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../Images/data_load_icon.png'))))
        self.top_logo_panel_label_import_file_pushbutton.setIconSize(QSize(29, 29))
        self.top_logo_panel_layout.addWidget(self.top_logo_panel_label_import_file_pushbutton)

        self.top_logo_panel_label_import_dicom_pushbutton = QPushButton()
        self.top_logo_panel_label_import_dicom_pushbutton.setFixedSize(QSize(30, 30))
        self.top_logo_panel_label_import_dicom_pushbutton.setIcon(QIcon(QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../Images/dicom_load_icon.png'))))
        self.top_logo_panel_label_import_dicom_pushbutton.setIconSize(QSize(29, 29))
        self.top_logo_panel_layout.addWidget(self.top_logo_panel_label_import_dicom_pushbutton)

        self.top_logo_panel_label_save_pushbutton = QPushButton()
        self.top_logo_panel_label_save_pushbutton.setFixedSize(QSize(30, 30))
        self.top_logo_panel_label_save_pushbutton.setIcon(QIcon(QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../Images/data_save_icon.png'))))
        self.top_logo_panel_label_save_pushbutton.setIconSize(QSize(29, 29))
        self.top_logo_panel_layout.addWidget(self.top_logo_panel_label_save_pushbutton)

        self.top_logo_panel_layout.addStretch(1)

    def __left_results_panel_interface(self):
        self.left_panel_layout = QVBoxLayout()
        self.left_panel_splitter = QSplitter(self, Qt.Horizontal)
        self.left_panel_splitter.setFixedSize(QSize(1290, 850))
        # self.left_dock = QLabel()
        # self.left_dock.setMaximumSize(QSize(150, 850))
        # self.left_dock.setStyleSheet("QLabel{background-color:rgb(255,0,0);}")
        # self.right_dock = QLabel()
        # self.right_dock.setMaximumSize(QSize(150, 850))
        # self.right_dock.setStyleSheet("QLabel{background-color:rgb(0,255,0);}")
        # self.center_dock = QLabel()
        # # self.center_dock.setMinimumSize(QSize(1140, 850))
        # self.center_dock.setMaximumSize(QSize(1440, 850))
        # self.center_dock.setStyleSheet("QLabel{background-color:rgb(0,0,255);}")
        self.results_panel = PatientResultsSinglePatientSidePanelWidget(self)
        self.results_panel.setBaseSize(QSize(200, self.baseSize().height()))
        self.results_panel.setMaximumSize(QSize(200, self.baseSize().height()))
        self.center_panel = CentralAreaWidget(self) #CentralDisplayAreaWidget(self)
        self.center_panel.setBaseSize(QSize(self.baseSize().width() - 400, self.baseSize().height()))
        self.layers_panel = LayersInteractorSinglePatientSidePanelWidget(self)
        self.layers_panel.setBaseSize(QSize(200, self.parent.baseSize().height()))
        self.layers_panel.setMaximumSize(QSize(200, self.parent.baseSize().height()))
        self.left_panel_splitter.addWidget(self.results_panel)
        self.left_panel_splitter.addWidget(self.center_panel)
        self.left_panel_splitter.setCollapsible(1, False)
        self.right_panel_splitter = QSplitter(self, Qt.Horizontal)
        self.right_panel_splitter.setFixedSize(QSize(1140, 850))
        self.right_panel_splitter.addWidget(self.left_panel_splitter)
        self.right_panel_splitter.addWidget(self.layers_panel)
        self.right_panel_splitter.setCollapsible(0, False)

        self.left_panel_layout.addWidget(self.right_panel_splitter)

    def __center_display_panel_interface(self):
        pass

    def __right_options_panel_interface(self):
        pass

    def __set_stylesheets(self):
        self.setStyleSheet("QWidget{font:11px;}")
        pass

    def __set_connections(self):
        self.top_logo_panel_label_import_file_pushbutton.clicked.connect(self.__on_import_file_clicked)
        self.top_logo_panel_label_import_dicom_pushbutton.clicked.connect(self.__on_import_dicom_clicked)
        self.top_logo_panel_label_save_pushbutton.clicked.connect(self.__on_save_clicked)
        self.__set_cross_connections()

    def __set_cross_connections(self):
        # Connections related to data import from the top contextual menu
        self.import_data_dialog.mri_volume_imported.connect(self.layers_panel.on_mri_volume_import)
        self.import_data_dialog.annotation_volume_imported.connect(self.layers_panel.on_annotation_volume_import)
        self.import_data_dialog.patient_imported.connect(self.results_panel.on_import_patient)
        self.import_dicom_dialog.patient_imported.connect(self.results_panel.on_import_patient)
        self.import_dicom_dialog.mri_volume_imported.connect(self.layers_panel.on_mri_volume_import)

        # Connections relating patient selection (left-hand side) with data display
        self.results_panel.patient_selected.connect(self.center_panel.on_patient_selected)
        self.results_panel.patient_selected.connect(self.layers_panel.on_patient_selected)

        # Connections related to data display (from right-hand panel to update the central viewer)
        self.layers_panel.volume_view_toggled.connect(self.center_panel.on_volume_layer_toggled)
        self.layers_panel.annotation_view_toggled.connect(self.center_panel.on_annotation_layer_toggled)
        self.layers_panel.annotation_opacity_changed.connect(self.center_panel.on_annotation_opacity_changed)
        self.layers_panel.annotation_color_changed.connect(self.center_panel.on_annotation_color_changed)
        # self.layers_panel.atlas_view_toggled.connect(self.center_panel.on_atlas_layer_toggled)
        self.layers_panel.atlas_structure_view_toggled.connect(self.center_panel.atlas_structure_view_toggled)
        self.center_panel.standardized_report_imported.connect(self.results_panel.on_standardized_report_imported)

        # To sort
        self.center_panel.mri_volume_imported.connect(self.layers_panel.on_mri_volume_import)
        self.center_panel.annotation_volume_imported.connect(self.layers_panel.on_annotation_volume_import)
        self.center_panel.atlas_volume_imported.connect(self.layers_panel.on_atlas_volume_import)
        # self.import_data_triggered.connect(self.center_panel.on_import_data)
        # self.import_data_triggered.connect(self.results_panel.on_import_data)
        # self.import_data_triggered.connect(self.layers_panel.on_import_data)
        # self.import_patient_triggered.connect(self.results_panel.on_import_patient)
        # self.center_panel.import_data_triggered.connect(self.layers_panel.on_import_data)

    def get_widget_name(self):
        return self.widget_name

    def __on_import_file_clicked(self) -> None:
        """

        """
        self.import_data_dialog.reset()
        code = self.import_data_dialog.exec_()
        # if code == QDialog.Accepted:
        #     self.import_data_triggered.emit()

    def __on_import_dicom_clicked(self) -> None:
        """

        """
        # @Behaviour. Do we reset the loader in case of DICOMs, might be worth to keep stuff in memory?
        # self.import_dicom_dialog.reset()
        code = self.import_dicom_dialog.exec_()
        # if code == QDialog.Accepted:
        #     self.import_data_triggered.emit()

    def __on_save_clicked(self):
        SoftwareConfigResources.getInstance().patients_parameters[SoftwareConfigResources.getInstance().active_patient_name].save_patient()

    def on_single_patient_clicked(self, patient_name):
        self.results_panel.add_new_patient(patient_name)

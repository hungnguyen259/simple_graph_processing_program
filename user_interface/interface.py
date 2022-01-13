import networkx as nx
from PyQt5 import QtCore, QtGui, QtWidgets
from user_interface.output import output
from graph_algorithms.run_algo import run_algo


class Ui_MainWindow(object):


    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 456)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 20, 161, 16))
        self.label_1.setObjectName("label")
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setGeometry(QtCore.QRect(50, 40, 401, 21))
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.directed_button = QtWidgets.QRadioButton(self.frame_1)
        self.directed_button.setGeometry(QtCore.QRect(10, 0, 121, 16))
        self.directed_button.setObjectName("directed_button")
        self.undirected_button = QtWidgets.QRadioButton(self.frame_1)
        self.undirected_button.setGeometry(QtCore.QRect(260, 0, 121, 16))
        self.undirected_button.setObjectName("undirected_button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 181, 16))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 60, 221, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_1.setGeometry(QtCore.QRect(20, 80, 201, 141))
        self.textEdit_1.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(310, 80, 191, 141))
        self.textEdit_2.setObjectName("textEdit_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 260, 561, 51))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.bfs_button = QtWidgets.QRadioButton(self.frame_2)
        self.bfs_button.setGeometry(QtCore.QRect(0, 20, 62, 14))
        self.bfs_button.setObjectName("bfs_button")
        self.dfs_button = QtWidgets.QRadioButton(self.frame_2)
        self.dfs_button.setGeometry(QtCore.QRect(80, 20, 62, 14))
        self.dfs_button.setObjectName("dfs_button")
        self.kruskal_button = QtWidgets.QRadioButton(self.frame_2)
        self.kruskal_button.setGeometry(QtCore.QRect(450, 20, 62, 14))
        self.kruskal_button.setObjectName("kruskal_button")
        self.bellman_button = QtWidgets.QRadioButton(self.frame_2)
        self.bellman_button.setGeometry(QtCore.QRect(250, 20, 92, 14))
        self.bellman_button.setObjectName("bellman_button")
        self.dijkstra_button = QtWidgets.QRadioButton(self.frame_2)
        self.dijkstra_button.setGeometry(QtCore.QRect(150, 20, 62, 14))
        self.dijkstra_button.setObjectName("dijkstra_button")
        self.prim_button = QtWidgets.QRadioButton(self.frame_2)
        self.prim_button.setGeometry(QtCore.QRect(360, 20, 62, 14))
        self.prim_button.setObjectName("prim_button")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 310, 101, 16))
        self.label_6.setObjectName("label_6")
        self.vertex_start = QtWidgets.QLineEdit(self.centralwidget)
        self.vertex_start.setGeometry(QtCore.QRect(120, 310, 101, 20))
        self.vertex_start.setObjectName("vertex_start")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 310, 121, 16))
        self.label_7.setObjectName("label_7")
        self.des_vertex = QtWidgets.QLineEdit(self.centralwidget)
        self.des_vertex.setGeometry(QtCore.QRect(410, 310, 101, 20))
        self.des_vertex.setObjectName("des_vertex")
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(240, 340, 56, 17))
        self.run_button.setObjectName("_button")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(540, 0, 431, 421))
        self.label_8.setObjectName("label_8")
        self.check_button = QtWidgets.QPushButton(self.centralwidget)
        self.check_button.setGeometry(QtCore.QRect(240, 230, 56, 17))
        self.check_button.setObjectName("check_button")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 360, 511, 20))
        self.label_9.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 390, 521, 10))
        self.label_10.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.directed_button.toggled.connect(self.control_ratio_button)
        self.undirected_button.toggled.connect(self.control_ratio_button)
        self.bfs_button.toggled.connect(self.control_ratio_button)
        self.dfs_button.toggled.connect(self.control_ratio_button)
        self.dijkstra_button.toggled.connect(self.control_ratio_button)
        self.bellman_button.toggled.connect(self.control_ratio_button)
        self.prim_button.toggled.connect(self.control_ratio_button)
        self.kruskal_button.toggled.connect(self.control_ratio_button)
        self.run_button.clicked.connect(self.process)
        self.check_button.clicked.connect(self.draw_graph)


    def draw_graph(self):
        """draw_graph is called when check button is pressed.
        It is used to draw the graph on the interface to check"""

        # Read the data from interface
        y = self.input_graph()
        if len(y) != 3:
            self.update_exception(y[0])
            return
        # Draw the graph and save it as a png file
        x, result, graph_type = y
        output(x, result, graph_type)
        # Update the image on the interface
        self.update_image()
        # Update the result on the interface
        self.update_result([])


    def process(self):
        """process is called when run button is pressed.
        It is used to write the result and draw the graph on the interface """

        # Read the data from interface
        y = self.input_data()
        if len(y) != 5:
            self.update_exception(y[0])
            return
        # Run algorithm
        x, start_vertex, des_vertex, graph_type, algo_type = y
        x, result, graph_type, path, error_code = run_algo(x, start_vertex, des_vertex, graph_type, algo_type)
        if error_code != 0:
            self.update_exception(error_code)
            if error_code <= 11 and error_code >= 9:
                output(x, result, graph_type)
                self.update_image()
            return
        # Draw the graph and save it as a png file
        output(x, result, graph_type)
        # Update the image on the interface
        self.update_image()
        # Update the result on the interface
        self.update_result(path)


    def input_graph(self):
        """Read vertices, edges from interface. Return graph, result, graph type.
           Return 1 if no graph type is selected.
           Return 2 if vertices are not entered correctly.
           Return 3 if edges are not entered correctly"""

        # Read graph type
        if self.directed_button.isChecked():
            x = nx.DiGraph()
            result = nx.DiGraph()
            graph_type = 1
        elif self.undirected_button.isChecked():
            x = nx.Graph()
            result = nx.Graph()
            graph_type = 0
        else:
            return [1]

        # Read vertices
        vertices_str = self.textEdit_1.toPlainText().splitlines()
        if len(vertices_str) == 0:
            return [2]
        for vertex in vertices_str:
            if len(vertex.split()) == 0:
                continue
            if len(vertex.split()) != 1:
                return [2]
            else:
                x.add_node(vertex.split()[0])

        # Read edges
        edges_str = self.textEdit_2.toPlainText().splitlines()

        def check_number(str):
            if str.isdigit():
                return 1
            if str[0] == '-' and str[1:].isdigit():
                return 1
            return 0

        if len(edges_str) == 0:
            return [3]
        for edge in edges_str:
            if len(edge.split()) == 0:
                continue
            if len(edge.split()) != 3:
                return [3]
            else:
                if check_number(edge.split()[2]) == 0:
                    return [3]
                x.add_edge(edge.split()[0], edge.split()[1], weight=int(edge.split()[2]))

        return x, result, graph_type


    def input_data(self):
        """Read the data from interface.
           Return graph, starting vertex, destination vertex, graph type, algorithm type.
           Return 1 if no graph type is selected.
           Return 2 if vertices are not entered correctly.
           Return 3 if edges are not entered correrctly.
           Return 4 or return 5 if starting vertex, destination vertex aren't entered."""
        try:
            # Read graph type
            if self.directed_button.isChecked():
                x = nx.DiGraph()
                graph_type = 1
            elif self.undirected_button.isChecked():
                x = nx.Graph()
                graph_type = 0
            else:
                return [1]

            # Read vertices
            vertices_str = self.textEdit_1.toPlainText().splitlines()
            if len(vertices_str) == 0:
                return [2]
            for vertex in vertices_str:
                if len(vertex.split()) == 0:
                    continue
                if len(vertex.split()) != 1:
                    return [2]
                else:
                    x.add_node(vertex.split()[0])

            # Read edges
            edges_str = self.textEdit_2.toPlainText().splitlines()

            def check_number(str):
                if str.isdigit():
                    return 1
                if str[0] == '-' and str[1:].isdigit():
                    return 1
                return 0

            if len(edges_str) == 0:
                return [3]
            for edge in edges_str:
                if len(edge.split()) == 0:
                    continue
                if len(edge.split()) != 3:
                    return [3]
                else:
                    if check_number(edge.split()[2]) == 0:
                        return [3]
                    x.add_edge(edge.split()[0], edge.split()[1], weight=int(edge.split()[2]))
            for node in x.nodes():
                x.nodes[node]['visited'] = 0

            # Read starting vertex, destination vertex, algorithm type
            start_vertex = ""
            des_vertex = ""
            if len(self.vertex_start.text().split()) != 0:
                start_vertex = self.vertex_start.text().split()[0]
            if len(self.des_vertex.text().split()) != 0:
                des_vertex = self.des_vertex.text().split()[0]

            algo = -1
            if self.bfs_button.isChecked():
                algo = 0
                if start_vertex == "":
                    return [4]
            if self.dfs_button.isChecked():
                algo = 1
                if start_vertex == "":
                    return [4]
            if self.dijkstra_button.isChecked():
                algo = 2
                if start_vertex == "" or des_vertex == "":
                    return [5]
            if self.bellman_button.isChecked():
                algo = 3
                if start_vertex == "" or des_vertex == "":
                    return [5]
            if self.prim_button.isChecked() and not self.prim_button.isHidden():
                algo = 4
                if start_vertex == "":
                    return [4]
            if self.kruskal_button.isChecked() and not self.kruskal_button.isHidden():
                algo = 5

            if algo == -1:
                return [-1]

            return x, start_vertex, des_vertex, graph_type, algo
        except:
            return [12]


    def update_exception(self, error_code):
        """Give an error notification on the interface"""

        self.label_9.setText("")
        self.label_10.setText("")
        self.label_8.clear()
        if error_code == 1:
            self.label_9.setText("Please select graph type: undirected or directed")
        if error_code == 2:
            self.label_9.setText("Please enter exactly one vertex in each line ")
        if error_code ==3 :
            self.label_9.setText("Please enter each line exactly 3 parameters: vertex, vertex, weight (weight is an interger)")
        if error_code == -1:
            self.label_9.setText("Please select the algorithm to execute")
        if error_code == 4:
            self.label_9.setText("Please enter starting vertex")
        if error_code == 5:
            self.label_9.setText("Please enter starting vertex and destination vertex")
        if error_code == 6:
            self.label_9.setText("The starting vertex is not in the graph")
        if error_code == 7:
            self.label_9.setText("The starting vertex or destination vertex is not in the graph")
        if error_code == 8:
            self.label_9.setText("Dijkstra algorithm does not apply to the graph with negative weights")
        if error_code == 9:
            self.label_9.setText("Bellman Ford algorithm does not apply to the graph with negative cycles")
        if error_code == 10:
            self.label_9.setText("Bellman Ford algorithm does not apply to the undirected graph with negative weights ")
        if error_code == 11:
            self.label_9.setText("No path")
        if error_code == 12:
            self.label_9.setText("The input data is wrong.")


    def update_image(self):
        """Update the graph on the interface"""

        self.label_8.setText(QtCore.QCoreApplication.translate("MainWindow", "Graph"))
        pixmap = QtGui.QPixmap("graph_image.png")
        self.label_8.setPixmap(pixmap)
        self.label_8.setObjectName("label_8")
        # MainWindow.show()

    def update_result(self, path):
        """Update the result on the interface"""
        if len(path)!=0:
            self.label_9.setText("Path: " + str(path[0]))
            self.label_10.setText(("Cost: " + str(path[1])))
        else:
            self.label_9.setText("")
            self.label_10.setText("")


    def control_ratio_button(self):

        self.label_9.setText("")
        self.label_10.setText("")
        #self.label_8.clear()
        if self.directed_button.isChecked():
            self.prim_button.setHidden(True)
            self.kruskal_button.setHidden(True)
        elif self.undirected_button.isChecked():
            self.prim_button.setHidden(False)
            self.kruskal_button.setHidden(False)
        if self.bfs_button.isChecked() or self.dfs_button.isChecked() or self.prim_button.isChecked():
            self.label_6.setText('Starting vertex: (*)')
            self.label_7.setText('')
            self.des_vertex.setVisible(False)
            self.vertex_start.setVisible(True)
        if self.dijkstra_button.isChecked() or self.bellman_button.isChecked():
            self.label_6.setText('Starting vertex: (*)')
            self.label_7.setText('Destination vertex: (*)')
            self.des_vertex.setVisible(True)
            self.vertex_start.setVisible(True)
        if self.kruskal_button.isChecked():
            self.label_6.setText('')
            self.label_7.setText('')
            self.vertex_start.setVisible(False)
            self.des_vertex.setVisible(False)


    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graph"))
        self.label_1.setText(_translate("MainWindow", "Choose the graph type: (*)"))
        self.directed_button.setText(_translate("MainWindow", "Directed Graph"))
        self.undirected_button.setText(_translate("MainWindow", "Undirected Graph"))
        self.label_3.setText(_translate("MainWindow", "Enter the vertices: (*)"))
        self.label_5.setText(_translate("MainWindow", "Enter the adjacency list and the weights: (*)"))
        self.bfs_button.setText(_translate("MainWindow", "BFS"))
        self.dfs_button.setText(_translate("MainWindow", "DFS"))
        self.kruskal_button.setText(_translate("MainWindow", "Kruskal"))
        self.bellman_button.setText(_translate("MainWindow", "Bellman Ford"))
        self.dijkstra_button.setText(_translate("MainWindow", "Dijkstra"))
        self.prim_button.setText(_translate("MainWindow", "Prim"))
        self.label_6.setText(_translate("MainWindow", "Starting vertex:(*)"))
        self.label_7.setText(_translate("MainWindow", "Destination vertex:(*)"))
        self.run_button.setText(_translate("MainWindow", "Run"))
        self.check_button.setText(_translate("MainWindow", "Check"))


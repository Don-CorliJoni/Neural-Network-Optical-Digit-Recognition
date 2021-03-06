from helper.numpy_helper import bytes_to_numpy_float64_array


class Configuration:

    def __init__(self, input_neurons: int, hidden_neurons: int, output_neurons: int, learning_rate: float,
                 train_epochs: int, wih, who, accuracy: float):
        self.neuron_nodes = (input_neurons, hidden_neurons, output_neurons)
        self.learning_rate = learning_rate
        self.train_epochs = train_epochs

        self.wih = wih
        self.who = who

        self.accuracy = accuracy

    def to_csv_one_line(self):
        bytes_wih = str(self.wih.tobytes())[2:-1]
        bytes_who = str(self.who.tobytes())[2:-1]
        return f"{self.accuracy};;{';;'.join([str(neuron_node) for neuron_node in self.neuron_nodes])};;" \
               f"{self.learning_rate};;{self.train_epochs};;{bytes_wih};;{bytes_who}\n "

    @staticmethod
    def create(data):
        input_nodes, hidden_nodes, output_nodes, learning_rate, train_epochs, wih, who, accuracy = \
            Configuration._cast_data(data)

        return Configuration(input_nodes, hidden_nodes, output_nodes, learning_rate, train_epochs,
                             bytes_to_numpy_float64_array(wih, (hidden_nodes, input_nodes)),
                             bytes_to_numpy_float64_array(who, (output_nodes, hidden_nodes)), accuracy)

    @staticmethod
    def _cast_data(data):
        input_nodes, hidden_nodes, output_nodes, learning_rate, train_epochs, wih, who, accuracy = data

        return (int(input_nodes), int(hidden_nodes), int(output_nodes), float(learning_rate), int(train_epochs),
                bytes(wih.encode().decode('unicode_escape'), encoding="raw_unicode_escape"),
                bytes(who.encode().decode('unicode_escape'), encoding="raw_unicode_escape"),
                float(accuracy))

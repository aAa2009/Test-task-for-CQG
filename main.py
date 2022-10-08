class Line:
    def __init__(self, line):
        self.text = line
        self.changes = 0
        self.new_text = ''

    def __repr__(self):
        return self.new_text

    def change_line(self, configuration):
        number_of_symbols = len(self.text)
        for i in range(number_of_symbols):
            if self.text[i] in configuration:
                symbol_for_change = self.text[i]
                self.new_text += configuration[symbol_for_change]
                self.changes += 1
            else:
                self.new_text += self.text[i]


def import_configuration(configuration = {}):
    with open('configuration.txt', 'r') as file:
        for line in file:
            key, value = line.strip().split("=")
            configuration[key] = value
    return configuration


def import_test_data(configuration, lines = []):
    with open('test_data.txt', 'r') as file:
        for line in file:
            line = Line(line.strip())
            line.change_line(configuration)
            lines.append(line)
    return lines


configuration = import_configuration()
lines = import_test_data(configuration)
lines = sorted(lines, key=lambda line: line.changes, reverse=True)
for line in lines:
    print(line)
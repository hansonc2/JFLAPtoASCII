import xml.etree.ElementTree as ET
import sys

class parser:

    def __init__(self):
        self.states = {}
        self.transitions = []
        self.filename = None

    def parse(self, filename):

        self.filename = filename
        tree = ET.parse(filename)
        root = tree.getroot()

        for child in root[1]:
            if child.tag == 'state':
                attr = child.attrib
                self.states[attr['id']] = attr['name']
            else:
                transition = [child[i].text for i in range(5)]
                self.transitions.append(transition)


    def save(self):
        self.transitions.sort(key=lambda x:int(x[0]))
        lines = []
        # format transitions
        for t in self.transitions:
            q = self.states[t[0]]
            q_prime = self.states[t[1]]
            read = t[2]
            write = t[3] + ',' if t[3] else ''
            move = t[4]

            lines.append(q + '->' + q_prime + ': ' + read + ';' + write + move)

        out_filename =  self.filename[:-3] + 'txt'
        with open(out_filename, 'w') as f:
            for l in lines:
                f.write(l + '\n')



def main():
    p = parser()
    p.parse(sys.argv[1])
    p.save()

if __name__ == '__main__':
    main()

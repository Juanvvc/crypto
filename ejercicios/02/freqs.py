# encoding: utf-8

import matplotlib.pyplot as plt

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def read_file(text_file, skip=0):
    # Initialize the dictionary of letter counts: {'A': 0, 'B': 0, ...}
    lcount = dict([(l, 0) for l in LETTERS])
    with open(text_file) as fin:
        for l in fin.read():            
            try:
                lcount[l.upper()] += 1
                if skip > 0:
                    fin.read(skip)
            except KeyError:
                # Ignore characters that are not letters
                pass
            
    # The total number of letters
    return lcount

def freq_letters(lcount):
    norm = sum(lcount.values())
    return [lcount[l] * 1.0/norm * 100 for l in LETTERS]
    

def plot_letters(lcount, title=''):
    freq = freq_letters(lcount)
    print(freq)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # The bar chart, with letters along the horizontal axis and the calculated
    # letter frequencies as percentages as the bar height
    x = range(26)
    ax.bar(x, freq, width=0.8, color='g', alpha=0.5, align='center')
    ax.set_xticks(x)
    ax.set_xticklabels(LETTERS)
    ax.tick_params(axis='x', direction='out')
    ax.set_xlim(-0.5, 25.5)
    ax.yaxis.grid(True)
    ax.set_ylabel('Letter frequency, %')
    plt.title(title)
    plt.show()

plot_letters(read_file('el_quijote.decrypt'), 'El Quijote')
plot_letters(read_file('el_quijote.caesar'), 'El Quijote. Caesar k=3')
plot_letters(read_file('el_quijote.vigenere'), 'El Quijote. Vigenère k=SESAMO')
plot_letters(read_file('el_quijote.vigenere', skip=5), 'El Quijote. Vigenère k=SESAMO group=6')

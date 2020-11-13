# https://github.com/minimaxir/textgenrnn
from textgenrnn import textgenrnn

textgen_2 = textgenrnn('textgenrnn_weights.hdf5')
#textgen_2.generate(1, temperature=0.1)

#textgen_2.generate(interactive=True, top_n=5)

#textgen_2.generate_samples()

#textgen_2.generate(10, temperature=0.3)

textgen_2.generate(interactive=True)



